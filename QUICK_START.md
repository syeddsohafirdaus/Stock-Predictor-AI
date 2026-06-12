# 🚀 Quick Start - 5 Minutes to Running

## 1️⃣ Open Terminal
```bash
cd C:\Users\syedd\Downloads\StockMarketPriceDetection-master\StockMarketPriceDetection-master
```

## 2️⃣ Activate Virtual Environment
```bash
.venv\Scripts\Activate.ps1
```

## 3️⃣ Install Requirements (First Time Only)
```bash
pip install -r requirements.txt
```
⏳ This takes 5-10 minutes on first run.

## 4️⃣ Run Server
```bash
python manage.py runserver
```

## 5️⃣ Open Browser
👉 **http://localhost:8000/**

---

## 🔗 Important URLs

| Page | URL |
|------|-----|
| 🏠 Home | http://localhost:8000/ |
| 👤 User Login | http://localhost:8000/UserLogin/ |
| 📝 Register | http://localhost:8000/UserRegister/ |
| 🔐 Admin Login | http://localhost:8000/AdminLogin/ |
| 💬 AI Chat | http://localhost:8000/ai-chat/ |
| ⚙️ Django Admin | http://localhost:8000/admin/ |

---

## 👤 Test Logins

**Admin:**
```
ID: admin
Password: admin
```

**User:** Create new via registration page

---

## 🎨 What's New - UI/UX

✅ Modern login pages
✅ Beautiful forms with validation
✅ Professional color scheme
✅ Responsive design (mobile, tablet, desktop)
✅ Interactive elements with smooth animations
✅ Admin dashboard with quick actions
✅ Feature showcase homepage
✅ Enhanced AI chat interface

---

## 📁 Files Modified

| File | Changes |
|------|---------|
| `UserLogin.html` | Modernized form design |
| `AdminLogin.html` | Admin portal styling |
| `UserRegistrations.html` | Multi-column form |
| `index.html` | Feature showcase |
| `AdminHome.html` | Dashboard cards |
| `custom-ui.css` | Enhanced styling |

---

## 🛠️ If Something Goes Wrong

**Port 8000 in use?**
```bash
python manage.py runserver 8001
```

**Dependencies missing?**
```bash
pip install --upgrade -r requirements.txt
```

**Database issues?**
```bash
del db.sqlite3
python manage.py migrate
```

---

## 📊 Tech Stack

- **Backend:** Django 5.2.14
- **Frontend:** Bootstrap 5 + Custom CSS
- **Database:** SQLite (local)
- **ML:** TensorFlow, XGBoost, Scikit-learn
- **AI:** DialoGPT-medium
- **Python:** 3.8+

---

## 📞 Need Help?

1. Check **LOCALHOST_SETUP.md** for detailed setup
2. Check **UI_UX_CHANGES.md** for design details
3. Check terminal output for specific errors
4. Visit http://localhost:8000/admin/ for database management

---

**✅ Setup Complete! Happy Coding!**
