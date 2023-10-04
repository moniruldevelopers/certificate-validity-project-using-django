from django.shortcuts import render
from .models import Student


def home(request):    
    return render(request, 'certificate_app/home.html')

def search_result(request):
    if request.method == 'GET':
        search_id = request.GET.get('search_id')
        student = Student.objects.filter(id_roll=search_id).first()
        return render(request, 'certificate_app/search_result.html', {'student': student})


