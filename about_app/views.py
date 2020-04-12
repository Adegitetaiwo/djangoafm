from django.shortcuts import render
from .models import testimony_s, firstMinister, secondMinister, thirdMinister
# Create your views here.

def testimony(request, id):
    testimonies = testimony_s.objects.get(id=id)
    testimony = testimony_s.objects.all()[:3]

    content = {
        'post':testimony,
        'testimony':testimonies,
    }
    return render(request, 'testimony-single.html', content)
    
def about(request):

    testimonies = testimony_s.objects.all()[:10]
    firstMinister_ = firstMinister.objects.last()
    secondMinister_ = secondMinister.objects.last()
    thirdMinister_ = thirdMinister.objects.last()

    content = {
        'testimonies':testimonies,
        'firstMinister':firstMinister_,
        'secondMinister':secondMinister_,
        'thirdMinister':thirdMinister_,
    }
    
    return render(request, 'about.html', content)

