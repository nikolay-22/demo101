from django import forms

from demo101.formsbasics.models import Employee


## Classic forms:
class EmployeeForm(forms.Form):
    first_name = forms.CharField(
        max_length=35,
        required=True,
        label="First Name label:",
        help_text="Enter your first name here",
        # initial="Nikolay", #will show in the form as filled in first name - this is not a placeholder
        # disabled=True #will prevent the user from entering data; will not be sent in the POST request!
    )

    last_name = forms.CharField(
        max_length=35,
        required=True,
        widget=forms.TextInput(
            attrs={
            'placeholder': "Enter your last name here",
            }
        )
    )

    age = forms.IntegerField(
        min_value=12,
    )

    INTERESTS = (
        (None, "------"),
        (1, "Gaming"),
        (2, "Drinking"),
        (3, "Swimming"),
    )

    interests = forms.ChoiceField( #returns string, e.g. "2"
        choices=INTERESTS,
    )

    interests2 = forms.IntegerField( #returns integer, e.g. 2
        widget=forms.Select(choices=INTERESTS),
        label="Choicefield interests select:",
    )

    interests3 = forms.IntegerField( #as above, but with radio buttons
        widget=forms.RadioSelect(choices=INTERESTS),
        label="Radio buttons interests select:",
    )

    interests4 = forms.CharField( #as above, but with checkboxes
        widget=forms.CheckboxSelectMultiple(choices=INTERESTS),
        label="Checkbox interests select:",
    )

    checkbox_field = forms.BooleanField(required=False)


class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee

        # Which model fields to include in the model form:
        # fields=('first_name', 'last_name', 'role',)
        # ## Other options:
        fields = '__all__'
        # # exclude=('role',)

        widgets = {
            'role': forms.RadioSelect(
                # attrs={
                #     'disabled': 'disabled',
                # }
            )
        }

        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'department': 'Department (from DB)', # a foreign key taht will appear as a drop-down in the form
        }

    # We can add fields, not related to the model, and we refer to it with form.cleaned_data['department']:
    department2 = forms.CharField(label="Department (not from DB)")

        # We also have:
        # help_texts
        # labels
        # error_messages



