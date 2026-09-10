from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            "employee_code",
            "first_name",
            "last_name",
            "email",
            "phone",
            "department",
            "designation",
            "salary",
            "joining_date",
            "is_active",
        ]

    def clean_employee_code(self):
        employee_code = self.cleaned_data["employee_code"].strip()

        if not employee_code:
            raise forms.ValidationError("Employee code is required.")

        return employee_code

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()

        if not email:
            raise forms.ValidationError("Email is required.")

        return email

    def clean_salary(self):
        salary = self.cleaned_data["salary"]

        if salary <= 0:
            raise forms.ValidationError("Salary must be greater than 0.")

        return salary