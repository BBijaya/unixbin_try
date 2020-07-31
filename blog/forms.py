from django import forms
from blog.models import Email



class NewsLetterForm(forms.ModelForm):

    class Meta():
        model = Email
        fields = ('email',)
