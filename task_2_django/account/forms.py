from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    phone = forms.CharField(required=True,help_text='Enter Phone',max_length=10,)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', )
        
        
class AccountAuthenticationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

	def clean(self):
			username = self.cleaned_data['username']
			password = self.cleaned_data['password']
			if not authenticate(username=username, password=password):
				raise forms.ValidationError("Invalid Login")