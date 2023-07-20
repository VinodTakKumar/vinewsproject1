from django.urls import path
from testapp import views

urlpatterns = [
    path('home_page_view/',views.home_page_view),
    path('pune_job_view/',views.pune_job_view),
]
