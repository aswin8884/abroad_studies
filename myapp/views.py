from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from django.utils import timezone
from datetime import date
from django.db.models import Q


####################### COMMON PAGES #######################################

def index(request):

    return render(request,"index.html")

def login(request):

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype=="homestudent":
                    user = Home_students.objects.get(email=email)
                    if user.approvel:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/home_student_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')
                elif user.usertype=="internationalstudent":
                    user = International_students.objects.get(email=email)
                    if user.approvel:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/international_student_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')


    return render(request,"login.html")

def home_student_registration(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['address']
        contact=request.POST['contact']
        qualification=request.POST['qualification']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="homestudent")
        log.save()

        regi=Home_students.objects.create(
            name=name,
            address=address,
            contact=contact,
            qualification=qualification,
            email=email,
            id_proof=id_proof,
            login_id=log,
            profile_picture=profile_picture
        )
        regi.save()
        messages.info(request,"Registration successful,Wait admin approvel")

    return render(request,"home_student_registration.html")

def international_student_registration(request):

    if request.POST:
        name=request.POST['name']
        nation=request.POST['nation']
        city=request.POST['city']
        address=request.POST['address']
        contact=request.POST['contact']
        course=request.POST['course']
        university=request.POST['university']
        email=request.POST['email']
        password=request.POST['password']
        id_proof=request.FILES['id_proof']
        profile_picture=request.FILES['profile_picture']

        log=Login_table.objects.create_user(username=email,password=password,usertype="internationalstudent")
        log.save()

        regi=International_students.objects.create(
            name=name,
            nation=nation,
            city=city,
            address=address,
            contact=contact,
            course=course,
            email=email,
            university=university,
            id_proof=id_proof,
            profile_picture=profile_picture,
            login_id=log
        )
        regi.save()
        messages.info(request,"Registration successful,Wait admin approvel")

    return render(request,"international_student_registration.html")

####################### ADMIN PAGES #######################################

def admin_home(request):

    home_students_count=0
    international_students_count=0
    universites_count=0
    courses_count=0

    home_students=Home_students.objects.filter(approvel=True)
    international_students=International_students.objects.filter(approvel=True)
    universites=Add_universites.objects.all()
    courses=Add_universites.objects.all()
   

    for h in home_students:
        home_students_count+=1
        h.id

    for i in international_students:
        international_students_count+=1
        i.id

    for u in universites:
        universites_count+=1
        u.id

    for c in courses:
        courses_count+=1
        c.id
 

    return render(request,"admin/admin_home.html",
    {
       "home_students_count":home_students_count,
       "international_students_count":international_students_count,
       "universites_count":universites_count,
       "courses_count":courses_count,
    })


def view_home_students_request(request):

    students=Home_students.objects.all()

    return render(request,"admin/view_home_students_request.html",{"students":students})

def view_international_students_request(request):

    students=International_students.objects.all()

    return render(request,"admin/view_international_students_request.html",{"students":students})


def accept_home_student(request):

    sid=request.GET.get('id')
    student=Home_students.objects.get(id=sid)
    student.approvel=True
    student.save()
    
    messages.info(request,"Accepted")
    return redirect('/view_home_students_request')

def reject_home_student(request):

    sid=request.GET.get('id')
    student=Home_students.objects.get(id=sid)
    student.delete()
    log=Login_table.objects.get(username=student.login_id)
    log.delete()
    
    messages.info(request,"Rejected")


    return redirect('/view_home_students_request')

def accept_international_student(request):

    sid=request.GET.get('id')
    student=International_students.objects.get(id=sid)
    student.approvel=True
    student.save()
    
    messages.info(request,"Accepted")

    return redirect('/view_international_students_request')

def reject_international_student(request):

    sid=request.GET.get('id')
    student=International_students.objects.get(id=sid)
    student.delete()
    log=Login_table.objects.get(id=student.login_id)
    log.delete()
    
    messages.info(request,"Rejected")

    return redirect('/view_international_students_request')

def view_home_students(request):

    students=Home_students.objects.filter(approvel=True)

    return render(request,"admin/view_home_students.html",{"students":students})

def view_international_students(request):

    students=International_students.objects.filter(approvel=True)

    return render(request,"admin/view_international_students.html",{"students":students})

def delete_home_student(request):

    sid=request.GET.get('id')
    student=Home_students.objects.get(id=sid)
    student.delete()
    log=Login_table.objects.get(username=student.login_id)
    log.delete()
    messages.info(request,"Deleted Sucessful")
    return redirect('/view_home_students')

def delete_international_student(request):

    sid=request.GET.get('id')
    student=International_students.objects.get(id=sid)
    student.delete()
    log=Login_table.objects.get(username=student.login_id)
    log.delete()
    messages.info(request,"Deleted Sucessful")
    return redirect('/view_international_students')

def add_universites(request):

    if request.POST:
        name=request.POST['name']
        location=request.POST['location']
        description=request.POST['description']
        requirements=request.POST['requirements']
        image_main=request.FILES['image_main']
        image_sub=request.FILES['image_sub']
        link=request.POST['link']

        uni=Add_universites.objects.create(
            name=name,
            location=location,
            description=description,
            requirements=requirements,
            image_main=image_main,
            image_sub=image_sub,
            link=link
        )
        uni.save()
        messages.info(request,"Added sucessfully")
        redirect('/add_universites')

    return render(request,"admin/add_universites.html")

def view_universites_admin(request):

    universites=Add_universites.objects.all()

    return render(request,"admin/view_universites_admin.html",{"universites":universites})

def update_universites(request):
    uid=request.GET.get('id')
    universites=Add_universites.objects.get(id=uid)

    if request.method == 'POST':
        section_name=request.POST["name"]
        universites.section_name=section_name
        location=request.POST["location"]
        universites.location=location
        description=request.POST["description"]
        universites.description=description
        requirements=request.POST["requirements"]
        universites.requirements=requirements
        link=request.POST["link"]
        universites.link=link
        image_main=request.FILES["image_main"]
        universites.image_main=image_main
        image_sub=request.FILES["image_sub"]
        universites.image_sub=image_sub

        universites.save()
      
        messages.info(request, "Updated Successfully")
        return redirect('/view_universites_admin')


    return render(request,"admin/update_universites.html",{"universites":universites})


def delete_universites(request):

    uid=request.GET.get('id')
    universites=Add_universites.objects.get(id=uid)
    universites.delete()
    messages.info(request, "Removed Successfully")

    return redirect("/view_universites_admin")

def add_courses_admin(request):

    universites=Add_universites.objects.all()

    if request.POST:
        course=request.POST['course']
        level=request.POST['level']
        details=request.POST['details']
        requirements=request.POST['requirements']
        application_link=request.POST['application_link']
        c_image=request.FILES['c_image']
        uni_id=request.POST['uni_id']

        uni=Add_universites.objects.get(id=uni_id)
       
        c=Add_course.objects.create(
            course=course,
            level=level,
            details=details,
            requirements=requirements,
            application_link=application_link,
            c_image=c_image,
            uni_id=uni
        )
        c.save()
        messages.info(request,"Added sucessfully")
        redirect('/add_courses')

    return render(request,"admin/add_courses.html",{"universites":universites})

def view_courses_admin(request):

    course=Add_course.objects.all()

    return render(request,"admin/view_courses_admin.html",{"course":course})

def update_course(request):

    cid=request.GET.get('id')
    c=Add_course.objects.get(id=cid)
    universites=Add_universites.objects.all()

    if request.method == 'POST':
        course=request.POST["course"]
        c.course=course
        level=request.POST["level"]
        c.level=level
        details=request.POST["details"]
        c.details=details
        requirements=request.POST["requirements"]
        c.requirements=requirements
        application_link=request.POST["application_link"]
        c.application_link=application_link
        uni_id=request.POST["uni_id"]
        c.uni_id=uni_id
        c_image=request.FILES["c_image"]
        c.c_image=c_image

        c.save()
      
        messages.info(request, "Updated Successfully")
        return redirect('/view_courses_admin')

    return render(request,'admin/update_course.html',{
        "course":c,
        "universites":universites
        })

def delete_course(request):

    cid=request.GET.get('id')
    course=Add_course.objects.get(id=cid)
    course.delete()
    messages.info(request, "Removed Successfully")

    return redirect('/view_courses_admin')

def add_agency(request):

    if request.POST:
        agency=request.POST['agency']
        contact=request.POST['contact']
        location=request.POST['location']
        link=request.POST['link']
        email=request.POST['email']
        a_image=request.FILES['a_image']

        agency=Add_agency.objects.create(
            agency=agency,
            contact=contact,
            email=email,
            link=link,
            location=location,
            image=a_image
        )
        agency.save()
        messages.info(request,"Added successfully")

    return render(request,"admin/add_agency.html")

def view_agency_admin(request):

    agency=Add_agency.objects.all()

    return render(request,"admin/view_agency.html",{"agency":agency})

def update_agency(request):

    aid=request.GET.get('id')
    a=Add_agency.objects.get(id=aid)

    if request.method == 'POST':
        agency=request.POST['agency']
        a.agency=agency
        contact=request.POST['contact']
        a.contact=contact
        email=request.POST['email']
        a.email=email
        location=request.POST['location']
        a.location=location
        link=request.POST['link']
        a.link=link
        a_image=request.FILES['a_image']
        a.image=a_image
        a.save()
        messages.info(request,"Sucessfully updated")

        return redirect('/view_agency_admin')

    return render(request,"admin/update_agency.html",{"agency":a})

def delete_agency(request):

    aid=request.GET.get('id')
    agency=Add_agency.objects.get(id=aid)
    agency.delete()
    messages.info(request,"Deleted Sucessfully")

    return redirect('/view_agency_admin')




####################### HOME STUDENT PAGES #######################################

def home_student_home(request):

    id=request.session['id']
    student=Home_students.objects.get(id=id)

    return render(request,"home_student/home_student_home.html",{"student":student})

def view_universities_home_students(request):

    universites=Add_universites.objects.all()

    return render(request,"home_student/view_universites_home_students.html",{"universites":universites})

def view_universities_home_students_single(request):

    uid=request.GET.get('id')
    university=Add_universites.objects.get(id=uid)

    return render(request,"home_student/view_universities_home_students_single.html",{"university":university})

def view_courses_home_students(request):

    courses=Add_course.objects.all()

    return render(request,"home_student/view_courses_home_students.html",{"courses":courses})

def view_course_home_students_single(request):

    cid=request.GET.get('id')
    course=Add_course.objects.get(id=cid)

    return render(request,"home_student/view_course_home_students_single.html",{"course":course})

def view_courses_by_university(request):

    uid=request.GET.get('id')
    university=Add_universites.objects.get(id=uid)
    courses=Add_course.objects.filter(uni_id=university)

    return render(request,"home_student/view_courses_by_university.html",{"courses":courses})

def view_agency_home_students(request):

    agency=Add_agency.objects.all()

    return render(request,"home_student/view_agency_home_students.html",{"agency":agency})

def view_blogs_home_students(request):

    blogs=Add_blog.objects.all()

    return render(request,"home_student/view_blogs_home_students.html",{"blogs":blogs})

def view_international_students_by_home_students(request):

    students=International_students.objects.filter(approvel=True)

    return render(request,"home_student/view_international_students_by_home_students.html",{"students":students})

def message_to_international_students(request):

    id=request.session['id']
    h_student_id=Home_students.objects.get(id=id)
    sid=request.GET.get('id')
    i_student_id=International_students.objects.get(id=sid)

    if request.POST:
        message=request.POST['message']
        
        msg=Messages.objects.create(
            message=message,
            send_on=timezone.now(),
            h_student_id=h_student_id,
            i_student_id=i_student_id,
            )
        msg.save()
        messages.info(request,"Message sent successful")
        return redirect('/replies_from_international_students')

    return render(request,"home_student/message_to_international_students.html")



def replies_from_international_students(request):

    id=request.session['id']
    student_id=Home_students.objects.get(id=id)

    message=Messages.objects.filter(h_student_id=student_id)

    return render(request,"home_student/replies_from_international_students.html",{"message":message})

def view_profile_home_students(request):

    id=request.session['id']
    student=Home_students.objects.get(id=id)

    return render(request,"home_student/view_profile_home_students.html",{"student":student})

def edit_profile_home_students(request):

    sid=request.GET.get('id')
    student=Home_students.objects.get(id=sid)

    if request.method == 'POST':
        name=request.POST['name']
        student.name=name
        address=request.POST['address']
        student.address=address
        contact=request.POST['contact']
        student.contact=contact
        profile_picture=request.FILES['profile_picture']
        student.profile_picture=profile_picture
        student.save()
    
        messages.info(request,"Sucessfully updated")

        return redirect('/view_profile_home_students')



    return render(request,"home_student/edit_profile_home_students.html",{"student":student})

def move_account_to_international(request):

    sid=request.GET.get('id')
    student=Home_students.objects.get(id=sid)

    if request.POST:
        nation=request.POST['nation']
        address=request.POST['address']
        city=request.POST['city']
        course=request.POST['course']
        university=request.POST['university']

        international=International_students.objects.create(

            nation=nation,
            city=city,
            course=course,
            university=university,
            address=address,
            name=student.name,
            contact=student.contact,
            email=student.email,
            id_proof=student.id_proof,
            profile_picture=student.profile_picture,
            login_id=student.login_id,
            approvel=True,
            converted=True
        )
        international.save()
        log=Login_table.objects.get(username=student.login_id)
        log.usertype="internationalstudent"
        log.save()
        student.delete()
        messages.info(request,"Youre account successfully converted,please re-login")
        return redirect('/login')


    return render(request,"home_student/move_account_to_international.html",{"student":student})




####################### INTERNATIONAL STUDENT PAGES #######################################

def international_student_home(request):

    id=request.session['id']
    student=International_students.objects.get(id=id)

    return render(request,"international_student/international_student_home.html",{"student":student})

def add_blog_interntional_students(request):

    id = request.session['id']
    student_id=International_students.objects.get(id=id)

    if request.POST:
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES['image']

        blog=Add_blog.objects.create(
            title=title,
            description=description,
            image=image,
            posted_date=timezone.now(),
            i_student_id=student_id
        )

        blog.save()
        messages.info(request,"Posted Sucessfully")

    return render(request,"international_student/add_blog_interntional_students.html")

def view_blogs_international_students(request):

    blogs=Add_blog.objects.all()

    return render(request,"international_student/view_blogs_international_students.html",{"blogs":blogs})


def view_messages_from_home_students(request):

    id=request.session['id']
    student_id=International_students.objects.get(id=id)

    message=Messages.objects.filter(i_student_id=student_id)

    return render(request,"international_student/view_messages_from_home_students.html",{"message":message})

def reply_to_home_students(request):

    mid=request.GET.get('id')
    msg=Messages.objects.get(id=mid)

    if request.method == 'POST':
        reply=request.POST["replay"]
        msg.reply=reply
        msg.reply_on=timezone.now()
        msg.save()
        messages.info(request,"Reply sent successfull")
        return redirect('/view_messages_from_home_students')

    return render(request,"international_student/reply_to_home_students.html")

def view_profile_international_students(request):

    id=request.session['id']
    student=International_students.objects.get(id=id)

    return render(request,"international_student/view_profile_international_students.html",{"student":student})

def edit_profile_international_students(request):

    sid=request.GET.get('id')
    student=International_students.objects.get(id=sid)

    if request.method == 'POST':
        name=request.POST['name']
        student.name=name
        nation=request.POST['nation']
        student.nation=nation
        city=request.POST['city']
        student.city=city
        address=request.POST['address']
        student.address=address
        course=request.POST['course']
        student.course=course   
        university=request.POST['university']
        student.university=university
        contact=request.POST['contact']
        student.contact=contact
        profile_picture=request.FILES['profile_picture']
        student.profile_picture=profile_picture
        student.save()
    
        messages.info(request,"Sucessfully updated")

        return redirect('/view_profile_international_students')



    return render(request,"international_student/edit_profile_international_students.html",{"student":student})


def view_universities_international_students(request):

    universites=Add_universites.objects.all()

    return render(request,"international_student/view_universites_i_students.html",{"universites":universites})

def view_universities_international_students_single(request):

    uid=request.GET.get('id')
    university=Add_universites.objects.get(id=uid)

    return render(request,"international_student/view_universities_i_students_single.html",{"university":university})

def view_courses_international_students(request):

    courses=Add_course.objects.all()

    return render(request,"international_student/view_courses_i_students.html",{"courses":courses})

def view_course_international_students_single(request):

    cid=request.GET.get('id')
    course=Add_course.objects.get(id=cid)

    return render(request,"international_student/view_course_i_students_single.html",{"course":course})

def view_courses_by_university_international_students(request):

    uid=request.GET.get('id')
    university=Add_universites.objects.get(id=uid)
    courses=Add_course.objects.filter(uni_id=university)

    return render(request,"international_student/view_courses_by_i_students_university.html",{"courses":courses})