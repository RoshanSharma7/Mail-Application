#  MailApp – Django-Based Email Sender

MailApp is a Django web application that allows users to register, log in, configure SMTP settings (like Gmail), and send emails securely from a web dashboard. All sent emails are stored and viewable in the dashboard.

---

## Features

-  User registration and login
-  SMTP configuration per user (supports Gmail or any custom SMTP)
-  Send plain text emails via secure SMTP
-  View sent email history in user dashboard
-  Built-in form validation
-  UTF-8 encoding support for non-ASCII characters

---

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, Bootstrap (optional)
- **Database**: SQLite (default), extendable to PostgreSQL/MySQL
- **SMTP**: Gmail or any SMTP server
- **Platform**: Linux Mint (developed on)

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/RoshanSharma7/Mail-Application.git
cd mailapp
```

2. **Create virtual environment**
```
python3 -m venv venv
source venv/bin/activate    # linux/Mac
venv/Script/Activate        # Windows
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Run migrations**
```
python manage.py migrate
```

5. **Start the server**
```
python manage.py runserver
```

---

## Gmail SMTP Setup
To use Gmail:

- Enable 2-Step Verification on your Google account
- Generate an App Password from: https://myaccount.google.com/apppasswords
- Use the generated password in your SMTP settings form

### How to get SMTP Password

### Step 1: Enable 2-Step Verification
- Go to https://myaccount.google.com/security
- Scroll to “Signing in to Google”
- Click on 2-Step Verification
- Set it up using your phone number or Google prompt

### Step 2: Generate an App Password
- After 2FA is enabled, go back to: https://myaccount.google.com/apppassword
- You may be asked to re-enter your password
- Under "Select app", choose "Mail"
- Under "Select device", choose "Other (Custom name)", and type: MailApp
- Click Generate

### Step 3: Copy the App Password
- Google will now show you a 16-character password like:
```
abcd efgh ijkl mnop
```

### Step 4: Use it in Django SMTP Settings
**4.1 Mention in Environment Variables.**  
If you prefer not to hard-code Gmail credentials:
Create a ```.env``` file and use ```python-decouple``` or ```django-environ``` to load:
```
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```
**4.2 Using UI For Setup SMTP Password.**  
- Run django server
```
python manage.py runserver
```
- Register your self in application
- Login in application
- Goto SMTP Setting
- Fill all the input fild like:
```
Smtp server: smtp.gmail.com          # Mandatory
Smtp port: 587                       # Mandatory
Email Host User: your_email
Email Host Password: generated 16 Char password
save
```
---

## Usage
- Register a new account
- Login and go to "SMTP Settings" to configure your email server
- Go to "Send Email", fill in the form, and hit Send
- View sent emails in your dashboard

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

## Author
### Roshan Kumar Sharma | Software Developer. 
You can reach out via: -
- Email: roshan.amlai96@gmail.com 
- LinkedIn: https://www.linkedin.com/in/RoshanSharma7/
- Twitter: https://www.twitter.com/imroshansharma7
- Portfolio: https://roshansharma7.github.io/Roshan.github.io/

---

#### If you found this helpful, please follow me on all platforms.
