from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.signup,name='signup'),
    path('signin/', views.signin,name='signin'),
    path('signout/', views.signout,name='signout'),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('profile/', views.profile,name='profile'),
    path('foodsharing/', views.foodsharing,name='foodsharing'),
    path('foodsharing/foodsharingform/', views.foodsharingform,name='foodsharingform'),
    path('buycategory/', views.buycategory,name='buycategory'),
    path('buycategory/rawfood/', views.rawfood,name='rawfood'),
    path('buycategory/cookedfood/', views.cookedfood,name='cookedfood'),
    path('buycategory/packedfood/', views.packedfood,name='packedfood'),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'),name='password_reset_complete'),

]



