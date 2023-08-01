from django.contrib import admin
from django.http import HttpResponse
from .models import Member,Courses_detail
from django.utils import timezone
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
import io



class MembersAdmin(admin.ModelAdmin):
    search_fields = ('name','id','courses')
    list_display = ["id", "name","surname",  "timestamp" , "fees"]
    
    def save_model(self, request, obj, form, change):
        if obj.id is None:
            courses = form.cleaned_data['courses']
            obj.courses.set(courses)
        else:
            # Update existing object
            pass
    

    def generate_pdf(self, request, queryset):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

        # Create text object
        textobj = c.beginText()
        textobj.setTextOrigin(inch, inch)
        textobj.setFont("Helvetica", 15)

        # Loop over selected members
        for member in queryset:
            # Append member details to the text object
            textobj.textLine(f"ID: {member.id}")
            textobj.textLine(f"Name: {member.name}")
            textobj.textLine(f"Surname: {member.surname}")
            textobj.textLine(f"courses: {member.courses}")
            textobj.textLine("")

        # Finish up
        c.drawText(textobj)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='all_details.pdf')

    generate_pdf.short_description = 'Generate PDF'
    actions = ['generate_pdf']

admin.site.register(Member)

class Courses_detailAdmin(admin.ModelAdmin):
    search_fields = ('course_list' , 'course_fee')
    list_display = ["course_list", "course_fee", "course_time", "course_time2", "instructor"]


    def generate_pdf(self, request, queryset):
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=letter, bottomup=0)

        # Create text object
        textobj = c.beginText()
        textobj.setTextOrigin(inch, inch)
        textobj.setFont("Helvetica", 15)

        # Loop over selected members
        for  Courses_detail in queryset:
            # Append member details to the text object
            textobj.textLine(f"course_name: { Courses_detail.course_list}")
            textobj.textLine(f"fee: { Courses_detail.course_fee}")
            textobj.textLine(f"time: { Courses_detail.course_time}")
            textobj.textLine(f"time2: { Courses_detail.course_time2}")
            textobj.textLine(f"instructor: { Courses_detail.instructor}")
            textobj.textLine("")

        # Finish up
        c.drawText(textobj)
        c.showPage()
        c.save()
        buf.seek(0)

        return FileResponse(buf, as_attachment=True, filename='all_details.pdf')

    generate_pdf.short_description = 'Generate PDF'
    actions = ['generate_pdf']
    
admin.site.register(Courses_detail)

# admin.site.register(UsCoursesDetail)



