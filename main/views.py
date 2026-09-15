from django.shortcuts import render

from main.forms import EducationForm
from main.models import Experience, Education

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


def show_main(request):
    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "npm": "2506609214",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "An ambitious Information Systems student passionate about bridging technology. With an unwavering commitment to personal development and a grit-driven mindset,"
            " I strive to excel in the information technology industry by leveraging analytical thinking, relationship-building skills, and a proactive approach to create impactful opportunities."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

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
    
def create_education(request):
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

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

# Create your views here.
