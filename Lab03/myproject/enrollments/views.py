from django.shortcuts import render



def payment_page(request):
    return render(request, 'payment.html')