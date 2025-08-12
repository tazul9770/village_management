from django import forms
from village.models import Complain, Village, UserProfile

class ComplainForm(forms.ModelForm):
    class Meta:
        model = Complain
        fields = ['title', 'description', 'image']

class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = ['name', 'description']

class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=30)
    last_name = forms.CharField(required=True, max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone', 'address', 'bio', 'profile_picture']

    field_order = ['first_name', 'last_name', 'phone', 'address', 'bio', 'profile_picture', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(EditProfileForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['first_name'].initial = self.user.first_name
            self.fields['last_name'].initial = self.user.last_name
            self.fields['email'].initial = self.user.email

    def save(self, commit=True):
        profile = super(EditProfileForm, self).save(commit=False)
        if commit:
            profile.save()
        user = self.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit: 
            user.save()
        return profile

