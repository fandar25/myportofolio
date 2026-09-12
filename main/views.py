from django.shortcuts import render

from main.models import Experience, Education



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
    context = {
        "name": "Muhammad Gathfaan Nur Aziz Suhendar",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

# Create your views here.
