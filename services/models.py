import email
import imp
import os
from tabnanny import verbose
from unicodedata import name
from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField    
from datetime import datetime
from django.utils import timezone

from services.views import previous_events


class HomeContent(models.Model):
    content_type = (
        ('1', 'Our History'),
        ('2', 'About Us'),
        ('3', 'About School'),
        ('4', 'At a Glance'),
    )
    content_for  = models.CharField(max_length=1, choices = content_type)
    details      = RichTextField(blank=True)
    pub_date     = models.DateField(auto_now_add = True)
    status       = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.content_for)
    
    class Meta:
        verbose_name = 'Home Content'
        verbose_name_plural = 'Home Contents'

class Batch(models.Model):
    year          = models.CharField(max_length=20, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=True) 
    
    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batch" 

class CommitteeInfo(models.Model):
    member_name        = models.CharField(max_length=100, blank=True)
    email              = models.EmailField(max_length=100, blank=True)
    phone              = models.CharField(max_length=100, blank=True)
    designation        = models.CharField(max_length=50, blank=True)
    qualification      = models.CharField(max_length=300, blank=True)
    date_of_birth      = models.DateField(auto_now_add = False)
    genders = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Others'),
    )
    gender             = models.CharField(max_length=1, choices = genders)
    present_address    = models.CharField(max_length=500,blank=True)
    permament_address  = models.CharField(max_length=500,blank=True)
    batch              = models.ForeignKey(Batch, on_delete=models.CASCADE)
    member_image       = models.FileField(upload_to='member_image',blank=True)
    order              = models.IntegerField(default=0)
    facebook           = models.CharField(max_length=200,blank=True)
    twitter            = models.CharField(max_length=200,blank=True)
    status             = models.BooleanField(default=True)
    
    def __str__(self):
        return self.member_name

    class Meta:
        verbose_name = 'Committee Information'
        verbose_name_plural = 'Committee Informations' 

class AllInfo(models.Model):
    info_type = (
        ('1', 'teacher info'),
        ('2', 'student info'),
    )
    info_for            = models.CharField(max_length=1, choices = info_type)
    name                = models.CharField(max_length=100, blank=True)
    designation         = models.CharField(max_length=100, blank=True)
    qualifications      = models.CharField(max_length=150, blank=True)
    info_image          = models.FileField(upload_to='Info_image',blank=True)
    email               = models.EmailField(max_length=100, blank = True)
    facebook            = models.CharField(max_length=200,blank=True)
    twitter             = models.CharField(max_length=200,blank=True)
    order               = models.IntegerField(default=0)
    status              = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'teacher students info'
        verbose_name_plural = 'teacher students infos'

class WorkGallery(models.Model):
    work_title          = models.CharField(max_length=100, blank=True)
    work_image          = models.FileField(upload_to='work_image',blank=True)
    order              = models.IntegerField(default=0)
    status              = models.BooleanField(default=True)

    def __str__(self):
        return self.work_title

    class Meta:
        verbose_name = 'work gallary'
        verbose_name_plural = 'add work gallary'

        
class SliderInfo(models.Model):
    slider_title   = models.CharField(max_length=100, blank=True)
    details        = models.TextField(max_length=5000, blank=True)
    images         = models.ImageField(upload_to='slider')
    slider_order   = models.IntegerField(default=0)
    status         = models.BooleanField(default=True)
    upload_date    = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.slider_title

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images' 
class GalleryInfo(models.Model):
    type = (
        ('1',  'Video Gallery'),
        ('2',  'Photo Gallery'),
    )
    gallery_type  = models.CharField(max_length=3, choices=type)
    image_choice = (
        ('1',  'Hostel'),
        ('2',  'Library'),
        ('3',  'Lab'),
        ('5',  'ID Card'),
    )
    gallery_for     = models.CharField(max_length=3, choices=image_choice, blank=True)
    gallery_title   = models.CharField(max_length=100, blank=True)
    gallery_images  = models.ImageField(upload_to='gallery', blank=True)
    gallery_link    = models.CharField(max_length=250)
    gallery_order   = models.IntegerField()
    status          = models.BooleanField(default=True)
    upload_date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery_title

    class Meta:
        verbose_name = 'Gallery Info'
        verbose_name_plural = 'Add Gallery'

class PreviousEvents(models.Model):
    previous_title  = models.CharField(max_length=250, blank = True)
    video_url       = models.CharField(max_length=250)
    gallery_order   = models.IntegerField()
    status          = models.BooleanField(default=True)
    upload_date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.previous_title

    class Meta:
        verbose_name = 'Previous Event'
        verbose_name_plural = 'Previous Event'

class SchoolProfile(models.Model):
    school_name       = models.CharField(max_length=160)
    slugan            = models.CharField(max_length=100, blank=True)
    email             = models.EmailField(max_length=70,blank=True)
    phone             = models.CharField(max_length=20)
    mobile            = models.CharField(max_length=15)
    address           = models.CharField(max_length=200)
    web_address       = models.CharField(max_length=200,blank=True)
    logo              = models.ImageField(upload_to='company_info')
    facebook_id       = models.CharField(max_length=200,blank=True)
    twitter_id        = models.CharField(max_length=200,blank=True)
    google_id         = models.CharField(max_length=200,blank=True)
    youtube_id        = models.CharField(max_length=200,blank=True)
    linkedin_id       = models.CharField(max_length=200,blank=True)
    copyright_name    = models.CharField(max_length=200,blank=True)
    status            = models.BooleanField(default=True)
    
    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = 'School Profile'
        verbose_name_plural = 'School Profile'


class MessageInfo(models.Model):
    message_type = (
        ('1',  'Welcome Message'),
        ('2',  'Chairman Message'),
        ('3',  'Principal Message'), 
        ('4',  'President Message'), 
        ('5',  'General Secretary Message'), 
    )
    message_for     = models.CharField(max_length=1, choices=message_type)
    # message_title   = models.CharField(max_length=100, blank=True)
    details         = RichTextField(blank=True)
    persion_images  = models.ImageField(upload_to='images/institute', blank=True)
    status          = models.BooleanField(default=True)
    upload_date     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.message_for)

    class Meta:
        verbose_name = 'Academic Message'
        verbose_name_plural = 'Academic Message'

class NoticeAndEvent(models.Model):
    type = (
        ('1',  'Notice'),
        ('2',  'Events'),
    )
    notice_or_event  = models.CharField(max_length=3, choices=type)
    title            = models.CharField(max_length=100, blank=True)
    details          = RichTextField(blank=True)
    upload_images    = models.ImageField(upload_to='notice_event_image', blank=True)
    notice_file      = models.FileField(upload_to='notice_file', blank=True)
    upload_date      = models.DateField(auto_now_add=True)
    status           = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Notice Event'
        verbose_name_plural = 'Add Notice and Event'

class ImportantLink(models.Model):
    link_name      = models.CharField(max_length=100)
    link_url       = models.CharField(max_length=60, blank=True)
    order          = models.IntegerField()
    status         = models.BooleanField(default=True)

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name = 'Important Link'
        verbose_name_plural = 'Add Important Link'

class Contact(models.Model):
    name             = models.CharField(max_length = 100)
    email            = models.EmailField(max_length = 100,blank = True)
    subject          = models.CharField(max_length = 150)
    phone            = models.CharField(max_length = 20)
    message          = RichTextField()
    message_date     = models.DateTimeField(auto_now_add=True)
    status           = models.BooleanField(default = True)

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

class Session(models.Model):
    session_name  = models.IntegerField(default=0, unique=True)
    insert_date   = models.DateTimeField(auto_now_add=True)
    status        = models.BooleanField(default=1)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = "Year"
        verbose_name_plural = "Years" 



class AllMember(models.Model):
    name               = models.CharField(max_length=100, blank=True)
    father_name        = models.CharField(max_length=100, blank=True)
    mother_name        = models.CharField(max_length=100, blank=True)
    qualification      = models.CharField(max_length=100, blank=True)
    email              = models.EmailField(max_length=100, blank=True)
    phone              = models.CharField(max_length=100, blank=True)
    date_of_birth      = models.DateField(auto_now_add = False)
    genders = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Others'),
    )
    gender             = models.CharField(max_length=1, choices = genders)
    present_address    = models.CharField(max_length=500,blank=True)
    permament_address  = models.CharField(max_length=500,blank=True)
    batch              = models.ForeignKey(Batch, on_delete=models.CASCADE)
    member_image       = models.FileField(upload_to='member_image',blank=True)
    password           = models.CharField(max_length=12)
    pass_inword        = models.CharField(max_length=12)
    order              = models.IntegerField(default=0)
    facebook           = models.CharField(max_length=200,blank=True)
    twitter            = models.CharField(max_length=200,blank=True)
    status             = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'All Member'
        verbose_name_plural = 'All Members'

class UserRegistion(models.Model):
    register_name      = models.CharField(max_length=100, blank=True)
    email              = models.EmailField(max_length=100, blank=True)
    phone              = models.CharField(max_length=100, blank=True)
    designation        = models.CharField(max_length=50, blank=True)
    qualification      = models.CharField(max_length=300, blank=True)
    date               = models.DateField(auto_now_add = False)
    password           = models.CharField(max_length=50, null=True)
       
    genders = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Others'),
    )
    gender             = models.CharField(max_length=1, choices = genders)
    present_address    = models.CharField(max_length=500,blank=True)
    permament_address  = models.CharField(max_length=500,blank=True)
    batch              = models.ForeignKey(Batch, on_delete=models.CASCADE,blank=True,null=True)
    register_image     = models.FileField(upload_to='member_image',blank=True)
    order              = models.IntegerField(default=0)
    facebook           = models.CharField(max_length=200,blank=True)
    twitter            = models.CharField(max_length=200,blank=True)
    status             = models.BooleanField(default=True)

class ContactUs(models.Model):
    name               = models.CharField(max_length=100, blank=True)
    email              = models.EmailField(max_length=100, blank=True)
    subject            = models.CharField(max_length=100, blank=True)
    phone              = models.CharField(max_length=100, blank=True)
    message            = models.CharField(max_length=100, blank=True)
    status             = models.BooleanField(default=True)

    def __str__(self):
        return self.name   

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact US'

class UserRegistration(models.Model):
    register_name     = models.CharField(max_length=160)
    email             = models.EmailField(max_length=70,blank=True)
    designation       = models.CharField(max_length=150)
    phone             = models.CharField(max_length=20)
    gender            = models.CharField(max_length=50)
    password          = models.CharField(max_length=20)
    facebook_id       = models.CharField(max_length=200,blank=True)
    twitter_id        = models.CharField(max_length=200,blank=True)
    status            = models.BooleanField(default=True)
    
    def __str__(self):
        return self.register_name

    class Meta:
        verbose_name = 'User Registration'
        verbose_name_plural = 'User Registration'
        
# class MemberAdmission(models.Model):
#     student_name     = models.CharField(max_length = 100)
#     father_name      = models.CharField(max_length = 100)
#     mother_name      = models.CharField(max_length = 100)
#     batch_list = (
#         ('1', 'ষষ্ঠ শ্রেণী'),
#         ('2', 'সপ্তম শ্রেণী'),
#         ('3', 'অষ্টম শ্রেণী'),
#         ('4', 'নবম শ্রেণী'),
#         ('৫', 'দশম শ্রেণী')
#     )
#     class_for        = models.CharField(max_length=1, choices = batch_list)
#     group_list = (
#         ('1',  'Science'),
#         ('2',  'Business'),
#         ('3',  'Humanities'),
#     )
#     group_for        = models.CharField(max_length=1, choices = group_list, blank = True, null=True)
#     genders_types    = (
#         ('Male',  'Male'),
#         ('Female', 'Female'),
#         ('Others', 'Others'),
#     )
#     st_gender        = models.CharField(max_length=20, choices = genders_types)
#     religion_types   = (
#         ('Islam', 'Islam'),
#         ('Christianity', 'Christianity'),
#         ('Hinduism', 'Hinduism'),
#         ('Buddhism', 'Buddhism'),
#     )
#     religion         = models.CharField(max_length=30, choices = religion_types) 
#     group_type = (
#         ('N/A', 'N/A'),
#         ('A+', 'A+'),
#         ('A-', 'A-'),
#         ('B+', 'B+'),
#         ('B-', 'B-'),
#         ('AB+', 'AB+'),
#         ('AB-', 'AB-'),
#         ('O+', 'O+'),
#         ('O-', 'O-'),
#     )
#     blood_group      = models.CharField(max_length=20, choices=group_type,blank=True) 
#     session          = models.ForeignKey(Session, on_delete=models.CASCADE)
#     date_of_birth    = models.DateField(auto_now_add=False)
#     photo            = models.ImageField(upload_to='photo',blank=True)
#     email            = models.EmailField(max_length = 100, blank = True)
#     phone            = models.CharField(max_length = 20)
#     nid              = models.CharField(max_length = 30)
#     address          = models.CharField(max_length = 150, blank=True)
#     admission_date   = models.DateTimeField(auto_now_add=True)
#     facebook_id      = models.CharField(max_length = 250, blank=True)
#     twitter_id       = models.CharField(max_length = 250, blank=True)
#     status           = models.BooleanField(default = True)

#     def __str__(self):
#         return self.student_name   

#     class Meta:
#         verbose_name = 'Member Admission'
#         verbose_name_plural = 'Member Admissions' 
   
# # .....................................admin.....................................................


class EmployeeList(models.Model):
    employee_id             = models.IntegerField(unique = True)
    employee_name           = models.CharField(max_length=40)
    short_name              = models.CharField(max_length=7, blank=True)
    father_name             = models.CharField(max_length=40, blank=True)
    mother_name             = models.CharField(max_length=40, blank=True)
    emp_img                 = models.ImageField(upload_to='emp_img', blank=True)
    emp_password            = models.CharField(max_length=100, blank=True)
    qualification           = models.CharField(max_length=70, blank=True)
    blood_group_type = (
        ('1', 'N/A'),
        ('2', 'A+'),
        ('3', 'A-'),
        ('4', 'B+'),
        ('5', 'B-'),
        ('6', 'AB+'),
        ('7', 'AB-'),
        ('8', 'O+'),
        ('9', 'O-'),
    )
    blood_group             = models.CharField(max_length=2, choices=blood_group_type,blank=True)
    religion_types        = (
        ('1',  'Islam'),
        ('2',  'Christianity'),
        ('3',  'Hinduism'),
        ('4',  'Buddhism'),
        ('5',  'Chinese traditional religion'),
        ('6',  'African traditional religions'),
    )
    emp_religion            = models.CharField(max_length=1, choices = religion_types)
    genders_types           = (
        ('1',  'Male'),
        ('2',  'Female'),
        ('3',  'Others'),
    )
    emp_gender              = models.CharField(max_length=1, choices = genders_types)
    desig_types           = (
        ('1',  'Principal'),
        ('2',  'Employee'),
        ('3',  'IT Officer'),
        ('4',  'Vice Principal'),
    )
    desig_name              = models.CharField(max_length=1, choices = desig_types)
    # dpt_name                = models.ForeignKey(Department, on_delete=models.CASCADE)
    fitness_details         = models.TextField(blank=True)
    medical_certificate     = models.ImageField(upload_to='medical_certificate', blank=True)    
    emp_mobile              = models.CharField(max_length=15, blank=True)
    email_address           = models.EmailField(max_length=80, blank = True)
    join_date               = models.DateField(auto_now_add=False)
    resign_date             = models.DateField(auto_now_add=True)
    date_of_birth           = models.DateField(auto_now_add=False)
    national_id             = models.CharField(max_length=40, blank=True)
    basic_salary            = models.FloatField(default=0)
    starting_salary         = models.FloatField(default=0, blank=True)
    present_address         = models.TextField(blank=True)
    permanent_address       = models.TextField(blank=True)
    added_by                = models.CharField(max_length=80, blank=True)
    is_teacher              = models.BooleanField(default=0)
    insert_date             = models.DateTimeField(auto_now_add=True)
    last_update             = models.DateTimeField(auto_now=True)
    insert_by               = models.IntegerField(default=0)
    update_by               = models.IntegerField(default=0)    
    status                  = models.BooleanField(default=1)

    def __str__(self):
        return self.employee_name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

# class TeacherList(models.Model):
#     teacher_name            = models.ForeignKey(EmployeeList, on_delete=models.CASCADE)
#     class_name              = models.ForeignKey(ClassInfo, on_delete=models.CASCADE)
#     shift_name              = models.ForeignKey(Shift, on_delete=models.CASCADE)
#     section_name            = models.ForeignKey(Section, on_delete=models.CASCADE)
#     running_year            = models.ForeignKey(Years, on_delete=models.CASCADE)
#     Version_type = (
#         ('1', 'Bangla Medium'),
#         ('2', 'English Version'),
#     )
#     Version                 = models.CharField(max_length=1, choices=Version_type, blank=True)   
#     group_type              = models.ForeignKey(GroupTypeList, on_delete = models.CASCADE, blank=True, null=True)
#     status                  = models.BooleanField(default=1)

#     def __str__(self):
#         return str(self.teacher_name)

#     class Meta:
#         verbose_name = "Teacher List"
#         verbose_name_plural = "Teacher List"


