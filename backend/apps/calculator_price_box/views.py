from django.shortcuts import render
from .forms import CartonForm

def carton_form(request):
    if request.method == "POST":
        form = CartonForm(request.POST)
        if form.is_valid():
            return render(request, "clac_box/success.html", {"form": form})  # نمایش صفحه موفقیت
    else:
        form = CartonForm()

    return render(request, "clac_box/carton_form.html", {"form": form})  # مسیر صحیح قالب