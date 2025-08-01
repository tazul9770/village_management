from django import forms

class DemoForm(forms.Form):
    name = forms.CharField(max_length=200)
    address = forms.CharField(widget=forms.Textarea)
    person = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        person = kwargs.pop("person", [])
        print(person)
        super().__init__(*args, **kwargs)
        self.fields['person'].choices = [(emp.id, emp.name) for emp in person]