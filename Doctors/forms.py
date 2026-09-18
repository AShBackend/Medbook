from django import forms
from .models import Reserver

class ReserverForm(forms.ModelForm):
    class Meta:
        model = Reserver
        fields = ("Doctors", "Date_Time", "Reason")
        widgets = {

            "Doctors": forms.Select(attrs={
                "class": "form-select",
            }),

            "Date_Time": forms.DateTimeInput(attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                }
            ),

            "Reason": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "توضیحات",
                "rows": 4,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["Doctors"].help_text = None
        self.fields["Date_Time"].help_text = None
        self.fields["Reason"].help_text = None

