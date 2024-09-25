from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from website.models import PDFDocument
from .forms import CarPassForm, PasswordOnlyAuthenticationForm, SupportRequestForm


def custom_login_view(request):
    if request.method == "POST":
        form = PasswordOnlyAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            return redirect("pvr")
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
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            # Process the form data here
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
        form = CarPassForm(request.POST)
        if form.is_valid():
            # Process the form data here
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

    context = {
        "username": (
            request.user.username if hasattr(request.user, "username") else "Anonymous"
        ),
    }

    return render(request, "website/calendar.html", context)
