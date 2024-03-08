from django.shortcuts import render , redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserData,Exam,Exam_data,User_history
from django.http import JsonResponse,Http404,FileResponse
from django.views.decorators.csrf import csrf_exempt
import json

import random

def index(request):
    return redirect('homepage')

def homepage(request):
    return render(request,'homepage.html')

def login_user(request):
    if request.method=="POST":
        name = request.POST["username"]
        pwd = request.POST["pwd"]
        print(name,pwd)
        user = authenticate(request, username=name, password=pwd)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request,'homepage.html')
    else:
        return render(request,'login.html')

def signup_user(request):
        if request.method=='POST':
            username=request.POST['username']
            pwd=request.POST['pwd']
            cnf_pwd=request.POST['cnf_pwd']
            email=request.POST['email']
            if User.objects.filter(username=username):
                messages.error(request,'Username already exist!')
                return redirect('login_user')
            
            if pwd==cnf_pwd:
                myuser=User.objects.create_user(username=username, email=email, password=pwd)
                
                newuser=UserData()
                
                newuser.name=request.POST['name']
                newuser.college_name=request.POST['clg_name']
                print(request.POST['exam'])
                newuser.exam=request.POST['exam']
                newuser.board_10=request.POST['board10']
                newuser.marks_10=request.POST['marks10']
                newuser.username=request.POST['username']
                newuser.pwd=request.POST['pwd']
                newuser.cnf_pwd=request.POST['cnf_pwd']
                newuser.email=request.POST['email']
            
                
                myuser.save()
                newuser.save()
                user = User.objects.get(username=username)
                login(request, user)
                messages.success(request,'Your account has been sucessfully created.')
                return redirect('home')
                #return render(request,'profile.html',context=mydict)
            else:
                messages.error(request,'Password does not match.Try again...')
                return redirect('login')
        else:
            return render(request,'signup.html')
def logout_user(request):
    logout(request)
    messages.success(request,'User loged out sucessfully')
    return redirect('homepage')

def home(request):
        if request.method=='GET':
            username=request.user
            user=UserData.objects.get(username=username)
            mhtcet={}
            Mathematics={}
            info={
                'username':user.username,
                'clg_name':user.college_name,
                'exam':user.exam,
                'board10':user.board_10,
                'marks10':user.marks_10,
                'email':user.email
            }
            for i in Exam.objects.all():
                mhtcet.update({i.id:{'name':i.exam_name,'year':i.exam_year,'date':i.exam_date,'shift':i.exam_shift,'marks':i.exam_marks,'time':f'{i.exam_time//60}:{i.exam_time%60}'}})
            Mathematics={'id':'Mathematics'}
            chem={'id':'Chemistry'}
            phy={'id':'Physics'}
            return render(request,'dashboard.html',{'test':{'MHT-CET':mhtcet},'subject':{'Mathematics':Mathematics,'Chemistry':chem,'Physics':phy},'info':info})
        

#----------------------------------changed for Exam-Window-----------------------------------#
def get_nested_dictionary(request):
    # Your code to fetch the nested dictionary
    global test_id
    try:
        data=Exam_data.objects.filter(exam_id=test_id)
        exam_data=[]
        for i in range(len(data)):
                exam_data.append(
                        {
                            'subject':data[i].subject,
                            'question_num':data[i].question_num,
                            'question':data[i].question,
                            'options':[data[i].option1,data[i].option2,data[i].option3,data[i].option4],
                            'correct_answer':str(data[i].ans),
                            'marks':data[i].marks,
                        }
                )
        random.shuffle(exam_data)
        exam_data= sorted(exam_data, key=lambda x: ("Physics", "Chemistry", "Mathematics").index(x["subject"]))
        nested_dictionary={'id':test_id,'questions':exam_data,'duration':Exam.objects.filter(id=test_id).first().exam_time}
    except:
        data=Exam_data.objects.all().filter(subject=test_id)
        exam_data=[]
        for i in range(len(data)):
                exam_data.append(
                        {
                            'subject':data[i].subject,
                            'question':data[i].question,
                            'options':[data[i].option1,data[i].option2,data[i].option3,data[i].option4],
                            'correct_answer':str(data[i].ans),
                            'marks':data[i].marks,
                        }
                )
        random.shuffle(exam_data)
        exam_data=exam_data[0:10]
        nested_dictionary={'questions':exam_data,'duration':300}
    return JsonResponse(nested_dictionary)

 
def exam(request):
    if request.method=='POST':
        global test_id
        test_id=request.POST['test_id']
        username=request.user
        user=UserData.objects.get(username=username)
        info={
            'username':user.username,
            'clg_name':user.college_name,
            'exam':user.exam,
            'board10':user.board_10,
            'marks10':user.marks_10,
            'email':user.email
        }
        return render(request,'exam_window.html',{'info':info})
    
def add(request):
    pass

def tan(request):
    return render(request,'tan.html')

def syllabus(request):
    with open('media/Syllabus.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=mypdf.pdf'
    return response
#--------------------------------------------------------------not working-------------------------------------------------------
