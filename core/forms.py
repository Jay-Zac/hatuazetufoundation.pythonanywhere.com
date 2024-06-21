from django import forms
from .models import UserComment


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = '__all__'
