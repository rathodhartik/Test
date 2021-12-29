from django.shortcuts import render,redirect
from app.models import Student
from.forms import StudentForm,UpdateForm
from django.contrib.auth.decorators import login_required


# View Student Details
@login_required(login_url='login_view')
def studentdetails(request):
    
    stu=Student.objects.all()
    context={"stu":stu}
    return render(request,"app/studentdetails.html",context)


# Add Student Data
@login_required(login_url='login_view')
def addstudent(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("studentdetails")
    context={"form":form}
    return render(request,"app/add.html",context)


# Update Student Data
@login_required(login_url='login_view')
def updatestudent(request,id):
    stud=Student.objects.get(id=id)
    form=UpdateForm(instance=stud)
    if request.method=="POST":
        form=UpdateForm(request.POST,instance=stud)
        if form.is_valid():
            form.save()
            return redirect("studentdetails")
    context={"form":form}
    return render(request,"app/updatestudent.html",context)


# Delete Student Data
@login_required(login_url='login_view')
def delete(request,id):
    st=Student.objects.get(id=id)
    st.delete()
    return redirect("studentdetails")


