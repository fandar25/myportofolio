from django.shortcuts import render

from main.models import Experience
from datetime import datetime


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

Experience.objects.create(
    title="Teaching Assistant Discrete Mathematics 1",
    description="Served as a teaching assistant for the Discrete Mathematics 1 course, responsible for grading quizzes, proctoring exams and quizzes, and conducting tutorials.",
    category="part-time",
    started_at= datetime(2026, 8, 19)
)

Experience.objects.create(
    title="DDP0 ARUNG",
    description="Served as a mentor teaching the fundamentals of Python programming to five first-year students from the Class of 2026.",
    category="volunteer",
    started_at= datetime(2026, 7, 13),
    ended_at= datetime(2026, 8, 23)
)

Experience.objects.create(
    title="BEM FASILKOM UI",
    description="I served as a staff member in the Community Service Department of BEM Fasilkom UI, where I managed a specific program called PEDAS. PEDAS is a donation drive aimed at supporting children associated with the Fasilkom UI community. My role involved setting up the donation platform, coordinating logistics, and distributing the collected donations.",
    category="part-time",
    started_at= datetime(2026, 7, 24),
)

Experience.objects.create(
    title="Open House Fasilkom UI 2026",
    description="Served as an expert staff member in the events division. Assisted the PIC and VPIC in overseeing the tasks of four staff members in accordance with their respective work programs. I was responsible for the Fun Coding, Parent's Talkshow, and Interactive Class programs.",
    category="part-time",
    started_at= datetime(2026, 5, 25),
)

Experience.objects.create(
    title="COMPFEST18",
    description="I served as a staff member for the Seminar Events team. I led one of the events, Xcelerate Foundations, which was attended by over 100 participants online. Additionally, I coordinated requests to other divisions to ensure the smooth execution of the event.",
    category="part-time",
    started_at= datetime(2026, 4, 18),
)

Experience.objects.create(
    title="BETIS",
    description="I work as an events staff member, assisting with stakeholder coordination to ensure the smooth running of events.",
    category="part-time",
    started_at= datetime(2026, 2, 19),
    ended_at= datetime(2026, 5, 28)
)

# Create your views here.
