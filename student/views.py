from django.shortcuts import render,redirect
from .models import *

def student_list(request):
    st = Student.objects.all()
    context = {
        "st":st
    }
    return render(request,"student/student_list.html",context)


def add_student(request):
    if request.method == "POST":
        data = request.POST
        name = data["name"]
        std = data["std"]
        section = data["section"]
        roll_no = data["roll_no"]
        address = data["address"]
        mobile_no = data["mobile_no"]
        blood_group = data["blood_group"]


        ast = Student(
            name = name,
            std = std,
            section = section,
            roll_no = roll_no,
            address= address,
            mobile_no = mobile_no,
            blood_group = blood_group, 
        )
        ast.save()
    return render(request,"student/add_student.html")

def edit_student(request,id):
        if request.method == "POST":
           data = request.POST
           name = data["name"]
           std = data["std"]
           section = data["section"]
           roll_no = data["roll_no"]
           address = data["address"]
           mobile_no = data["mobile_no"]
           blood_group = data["blood_group"]

           s = Student.objects.get(pk=id)
           s.name = name
           s.std = std
           s.section = section
           s.roll_no = roll_no
           s.address= address
           s.mobile_no = mobile_no
           s.blood_group = blood_group

           s.save()
           return redirect("student_list")
        else:
            est = Student.objects.get(pk=id)
        return render(request,"student/edit_student.html",{"est":est})

def delete_student(request,id):
    dst = Student.objects.filter(id=id)
    dst.delete()
    context = {
        'dst':dst
    }
    return redirect("student_list")