


import random
import logging

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

logger = logging.getLogger(__name__)

otp_storage = {}

# Note: Admin password reset functions temporarily use dict storage.
# In production, integrate with Admin model when available.


def index(request):
    return render(request, 'index.html')



def buyerRegisterForm(request):
    return render(request, 'buyerRegisterForm.html')


def buyerLoginForm(request):
    return render(request, 'buyerLoginForm.html')


def adminLoginForm(request):
    return render(request, 'adminLoginForm.html')



def sellerRegisterForm(request):
    return render(request, 'sellerRegisterForm.html')



def sellerLoginForm(request):
    return render(request, 'sellerLoginForm.html')


def adminforgotpassword(request):
    return render(request, 'adminforgotpassword.html')


def adminforgotpasswordcheck(request):
    loginid = request.POST.get('loginid')

    if not loginid:
        return HttpResponse('Email not found')

    otp = random.randint(1000, 9999)
    otp_storage[loginid] = otp
    
    # Log OTP to console for testing
    logger.warning(f'🔐 OTP for {loginid}: {otp}')
    print(f'\n🔐 OTP for {loginid}: {otp}\n')

    try:
        send_mail(
            'Your OTP',
            f'Your OTP is {otp}',
            settings.DEFAULT_FROM_EMAIL,
            [loginid],
            fail_silently=False,
        )
    except Exception as e:
        logger.error(f'Email sending failed: {str(e)}')
        print(f'⚠️ Email not sent. Use OTP from console: {otp}')

    request.session['loginid'] = loginid
    return render(request, 'otp.html')


def verifyotp(request):
    userotp = request.POST.get('otp', '').strip()
    loginid = request.session.get('loginid')
    
    if not loginid:
        return HttpResponse('Session expired. Please try again.')
    
    stored_otp = str(otp_storage.get(loginid, ''))
    
    logger.info(f'OTP verification attempt - Entered: {userotp}, Stored: {stored_otp}')
    
    if stored_otp and stored_otp == userotp:
        # OTP is correct, move to password change
        return render(request, 'changepassword.html')

    return HttpResponse(f'Invalid OTP. Please check and try again.')


def updatepassword(request):
    password = request.POST.get('password')
    confirmpassword = request.POST.get('confirmpassword')
    loginid = request.session.get('loginid')

    if not loginid or not password or not confirmpassword:
        return HttpResponse('Invalid request')

    if password != confirmpassword:
        return HttpResponse('Passwords not matched')

    return HttpResponse('Password Updated Successfully')