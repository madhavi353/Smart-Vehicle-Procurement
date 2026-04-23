"""Smart_Vehicle_Procurement_System_using_Blockchain_Technology URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from Admin import views as av
from Buyers import views as bv
from Smart_Vehicle_Procurement_System_using_Blockchain_Technology import views as mv
from seller import views as sv


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mv.index, name='index'),

    # COMMON FORMS
    path('buyerRegisterForm', mv.buyerRegisterForm, name='buyerRegisterForm'),
    path('buyerLoginForm', mv.buyerLoginForm, name='buyerLoginForm'),
    path('adminforgotpassword', mv.adminforgotpassword, name='adminforgotpassword'),
    path('adminLoginForm', mv.adminLoginForm, name='adminLoginForm'),
    path('sellerRegisterForm', mv.sellerRegisterForm, name='sellerRegisterForm'),
    path('sellerLoginForm', mv.sellerLoginForm, name='sellerLoginForm'),
    path('adminforgotpasswordcheck', mv.adminforgotpasswordcheck, name='adminforgotpasswordcheck'),
    path('verifyotp', mv.verifyotp, name='verifyotp'),
    path('updatepassword', mv.updatepassword, name='updatepassword'),


    # ================= ADMIN URLS =================
    path('adminLoginCheck', av.adminLoginCheck, name='adminLoginCheck'),
    path('adminHome', av.adminHome, name='adminHome'),
    path('userdetails', av.userList, name='userdetails'),
    path('activate_user', av.activate_user, name='activate_user'),
    path('deactivate_user', av.deactivate_user, name='deactivate_user'),
    path('sellerdetails', av.sellerdetails, name='sellerdetails'),
    path('Sdeactivate_user', av.Sdeactivate_user, name='Sdeactivate_user'),
    path('Sactivate_user', av.Sactivate_user, name='Sactivate_user'),
    path('delete_seller', av.delete_seller, name='delete_seller'),
    path('deleteVehicle/<int:vehicle_id>/', av.deleteVehicle, name='adminDeleteVehicle'),
    path('vehicleList', av.vehicleList, name='vehicleList'),
    path('log', av.log, name='log'),

    # ================= BUYER URLS =================
    path('buyerHome', bv.buyerHome, name='buyerHome'),
    path('buyerRegisterCheck', bv.buyerRegisterCheck, name='buyerRegisterCheck'),
    path('buyerLoginCheck', bv.buyerLoginCheck, name='buyerLoginCheck'),
    path('browseVehicles', bv.browseVehicles, name='browseVehicles'),
    
    # 🔥 NEW PAYMENT FLOW
    path('payment/<int:id>/', bv.payment_page, name='payment_page'),
    path('process_payment', bv.process_payment, name='process_payment'),

    path('purchaseHistory', bv.purchase_history, name='purchaseHistory'),

    # ================= SELLER URLS =================
    path('sellerRegisterCheck', sv.sellerRegisterCheck, name='sellerRegisterCheck'),
    path('sellerLoginCheck', sv.sellerLoginCheck, name='sellerLoginCheck'),
    path('sellerHome', sv.sellerHome, name='sellerHome'),
    path('addVehicle', sv.addVehicle, name='addVehicle'),
    path('vehicleHistory', sv.vehicleHistory, name='vehicleHistory'),
    path('deleteVehicle/<int:vehicle_id>/', sv.deleteVehicle, name='deleteVehicle'),
    path('sellerForgotPassword', sv.sellerForgotPassword, name='sellerForgotPassword'),
    path('sellerForgotPasswordCheck', sv.sellerForgotPasswordCheck, name='sellerForgotPasswordCheck'),
    path('sellerVerifyOtp', sv.sellerVerifyOtp, name='sellerVerifyOtp'),
    path('sellerUpdatePassword', sv.sellerUpdatePassword, name='sellerUpdatePassword'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)