from multiprocessing import context
from operator import mod
from turtle import st
from unicodedata import name
from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from . import models
import datetime, random, requests, hashlib, socket, string, os, re,json
from django.http import JsonResponse
from django.utils.dateparse import parse_date, parse_datetime
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.db.models import Sum
from django.db.models import F,Q,Count
from services.utils import render_to_pdf
from django.contrib.auth.forms import UserCreationForm

import services

# Create your views here.
def index_page(request):
    welcome_message  = models.MessageInfo.objects.filter( message_for = 1 ).first()
    # activities_list  = models.Activities.objects.filter( status= True).order_by('order')[:8]
    noties_list      = models.NoticeAndEvent.objects.filter(notice_or_event = 1).order_by('-id')[:4]
    
    event_list       = models.NoticeAndEvent.objects.filter(notice_or_event = 2).order_by('-id')[:3]
    linklist         = models.ImportantLink.objects.filter(status= True)
    banner_list      = models.SliderInfo.objects.all()
    corner_list      = models.MessageInfo.objects.filter(Q(message_for = 2)|Q(message_for = 3)|Q(message_for = 4)).order_by('-id')

    context = {
        'welcome_message':welcome_message,
        # 'activities_list':activities_list,
        'linklist':linklist,
        'noties_list':noties_list,
        'event_list':event_list,
        'banner_list':banner_list,
        'corner_list':corner_list,
    }
    return render(request, 'services/index.html', context)

def our_history(request):
    history     = models.HomeContent.objects.filter(content_for=1, status= True).last()
    context = {
        'history':history,
    }
    return render(request, 'services/our_history.html', context)  

def at_a_glance(request):
    glance      = models.HomeContent.objects.filter(content_for=4, status = True).last()
    context = {
        'glance':  glance,
    }
    return render(request, 'services/at_a_glance.html', context)

def about_school(request):
    about_school   = models.HomeContent.objects.filter(content_for=3, status = True).last()
    context = {
        'about_school': about_school,
    }
    return render(request, 'services/about_school.html', context)

def about_us(request):
    about_us   = models.HomeContent.objects.filter(content_for=2, status = True).last()
    context = {
        'about_us': about_us,
    }
    return render(request, 'services/about_us.html', context)
    
def teacher_info(request):
    teacher_info  = models.AllInfo.objects.filter(info_for=1, status = True)
    context = {
        'teacher_info': teacher_info,
    }
    return render(request, 'services/teacher_info.html', context)

def student_info(request):
    student_info  = models.AllInfo.objects.filter(info_for=2, status = True)
    context = {
        'student_info': student_info,
    }
    return render(request, 'services/student_info.html', context)

def work_gallary(request):
    work_gallary  = models.WorkGallery.objects.all
    context = {
        'work_gallary': work_gallary,
    }
    return render(request, 'services/work_gallary.html', context)


def user_registation(request):
    if request.method == 'POST':
        register_name  = request.POST['register_name']
        email          = request.POST['email']
        phone          = request.POST['phone']
        designation    = request.POST['designation']
        date           = request.POST['birthday']
        password       = request.POST['password']

        models.UserRegistion.objects.create(register_name = register_name, email = email, phone = phone, designation = designation, date = date, password = password)
        messages.success(request,"Successful! Your account activated.")
        return redirect('/login/')

    return render(request, 'services/user_registation.html')


def login(request):
    if request.method=="POST": 
        email_number   = request.POST['email_number'].strip()
        password  = request.POST['emp_password'].strip()

        # new_md5_obj     = hashlib.md5(password.encode())
        # enc_pass        = new_md5_obj.hexdigest()

        employee_check    = models.UserRegistion.objects.filter(email=email_number, password=password, status=True ).first()
        if employee_check:
            # request.session['short_name']   = str(employee_check.short_name)
            # request.session['id']          = employee_check.employee_id
            # request.session['emp_img']  = str(employee_check.emp_img)
            return redirect('/dashboard/') 
            
        else:
            messages.error(request,"ID and Password incorrect.")  
            return redirect('/login/') 

    return render(request, 'services/login.html')  

# def admin_logout(request):  
#     request.session['employee_id']  = False
#     return redirect('/login/')

# def institute_message(request):
#     school_info      = models.SchoolProfile.objects.all().last()
#     home_content     = models.HomeContent.objects.all().last()
#     context = {
#         'school_info':school_info,
#         'home_content':home_content,
#     }
#     return render(request, 'services/institute_message.html', context)   


def contact_us(request):
    if request.method == 'POST':
        name       = request.POST['name']
        email      = request.POST['email']
        subject    = request.POST['subject']
        phone      = request.POST['phone']
        message    = request.POST['message']

        models.ContactUs.objects.create(name = name, email = email, subject = subject, phone = phone, message = message)
        messages.success(request,"Thank you! Your message has been successfully sent.")
        return redirect('/contact-us/')
    return render(request, 'services/contact_us.html')   


# def result_history(request):

#     return render(request, 'services/result_history.html')   

# def our_history(request):
#     home_content     = models.HomeContent.objects.filter( content_for = 1, status= True ).last()
#     context = {
#         'home_content':home_content,
#     }
#     return render(request, 'services/our_history.html', context)   

def chairman_message(request):
    chairman     = models.MessageInfo.objects.filter(message_for = 2).last()
    context = {
        'chairman':chairman,
    }
    return render(request, 'services/chairman_message.html', context)   

def principal_message(request):
    principal         = models.MessageInfo.objects.filter(message_for = 3).last() 
    context = {
        'principal_message':principal, 
    }
    return render(request, 'services/principal_message.html', context)  

def president_message(request):
    president = models.MessageInfo.objects.filter(message_for = 4).last()
    context = {
        'president': president,
    }
    return render(request, 'services/president_message.html', context)

def general_secretary(request):
    secretary = models.MessageInfo.objects.filter(message_for = 5).last()
    context = {
        'secretary': secretary,
    } 
    return render(request, 'services/general_secretary.html', context)

def employee_list(request): 

    employee_list = models.UserRegistration.objects.all()
    return render(request, 'services/admin/employee_list.html', {'employee_list':employee_list })   

# def at_a_glance(request):
#     at_a_glance      = models.HomeContent.objects.filter(content_for = 2).last()
    
#     context = {
#         'at_a_glance':at_a_glance,
#     }
#     return render(request, 'services/at_a_glance.html', context)   

# def teacher_info(request):
#     school_info    = models.SchoolProfile.objects.all().last()
#     teacher_list   = models.AcademicTeam.objects.filter(academic_member = 2)
    
#     context = {
#         'school_info':school_info,
#         'teacher_list':teacher_list,
        
#     }
#     return render(request, 'services/teacher_info.html', context)   

def committee_info(request): 
    committee_list   = models.CommitteeInfo.objects.filter(status=True).order_by("order")
    context = { 
        'committee_list':committee_list, 
    }
    return render(request, 'services/committee_info.html', context)   

# def why_study_here(request):
#     why_study_here      = models.HomeContent.objects.filter(content_for = 3).last()
    
#     context = {
#         'why_study_here':why_study_here,
#     }
#     return render(request, 'services/why_study_here.html', context) 

# def admission_form(request):
#     if request.method == 'POST':
#         student_name   = request.POST['student_name']
#         father_name    = request.POST['father_name']
#         mother_name    = request.POST['mother_name']
#         class_for      = int(request.POST['class_for'])
#         group_for      = int(request.POST['group_for'])
#         email          = request.POST['email']
#         phone          = request.POST['phone']
#         address        = request.POST['address']

#         models.AdmissionRequest.objects.create(student_name = student_name, father_name = father_name, mother_name = mother_name, class_for = class_for, 
#         group_for = group_for, email= email, phone=phone, address = address)
#         messages.success(request,"Thank you! Your informations has been successfully sent.")
#         return redirect('/admission/')

#     return render(request, 'services/admission_form.html') 

# def exam_regulations(request):
    
#     return render(request, 'services/exam_regulations.html') 

# def admission_suspension(request):
    
#     return render(request, 'services/admission_suspension.html') 

# def admission_information(request):
#     advice_list   = models.ExamAdvice.objects.filter(status = True)
    
#     context = {
#         'advice_list':advice_list,
#     }
#     return render(request, 'services/admission_information.html', context) 

# def institute_facility(request):
#     school_info      = models.SchoolProfile.objects.all().last()
#     activities_list  = models.Activities.objects.filter(status= True).order_by('order')[:8]
#     context = {
#         'school_info':school_info,
#         'activities_list':activities_list,
#     }
#     return render(request, 'services/institute_facility.html', context)   

def photo_gallery(request):
    school_info      = models.SchoolProfile.objects.all().last()
    gallery_list       = models.GalleryInfo.objects.filter(gallery_type = 2).order_by('-id')
    context = {
        'school_info':school_info,
        'gallery_list':gallery_list,
    }
    return render(request, 'services/photo_gallery.html', context)   

def video_gallery(request):
    school_info      = models.SchoolProfile.objects.all().last()
    video_list       = models.GalleryInfo.objects.filter(gallery_type = 1).order_by('-id')
    context = {
        'school_info':school_info,
        'video_list':video_list,
    }
    return render(request, 'services/video_gallery.html', context)   

def previous_events(request):
    video_list       = models.PreviousEvents.objects.order_by('-gallery_order')
    context = {
        'video_list':video_list,
    }
    return render(request, 'services/previous_events.html', context)

def all_member(request):
    all_member       = models.AllMember.objects.all()
    context = {
        'all_member': all_member,
    }
    return render(request, 'services/all_member.html', context)

# def previous_events(request):
#     school_info      = models.SchoolProfile.objects.all().last()
#     video_list       = models.GalleryInfo.objects.filter(gallery_type = 1).order_by('-id')
#     context = {
#         'school_info':school_info,
#         'video_list':video_list,
#     }
#     return render(request, 'services/video_gallery.html', context)

def all_notices(request):
    school_info      = models.SchoolProfile.objects.all().last()
    event_list       = models.NoticeAndEvent.objects.filter(notice_or_event = 2).order_by('-id')[:3]
    linklist         = models.ImportantLink.objects.filter(status= True)
    context = {
        'school_info':school_info,
        'event_list':event_list,
        'linklist':linklist,
        'all_noties': models.NoticeAndEvent.objects.filter(notice_or_event = 1).order_by('-id'),
    }
    return render(request, 'services/all_notices.html', context)   

def view_notices(request,id):
    view_notices     = models.NoticeAndEvent.objects.get(id = id)
    school_info      = models.SchoolProfile.objects.all().last()
    event_list       = models.NoticeAndEvent.objects.filter(notice_or_event = 2).order_by('-id')[:3]
    linklist         = models.ImportantLink.objects.filter(status= True)
    context = {
        'school_info':school_info,
        'event_list':event_list,
        'linklist':linklist,
        'view_notices': view_notices,
    }
    return render(request, 'services/view_notice.html', context)   

def job_vacancy(request):
    job_vacancy         = models.JobCircular.objects.filter(status= True)
    context = {
        'job_vacancy':job_vacancy,
    }
    return render(request, 'services/job_vacancy.html', context) 

# def all_events(request):
#     school_info      = models.SchoolProfile.objects.all().last()
#     event_list       = models.NoticeAndEvent.objects.filter(notice_or_event = 2).order_by('-id')[:3]
#     linklist         = models.ImportantLink.objects.filter(status= True)
#     context = {
#         'school_info':school_info,
#         'event_list':event_list,
#         'linklist':linklist,
#         'all_events': models.NoticeAndEvent.objects.filter(notice_or_event = 2).order_by('-id'),
#     }
#     return render(request, 'services/all_events.html', context)   

# def view_events(request,id):
#     view_events      = models.NoticeAndEvent.objects.get(id = id)
#     school_info      = models.SchoolProfile.objects.all().last()
#     event_list       = models.NoticeAndEvent.objects.filter(notice_or_event = 2).order_by('-id')[:3]
#     linklist         = models.ImportantLink.objects.filter(status= True)
#     context = {
#         'school_info':school_info,
#         'event_list':event_list,
#         'linklist':linklist,
#         'view_events':view_events,
#     }
#     return render(request, 'services/view_events.html', context)   

# def eiin_number(request):
#     context = {
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/eiin_number.html', context)  

# def library_page(request):
#     facility = models.FacilityItem.objects.filter(facility_type = 1, status = True).first()
#     library_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 2, status = True)
#     context = {
#         'facility':facility,
#         'library_image':library_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/library_page.html', context)   

# def hostel_page(request):
#     hostel_info = models.FacilityItem.objects.filter(facility_type = 2, status = True).first()
#     hostel_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 1, status = True)
#     context = {
#         'hostel_info':hostel_info,
#         'hostel_image':hostel_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/hostel_page.html', context)   

# def lab_page(request):
#     lab_info = models.FacilityItem.objects.filter(facility_type = 3, status = True).first()
#     lab_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 3, status = True)
#     context = {
#         'lab_info':lab_info,
#         'lab_image':lab_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/lab_page.html', context)   

# def idcard_page(request):
#     idcard = models.FacilityItem.objects.filter(facility_type = 4, status = True).first()
#     idcard_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 5, status = True)
#     context = {
#         'idcard':idcard,
#         'idcard_image':idcard_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/idcard_page.html', context)   

# def quran_class(request):

#     quran_class = models.FacilityItem.objects.filter(facility_type = 7, status = True).first()
#     quran_class_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 7, status = True)
#     context = {
#         'quran_class':quran_class,
#         'quran_class_image':quran_class_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/quran_class.html', context)   

# def bncc_page(request):
#     bncc_page = models.FacilityItem.objects.filter(facility_type = 5, status = True).first()
#     bncc_page_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 4, status = True)
#     context = {
#         'bncc_page':bncc_page,
#         'bncc_page_image':bncc_page_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/bncc_page.html', context)   

# def scout_page(request):
#     scout_info = models.FacilityItem.objects.filter(facility_type = 6, status = True).first()
#     scout_info_image = models.GalleryInfo.objects.filter(gallery_type = 2, gallery_for = 6, status = True)
#     context = {
#         'scout_info':scout_info,
#         'scout_info_image':scout_info_image,
#         'school_info':models.SchoolProfile.objects.all().last(),
#     }
#     return render(request, 'services/scout_page.html', context)   

# def search_result(request):
#     class_list = models.ClassInfo.objects.filter(status = True)
#     year_list  = models.Years.objects.filter(status = True)
#     if request.method == "POST":
#         roll        = request.POST['roll']
#         class_obj  = int(request.POST['class'])
#         year        = int(request.POST['year'])

#         result   = models.Result.objects.filter( student_id__st_roll = roll, class_name_id = class_obj, student_id__running_year = year).first()
#         context = {
#             'result':result,
#             'class_list':class_list,
#             'year_list':year_list,
#             'roll':roll,
#             'class_obj':class_obj,
#             'year':year,
#         }
#         if result:      
#             return render(request, 'services/search_result.html', context) 
#         else:
#             messages.error(request,"Please Input Valid Value.")
#             return render(request, 'services/search_result.html', context)  
#     context={
#         'class_list':class_list,
#         'year_list':year_list,
#     }

#     return render(request, 'services/search_result.html', context)   


def dashboard(request): 
    # total_student       = models.Student.objects.filter(status = True).count()
    # total_employees     = models.EmployeeList.objects.all().count()
    # total_teacher       = models.EmployeeList.objects.filter(is_teacher = True).count()
    # new_student         = models.Student.objects.filter(new_student = True).count()
    # region_emp_list  = models.Student.objects.values('class_name_id__class_name').filter(status = True).annotate(region_emp_count = Count('class_name')).order_by('class_name')

    context={
        # 'total_student':total_student,
        # 'total_employees':total_employees,
        # 'total_teacher':total_teacher,
        # 'new_student':new_student,
        # 'region_emp_list':region_emp_list,
    }
    return render(request, 'services/admin/index.html', context)   

# def student_dashboard(request):

#     return render(request, 'services/admin/student_dashboard.html')   

# def student_reg(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     class_list = models.ClassInfo.objects.filter(status = True)
#     shift_list = models.Shift.objects.filter(status = True)
#     section_list = models.Section.objects.filter(status = True)
#     session_list = models.SessionInfo.objects.filter(status = True)
#     running_year = models.Years.objects.filter(status = True)
#     group_lsit = models.GroupTypeList.objects.filter(status = True).order_by("-id")

#     context={
#         'class_list':class_list,
#         'shift_list':shift_list,
#         'section_list':section_list,
#         'session_list':session_list,
#         'running_year':running_year,
#         'group_lsit':group_lsit,
#     }
#     try:
#         if request.method == 'POST':
#             student_id              = request.POST['student_id']
#             st_first_name           = request.POST['st_first_name']
#             st_last_name            = request.POST['st_last_name']
#             st_bangla_name          = request.POST['st_bangla_name']
#             st_gender               = request.POST['st_gender']
#             st_religion             = request.POST['st_religion']
#             date_of_birth           = parse_date(request.POST['date_of_birth'])
#             birth_certificate_no    = request.POST['birth_certificate_no']
#             st_mobile               = request.POST['st_mobile']
#             st_email                = request.POST['st_email']
#             st_blood_group          = request.POST['st_blood_group']
#             class_name              = int(request.POST['class_name'])
#             shift_name              = int(request.POST['shift_name'])
#             section_name            = int(request.POST['section_name'])
#             session_name            = int(request.POST['session_name'])
#             running_year            = int(request.POST['running_year'])
#             group_type              = int(request.POST['group_type'])
#             student_type            = request.POST['student_type']
#             st_roll                 = request.POST['st_roll']
#             st_reg                  = request.POST['st_reg']
#             psc_roll                = request.POST['psc_roll']
#             jsc_roll                = request.POST['jsc_roll']
#             father_name             = request.POST['father_name']
#             father_bangla_name      = request.POST['father_bangla_name']
#             father_occupation       = request.POST['father_occupation']
#             father_mobile           = request.POST['father_mobile']
#             mother_name             = request.POST['mother_name']
#             mother_bangla_name      = request.POST['mother_bangla_name']
#             mother_occupation       = request.POST['mother_occupation']
#             mother_mobile           = request.POST['mother_mobile']
#             guardian_name           = request.POST['guardian_name']
#             guardian_relation       = request.POST['guardian_relation']
#             guardian_mobile         = request.POST['guardian_mobile']
#             guardian_monthly_income = request.POST['guardian_monthly_income']
#             present_address         = request.POST['present_address']
#             parmanent_address       = request.POST['parmanent_address']
#             previous_school_name    = request.POST['previous_school_name']
#             previous_school_address = request.POST['previous_school_address']
#             tc_no                   = request.POST['tc_no']
#             tc_date                 = parse_date(request.POST['tc_date'])
#             fitness_details         = request.POST['fitness_details']
#             student_status          = request.POST['student_status']
#             new_student             = True if request.POST['new_student'] else False

#             print("joshef", student_status)
#             order_file1 = ""
#             if bool(request.FILES.get('student_img', False)) == True:
#                 file = request.FILES['student_img']
#                 order_file1 = "student_img"+file.name
#                 if not os.path.exists(settings.MEDIA_ROOT+"student_img"):
#                     os.mkdir(settings.MEDIA_ROOT+"student_img")
#                 default_storage.save(settings.MEDIA_ROOT+"student_img"+file.name, ContentFile(file.read()))
            
#             order_file2 = ""
#             if bool(request.FILES.get('father_photo', False)) == True:
#                 file = request.FILES['father_photo']
#                 order_file2 = "father_photo"+file.name
#                 if not os.path.exists(settings.MEDIA_ROOT+"father_photo"):
#                     os.mkdir(settings.MEDIA_ROOT+"father_photo")
#                 default_storage.save(settings.MEDIA_ROOT+"father_photo"+file.name, ContentFile(file.read()))
            
#             order_file3 = ""
#             if bool(request.FILES.get('mother_photo', False)) == True:
#                 file = request.FILES['mother_photo']
#                 order_file3 = "mother_photo"+file.name
#                 if not os.path.exists(settings.MEDIA_ROOT+"mother_photo"):
#                     os.mkdir(settings.MEDIA_ROOT+"mother_photo")
#                 default_storage.save(settings.MEDIA_ROOT+"mother_photo"+file.name, ContentFile(file.read()))
            
#             order_file4 = ""
#             if bool(request.FILES.get('medical_certificate', False)) == True:
#                 file = request.FILES['medical_certificate']
#                 order_file4 = "medical_certificate"+file.name
#                 if not os.path.exists(settings.MEDIA_ROOT+"medical_certificate"):
#                     os.mkdir(settings.MEDIA_ROOT+"medical_certificate")
#                 default_storage.save(settings.MEDIA_ROOT+"medical_certificate"+file.name, ContentFile(file.read()))
            
#             order_file5 = ""
#             if bool(request.FILES.get('guardian_photo', False)) == True:
#                 file = request.FILES['guardian_photo']
#                 order_file5 = "guardian_photo"+file.name
#                 if not os.path.exists(settings.MEDIA_ROOT+"guardian_photo"):
#                     os.mkdir(settings.MEDIA_ROOT+"guardian_photo")
#                 default_storage.save(settings.MEDIA_ROOT+"guardian_photo"+file.name, ContentFile(file.read()))
            
#             if student_status == 1:
#                 student_status = True

#             elif student_status == 2:
#                 student_status = False
            
#             if models.Student.objects.create(student_id= student_id, st_first_name = st_first_name, st_last_name = st_last_name, st_bangla_name = st_bangla_name, st_gender = st_gender, 
#                     st_religion = st_religion, date_of_birth= date_of_birth, birth_certificate_no=birth_certificate_no,
#                     st_mobile = st_mobile, st_blood_group= st_blood_group, class_name_id =class_name, shift_name_id = shift_name, section_name_id = section_name,
#                     session_name_id = session_name, running_year_id = running_year, group_type_id = group_type,
#                     student_type = student_type, st_roll= st_roll, st_reg=st_reg, psc_roll =psc_roll, jsc_roll = jsc_roll,
#                     father_name= father_name, father_bangla_name=father_bangla_name, father_occupation = father_occupation, father_mobile = father_mobile,
#                     mother_name = mother_name, mother_bangla_name= mother_bangla_name, mother_occupation=mother_occupation, mother_mobile = mother_mobile, guardian_name = guardian_name,
#                     guardian_relation = guardian_relation, guardian_mobile= guardian_mobile, guardian_monthly_income=guardian_monthly_income, 
#                     present_address = present_address, parmanent_address = parmanent_address, previous_school_name= previous_school_name, 
#                     previous_school_address = previous_school_address, tc_no = tc_no, tc_date = tc_date,
#                     fitness_details = fitness_details,status = student_status, new_student = new_student, student_img = order_file1, father_photo = order_file2, mother_photo = order_file3, 
#                     medical_certificate = order_file4, guardian_photo = order_file5
#                 ):
#                 messages.success(request,"Student Admission Successful")
#                 return redirect('/student-list/')
#             else:
#                 messages.success(request,"Please Input Valid Value.")
#                 return redirect('/student-registration/')
#     except:
#         messages.success(request,"Please Input Valid Value.")

#     return render(request, 'services/admin/reg_student.html', context)   

# def student_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     student_list = models.Student.objects.all().order_by("-id")
#     return render(request, 'services/admin/student_list.html',{'student_list':student_list})   

# def remove_student(request, id):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     models.Student.objects.filter(id = id).update(status=False)
#     return redirect("/student-list/")

# def student_photos_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     student_photos_list = models.Student.objects.all().order_by("-id")
#     return render(request, 'services/admin/student_photos_list.html',{'student_photos_list':student_photos_list})   

# def parents_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     parents_list = models.Student.objects.all().order_by("-id")
#     return render(request, 'services/admin/parents_list.html',{'parents_list':parents_list})   

# def parents_photos_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     parents_photos_list = models.Student.objects.all().order_by("-id")
#     return render(request, 'services/admin/parents_photos_list.html',{'parents_photos_list':parents_photos_list})   

# def guardian_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     guardian_list = models.Student.objects.all().order_by("-id")
#     return render(request, 'services/admin/guardian_list.html',{'guardian_list':guardian_list})   

# def guardian_photos_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     guardian_photos_list = models.Student.objects.all().order_by("-id")
#     return render(request, 'services/admin/guardian_photos_list.html',{'guardian_photos_list':guardian_photos_list})   

# def scholarship_student_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     scholarship_student_list = models.Student.objects.filter(Q(student_type = "2")|Q(student_type = "3")).order_by("-id")
#     return render(request, 'services/admin/scholarship_student_list.html',{'scholarship_student_list': scholarship_student_list})   

# def inactive_student_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     inactive_student_list = models.Student.objects.filter(status = False).order_by("-id")
#     return render(request, 'services/admin/inactive_student.html',{'inactive_student_list': inactive_student_list})   

# def quick_admission_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     quick_admission_list = models.AdmissionRequest.objects.all().order_by("-id")
#     return render(request, 'services/admin/quick_admission_list.html',{'quick_admission_list': quick_admission_list})   

# def quick_admission(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     if request.method == 'POST':
#         student_name   = request.POST['student_name']
#         father_name    = request.POST['father_name']
#         mother_name    = request.POST['mother_name']
#         class_for      = int(request.POST['class_for'])
#         group_for      = int(request.POST['group_for'])
#         email          = request.POST['email']
#         phone          = request.POST['phone']
#         address        = request.POST['address']

#         models.AdmissionRequest.objects.create(student_name = student_name, father_name = father_name, mother_name = mother_name, class_for = class_for, 
#         group_for = group_for, email= email, phone=phone, address = address)
#         messages.success(request,"Thank you! Your informations has been successfully sent.")
#         return redirect('/quick-admission/')
#     return render(request, 'services/admin/quick_admission.html')   

# def mark_distribution(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     class_list    = models.ClassInfo.objects.filter(status = True)
#     class_subject = models.Subject.objects.filter(status = True).order_by("ordering")

#     if request.method == 'POST':
#         class_name    = int(request.POST['class_name'])
#         class_subject = int(request.POST['class_subject'])
#         mark_type     = request.POST['mark_type']
#         total_mark    = request.POST['total_mark']
#         pass_mark     = request.POST['pass_mark']
#         if models.MarkDistribution.objects.create(class_name_id = class_name, class_subject_id = class_subject, mark_type = mark_type, total_mark = total_mark, pass_mark= pass_mark):
#             messages.success(request,"Mark distribution save successful.")
#             return redirect("/mark-distribution-list/")
#         else:
#             messages.error(request,"Please Input Valid Value.")
#             return redirect("/mark-distribution/")
            
#     context={
#         'class_list':class_list,
#         'class_subject':class_subject,
#     }
#     return render(request, 'services/admin/mark_distribution.html', context )   

# def mark_distribution_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     mark_distribution_list    = models.MarkDistribution.objects.filter(status = True)
#     context={
#         'mark_distribution_list':mark_distribution_list
#     }
#     return render(request, 'services/admin/mark_distribution_list.html', context )   

# def delete_mark_distribution(request, id):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     models.MarkDistribution.objects.filter(id = id).delete()
#     return redirect("/mark-distribution-list/")

# # Employee 

# def employee_reg(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     department_list = models.Department.objects.filter(status = True)

#     if request.method == 'POST':
#         employee_id        = request.POST['employee_id']
#         employee_name      = request.POST['employee_name']
#         short_name         = request.POST['short_name']
#         emp_password       = request.POST['emp_password']
#         dpt_name           = int(request.POST['dpt_name'])
#         father_name        = request.POST['father_name']
#         mother_name        = request.POST['mother_name']
#         desig_name         = request.POST['desig_name']
#         qualification      = request.POST['qualification']
#         emp_gender         = request.POST['emp_gender']
#         emp_religion       = request.POST['emp_religion']
#         blood_group        = request.POST['blood_group']
#         emp_mobile         = request.POST['emp_mobile']
#         email_address      = request.POST['email_address']
#         join_date          = request.POST['join_date']
#         date_of_birth      = request.POST['date_of_birth']
#         national_id        = request.POST['national_id']
#         basic_salary       = request.POST['basic_salary']
#         starting_salary    = request.POST['starting_salary']
#         present_address    = request.POST['present_address']
#         permanent_address  = request.POST['permanent_address']
#         fitness_details    = request.POST['fitness_details']
#         is_teacher         = True if request.POST['is_teacher'] else False

#         new_md5_obj     = hashlib.md5(emp_password.encode())
#         new_enc_pass    = new_md5_obj.hexdigest()

#         order_file1 = ""
#         if bool(request.FILES.get('emp_img', False)) == True:
#             file = request.FILES['emp_img']
#             order_file1 = "emp_img"+file.name
#             if not os.path.exists(settings.MEDIA_ROOT+"emp_img"):
#                 os.mkdir(settings.MEDIA_ROOT+"emp_img")
#             default_storage.save(settings.MEDIA_ROOT+"emp_img"+file.name, ContentFile(file.read()))
        
#         order_file2 = ""
#         if bool(request.FILES.get('medical_certificate', False)) == True:
#             file = request.FILES['medical_certificate']
#             order_file2 = "medical_certificate"+file.name
#             if not os.path.exists(settings.MEDIA_ROOT+"medical_certificate"):
#                 os.mkdir(settings.MEDIA_ROOT+"medical_certificate")
#             default_storage.save(settings.MEDIA_ROOT+"medical_certificate"+file.name, ContentFile(file.read()))
        
#         if models.EmployeeList.objects.create(
#                 employee_id = employee_id, employee_name = employee_name, short_name = short_name, emp_password = new_enc_pass, dpt_name_id = dpt_name, 
#                 father_name = father_name, mother_name = mother_name, desig_name = desig_name, qualification = qualification,
#                 emp_gender = emp_gender, emp_religion = emp_religion, blood_group = blood_group, emp_mobile = emp_mobile,
#                 email_address = email_address, join_date = join_date, date_of_birth = date_of_birth, national_id = national_id,
#                 basic_salary = basic_salary, starting_salary = starting_salary, present_address = present_address, permanent_address = permanent_address,
#                 fitness_details = fitness_details, is_teacher = is_teacher, emp_img =order_file1, medical_certificate = order_file2
#             ):
#             messages.success(request,"Employee Registration Successful.")

#         else:
#             messages.error(request,"Please Input Valid Value.")

#         return redirect('/employee-list/')

#     context={
#         'department_list':department_list,
#         'last_employee_id':models.EmployeeList.objects.filter(status = True).last(),
#     }

#     return render(request, 'services/admin/reg_employee.html', context)   

# def employee_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     employee_list = models.EmployeeList.objects.all()
#     return render(request, 'services/admin/employee_list.html', {'employee_list':employee_list })   

# def remove_employee(request, id):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     models.EmployeeList.objects.filter(id = id).update(status= False)
#     return redirect("/employee-list/") 

# def add_class_teacher(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     teacher_list = models.EmployeeList.objects.filter(status = True, is_teacher = True)
#     class_list = models.ClassInfo.objects.filter(status = True)
#     shift_list = models.Shift.objects.filter(status = True)
#     section_list = models.Section.objects.filter(status = True)
#     running_year = models.Years.objects.filter(status = True)
#     group_lsit = models.GroupTypeList.objects.filter(status = True)

#     if request.method == 'POST':
#         teacher_name    = int(request.POST['teacher_name'])
#         class_name      = int(request.POST['class_name'])
#         Version         = request.POST['Version']
#         shift_name      = int(request.POST['shift_name'])
#         section_name    = int(request.POST['section_name'])
#         group_type      = int(request.POST['group_type'])
#         running_year    = int(request.POST['running_year'])
#         if models.TeacherList.objects.create(
#                 teacher_name_id = teacher_name, class_name_id = class_name, Version = Version, shift_name_id = shift_name, 
#                 section_name_id = section_name, group_type_id = group_type, running_year_id = running_year
#             ):
#             messages.success(request,"Class teacher assign save successful.")
#             return redirect("/teacher-list/")
#         else:
#             messages.error(request,"Please Input Valid Value.")
#             return redirect("/add-class-teacher/")
            
#     context={
#         'teacher_list':teacher_list,
#         'class_list':class_list,
#         'shift_list':shift_list,
#         'section_list':section_list,
#         'running_year':running_year,
#         'group_lsit':group_lsit,
#     }
#     return render(request, 'services/admin/add_class_teacher.html', context )   

# def student_exam_mark(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     student = models.Student.objects.filter(status = True)
#     class_list = models.ClassInfo.objects.filter(status = True)
#     shift_list = models.Shift.objects.filter(status = True)

#     if request.method == 'POST':
#         student                    = request.POST['student']
#         class_name                 = request.POST['class_name']
#         shift_name                 = request.POST['shift_name']
#         bangla                     = request.POST['bangla']
#         bangla_2nd                 = request.POST['bangla_2nd']
#         english                    = request.POST['english']
#         english_2nd                = request.POST['english_2nd']
#         mathematics                = request.POST['mathematics']
#         general_science            = request.POST['general_science']
#         bangladesh_global_studies  = request.POST['bangladesh_global_studies']
#         islamic_studies            = request.POST['islamic_studies']
#         hindu_studies              = request.POST['hindu_studies']
#         ict                        = request.POST['ict']
#         agriculture_studies        = request.POST['agriculture_studies']
#         if models.Result.objects.create(
#                 student_id = student, class_name_id = class_name, shift_name_id = shift_name, 
#                 bangla = bangla, bangla_2nd = bangla_2nd, english = english, english_2nd =english_2nd, 
#                 mathematics = mathematics, general_science =general_science, bangladesh_global_studies =bangladesh_global_studies, islamic_studies =islamic_studies,
#                 hindu_studies =hindu_studies, ict =ict, agriculture_studies =agriculture_studies
#             ):
#             messages.success(request,"Exam Mark Entry Successful.")
#             return redirect("/student-exam-marks-entry/")
#         else:
#             messages.error(request,"Please Input Valid Value.")
            
#     context={
#         'student':student,
#         'class_list':class_list,
#         'shift_list':shift_list,
#     }
#     return render(request, 'services/admin/report/student_exam_mark.html', context )   

# def teacher_list(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     teacher_list = models.TeacherList.objects.all()
#     return render(request, 'services/admin/teacher_list.html', {'teacher_list':teacher_list })   


# def delete_teacher(request, id):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     models.TeacherList.objects.filter(id = id).update(status=False)
#     return redirect("/teacher-list/")





# # api test
# import requests
# import json
# def apiTest(request):
#     api_request = requests.get("http://worldclockapi.com/api/json/est/now")
#     try:
#         api = json.loads(api_request.content)
#     except :
#         api ="Error"
    
#     return render(request, 'services/api.html', {'api':api}) 


# import random, string, os, smtplib, datetime, hashlib, json, xlsxwriter, pandas  as pd
# #  Download to Excle

# def export_student_list(request):
#     if request.session.get("employee_id"):
#         student_list = models.Student.objects.all()
#         if student_list:
#             if not os.path.exists(settings.MEDIA_ROOT):
#                 os.mkdir(settings.MEDIA_ROOT)

#             if not os.path.exists(settings.MEDIA_ROOT + "/excel_templates"):
#                 os.mkdir(settings.MEDIA_ROOT + "/excel_templates")

#             file_name = "Student_List_Sheet.xlsx"
#             if os.path.exists(settings.MEDIA_ROOT + "/excel_templates/" + file_name):
#                 os.remove(os.path.join(settings.MEDIA_ROOT + '/excel_templates/', file_name))

#             file_path = os.path.join(settings.MEDIA_ROOT + '/excel_templates/', file_name)

#             if not os.path.exists(file_path):
#                 workbook = xlsxwriter.Workbook(settings.MEDIA_ROOT + '/excel_templates/' + file_name)
#                 worksheet = workbook.add_worksheet()
#                 worksheet.write('A1', 'Student Id')
#                 worksheet.write('B1', 'Student Frist Name')
#                 worksheet.write('C1', 'Student Last Name')
#                 worksheet.write('D1', 'Gender')
#                 worksheet.write('E1', 'Religion')
#                 worksheet.write('F1', 'Date of Birth')
#                 worksheet.write('G1', 'Birth Certificate No')
#                 worksheet.write('H1', 'Mobile')
#                 worksheet.write('I1', 'Blood Group')
#                 worksheet.write('J1', 'Email')
#                 worksheet.write('K1', 'Roll')
#                 worksheet.write('L1', 'Reg.')
#                 worksheet.write('M1', 'PSC Roll')
#                 worksheet.write('N1', 'JSC Roll')
#                 worksheet.write('O1', 'Class Name')
#                 worksheet.write('P1', 'Shift Name')
#                 worksheet.write('Q1', 'Section Name')
#                 worksheet.write('R1', 'Session Name')
#                 worksheet.write('S1', 'Running Year')
#                 worksheet.write('T1', 'Group Type')
#                 worksheet.write('U1', 'Admission Date')
#                 worksheet.write('V1', 'Father Name')
#                 worksheet.write('W1', 'Mother Name')
#                 worksheet.write('X1', 'Guardian Name')
#                 worksheet.write('Y1', 'Father Mobile')
#                 worksheet.write('Z1', 'Present Address')
#                 worksheet.write('AA1', 'Parmanent Address')
#                 worksheet.write('AB1', 'TC. NO')
#                 worksheet.write('AC1', 'Student Type')
#                 worksheet.write('AD1', 'Status')
#                 worksheet.set_column(0, 10, 15)
#                 worksheet.autofilter('A1:AD1')
#                 count = 2
                
#                 for data in student_list: 
#                     if data.status == True:
#                         status="Active"
#                     else:
#                         status="Inactive" 
                             
#                     worksheet.write('A' + str(count), str(data.student_id))
#                     worksheet.write('B' + str(count), str(data.st_first_name))
#                     worksheet.write('C' + str(count), str(data.st_last_name))
#                     worksheet.write('D' + str(count), str(data.st_gender))
#                     worksheet.write('E' + str(count), str(data.st_religion))
#                     worksheet.write('F' + str(count), str(data.date_of_birth))
#                     worksheet.write('G' + str(count), str(data.birth_certificate_no))
#                     worksheet.write('H' + str(count), str(data.st_mobile))
#                     worksheet.write('I' + str(count), str(data.st_blood_group))
#                     worksheet.write('J' + str(count), str(data.st_email))
#                     worksheet.write('K' + str(count), str(data.st_roll))
#                     worksheet.write('L' + str(count), str(data.st_reg))
#                     worksheet.write('M' + str(count), str(data.psc_roll))
#                     worksheet.write('N' + str(count), str(data.jsc_roll))
#                     worksheet.write('O' + str(count), str(data.class_name))
#                     worksheet.write('P' + str(count), str(data.shift_name))
#                     worksheet.write('Q' + str(count), str(data.section_name))
#                     worksheet.write('R' + str(count), str(data.session_name))
#                     worksheet.write('S' + str(count), str(data.running_year))
#                     worksheet.write('T' + str(count), str(data.group_type))
#                     worksheet.write('U' + str(count), str(data.admission_date))
#                     worksheet.write('V' + str(count), str(data.father_name))
#                     worksheet.write('W' + str(count), str(data.mother_name))
#                     worksheet.write('X' + str(count), str(data.guardian_name))
#                     worksheet.write('Y' + str(count), str(data.father_mobile))
#                     worksheet.write('Z' + str(count), str(data.present_address))
#                     worksheet.write('AA' + str(count), str(data.parmanent_address))
#                     worksheet.write('AB' + str(count), str(data.tc_no))
#                     worksheet.write('AC' + str(count), str(data.student_type))
#                     worksheet.write('AD' + str(count), str('Active' if data.status else 'Inactive'))
#                     count += 1
#                 workbook.close()
#             return download_excel_sheet(file_name)
#         else:
#             messages.warning(request, "Something went wrong!")
#             return redirect("/student-list/")
#     else:
#         messages.warning(request, "Something went wrong!")
#         return redirect("/student-list/")

# def download_excel_sheet(file_name):
#     file_path = os.path.join(settings.MEDIA_ROOT + '/excel_templates/', file_name)
#     if os.path.exists(file_path):
#         with open(file_path, 'rb') as fh:
#             response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
#             response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
#             return response
#     raise Http404



# # Report 

# def class_wise_report(request):
#     if not request.session['employee_id']:
#         return redirect('/login/')

#     class_list   = models.ClassInfo.objects.filter(status = True)
#     shift_list   = models.Shift.objects.filter(status = True)
#     school_info  = models.SchoolProfile.objects.filter(status = True).first()

#     if request.method == "POST":
#         class_name    = int(request.POST['class_name'])
#         shift_name    = int(request.POST['shift_name'])

#         class_wise_report   = models.Result.objects.filter( class_name_id = class_name, shift_name_id = shift_name)
#         context = {
#             'class_list':class_list,
#             'shift_list':shift_list,
#             'class_name':class_name,
#             'shift_name':shift_name,
#             'school_info':school_info,
#             'class_wise_report':class_wise_report,
#         }
#         if class_wise_report:      
#             pdf = render_to_pdf('services/admin/report/class_wise_report_pdf.html',context)
#             return HttpResponse(pdf, content_type='application/pdf')
#         else:
#             context = {
#                 'class_list':class_list,
#                 'shift_list':shift_list,
#                 'class_name':class_name,
#                 'shift_name':shift_name,
#             }
#             messages.error(request, "No Data Found!")
#             return render(request, 'services/admin/report/class_wise_report.html', context)
#     return render(request, 'services/admin/report/class_wise_report.html',{"class_list" : class_list, 'shift_list':shift_list})
