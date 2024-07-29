from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse
from core.models import Course, CourseContent, CourseMember, User

# Create your views here.
def index(request):
    return HttpResponse("<h1>Selamat datang di LMS Kita</h1>")
        
def testing(request):
    guru = User.objects.create_user(
            username="guru_1", email="guru_1@email.com",
            password="rahasia", first_name="Guru", last_name="Satu"
            )
    
    Course.objects.create(
        name="Pemrograman Python",
        description="Belajar Pemrograman Python",
        price=500000,
        teacher=guru
    )
    
    return HttpResponse("kosongan")

def allCourses(request):
    courses = Course.objects.all()
    data_resp = []
    for course in courses:
        record = {'id' : course.id, 'name': course.name,
                  'price' : course.price,
                  'teacher':{
                      'id': course.teacher.id,
                      'username': course.teacher.username,
                      'fullname': f"{course.teacher.first_name} {course.teacher.last_name}"
                  }}
        data_resp.append(record)
        
    return JsonResponse(data_resp, safe=False)    


def userProfile(request, user_id):
    user = User.objects.get(pk=user_id)
    data_resp = {'username' : user.username, 'email':user.email, 
                 'fullname':f"{user.first_name} {user.last_name}"}
    
    return JsonResponse(data_resp, safe=False)