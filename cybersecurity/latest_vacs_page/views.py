from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_vacancies


async def fetch_vacancies(request):
    """Ответ API"""
    profession = request.GET.get('profession', 'безопасность')
    vacancies = await get_vacancies(profession)
    return JsonResponse({'vacancies': vacancies})


async def render_vacancies(request):
    """Рендер страницы последних вакансий"""
    vacancies = await get_vacancies('Специалиста по информационной безопасности')
    return render(request, 'lastest_vacs_page.html', {'vacancies': vacancies})
