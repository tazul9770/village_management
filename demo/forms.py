from django import forms
from demo.models import Person

class DemoForm(forms.Form):
    name = forms.CharField(max_length=200)
    address = forms.CharField(widget=forms.Textarea)
    person = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        person = kwargs.pop("person", [])
        super().__init__(*args, **kwargs)
        self.fields['person'].choices = [(emp.id, emp.name) for emp in person]

class StyledFormMixin:
    default_class = "border shadow-md border-blue-500 py-2 px-3 rounded-md w-full focus:border-blue-500 focus:ring-blue-500"

    def apply_styled_widget(self):
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_class,
                    'placeholder':f'Enter {field.label.lower()}'
                })
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class':self.default_class,
                    'placeholder':f'Enter {field.label.lower()}'
                })

class Modelform(StyledFormMixin,forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'address']

    #widget use mixin
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widget()

        #manually use widget
        # widgets = {

        #     "name":forms.TextInput(attrs={
        #         'class':"border shadow-md border-blue-500 py-2 px-3 rounded-md w-full focus:border-blue-500 focus:ring-blue-500",
        #         'placeholder':"Enter your name"
        #     }),

        #     'address':forms.Textarea(attrs={
        #         'class':"border shadow-md border-blue-500 py-2 px-3 rounded-md w-full focus:border-blue-500 focus:ring-blue-500",
        #         'placeholder':"Write address"
        #     })
        # }