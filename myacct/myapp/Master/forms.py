from django import forms
from .models import Classification, Purpose


class ClassificationForm(forms.ModelForm):

    class Meta:
        model = Classification
        fields = (
            'c_id',
            'c_name',
        )

class PurposeForm(forms.ModelForm):
    class Meta:
        model = Purpose
        fields = (
            'c_id',
            'p_sub_id',
            'p_name',
        )
