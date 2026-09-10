# Employee Management Backend

A Django-based backend project for an Employee Management System.

## Project Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd employee_management_backend
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

The server will be available at:

`http://127.0.0.1:8000/`

---

## Health Check API

### Endpoint

`GET /api/health/`

### Response

```json
{
    "status": "success",
    "message": "Employee Management Backend is running"
}
```

---

## Employee API Endpoints

| Method | Endpoint               | Description          |
| ------ | ---------------------- | -------------------- |
| GET    | `/api/employees/`      | List employees       |
| POST   | `/api/employees/`      | Create an employee   |
| GET    | `/api/employees/<id>/` | Retrieve an employee |
| PUT    | `/api/employees/<id>/` | Update an employee   |
| DELETE | `/api/employees/<id>/` | Delete an employee   |

---

## Employee Model

The `employees` application contains the `Employee` model.

### Fields

| Field           | Type          | Description                         |
| --------------- | ------------- | ----------------------------------- |
| `id`            | AutoField     | Automatically generated primary key |
| `employee_code` | CharField     | Unique employee code                |
| `first_name`    | CharField     | Employee first name                 |
| `last_name`     | CharField     | Employee last name                  |
| `email`         | EmailField    | Unique email address                |
| `phone`         | CharField     | Employee phone number               |
| `department`    | CharField     | Employee department                 |
| `designation`   | CharField     | Employee designation                |
| `salary`        | DecimalField  | Employee salary                     |
| `joining_date`  | DateField     | Employee joining date               |
| `is_active`     | BooleanField  | Employee active status              |
| `created_at`    | DateTimeField | Record creation time                |
| `updated_at`    | DateTimeField | Last update time                    |

The model also implements `__str__()` to display the employee code and name.

---

## Database & Migrations

The Employee model is stored in the database using Django ORM.

### Generate migrations

```bash
python manage.py makemigrations
```

### Apply migrations

```bash
python manage.py migrate
```

Migration created:

```text
employees/migrations/0001_initial.py
```

---

## Django ORM

Employee records were created and tested using the Django shell.

### Open Django Shell

```bash
python manage.py shell
```

### Import Employee Model

```python
from employees.models import Employee
```

### Create Employee

```python
Employee.objects.create(
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
```

### Retrieve All Employees

```python
Employee.objects.all()
```

### Filter Active Employees

```python
Employee.objects.filter(is_active=True)
```

### Filter Inactive Employees

```python
Employee.objects.filter(is_active=False)
```

### Filter IT Employees

```python
Employee.objects.filter(department="IT")
```

### Filter Employees With Salary Above 50000

```python
Employee.objects.filter(salary__gt=50000)
```

### Exclude IT Employees

```python
Employee.objects.exclude(department="IT")
```

### Get a Single Employee

```python
Employee.objects.get(employee_code="EMP001")
```

### Update Employee

```python
employee = Employee.objects.get(employee_code="EMP001")
employee.salary = 65000
employee.save()
```

### Delete Employee

```python
employee = Employee.objects.get(employee_code="EMP015")
employee.delete()
```

### Order Employees by Joining Date

Ascending:

```python
Employee.objects.order_by("joining_date")
```

Descending:

```python
Employee.objects.order_by("-joining_date")
```

---

## ORM Query Differences

### `get()`

Returns exactly one object.

```python
Employee.objects.get(employee_code="EMP001")
```

Raises `DoesNotExist` when no matching employee exists.

### `filter()`

Returns all matching records as a QuerySet.

```python
Employee.objects.filter(department="IT")
```

### `exclude()`

Returns records that do not match the condition.

```python
Employee.objects.exclude(department="IT")
```

---

## ORM Testing

The following operations were tested through Django shell:

* Created 15 employee records
* Retrieved all employees
* Retrieved active employees
* Retrieved inactive employees
* Retrieved IT employees
* Filtered employees with salary greater than 50,000
* Ordered employees by joining date
* Used `get()`
* Used `filter()`
* Used `exclude()`
* Updated employee salary
* Deleted an employee
* Recreated the deleted employee
* Verified record counts
* Tested `DoesNotExist` exception
* Tested and fixed invalid ORM field filters

---

## Debugging

The following errors were intentionally tested and resolved:

### Invalid ORM Field

Incorrect:

```python
Employee.objects.filter(departments="IT")
```

Correct:

```python
Employee.objects.filter(department="IT")
```

### Invalid Field Name

Incorrect:

```python
Employee.objects.filter(nonexistent_field="test")
```

This produces a Django `FieldError`.

### Employee Not Found

```python
Employee.objects.get(employee_code="EMP999")
```

Produces:

```text
Employee.DoesNotExist
```

---

## Project Structure

```text
employee_management_backend/
├── employee_management/
├── employees/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Development

Run Django's system checks with:

```bash
python manage.py check
```

---

## Git Progress

### Day 1 — Django Project Setup

Branch:

```text
feature/django-project-setup
```

Commit:

```text
4805006 feat: initialize django employee management backend
```

### Day 2 — Employee URLs and Views

Branch:

```text
feature/employee-views
```

Commit:

```text
806cc59 feat: implement employee urls and views
```

### Day 3 — Employee Model and ORM

Branch:

```text
feature/employee-model
```

Code commit:

```text
09c95d9 feat: add employee model and orm operations
```

README commit:

```text
e900630 docs: update README with employee model and ORM
```

All three branches have been pushed to GitHub.

---

## Current Status

### Completed

* Django project setup
* Employee application setup
* Health Check API
* Employee URLs and views
* Employee model
* Database migration
* 15 employee records
* Django ORM CRUD operations
* Filtering
* Excluding records
* Ordering
* ORM error handling
* Debugging
* README documentation
* Git branches and commits
* GitHub push


## Employee CRUD & Django Admin

### Django Admin

The Employee model is registered in Django Admin with:

- Employee ID
- Employee Code
- First Name
- Last Name
- Email
- Salary
- Search by employee code, name and email
- Filter by salary
- Ordering by employee ID

### Employee APIs

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees/` | Get all employees |
| POST | `/api/employees/` | Create an employee |
| GET | `/api/employees/<id>/` | Get a single employee |
| PUT | `/api/employees/<id>/` | Update an employee |
| PATCH | `/api/employees/<id>/` | Update an employee |
| DELETE | `/api/employees/<id>/` | Delete an employee |

### Validation

Employee creation and update use `EmployeeForm` validation for:

- Required fields
- Valid email
- Unique employee code
- Unique email
- Salary greater than zero

### Testing

Tested the following scenarios:

- Create employee
- Get all employees
- Get employee by ID
- Update employee
- Delete employee
- Missing email
- Duplicate employee code
- Duplicate email
- Invalid salary
- Missing required field
- Invalid employee ID
- CSRF error debugging
- Invalid redirect debugging

### Git

Feature branch:

`feature/employee-crud`

Latest commit:

`20d1aaa - feat: implement employee crud and admin`