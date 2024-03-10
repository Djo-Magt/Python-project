from django import forms

from blog.models import BlogPost

JOBS = (
    ("python", "Dév Python"),
    ("js", "Dév JS"),
    ("csharp", "Dév C#"),
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6)
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "date", "category","description",]
        