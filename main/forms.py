from django.forms import ModelForm, TextInput, Textarea, URLInput, DateInput

from main.models import Education

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = "__all__"

        labels = {
            "title": "Nama Pendidikan",
            "description": "Deskripsi Pendidikan",
            "category": "Jenjang Pendidikan",
            "thumbnail": "URL Gambar Pendidikan",
            "started_at": "Tanggal mulai",
            "ended_at": "Tanggal akhir",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Sekolah",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan pendidikanmu",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "HIGH SCHOOL, UNDERGRADUATE",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://pws.cs.ui.ac.id/web/makara.png",
                }
            ),
            "started_at": DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type" : "date",
                    "placeholder": "YYYY-MM-DD",
                }
            ),
            "ended_at": DateInput(
                format="%Y-%m-%d",
                attrs={
                    "type" : "date",
                    "placeholder": "YYYY-MM-DD",
                }
            ),
        }