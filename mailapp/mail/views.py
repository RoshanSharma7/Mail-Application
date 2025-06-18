from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SMTPForm, EmailForm
from .models import SMTPSetting, SentEmail
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.header import Header
import unicodedata
import quopri
from email.utils import formataddr
from django.contrib import messages
# from django.utils import strip_tags 

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = None
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            error = "Invalid username or password"
    return render(request, 'login.html', {'error': error})

@login_required
def dashboard_view(request):
    emails = SentEmail.objects.filter(user=request.user).order_by('-sent_at')
    return render(request, 'dashboard.html', {'emails': emails})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def smtp_settings_view(request):
    smtp = SMTPSetting.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = SMTPForm(request.POST, instance=smtp)
        if form.is_valid():
            smtp_obj = form.save(commit=False)
            smtp_obj.user = request.user
            smtp_obj.save()
            return redirect('dashboard')
    else:
        form = SMTPForm(instance=smtp)
    return render(request, 'smtp_settings.html', {'form': form})


@login_required
def send_mail_view(request):
    smtp = SMTPSetting.objects.filter(user=request.user).first()
    error = None

    if not smtp:
        error = "Please configure SMTP settings first."

    if request.method == 'POST' and smtp:
        form = EmailForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Clean input (remove non-breaking space)
            subject = data['subject'].replace('\xa0', ' ').strip()
            message = data['message'].replace('\xa0', ' ').strip()
            to_email = data['to_email'].replace('\xa0', ' ').strip()
            from_email = smtp.email_host_user.strip()

            try:
                msg = EmailMessage()

                # Set message content with UTF-8 charset
                msg.set_content(message)
                
                # Encode Subject properly using quopri (quoted-printable)
                encoded_subject = quopri.encodestring(subject.encode('utf-8')).decode('utf-8')
                msg['Subject'] = f"=?utf-8?q?{encoded_subject}?="

                msg['From'] = formataddr(("Sender", from_email))
                msg['To'] = to_email

                server = smtplib.SMTP(smtp.smtp_server, smtp.smtp_port)
                server.starttls()
                server.login(from_email, smtp.email_host_password)
                server.send_message(msg)
                server.quit()

                SentEmail.objects.create(
                    user=request.user,
                    to_email=to_email,
                    subject=subject,
                    message=message
                )

                return redirect('dashboard')

            except Exception as e:
                error = f"Error sending email: {e}"

    else:
        form = EmailForm()

    return render(request, 'send_mail.html', {'form': form, 'error': error})

def delete_mail(request, mail_id):
    try:
        email = SentEmail.objects.get(id=mail_id, user=request.user)
        email.delete()
        messages.success(request, "Email deleted successfully.")
    except SentEmail.DoesNotExist:
        messages.error(request, "Email not found or access denied.")
    return redirect('dashboard')
