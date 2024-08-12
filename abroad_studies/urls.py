
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path("login", views.login),
    path("home_student_registration", views.home_student_registration),
    path("international_student_registration", views.international_student_registration),
    ################### admin pages ###########################
    path("admin_home", views.admin_home),
    path("home_student_home", views.home_student_home),
    path("international_student_home", views.international_student_home),
    path("view_home_students_request", views.view_home_students_request),
    path("view_international_students_request", views.view_international_students_request),
    path("accept_home_student", views.accept_home_student),
    path("reject_home_student", views.reject_home_student),
    path("accept_international_student", views.accept_international_student),
    path("reject_international_student", views.reject_international_student),
    path("view_home_students", views.view_home_students),
    path("view_international_students", views.view_international_students),
    path("add_universites", views.add_universites),
    path("view_universites_admin", views.view_universites_admin),
    path("update_universites", views.update_universites),
    path("delete_universites", views.delete_universites),
    path("add_courses_admin", views.add_courses_admin),
    path("view_courses_admin", views.view_courses_admin),
    path("update_course", views.update_course),
    path("delete_course", views.delete_course),
    path("add_agency", views.add_agency),
    path("view_agency_admin", views.view_agency_admin),
    path("update_agency", views.update_agency),
    path("delete_agency", views.delete_agency),
    path("delete_home_student", views.delete_home_student),
    path("delete_international_student", views.delete_international_student),

    ############## home students page ####################

    path("home_student_home", views.home_student_home),
    path("view_universities_home_students", views.view_universities_home_students),
    path("view_universities_home_students_single", views.view_universities_home_students_single),
    path("view_courses_home_students", views.view_courses_home_students),
    path("view_course_home_students_single", views.view_course_home_students_single),
    path("view_courses_by_university", views.view_courses_by_university),
    path("view_agency_home_students", views.view_agency_home_students),
    path("view_blogs_home_students", views.view_blogs_home_students),
    path("view_international_students_by_home_students", views.view_international_students_by_home_students),
    path("message_to_international_students", views.message_to_international_students),
    path("replies_from_international_students", views.replies_from_international_students),
    path("view_profile_home_students", views.view_profile_home_students),
    path("edit_profile_home_students", views.edit_profile_home_students),
    path("move_account_to_international", views.move_account_to_international),

    ################# International students page #####################

    path("add_blog_interntional_students", views.add_blog_interntional_students),
    path("view_blogs_international_students", views.view_blogs_international_students),
    path("reply_to_home_students", views.reply_to_home_students),
    path("view_messages_from_home_students", views.view_messages_from_home_students),
    path("view_profile_international_students", views.view_profile_international_students),
    path("edit_profile_international_students", views.edit_profile_international_students),
    path("view_universities_international_students", views.view_universities_international_students),
    path("view_universities_international_students_single", views.view_universities_international_students_single),
    path("view_courses_international_students", views.view_courses_international_students),
    path("view_course_international_students_single", views.view_course_international_students_single),
    path("view_courses_by_university_international_students", views.view_courses_by_university_international_students),

]
