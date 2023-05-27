from django.http import HttpResponse
from django.shortcuts import render

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
    return HttpResponse("Wallahh chall gayaaa... !!!!")


def courses(request):
    return HttpResponse("Achha ab padhega bhiii... !!!!")

def courseDetails(request, courseId):
    return HttpResponse(courseId)



