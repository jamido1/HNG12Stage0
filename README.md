 Public API with Django | Django Rest Framework

 Project Overview
This project is a simple public API built using Django , Django Rest Framework (DRF). It provides a single endpoint that returns:
- My registered email address (used in the HNG12 Slack workspace).
- The current datetime in ISO 8601 format (UTC).
- The GitHub repository URL containing the project code.

  Features
- Returns JSON response with email, current datetime, and GitHub repository link.
- Uses Django Rest Framework for API development.
- Handles Cross-Origin Resource Sharing (CORS).
- Deployed on a publicly accessible platform.

## Tech Stack
- Backend: Python, Django, Django Rest Framework
- Version Control: Git
- Repository host: Github
- Deployment: Render

Installation and Setup
Prerequisites
Ensure you have the following installed:
- Python (>=3.8)
- pip
- pipenv

 Setup Instructions
1. Clone the repository:
   ```
   git clone "https://github.com/jamido1/HNG12Stage0.git"
   cd hngXII0
   ```
   
2. **Create and activate a virtual environment:**
   ```
   pipenv shell    # On Windows/MacOS/Linux
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```
6. Test the API locally:
   Open your browser or Postman and visit:
   ```
   http://127.0.0.1:8000/api/info/
   ```

 API Documentation
Endpoint:
GET /api/info/
```urls
https://hng12-api-neel.onrender.com/info/
https://hng.tech/hire/python-developers
```

Response (200 OK)
```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

 CORS Handling
CORS has been configured to allow cross-origin requests. The `django-cors-headers` package is used.
Ensure it is installed:
```
pip install django-cors-headers
```
Add it to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'corsheaders',
]
```
Add CORS middleware in `settings.py`:
```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```
Allow all origins (for development purposes) or specify allowed origins:
```python
CORS_ALLOWED_ORIGINS = [
    "https://jamido1.com",
]
```
 Resources
- [HNG Python Developers](https://hng.tech/hire/python-developers)



