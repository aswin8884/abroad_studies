from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Login_table(AbstractUser):
    usertype=models.CharField(max_length=25)

class Home_students(models.Model):

    name=models.CharField(max_length=25,null=True)
    address=models.CharField(max_length=150,null=True)
    contact=models.CharField(max_length=25,null=True)
    qualification=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    approvel=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)


class International_students(models.Model):

    name=models.CharField(max_length=25,null=True)
    nation=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=150,null=True)
    course=models.CharField(max_length=25,null=True)
    university=models.CharField(max_length=100,null=True)
    contact=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    id_proof=models.FileField(null=True)
    profile_picture=models.ImageField(null=True)
    approvel=models.BooleanField(default=False)
    converted=models.BooleanField(default=False)
    login_id=models.ForeignKey(Login_table,on_delete=models.CASCADE,null=True)


class Add_universites(models.Model):

    name=models.CharField(max_length=100,null=True)
    location=models.CharField(max_length=250,null=True)
    description=models.CharField(max_length=500,null=True)
    requirements=models.CharField(max_length=500,null=True)
    link=models.CharField(max_length=250,null=True)
    image_main=models.ImageField(null=True)
    image_sub=models.ImageField(null=True)

class Add_course(models.Model):

    course=models.CharField(max_length=50,null=True)
    level=models.CharField(max_length=50,null=True)
    details=models.CharField(max_length=150,null=True)
    requirements=models.CharField(max_length=500,null=True)
    application_link=models.CharField(max_length=500,null=True)
    uni_id=models.ForeignKey(Add_universites,on_delete=models.CASCADE,null=True)
    c_image=models.ImageField(null=True)
    
class Add_agency(models.Model):

    agency=models.CharField(max_length=50,null=True)
    location=models.CharField(max_length=150,null=True)
    link=models.CharField(max_length=150,null=True)
    contact=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    image=models.ImageField(null=True)

class Add_blog(models.Model):

    title=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=500,null=True)
    posted_date=models.DateField(null=True)
    image=models.ImageField(null=True)
    i_student_id=models.ForeignKey(International_students,on_delete=models.CASCADE,null=True)

class Messages(models.Model):

    message=models.CharField(max_length=500,null=True)
    reply=models.CharField(max_length=500,default='pending')
    send_on=models.DateTimeField(null=True)
    reply_on=models.DateTimeField(null=True)
    i_student_id=models.ForeignKey(International_students,on_delete=models.CASCADE,null=True)
    h_student_id=models.ForeignKey(Home_students,on_delete=models.CASCADE,null=True)

