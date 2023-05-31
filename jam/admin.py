from django.contrib import admin
from . models import Login, JobSeeker, Employer, Enquiry, Jobs, Appliedjobs, News
# Register my models
admin.site.register(Login)
admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(Enquiry)
admin.site.register(Jobs)
admin.site.register(Appliedjobs)
admin.site.register(News)
