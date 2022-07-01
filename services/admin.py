from django.contrib import admin
from . import models

class HomeContentAdmin(admin.ModelAdmin):
    list_display    = ['content_for', 'pub_date', 'status',]
    search_fields   = [ 'pub_date', 'status',]
    list_filter     = ['status',]

class SliderInfoAdmin(admin.ModelAdmin):
    list_display    = ['slider_title', 'slider_order', 'upload_date', 'status',]
    search_fields   = ['slider_title', 'slider_order', 'status',]
    list_filter     = ['status',]

class AllMemberAdmin(admin.ModelAdmin):
    list_display    = ['name', 'batch','order', 'status',]
    search_fields   = ['name', 'order', 'status',]
    list_filter     = ['status',]

class AllInfoAdmin(admin.ModelAdmin):
    list_display    = ['name', 'designation','order', 'status',]
    search_fields   = ['name', 'order', 'status',]
    list_filter     = ['status',]

class WorkGalleryAdmin(admin.ModelAdmin):
    list_display    = ['work_title','order', 'status',]
    search_fields   = ['work_title', 'order', 'status',]
    list_filter     = ['status',]

class UserRegistionAdmin(admin.ModelAdmin):
    list_display    = ['register_name','email', 'designation','status',]
    search_fields   = ['register_name', 'email', 'status',]
    list_filter     = ['status',]

# class ActivitiesAdmin(admin.ModelAdmin):
#     list_display    = ['activites_name', 'icon', 'order', 'status',]
#     search_fields   = ['activites_name', 'status',]
#     list_filter     = ['status',]

# class FacilityItemAdmin(admin.ModelAdmin):
#     list_display    = ['facility_title', 'facility_type', 'status',]
#     search_fields   = ['facility_title', 'status',]
#     list_filter     = ['status',]

class SchoolProfileAdmin(admin.ModelAdmin):
    list_display    = ['school_name', 'email', 'phone',  'mobile', 'web_address', 'status',]
    search_fields   = ['school_name', 'email', 'phone',  'mobile', 'status',]
    list_filter     = ['status',]

class GalleryInfoAdmin(admin.ModelAdmin):
    list_display    = ['gallery_type', 'gallery_title', 'gallery_for',  'gallery_order', 'gallery_images', 'status',]
    search_fields   = ['gallery_title',]
    list_filter     = ['status',]

class PreviousEventAdmin(admin.ModelAdmin):
    list_display    = ['previous_title', 'gallery_order','status', 'status']
    search_fields   = ['previous_title']
    list_filter     = ['status']

# class PreviousEventsAdmin(admin.ModelAdmin):
#     list_display    = ['gallery_type', 'gallery_title', 'gallery_for',  'gallery_order', 'gallery_images', 'status',]
#     search_fields   = ['gallery_title',]
#     list_filter     = ['status',]

# class AcademicTeamAdmin(admin.ModelAdmin):
#     list_display    = ['academic_member','member_name','designation', 'qualification', 'email', 'team_order', 'status']
#     search_fields   = ['member_name', 'email', 'mobile',]
#     list_filter     = ['status',]

class MessageInfoAdmin(admin.ModelAdmin):
    list_display    = ['message_for', 'upload_date', 'status']
    search_fields   = ['message_for', 'upload_date', 'status']
    list_filter     = ['status',]


class NoticeAndEventAdmin(admin.ModelAdmin):
    list_display    = ['notice_or_event','title', 'upload_date', 'status']
    search_fields   = ['notice_or_event','title', 'upload_date', 'status']
    list_filter     = ['status',]

# class ImportantLinkAdmin(admin.ModelAdmin):
#     list_display    = ['link_name','link_url', 'order', 'status']
#     search_fields   = ['link_name', 'status']
#     list_filter     = ['status',]

# class JobCircularAdmin(admin.ModelAdmin):
#     list_display    = ['job_title', 'deadline', 'publish_date', 'status']
#     search_fields   = ['job_title', 'deadline',]
#     list_filter     = ['status',]

# class ContactAdmin(admin.ModelAdmin):
#     list_display    = ['name', 'email','subject','message_date','status']
#     search_fields   = ['email']
#     date_hierarchy = 'message_date'

 
admin.site.register(models.HomeContent, HomeContentAdmin)
admin.site.register(models.SliderInfo, SliderInfoAdmin)
admin.site.register(models.AllMember, AllMemberAdmin)
admin.site.register(models.AllInfo, AllInfoAdmin)
admin.site.register(models.WorkGallery, WorkGalleryAdmin)
admin.site.register(models.UserRegistion, UserRegistionAdmin)
admin.site.register(models.ContactUs)


# admin.site.register(models.Activities, ActivitiesAdmin)
# admin.site.register(models.FacilityItem, FacilityItemAdmin)
admin.site.register(models.SchoolProfile, SchoolProfileAdmin)
admin.site.register(models.GalleryInfo, GalleryInfoAdmin)
admin.site.register(models.PreviousEvents, PreviousEventAdmin)
# admin.site.register(models.AcademicTeam, AcademicTeamAdmin)
admin.site.register(models.MessageInfo, MessageInfoAdmin)
admin.site.register(models.NoticeAndEvent)
admin.site.register(models.ImportantLink)
# admin.site.register(models.JobCircular, JobCircularAdmin)
# admin.site.register(models.ExamAdvice)
admin.site.register(models.CommitteeInfo)
admin.site.register(models.Contact)
# admin.site.register(models.AdmissionRequest)
# admin.site.register(models.ExamInfo)
# admin.site.register(models.GroupTypeList)
# admin.site.register(models.Department)
# admin.site.register(models.Shift)
# admin.site.register(models.Section)
admin.site.register(models.Session)   
admin.site.register(models.Batch)  


