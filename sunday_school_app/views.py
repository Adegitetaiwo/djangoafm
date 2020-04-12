from django.shortcuts import render
from .models import englishSchoolA, frenchSchoolA, yorubaSchoolI
from .models import yorubaSchoolA, englishSchoolI, frenchSchoolI, elementarySchool
# Create your views here.
def sundaySchool(request):

    english_lesson_adult = englishSchoolA.objects.last()
    french_lesson_adult = frenchSchoolA.objects.last()
    yoruba_lesson_adult = yorubaSchoolA.objects.last()
    english_lesson_intermediate = englishSchoolI.objects.last()
    french_lesson_intermediate = frenchSchoolI.objects.last()
    yoruba_lesson_intermediate = yorubaSchoolI.objects.last()
    english_lesson_Elementary = elementarySchool.objects.last()

    content = {
        'englishA': english_lesson_adult,
        'frenchA':french_lesson_adult,
        'yorubaA' : yoruba_lesson_adult,
        'englishI': english_lesson_intermediate,
        'frenchI':french_lesson_intermediate,
        'yorubaI' : yoruba_lesson_intermediate,
        'element':english_lesson_Elementary,

    }

    return render(request, 'sunday_school.html', content)

def lesson_adult_e(request, id):
    english_lesson_adult = englishSchoolA.objects.get(id=id)
    
    content = {
        'englishA': english_lesson_adult,
    }
    return render(request, 'school-single.html', content)

def lesson_adult_f(request, id):
    french_lesson_adult = frenchSchoolA.objects.get(id=id)
    content = {
        'frenchA':french_lesson_adult,
    }
    return render(request, 'school-single.html', content)

def lesson_adult_y(request, id):
    yoruba_lesson_adult = yorubaSchoolA.objects.get(id=id)
    content = {
        'yorubaA' : yoruba_lesson_adult,
    }
    return render(request, 'school-single.html', content)

def lesson_inter_e(request, id):
    english_lesson_intermediate = englishSchoolI.objects.get(id=id)
    content = {
        'englishI': english_lesson_intermediate,
    }
    return render(request, 'school-single.html', content)

def lesson_inter_f(request, id):
    french_lesson_intermediate = frenchSchoolI.objects.get(id=id)
    content = {
        'frenchI':french_lesson_intermediate,
    }
    return render(request, 'school-single.html', content)

def lesson_inter_y(request, id):
    yoruba_lesson_intermediate = yorubaSchoolI.objects.get(id=id)
    content = {
        'yorubaI' : yoruba_lesson_intermediate,
    }
    return render(request, 'school-single.html', content)

def lesson_element(request, id):
    english_lesson_Elementary = elementarySchool.objects.get(id=id) 
    content = {
        'element':english_lesson_Elementary
    }
    return render(request, 'school-single.html', content)