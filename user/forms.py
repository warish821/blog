from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # self.fields["username"].widget.attrs
        self.fields["username"].widget.attrs["Placeholder"] = " Your Username" 
        self.fields["email"].widget.attrs["Placeholder"] = " Your email"    
        self.fields["password1"].widget.attrs["Placeholder"] = " Your password"    
        self.fields["password2"].widget.attrs["Placeholder"] = " Your confirm password"       