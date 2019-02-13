from django.shortcuts import render

def Mentee(request):
    return render (request, 'Mentee/Mentee.html', {})
