from django.shortcuts import render, HttpResponseRedirect

from Users.models import *


def sliders(request):
    if request.method == 'GET':
        context = {}
        Sliders = slider.objects.all()
        context['slider'] = Sliders
        return render(request, 'Admin/Slider.html', context)
    else:
        if request.method == 'POST':

            slidename = request.POST['name']
            slidedesc = request.POST['desc']
            slideimg = request.FILES['slideimg']

            user = slider.objects.create(
                slider_name=slidename, slider_describe=slidedesc, slider_img=slideimg)
    return HttpResponseRedirect('/Admins/Admin')


def delete(request, list_id):
    item = slider.objects.get(pk=list_id)
    item.delete()
    return HttpResponseRedirect('../../Admin')


def Featurd(request):
    if request.method == 'GET':
        context = {}
        Project = Projects.objects.all()
        Featuredss = Featured.objects.all()
        context['Project'] = Project
        context['Feature'] = Featuredss
        pubs = Featured.objects.select_related()
        context['pub'] = pubs
        return render(request, 'Admin/Feature.html', context)
    else:
        if request.method == 'POST':

            proid = request.POST['project']
            user = Featured.objects.create(pro_id=proid)
    return HttpResponseRedirect('/Admins/Featured')


def deletefeate(request, list_id):
    item = Featured.objects.get(pk=list_id)
    item.delete()
    return HttpResponseRedirect('../../Featured')
