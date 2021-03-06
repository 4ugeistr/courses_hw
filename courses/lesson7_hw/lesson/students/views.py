from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
from students.models import Student


def my_view(request):
    if request.method == 'GET':
        return HttpResponse('result')


class MyView(View):
    def get(self, request):
        name = request.GET.get('name', False)
        students = Student.objects.all()
        if name:
            students = students.filter(name=name)
        students_data = []
        for student in students:
            students_data.append({
                "name":student.name
            })
        return JsonResponse({"data":students_data})

    def post(self, request):
        name = request.POST.get('name', '')

        print(name)
        return HttpResponse(name)




class MyViewWithPK(View):
    def get(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            students_data = {
                "name":student.name
            }
        except Student.DoesNotExist:
            students_data = {}

        return JsonResponse({"data":students_data})
