from django.shortcuts import render
from vacancies.models import Vacancy


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'vacancies.html', context)
