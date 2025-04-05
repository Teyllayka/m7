from django.contrib.auth import login
from django.shortcuts import get_object_or_404, render, redirect
import requests

from website.models import  Pages
from .forms import PasswordOnlyAuthenticationForm, SupportRequestForm
from django.contrib.auth import logout


def custom_login_view(request):
    if request.method == "POST":
        form = PasswordOnlyAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            return redirect("application")
        else:
            return render(request, "website/auth.html", {"form": form})
    else:
        if request.user.is_authenticated:
            return redirect("application")
        form = PasswordOnlyAuthenticationForm()
    return render(request, "website/auth.html", {"form": form})




def application(request):
    if request.method == "POST":
        form = SupportRequestForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.POST


            params = {
                "key": "ogFGBvgVVJ8gCA8Eo2v81UbEeA6yqA5syqoFZtdT",
                "username": "tech",
                "password": "!tech@2024",
                "action": "insert",
                "entity_id": 53,
                "items[field_773]": "Арендатор",
                "items[field_543]": request.user.username,
                "items[field_547]": data["phone"],
                "items[field_544]": data["message"],
                "items[field_542]": data["type"],
                "items[field_546]": request.user.email,
                "items[field_2972]": form.cleaned_data.get("file"),
            }

            url = "https://tm.vvvgroup.ru/api/rest.php"
            try:
                response = requests.post(url, data=params, timeout=10, verify=False)
                response.raise_for_status() 
                result = response.json()
                print(result)  
                return redirect("application")

            except requests.exceptions.RequestException as e:
                return redirect("application")
       

    if not request.user.is_authenticated:
        return redirect("/")

    page = Pages.objects.filter(page="application").first()

    context = {
        "username": (
            request.user.username if hasattr(request.user, "username") else "Anonymous"
        ),
        "user_phone" : request.user.phone if hasattr(request.user, "phone") else None,
        "user_email" : request.user.email if hasattr(request.user, "email") else None,
        "form": SupportRequestForm(), 
        "page": page

    }

    return render(request, "website/order.html", context)


def logout_view(request):
    logout(request)
    return redirect('/')

def page_detail(request, page):
    if not request.user.is_authenticated:
        return redirect("/")
    
 
    page_obj = get_object_or_404(Pages, page=page)
    return render(request, 'website/page.html', {'page': page_obj,    "username": (
        request.user.username if hasattr(request.user, "username") else "Anonymous"
    ),
})