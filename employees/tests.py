from django.test import TestCase
from django.urls import reverse

from .models import Employee


class EmployeeAPITestCase(TestCase):

    def setUp(self):
        self.employee = Employee.objects.create(
            employee_code="EMP001",
            first_name="Rahul",
            last_name="Sharma",
            email="rahul@example.com",
            phone="9876543210",
            department="IT",
            designation="Software Engineer",
            salary=60000,
            joining_date="2024-01-15",
            is_active=True
        )

    def test_create_employee(self):
        data = {
            "employee_code": "EMP002",
            "first_name": "Priya",
            "last_name": "Kumar",
            "email": "priya@example.com",
            "phone": "9876543211",
            "department": "HR",
            "designation": "HR Executive",
            "salary": 50000,
            "joining_date": "2024-02-15",
            "is_active": True
        }

        response = self.client.post(
            reverse("employee-list"),
            data=data,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Employee.objects.count(), 2)

    def test_view_employee(self):
        response = self.client.get(
            reverse(
                "employee-detail",
                kwargs={"id": self.employee.id}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()["employee"]["employee_code"],
            "EMP001"
        )

    def test_update_employee(self):
        data = {
            "employee_code": "EMP001",
            "first_name": "Rahul",
            "last_name": "Sharma",
            "email": "rahul@example.com",
            "phone": "9876543210",
            "department": "IT",
            "designation": "Senior Software Engineer",
            "salary": 70000,
            "joining_date": "2024-01-15",
            "is_active": True
        }

        response = self.client.put(
            reverse(
                "employee-detail",
                kwargs={"id": self.employee.id}
            ),
            data=data,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        self.employee.refresh_from_db()

        self.assertEqual(
            self.employee.designation,
            "Senior Software Engineer"
        )
        self.assertEqual(
            float(self.employee.salary),
            70000.0
        )

    def test_search_employee(self):
        response = self.client.get(
            reverse("employee-list"),
            {"search": "Rahul"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["employees"]), 1)

    def test_filter_employee_by_department(self):
        response = self.client.get(
            reverse("employee-list"),
            {"department": "IT"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["employees"]), 1)

    def test_filter_active_employee(self):
        response = self.client.get(
            reverse("employee-list"),
            {"is_active": "true"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["employees"]), 1)

    def test_delete_employee(self):
        response = self.client.delete(
            reverse(
                "employee-detail",
                kwargs={"id": self.employee.id}
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.count(), 0)

    def test_employee_not_found(self):
        response = self.client.get(
            reverse(
                "employee-detail",
                kwargs={"id": 99999}
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_salary(self):
        data = {
            "employee_code": "EMP003",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "phone": "9876543212",
            "department": "IT",
            "designation": "Developer",
            "salary": -100,
            "joining_date": "2024-03-15",
            "is_active": True
        }

        response = self.client.post(
            reverse("employee-list"),
            data=data,
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)