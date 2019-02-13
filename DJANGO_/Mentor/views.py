from django.shortcuts import render

def Mentor(request):
    return render (request, 'Mentor/Mentor.html', {})