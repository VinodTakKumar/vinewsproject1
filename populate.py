import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','vinewsproject1.settings')
django.setup()


from faker import Faker
from testapp.models import *
from random import *
faker=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=faker.date()
        fcompany=faker.company()
        ftitle=faker.random_element(elements=('Project Manager','Team Lead','Software Engineer','Test Lead'))
        felegibility=faker.random_element(elements=('B-Tech','M-Tech','BCA','MCA','PHD'))
        faddress=faker.address()
        femail=faker.email()
        fphonenumber=phonenumbergen()
        p_jobs_rec=pune_jobs_tab.objects.get_or_create(date=fdate,company=fcompany,
        title=ftitle,elegibility=felegibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(30)
