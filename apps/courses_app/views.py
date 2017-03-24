from django.shortcuts import render, redirect
from .models import Course
from ..login.models import User
from django.db.models import F, Count


def index(request):
    context = {
    'courses': Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def process(request):
    if request.method == 'POST':
        course = Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('courses:index')

def destroy(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, 'courses_app/destroy.html', context)

def delete(request, id):
    post_id = Course.objects.get(id=id)
    post_id.delete()
    return redirect('courses:index')

def add_user(request):
    if request.method == 'POST':
        selected_user = User.objects.get(id = request.POST['user'])
        selected_course = Course.objects.get(id = request.POST['course'])
        selected_course.user.add(selected_user)
        selected_course.save()

    countusers = Course.objects.annotate(num_users=Count('user'))

    context = {
        "users": User.objects.all(),
        "courses": Course.objects.all(),
        "counts": countusers
    }
    return render(request, 'courses_app/user_courses.html', context)

def back(request):
    return redirect('/')
