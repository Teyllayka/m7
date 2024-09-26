from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
import requests

from website.models import PDFDocument, Post
from .forms import CarPassForm, PasswordOnlyAuthenticationForm, SupportRequestForm


def custom_login_view(request):
    if request.method == "POST":
        form = PasswordOnlyAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            return JsonResponse({"success": True}, status=200)

        errors = form.errors.get_json_data()
        print(errors)
        return JsonResponse({"success": False, "errors": errors}, status=200)

    else:
        if request.user.is_authenticated:
            return redirect("pvr")

        form = PasswordOnlyAuthenticationForm()

    return render(request, "website/login.html", {"form": form})


def homepage_view(request):
    if request.user.is_authenticated:
        username = (
            request.user.username
            if hasattr(request.user, "username")
            else "No username set"
        )
        return HttpResponse(f"Welcome to the homepage, {username}!")
    else:
        return HttpResponse("Welcome to the homepage! Please log in.")


def pvr(request):
    if not request.user.is_authenticated:
        return redirect("/")

    pdf_document = (
        PDFDocument.objects.filter(title="pvr").order_by("-uploaded_at").first()
    )

    context = {
        "username": (
            request.user.username if hasattr(request.user, "username") else "Anonymous"
        ),
        "pdf_document": pdf_document,
    }

    return render(request, "website/pvr.html", context)


def ppb(request):
    if not request.user.is_authenticated:
        return redirect("/")

    pdf_document = (
        PDFDocument.objects.filter(title="ppb").order_by("-uploaded_at").first()
    )

    context = {
        "username": (
            request.user.username if hasattr(request.user, "username") else "Anonymous"
        ),
        "pdf_document": pdf_document,
    }

    return render(request, "website/ppb.html", context)


def application(request):
    if request.method == "POST":

        # print(
        #     data["phone_number"]
        #     .replace(" ", "")
        #     .replace("(", "")
        #     .replace(")", "")
        #     .replace("-", "")
        # )

        form = SupportRequestForm(request.POST)
        if form.is_valid():
            data = request.POST

            params = {
                "key": "at9DgisOQMiBxKS4V1HA5RXmTgl4D6v2aLsIb6ge",
                "username": "tech",
                "password": "!tech@2024",
                "action": "insert",
                "entity_id": 33,
                "items[field_330]": data["contact_name"],
                "items[field_331]": data["phone_number"],
                "items[field_324]": data["message"],
                "items[parent_item_id]": "1",
            }

            url = "https://vvvgroup.ru/ts/api/rest.php"
            try:
                response = requests.post(url, data=params, timeout=10, verify=False)
                response.raise_for_status()  # Raise an exception for HTTP errors
                result = response.json()
                print(result)  # Or handle the result as needed
                return JsonResponse({"success": True}, status=200)

            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                errors = form.errors.get_json_data()
                print(errors)
                return JsonResponse({"success": False, "errors": errors}, status=200)

            pass

    if not request.user.is_authenticated:
        return redirect("/")

    context = {
        "username": (
            request.user.username if hasattr(request.user, "username") else "Anonymous"
        ),
        "form": SupportRequestForm(),  # Include form in the context
    }

    return render(request, "website/application.html", context)


def kpp(request):
    if request.method == "POST":
        print(request.POST)
        form = CarPassForm(request.POST)
        if form.is_valid():
            data = request.POST

            params = {
                "key": "at9DgisOQMiBxKS4V1HA5RXmTgl4D6v2aLsIb6ge",
                "username": "tech",
                "password": "!tech@2024",
                "action": "insert",
                "entity_id": 31,
                "items[field_295]": request.user.username,
                "items[field_296]": data["car_number"],
                "items[field_297]": data["car_type"],
                "items[field_298]": data["entry_date"],
                "items[parent_item_id]": "1",
            }

            url = "https://vvvgroup.ru/ts/api/rest.php"
            try:
                response = requests.post(url, data=params, timeout=10, verify=False)
                response.raise_for_status()  # Raise an exception for HTTP errors
                result = response.json()
                print(result)  # Or handle the result as needed
                return JsonResponse({"success": True}, status=200)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
                errors = form.errors.get_json_data()
                print(errors)
                return JsonResponse({"success": False, "errors": errors}, status=200)

            pass
    else:
        if not request.user.is_authenticated:
            return redirect("/")

        context = {
            "username": (
                request.user.username
                if hasattr(request.user, "username")
                else "Anonymous"
            ),
            "form": CarPassForm(),  # Include form in the context
        }

        return render(request, "website/kpp.html", context)


def calendar(request):

    if not request.user.is_authenticated:
        return redirect("/")


    posts = Post.objects.all()

    context = {
        "username": (
            request.user.username if hasattr(request.user, "username") else "Anonymous"
        ),
        "posts": posts,
    }

    return render(request, "website/calendar.html", context)
