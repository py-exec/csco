from django.shortcuts import render
from .forms import CartonForm

def carton_form_view(request):
    if request.method == "POST":
        form = CartonForm(request.POST)
        if form.is_valid():
            # ذخیره اطلاعات فرم یا پردازش آن
            return render(request, "your_app/success.html", {"form": form})
    else:
        form = CartonForm()

    return render(request, "your_app/carton_form.html", {"form": form})