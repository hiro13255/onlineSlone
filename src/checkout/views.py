from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse
from django.shortcuts import redirect
from django.http import JsonResponse

import os
import stripe
import json
import environ

env = environ.Env()
env.read_env('.env')



# Create your views here.
class PaymentCheckoutView(generic.TemplateView):
    template_name = 'payment/checkout.html'

class PaymentSuccessView(generic.TemplateView):
    template_name = 'payment/success.html'

class PaymentCancelView(generic.TemplateView):
    template_name = 'payment/cancel.html'

def create_checkout_session(request):
    stripe.api_key = env('STRIPE_SECRET_KEY')

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'jpy',
                        'unit_amount': 980,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('checkout:success')),
            cancel_url=request.build_absolute_uri(reverse('checkout:cancel')),
        )
        print("hi")
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error':str(e)})
