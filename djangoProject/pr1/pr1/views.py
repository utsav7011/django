from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import userFrom

def homePage(request):
    data = {
        'title':'Home Page -_-',
        "h1": "this is the heading 1 from the django to HTML",
        'cList': ['php', 'java','c++', 'Django'],
        'numbers':[10, 20, 40, 30, 60, 50],
        'studentDetails': [
            {'name':'one', 'phone':9999999999},
            {'name':'two', 'phone':8888888888}
        ]
    }
    return render(request, "index.html", data)

def aboutUs(request):
    
    if request.method == "GET":
        output = request.GET.get('finalMarks')
    return HttpResponse("Wallahh chall gayaaa... !!!!")


def courses(request):
    return HttpResponse("Achha ab padhega bhiii... !!!!")

def courseDetails(request, courseId):
    return HttpResponse(courseId)

def userForm(request):
    finalMarks = 0
    fn = userForm()
    data = {'form':fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
        finalMarks = n1 + n2
        data = {
            'form':fn,
            'output': finalMarks
        }
        print(n1+n2)
        
        url = '/about-us/?finalMaks={}'.format(finalMarks)
        return HttpResponseRedirect(url)
        
        
    except:
        pass
    return render(request, "userForm.html", {'output' : finalMarks})


def calculator(request):
    c = ''
    try:
        
        if request.method == 'POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            
            if opr == '+':
                c = n1 + n2
            elif opr == '-':
                c = n1 - n2
            elif opr == '*':
                c = n1 * n2
            elif opr == '/':
                c = n1 / n2
            
        print(c)
        
    except:
        c = 'invalid opr....'
    return render(request, "calculator.html", {'c': c})