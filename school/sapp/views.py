from django.contrib import auth, messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import register, order, Course, Department,material,purpose
from .forms import LoginForm
# Create your views here.
from django.template.context_processors import request


def index(request):

     return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                user = register.objects.get(name=name,password=password)
                # User authenticated, you can set a session here
                # For security reasons, it's recommended to use Django's built-in authentication system instead of storing passwords in plain text.
                return redirect("/welcome/")  # Redirect to a success page
            except register.DoesNotExist:
                # User not found, handle authentication failure
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





def reg(request):
   if request.method=='POST':
        name=request.POST.get('name','')
        password=request.POST.get('psw','')
        cpassword=request.POST.get('cpsw','')
        t1=register(name=name,password=password,cpassword=cpassword)
        if password==cpassword:
            t1.save()
            return redirect("/login/")

        else:
              messages.info(request, "Invalid")
              return redirect("/reg/")

   return render(request,'register.html')


def newpage(request):
     user=register.objects.all()
     return render(request,'newpage.html',{'user':user})





def tnx(request):
   return render(request,'tnx.html')
def profile(request):

    department = Department.objects.all()
    course = Course.objects.all()
    mat=material.objects.all()
    purpos=purpose.objects.all()





    if request.method=='POST':
        nam=request.POST.get('nam',)
        dob=request.POST.get('dob',)
        age=request.POST.get('age',)
        gender=request.POST.get('gender',)
        phone=request.POST.get('phone',)
        email=request.POST.get('email',)
        address=request.POST.get('address',)
        dep=request.POST.get('dep',)
        cou=request.POST.get('cou',)
        pur=request.POST.get('pur',)
        mate=request.POST.get('mate',)

        prof=order(nam=nam,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,dep=dep,cou=cou,pur=pur,mate=mate)
        prof.save()
        return redirect("/tnx/")


    return render(request,'course.html',{'mat':mat,'purpos':purpos})
    # appname/views.py

#
#
#     department = Department.objects.all()
#     course = Course.objects.all()
#
#
# def getdata(request):
#     # template_name = 'course.html'
#     # deptcontext = Department.objects.all()
#     # coucontext = Course.objects.all()
#
#     return render(request,'.html')


