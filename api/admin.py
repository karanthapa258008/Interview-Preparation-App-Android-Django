from django.contrib import admin
from .models import Question,InterviewQuestion,ApptitudeQuestion

admin.site.register(Question)
admin.site.register(InterviewQuestion)
admin.site.register(ApptitudeQuestion)
# Register your models here.
