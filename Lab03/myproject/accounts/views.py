from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # اذا ما كان في اعدادات templets مارح اقدر اكتب الصفحة بدون الامتداد بعدين احنا كتبنا اسم الرابط وليس الملف
            return redirect('home')  # تقدر تغيره لأي صفحة ثانية
        else:
            messages.error(request, "البيانات غير صحيحة")

    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')