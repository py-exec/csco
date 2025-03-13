document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ مدیریت مشتری اجرا شد!");

    /** 📌 دریافت CSRF Token **/
    const csrfTokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    const csrfToken = csrfTokenElement ? csrfTokenElement.value : null;
    if (!csrfToken) {
        console.error("❌ CSRF Token یافت نشد!");
        return;
    }

    /** 📌 دریافت عناصر و بررسی وجود آنها **/
    function getElement(id) {
        const element = document.getElementById(id);
        if (!element) {
            console.error(`❌ عنصر با id="${id}" پیدا نشد! لطفاً بررسی کنید که این ID در HTML وجود دارد.`);
        }
        return element;
    }

    /** 📌 متغیرهای اصلی **/
    const customerSearch = getElement("customer_search");
    const customerList = getElement("customer_result_list");
    const selectedCustomerName = getElement("selected_customer_name");
    const customerPhoneInput = getElement("customer_phone");
    const confirmCustomerBtn = getElement("confirm_customer_btn");
    const selectCustomerBtn = getElement("select_customer_btn");
    const modalElement = getElement("customerModal");
    let selectedCustomer = null;

    if (!customerSearch || !customerList || !selectedCustomerName || !customerPhoneInput || !modalElement) {
        console.error("❌ برخی از عناصر فرم یافت نشدند! بررسی کنید که تمام IDها در HTML موجود باشند.");
        return;
    }

    // **🚨 بررسی دکمه تایید مشتری**
    if (!confirmCustomerBtn) {
        console.error("❌ دکمه تایید مشتری یافت نشد! لطفاً بررسی کنید که `id='confirm_customer_btn'` در HTML موجود باشد.");
        return;
    }

    const modal = new bootstrap.Modal(modalElement);
    let customers = [];

    /** 📌 دریافت لیست مشتریان **/
    async function fetchCustomers() {
        try {
            const response = await fetch("/calculator/get-customers/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": csrfToken
                }
            });
            const data = await response.json();

            if (data.success) {
                customers = data.customers;
                console.log("✅ مشتریان دریافت شدند:", customers);
            } else {
                console.error("❌ خطا در دریافت مشتریان:", data.error);
            }
        } catch (error) {
            console.error("❌ خطا در دریافت مشتریان:", error);
        }
    }

    fetchCustomers();

    /** 🔎 جستجوی مشتری **/
    customerSearch.addEventListener("input", function () {
        const query = customerSearch.value.trim().toLowerCase();
        customerList.innerHTML = "";

        if (query.length < 3) {
            customerList.classList.add("d-none");
            return;
        }

        const filteredCustomers = customers.filter(customer =>
            customer.name.toLowerCase().includes(query) || customer.phone.includes(query)
        );

        if (filteredCustomers.length > 0) {
            customerList.classList.remove("d-none");
            filteredCustomers.forEach(customer => {
                const item = document.createElement("li");
                item.classList.add("list-group-item", "list-group-item-action");
                item.textContent = `${customer.name} - 📞 ${customer.phone}`;
                item.addEventListener("click", function () {
                    selectCustomer(customer);
                });
                customerList.appendChild(item);
            });
        } else {
            customerList.classList.add("d-none");
        }
    });

    /** ✅ انتخاب مشتری از لیست **/
    function selectCustomer(customer) {
        selectedCustomer = customer;
        console.log("✅ مشتری انتخاب شد:", selectedCustomer);
        confirmCustomerBtn.disabled = false;
        confirmCustomerBtn.textContent = `✅ تایید ${customer.name}`;
    }

    /** 🎯 تایید انتخاب مشتری **/
    confirmCustomerBtn.addEventListener("click", function () {
        if (!selectedCustomer) {
            console.error("❌ خطا: هیچ مشتری انتخاب نشده است!");
            return;
        }

        console.log("📌 انتخاب نهایی مشتری:", selectedCustomer);
        selectedCustomerName.value = selectedCustomer.name;
        customerPhoneInput.value = selectedCustomer.phone;

        // **اصلاح مشکل `modal.hide()`**
        setTimeout(() => {
            modal.hide();
        }, 200);
    });

});