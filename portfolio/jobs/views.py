from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def homepage(request):
    jobs=Job.objects.all()
    return render(request,'jobs/home.html',{'jobs':jobs})

def details(request, job_id):
    job_details=get_object_or_404(Job, pk=job_id)
    return render(request,'jobs/details.html',{'job':job_details})