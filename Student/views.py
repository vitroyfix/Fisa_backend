from django.shortcuts import render
from .models import Student
from Attendees.models import Attend  # model linking student to events

def students_view(request):
    students = Student.objects.all()
    
    # Prepare a dictionary of student -> events
    student_events = {}
    for student in students:
        attends = Attend.objects.filter(student=student)
        student_events[student.id] = [attend.event for attend in attends]
    
    return render(request, "students.html", {
        "students": students,
        "student_events": student_events
    })
