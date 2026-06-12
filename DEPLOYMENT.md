# Deployment Guide

## Quick Start - Choose Your Option

This guide provides two ways to deploy and run the Stock Market Price Detection application:
- **Option A**: Run locally without Docker (simpler, faster to get started)
- **Option B**: Run with Docker (for production deployment and containerization)

---

## Option A: Local Deployment (No Docker Required)

This is the quickest way to get the application running on your machine.

### Prerequisites
- Python 3.11 or later (recommended for this project)
- PowerShell (Windows) or Terminal (Mac/Linux)
- Git (optional, for version control)

### Step-by-Step Instructions

#### Step 1: Navigate to the project directory
Open PowerShell and run:
```powershell
cd "C:\Users\syedd\Downloads\StockMarketPriceDetection-master\StockMarketPriceDetection-master"
```

#### Step 2: Create a Python virtual environment
```powershell
python -m venv venv
```

This creates an isolated Python environment for your project.

#### Step 3: Activate the virtual environment
```powershell
.\venv\Scripts\Activate
```

Your prompt should now show `(venv)` at the beginning.

#### Step 4: Install project dependencies
```powershell
pip install -r requirements.txt
```

This installs all required Python packages including Django, pandas, numpy, scikit-learn, etc.

#### Step 4.5: Create and configure .env file
The `.env` file contains your secret configuration variables. It's automatically loaded by Django.

The `.env` file is already configured with your Django secret key:
```
DJANGO_SECRET_KEY=xoc3kuPrTjtcNELgOSvVp4W3fh2MrC6sXCCOmPJYKUG7XJ2wrzf8rBIIYCn5BZ4gI5o
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,127.0.0.1:8000
```

**Important:** Never commit `.env` to version control. The `.gitignore` file already excludes it.

#### Step 5: Apply database migrations
```powershell
python manage.py migrate
```

This sets up the SQLite database with necessary tables.

#### Step 6: Create a superuser (admin account)
```powershell
python manage.py createsuperuser
```

Follow the interactive prompts:
- Enter username (e.g., `admin`)
- Enter email address
- Enter password (you'll be asked to confirm)

#### Step 7: Start the Django development server
```powershell
python manage.py runserver
```

You should see output like:
```
Starting development server at http://127.0.0.1:8000/
```

#### Step 8: Access the application
Open your web browser and go to:
```
http://127.0.0.1:8000
```

You should see the Stock Market Price Detection home page.

#### Step 9: Access the admin panel
Navigate to:
```
http://127.0.0.1:8000/admin
```

Login with the superuser credentials you created in Step 6.

---

## Option B: Docker Deployment (Production-Ready)

Use this option if you want to containerize the application for production or cloud deployment.

### Prerequisites
- Docker Desktop installed and running
- PowerShell or Terminal
- 2-4 GB available disk space

### Step-by-Step Instructions

#### Step 1: Install Docker Desktop

1. Visit https://www.docker.com/products/docker-desktop
2. Download the Windows version
3. Run the installer and follow the setup wizard
4. Restart your computer
5. Verify installation by opening PowerShell and running:
```powershell
docker --version
```

#### Step 2: Navigate to the project directory
```powershell
cd "C:\Users\syedd\Downloads\StockMarketPriceDetection-master\StockMarketPriceDetection-master"
```

#### Step 3: Build the Docker image
```powershell
docker build -t stock-market-app .
```

This process takes 2-5 minutes. It downloads Python 3.11, installs dependencies, and creates the container image.

#### Step 4: Run the container
```powershell
docker run -p 8000:8000 stock-market-app
```

The `-p 8000:8000` flag maps port 8000 from the container to your machine.

#### Step 5: Access the application
Open your web browser and go to:
```
http://127.0.0.1:8000
```

#### Step 6: Stop the container
Press `Ctrl + C` in PowerShell to stop the running container.

---

## Post-Deployment Configuration

### Setting Environment Variables (For Production)

When deploying to a cloud platform (Vercel, Azure, AWS, etc.), set these environment variables:

#### Required Variables
```
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

#### How to set on different platforms:

**Windows (PowerShell) - For Local Testing:**
```powershell
$env:DJANGO_SECRET_KEY="your-secret-key"
$env:DJANGO_DEBUG="False"
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost"
```

**Vercel:**
1. Go to your Vercel project settings
2. Navigate to "Environment Variables"
3. Add each variable listed above
4. Re-deploy

**Azure:**
1. Go to your App Service
2. Navigate to "Configuration"
3. Add each variable under "Application settings"
4. Save and restart

**AWS (Elastic Beanstalk):**
1. Go to your environment
2. Click "Configuration"
3. Edit "Software" section
4. Add environment properties

### Switching from SQLite to PostgreSQL (Production)

For production deployments, replace SQLite with PostgreSQL:

1. Install psycopg2:
```powershell
pip install psycopg2-binary
```

2. Update `requirements.txt`:
```
psycopg2-binary==2.9.6
```

3. Modify `InternationalStock/settings.py` to use PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
```

4. Set database environment variables on your host platform

---

## Troubleshooting

### Issue: `python` command not found
**Solution:** Make sure Python 3.11+ is installed and added to PATH. Download from https://www.python.org/downloads/

### Issue: Virtual environment activation fails
**Solution:** Use the full path:
```powershell
& "C:\path\to\venv\Scripts\Activate.ps1"
```

### Issue: `pip install` fails with permission denied
**Solution:** Make sure the virtual environment is activated first (you should see `(venv)` in your prompt)

### Issue: TensorFlow install fails on Windows due to long paths
**Solution:** Create a virtual environment in a short path, then install dependencies from there:
```powershell
python -m venv C:\tmp\stockenv
C:\tmp\stockenv\Scripts\python.exe -m pip install --upgrade pip
C:\tmp\stockenv\Scripts\python.exe -m pip install -r requirements.txt
```
If you prefer to keep the venv inside the project, enable Windows long path support in your system settings.

### Issue: Port 8000 already in use
**Solution:** Either stop the other process or use a different port:
```powershell
python manage.py runserver 8001
```

### Issue: Docker build fails
**Solution:** 
1. Make sure Docker Desktop is running
2. Check your internet connection
3. Try: `docker build --no-cache -t stock-market-app .`

### Issue: Database errors
**Solution:** Run migrations again:
```powershell
python manage.py migrate --run-syncdb
```

---

## First Time User Login

1. **Create Admin Account:**
   - Run: `python manage.py createsuperuser`
   - Follow the prompts

2. **Create Regular User Account:**
   - Go to http://127.0.0.1:8000/UserRegister/
   - Fill in registration details
   - Submit

3. **Admin Approval (Required):**
   - Login to admin: http://127.0.0.1:8000/admin
   - Go to "Users" section
   - Approve the newly registered user

4. **User Login:**
   - Go to http://127.0.0.1:8000/UserLogin/
   - Login with approved credentials
   - Access prediction features

---

## Deactivating Virtual Environment

When you're done working, deactivate the virtual environment:

```powershell
deactivate
```

---

## Project Structure Reference

```
StockMarketPriceDetection-master/
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python version for hosting
├── Dockerfile                 # Container configuration
├── build_files.sh             # Build script for deployment
├── db.sqlite3                 # Development database
├── InternationalStock/        # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL routing
│   ├── wsgi.py               # WSGI application
│   └── views.py              # Main views
├── admins/                    # Admin app
│   ├── views.py
│   ├── models.py
│   └── utility/
│       └── foreCast_Model.py # Forecasting AI model
├── users/                     # User app
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── utility/
│       ├── stock_predictions.py
│       └── FuturePredections.py
└── assets/                    # Static files
    ├── static/               # CSS, JS, Images
    └── templates/            # HTML templates
```

---

## Useful Commands Reference

### Development
```powershell
# Create superuser
python manage.py createsuperuser

# Apply migrations
python manage.py migrate

# Create new migration
python manage.py makemigrations

# Run tests
python manage.py test

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver
```

### Docker
```powershell
# Build image
docker build -t stock-market-app .

# Run container
docker run -p 8000:8000 stock-market-app

# List running containers
docker ps

# Stop container
docker stop <container_id>

# View logs
docker logs <container_id>
```

---

## Support & Next Steps

### To Test the Application:
1. Create a user account via registration
2. Wait for admin approval
3. Login and test stock prediction features
4. Try different stock symbols (AMZN, GOOGL, etc.)

### To Deploy to Production:
1. Follow Option B (Docker)
2. Set environment variables
3. Replace SQLite with PostgreSQL
4. Deploy to your cloud platform (Vercel, Azure, AWS, etc.)
5. Configure domain and SSL certificate

### To Modify the Code:
1. Edit files in the `users/`, `admins/`, or other app folders
2. Test locally with `python manage.py runserver`
3. Rebuild Docker image if deploying
4. Commit changes to version control (Git)

---

**Last Updated:** May 2026  
**Python Version:** 3.11+  
**Django Version:** 2.2  
**Docker Support:** Yes
