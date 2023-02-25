from django.shortcuts import render, redirect
from .forms import RegistrationForm
def register(response):
    form = RegistrationForm()

    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/shop")
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(response, "register/register.html", context)
