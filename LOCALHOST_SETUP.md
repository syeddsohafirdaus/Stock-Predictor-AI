# Stock Market Price Detection - Local Development Setup

## 📋 System Requirements
- Python 3.8+
- pip (Python package manager)
- Git (optional, for version control)

## 🚀 Quick Start Guide

### Step 1: Navigate to Project Directory
```bash
cd C:\Users\syedd\Downloads\StockMarketPriceDetection-master\StockMarketPriceDetection-master
```

### Step 2: Activate Virtual Environment
If not already activated, run:
```bash
.venv\Scripts\Activate.ps1
```

For Command Prompt (cmd):
```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note:** This may take 5-10 minutes as it installs:
- Django 5.2.14
- TensorFlow 2.21.0
- PyTorch 2.12.0
- XGBoost, scikit-learn, pandas, numpy
- Transformers (for DialoGPT AI model)

### Step 4: Apply Database Migrations
```bash
python manage.py migrate
```

### Step 5: Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```
Follow prompts to create admin credentials.

### Step 6: Run Development Server
```bash
python manage.py runserver
```

You'll see output like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## 🌐 Access the Application

### Open in Browser:
- **Home Page:** http://localhost:8000/
- **User Login:** http://localhost:8000/UserLogin/
- **User Register:** http://localhost:8000/UserRegister/
- **Admin Login:** http://localhost:8000/AdminLogin/ (admin/admin)
- **AI Chat:** http://localhost:8000/ai-chat/
- **Django Admin:** http://localhost:8000/admin/

## 👤 Test Credentials

### Admin Login:
```
Login ID: admin
Password: admin
```

### Create User Account:
1. Go to http://localhost:8000/UserRegister/
2. Fill in the registration form
3. Login with created credentials
4. Admin must activate account at http://localhost:8000/RegisterUsersView/

## 📁 Project Structure
```
StockMarketPriceDetection-master/
├── manage.py                    # Django management
├── requirements.txt             # Python dependencies
├── db.sqlite3                   # Local database
├── admins/                      # Admin app
│   ├── views.py                # Admin views
│   └── utility/
│       └── foreCast_Model.py   # ML forecasting
├── users/                       # User app
│   ├── views.py                # User views
│   └── utility/
│       ├── ai_chat.py          # AI chatbot
│       ├── stock_predictions.py # ML predictions
│       └── FuturePredections.py # Future predictions
├── assets/
│   ├── templates/              # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── UserLogin.html      # 🆕 Modernized
│   │   ├── AdminLogin.html     # 🆕 Modernized
│   │   ├── UserRegistrations.html # 🆕 Modernized
│   │   ├── users/
│   │   │   ├── chat.html       # AI Chat
│   │   │   ├── UserHomePage.html
│   │   │   ├── ml_results.html
│   │   │   ├── futures.html
│   │   │   └── view_dataset.html
│   │   └── admins/
│   │       ├── AdminHome.html  # 🆕 Modernized
│   │       └── admin_future.html
│   └── static/
│       ├── css/
│       │   ├── custom-ui.css   # 🆕 Enhanced styling
│       │   └── bootstrap.min.css
│       ├── js/
│       └── fonts/
└── InternationalStock/
    ├── settings.py              # Django settings
    ├── urls.py                  # URL routing
    └── wsgi.py
```

## 🎯 Key Features

### ✨ New/Updated UI/UX
- **Modern Login Pages** - Centered card forms with validation
- **Feature Showcase Home** - Six feature cards with tech stack
- **Admin Portal** - Quick-action dashboard
- **Responsive Design** - Works on mobile, tablet, desktop
- **Professional Colors** - Blue/dark gradient theme
- **Form Validation** - Real-time Bootstrap validation feedback

### 🤖 AI Features
- **AI Chat Assistance** - DialoGPT-medium powered chatbot
- **Stock Predictions** - ML models for forecasting
- **Future Price Predictions** - LSTM with attention layers
- **Dataset Analysis** - CSV data visualization

### 🧠 ML Models
- **TensorFlow/Keras** - Deep Neural Networks (5-layer LSTM)
- **XGBoost** - Gradient boosting for predictions
- **Scikit-learn** - Classification and regression
- **Statsmodels** - Time series analysis
- **Pandas/NumPy** - Data processing

## ⚙️ Configuration

### settings.py Key Settings:
```python
DEBUG = True  # Development mode
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
```

## 🔧 Troubleshooting

### Issue: "Python not found"
**Solution:** Add Python to PATH or use full path:
```bash
C:\Python39\python.exe manage.py runserver
```

### Issue: "ModuleNotFoundError: transformers"
**Solution:** Reinstall requirements:
```bash
pip install --upgrade -r requirements.txt
```

### Issue: Database locked
**Solution:** Delete db.sqlite3 and run migrations again:
```bash
del db.sqlite3
python manage.py migrate
```

### Issue: Port 8000 already in use
**Solution:** Use different port:
```bash
python manage.py runserver 8001
```

### Issue: AI Chat model taking too long to load
**Solution:** This is normal on first run. DialoGPT-medium (~400MB) is downloaded and cached. Subsequent requests are faster.

## 📚 Common Commands

```bash
# Create new app
python manage.py startapp appname

# Make migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Shell
python manage.py shell

# Show URLs
python manage.py show_urls
```

## 🚀 Production Deployment

For deployment to production:
1. Set `DEBUG = False` in settings.py
2. Update `ALLOWED_HOSTS` with your domain
3. Use a production WSGI server (Gunicorn, uWSGI)
4. Set up PostgreSQL or MySQL instead of SQLite
5. Configure environment variables with `.env` file
6. Enable HTTPS and CSRF protection

## 📞 Support

For issues or questions:
1. Check logs in terminal
2. Visit http://localhost:8000/admin/ for database management
3. Review Django documentation: https://docs.djangoproject.com/

## ✅ Verification Checklist

- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip list` shows all packages)
- [ ] Database migrated (`db.sqlite3` file exists)
- [ ] Server running (no errors in terminal)
- [ ] Can access http://localhost:8000/ in browser
- [ ] Admin login works (admin/admin)
- [ ] Can register new user account
- [ ] AI Chat loads and responds
- [ ] ML predictions work on dashboard

---

**Last Updated:** May 20, 2026
**Django Version:** 5.2.14
**Python Version:** 3.8+
