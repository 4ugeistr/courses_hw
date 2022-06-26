from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Subject, StudentGroup, Student

# Create your views here.
class MyView(View):
    def get(self, request):
        subjects = Subject.objects.all()
        subjects_data=[]
        for subject in subjects:
            subjects_data.append({
                "name":subject.name
            })
        return JsonResponse({"data":subjects_data})

    def post(self, request):
        return HttpResponse('no POST response yet')


class MyViewWithPK(View):
    def get(self, request, pk):
        try:
            #subject = Subject.objects.get(pk=pk)
            groups=StudentGroup.objects.filter(subjects__id=pk)
            students=Student.objects.filter(group__subjects__id=pk)
            data=[]
            for student in students:
                data.append({"name":student.name})
        except Subject.DoesNotExist:
            subjects_data = {}
        return JsonResponse({"data":data})

    def post(self, request):
        return HttpResponse('no POST response yet')
