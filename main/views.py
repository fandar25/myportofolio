from django.shortcuts import render

from main.forms import EducationForm, ExperienceForm
from main.models import Experience, Education

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "npm": "2506609214",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An ambitious Information Systems student passionate about bridging technology. With an unwavering commitment to personal development and a grit-driven mindset,"
            " I strive to excel in the information technology industry by leveraging analytical thinking, relationship-building skills, and a proactive approach to create impactful opportunities."
        ),
        "last_login" : last_login,
    }
    return render(request, "index.html", context)


def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experience = Experience.objects.all()

    if title_query:
        experience = experience.filter(title__icontains=title_query)

    experience_json = serializers.serialize("json", experience, use_natural_foreign_keys=True)
    return HttpResponse(experience_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)

    experiences = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    experiences = [experience.object for experience in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "form": form,
    }
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")

    return redirect("main:show_experience")

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    educations = [education.object for education in educations]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "education_list": educations,
        "title_query": title_query,
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Education baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%H:%S'))
        return response

    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)

    return redirect("main:show_experience")

