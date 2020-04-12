from django.shortcuts import render, redirect
from .models import displaySilder, setCountdownDate, userType
from .models import urgentMessage, sermonUpdate, event, subcribe
from blog_app.models import blog
from sunday_school_app.models import englishSchoolA, englishSchoolI, elementarySchool
from about_app.models import testimony_s
# Create your views here.

def index(request):

    displaySlider = displaySilder.objects.all()
    setCountdownDateTime = setCountdownDate.objects.last()
    userTypes =  userType.objects.all()
    alertMessage = urgentMessage.objects.last()
    sermons = sermonUpdate.objects.all().order_by('-id')[:3]
    blogs = blog.objects.all().order_by('-id')[:3]
    testimonies = testimony_s.objects.all()[:10]
    adult = englishSchoolA.objects.last()
    inter = englishSchoolI.objects.last()
    element = elementarySchool.objects.last()

    if request.method == 'POST':
        email = request.POST['sub']
        subcribe_form = subcribe()
        subcribe_form.email = email
        subcribe_form.save()
        return redirect('.')
    else:
        content = {
            'displaySliders': displaySlider ,
            'setCountdownDates':setCountdownDateTime,
            'userType': userTypes,
            'urgentMessage': alertMessage,
            'sermonUpdates':sermons,
            'blogs':blogs,
            'testimonies':testimonies,
            'adult':adult,
            'inter': inter,
            'element':element,
        }

    return render(request, 'index.html', content )

def events(request):
    events = event.objects.last()

    content = {
        'event':events,
    }
    return render(request, 'event_detail.html', content )