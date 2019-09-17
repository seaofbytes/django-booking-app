from django import forms

from polls.models import Poll


class PollWizardForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = []
