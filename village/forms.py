from django import forms
from village.models import Complain, Village, UserProfile, Tag, ComplainResponse


class ComplainForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
        label="Select Tags"
    )

    class Meta:
        model = Complain
        fields = ['title', 'description', 'image', 'tags']

    def save(self, commit=True):
        complain = super().save(commit=False)
        if commit:
            complain.save()
            self.save_m2m()
        return complain
    
class ResponseForm(forms.ModelForm):
    class Meta:
        model = ComplainResponse
        fields = ['message']

class VillageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = [
            'name', 'description', 'post_code', 'population', 'total_voters',
            'area_sq_km', 'head_of_village', 'literacy_rate', 'established_year',
            'number_of_houses', 'number_of_schools', 'number_of_health_centers', 'image'
        ]

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
    


