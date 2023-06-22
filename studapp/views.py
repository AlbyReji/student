from django.shortcuts import render,redirect
from .models import Studentdb
from .forms import StudentForm

# Create your views here.

def base(request):

    return render(request ,'base.html')



def studhome(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studhome')

    context  = {"form":form}

    return render(request,'studapp_temp/home.html',context)



