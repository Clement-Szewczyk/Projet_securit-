from django import forms
from common.models import student


# RegisterForm pour la bdd common.student avec ajout mdp crypté, firstname, lastname, birthdate
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = student
        fields = ('email', 'password', 'password2',
                  'first_name', 'last_name', 'birth_date')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(
                'Les mots de passe ne correspondent pas.')
        return cd['password2']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
