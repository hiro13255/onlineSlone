from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('', views.PaymentCheckoutView.as_view(), name='checkout'),
    path('create_checkout_session/', views.create_checkout_session, name='checkout_session'),
    path('success/', views.PaymentSuccessView.as_view(), name='success'),
    path('cancel/', views.PaymentCancelView.as_view(), name='cancel'),
]