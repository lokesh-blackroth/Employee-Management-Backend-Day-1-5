# Employee Management Backend

A Django-based backend project for an Employee Management System.

## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd employee_management_backend

2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment

Windows PowerShell:

.venv\Scripts\Activate.ps1
4. Install dependencies
python -m pip install -r requirements.txt
5. Apply migrations
python manage.py migrate
6. Run the development server
python manage.py runserver

The server will be available at:

http://127.0.0.1:8000/

Health Check API
Endpoint

GET /api/health/

Response
{
    "status": "success",
    "message": "Employee Management Backend is running"
}
Project Structure
employee_management_backend/
├── employee_management/
├── employees/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
Application

The employees Django application contains the employee management functionality.

Development

Run Django's system checks with:

python manage.py check
Employee API
Endpoints
GET /api/employees/ - List employees
POST /api/employees/ - Create an employee
GET /api/employees/<id>/ - Retrieve an employee
PUT /api/employees/<id>/ - Update an employee
DELETE /api/employees/<id>/ - Delete an employee
Employee Model

The Employee model contains:

id
employee_code
first_name
last_name
email
phone
department
designation
salary
joining_date
is_active
created_at
updated_at
Database & ORM
Generated and applied Django migrations.
Created 15 employee records using Django ORM.
Tested Create, Read, Update, and Delete operations.
Tested get(), filter(), and exclude().
Tested active and inactive employee filtering.
Tested IT department filtering.
Tested salary filtering (salary > 50000).
Tested ordering by joining date.
Verified ORM operations through Django shell.
Migrations
python manage.py makemigrations
python manage.py migrate
Django Shell
python manage.py shell

## Development

Run Django's system checks with:

```bash
python manage.py check

## Employee API

### Endpoints

- `GET /api/employees/` - List employees
- `POST /api/employees/` - Create an employee
- `GET /api/employees/<id>/` - Retrieve an employee
- `PUT /api/employees/<id>/` - Update an employee
- `DELETE /api/employees/<id>/` - Delete an employee

## Employee Model

The `Employee` model contains:

- `id`
- `employee_code`
- `first_name`
- `last_name`
- `email`
- `phone`
- `department`
- `designation`
- `salary`
- `joining_date`
- `is_active`
- `created_at`
- `updated_at`

## Database & ORM

- Generated and applied Django migrations.
- Created 15 employee records using Django ORM.
- Tested Create, Read, Update, and Delete operations.
- Tested `get()`, `filter()`, and `exclude()`.
- Tested active and inactive employee filtering.
- Tested IT department filtering.
- Tested salary filtering (`salary > 50000`).
- Tested ordering by joining date.
- Verified ORM operations through Django shell.

### Migrations

```bash
python manage.py makemigrations
python manage.py migrate

Django Shell
python manage.py shell

ORM operations were verified through the Django shell.

Git Progress
Day 1

Branch: feature/django-project-setup

Commit: 4805006 feat: initialize django employee management backend

Day 2

Branch: feature/employee-views

Commit: 806cc59 feat: implement employee urls and views

Day 3

Branch: feature/employee-model

Commit: 09c95d9 feat: add employee model and orm operations