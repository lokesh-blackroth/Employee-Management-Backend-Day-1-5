# Employee Management Backend

A Django-based backend project for an Employee Management System.

## Project Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd employee_management_backend
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the development server

```bash
python manage.py runserver
```

The server will be available at:

`http://127.0.0.1:8000/`

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

## Project Structure

```text
employee_management_backend/
├── employee_management/
├── employees/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Application

The `employees` Django application contains the employee management functionality.

## Development

Run Django's system checks with:

```bash
python manage.py check
```
