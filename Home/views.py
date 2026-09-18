from django.shortcuts import render, redirect

from django.contrib import messages

from Doctors.models import Doctor

from django.db.models import Q

from . forms import ContactForm

# ___________________________________________________________

def Home(request):
    query = request.GET.get("q", "")
    doctors = Doctor.objects.all()
    if query:
        doctors = doctors.filter(Q(Fullname__icontains=query) | Q(speciality__Name__icontains=query) | Q(City__icontains=query))
    return render(request, "Home/index.html", {"doctors": doctors[:3], "query": query})

# ___________________________________________________________

def Aboutus(request):
    return render(request, "Home/about.html")

# ___________________________________________________________

def Contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد ممنون❤️")
            return redirect('Home:Home')
    else:
        form = ContactForm()
    return render(request, "Home/contact.html", {"form": form})

# ___________________________________________________________

def Services(request):
    return render(request, "Home/services.html")

# ___________________________________________________________

