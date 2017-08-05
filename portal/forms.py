from django.forms import ModelForm
import django.forms as forms

from .models import User, Address, Qualification, WorkExperience

# forms
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)


class User_BasicInfoForm(ModelForm):
    class Meta:
        model = User
        fields = ['roll_no', 'name', 'email_1', 'date_of_birth', 'gender']


class User_MiscInfoForm(ModelForm):
    class Meta:
        model = User
        fields = ['email_2', 'phone_1', 'phone_2', 'marital_status',
                  'blood_group', 'photograph', 'nationality',
                  'permanent_address', 'scope_permanent_address',
                  'current_address', 'scope_current_address']


class User_SocialLinksForm(ModelForm):
    class Meta:
        model = User
        fields = ['link_facebook', 'scope_facebook',
                  'link_twitter', 'scope_twitter',
                  'link_linkedin', 'scope_linkedin',
                  'link_skype', 'scope_skype',
                  'link_github', 'link_blog', 'link_website']


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'
        # set user_roll_no as hidden


class QualificationForm(ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'


class WorkExperienceForm(ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'
