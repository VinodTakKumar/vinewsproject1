from django.shortcuts import render
from testapp.models import pune_jobs_tab
# Create your views here.

def home_page_view(request):
    return render(request,'testapp/home.html',context=None)

def pune_job_view(request):
    jobdetails=pune_jobs_tab.objects.all();
    return render(request,'testapp/pjobs.html',{'jobdetails':jobdetails})
