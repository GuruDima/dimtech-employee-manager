# 🌐 DimTech – Digital HR Management System

**DimTech** is a modern employee management system built with Django. It allows admins to manage staff, view statistics, and export data to Excel. Regular users can log in and view profiles in a clean, responsive interface.

---

## 🚀 Features

- 👥 Add / edit / delete employees (admin only)
- 🔍 Search, filter and sort employees
- 📈 Employee statistics (by level & salary)
- 📥 Export data to Excel (.xlsx)
- 🔐 User login & registration
- 🌗 Light/Dark mode toggle
- 🧱 Custom 403 / 404 error pages

---

## 🧰 Tech Stack

- **Python** 3.12  
- **Django** 5.2  
- **Bootstrap** 5.3  
- **SQLite** (default DB)  
- **Openpyxl** (Excel export)

---

## ⚙️ Installation

**Clone the repository:**

```bash
git clone https://github.com/GuruDima/dimtech.git
cd dimtech

python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt

SECRET_KEY=your-secret-key
DEBUG=True

Run migrations and create superuser:
python manage.py migrate
python manage.py createsuperuser

Run development server:
python manage.py runserver

Visit: http://127.0.0.1:8000

📁 Project Structure
csharp
Copy
Edit
dimtech/
│
├── employees/              # Main Django app
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   └── ...
├── dimtech/                # Django project settings
├── media/                  # Uploaded employee photos
├── static/                 # Custom static files
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
📄 License
MIT License – Free to use and modify.

👨‍💻 Author
Made with ❤️ by Sabituly Dinmukhamed

yaml
Copy
Edit











