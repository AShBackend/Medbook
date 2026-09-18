from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from . forms import ReserverForm

from .models import Doctor

from django.db.models import Q


def Doctors(request):
    query = request.GET.get("q", "")
    speciality = request.GET.get("speciality")
    doctors = Doctor.objects.all()
    if query:
        doctors = doctors.filter(Q(Fullname__icontains=query) | Q(speciality__Name__icontains=query) | Q(City__icontains=query))
    if speciality:
        doctors = doctors.filter(speciality__Name=speciality)
    return render(request, "Doctors/doctors.html", {"Doctors": doctors, "query": query, "speciality": speciality})

# ___________________________________________________________ 


def Profiles(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, "Doctors/doctor-profile.html", {"doctor": doctor})

# ___________________________________________________________

@login_required
def Appointment(request):
    if request.method == "POST":
        form = ReserverForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.Name = request.user
            appointment.save()
            messages.success(request, "رزرو شما با موفقیت انجام شد ❤️")
            return redirect("Home:Home")
    else:
        form = ReserverForm()
    return render(request, "Doctors/appointment.html", {"form": form})


