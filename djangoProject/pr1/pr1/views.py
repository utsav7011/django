from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title':'Home Page -_-',
        "h1": "this is the heading 1 from the django to HTML"
    }
    return render(request, "index.html", data)

def aboutUs(request):
    return HttpResponse("Wallahh chall gayaaa... !!!!")


def courses(request):
    return HttpResponse("Achha ab padhega bhiii... !!!!")

def courseDetails(request, courseId):
    return HttpResponse(courseId)



