# TODO App 📝

A simple **Django-based To-Do Application** with user authentication (login, register) and task management features.

## 🚀 Features
- **User Registration & Login** (via `accounts` app)
- **Add, View, Update, and Delete Tasks**
- **Mark Tasks as Complete or Incomplete**
- **User-Specific Task Management**
- **Responsive UI** with HTML templates

## 🛠 Tech Stack
- **Backend:** Django (Python)
- **Database:** SQLite (default)
- **Frontend:** HTML, CSS (Django templates)
- **Authentication:** Django's built-in user model

## 📦 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TODO-APP.git
   cd TODO-APP
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
  To access the Django admin panel:

   1. Run the following command inside the project folder:
   ```bash
   python manage.py createsuperuser
   
  ---

   I can now **add this section into the README.md file** I already generated so it’s ready for GitHub.  
   Do you want me to update the file directly?


7. Open the app in your browser:
   ```
   http://127.0.0.1:8000/
   ```

## 📂 Project Structure
```
TODO-APP/
│── accounts/          # Authentication app
│── templates/         # HTML templates
│── db.sqlite3         # Database file
│── manage.py          # Django project manager
│── requirements.txt   # Python dependencies
```

## 📝 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
**Author:** Naveenkumar S  
**GitHub:** [@Naveenks2708](https://github.com/Naveenks2708)
