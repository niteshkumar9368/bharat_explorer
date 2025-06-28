# 🇮🇳 Bharat Explorer

**Bharat Explorer** is a travel discovery web application built with Django that lets users explore tourist destinations across India, state-wise. Logged-in users can also add destinations to their wishlist for future trips.

🚀 **Live Demo:** [Visit the Live Website](https://nitesh05.pythonanywhere.com/)

---

## 🌟 Features

- 🗺️ Browse Indian tourist destinations by **state**
- 🖼️ View place details with **images**, **location map**, and **best time to visit**
- ❤️ Add/remove tourist places to your **personal wishlist**
- 🔐 User **registration and login system**
- 🧭 Gallery view with multiple images for each tourist place
- ✨ Fully responsive and clean UI

---

## 🛠️ Tech Stack

- **Backend:** Django 5.x (Python)
- **Frontend:** HTML, CSS, Bootstrap (Django templates)
- **Database:** SQLite
- **Authentication:** Django's built-in auth system
- **Deployment:** [PythonAnywhere](https://www.pythonanywhere.com/)

---

## 🧩 How to Run Locally

### 1. Clone this repository
```bash
git clone https://github.com/niteshkumar9368/bharat_explorer.git
cd bharat_explorer
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
bharat_explorer/
│
├── core/                    # Project settings and configurations
├── accounts/                # User login and registration
├── places/                  # Tourist places and wishlist features
├── media/                   # Uploaded place images
├── static/                  # Static files (CSS, JS, images)
├── db.sqlite3               # SQLite database
├── manage.py                # Django CLI utility
├── .gitignore               # Files and folders to ignore in git
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies


🧾 License
This project is licensed under the MIT License. You can use, modify, and distribute it freely.

👨‍💻 Author
Nitesh Kumar
📧 niteshkumar2004.in@gmail.com
🔗 GitHub Profile
