from django.shortcuts import render
from vacancies.models import Vacancy


def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    context = {'vacancies': vacancies}
    return render(request, 'example_for_vacancy.html', context)
