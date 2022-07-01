from django.shortcuts import render
from .templates import *
from .models import project
# Create your views here.
def home(req):
    context = {}
    projects_for_slide = project.objects.all()
    projects = project.objects.all()
    latest_5projects = project.objects.all()
    context['projects_for_slide'] = projects_for_slide
    context['projects'] = projects
    context['latest_5projects'] = latest_5projects
    return render(req, 'home.html', context)
def about(req):
    return render(req,'about.html')
def boot(req):
    context = {}
    projects_for_slide=project.objects.all()
    projects=project.objects.all()
    latest_5projects = project.objects.all()
    context['projects_for_slide']=projects_for_slide
    context['projects']=projects
    context['latest_5projects']=latest_5projects
    return render(req,'boottemp.html',context)
def cartegory(req,category_name):
    context = {}
    categoryr = project.objects.filter(category=category_name)
    projects_for_slide = project.objects.all()
    #projects = project.objects.all()
    latest_5projects = project.objects.all()
    context['projects_for_slide'] = projects_for_slide
    context['projects'] = categoryr
    context['latest_5projects'] = latest_5projects
    return render(req, 'boottemp.html', context)
def insert(req):
    context={}
    INtrainne = project.objects.all()
    if (req.method == 'GET'):
        return render(req, 'insert.html', context)
    else:
        project.objects.create(
            name=req.POST['name'],
            category=req.POST['category'],
            description=req.POST['description'],
            coverimage=req.POST['coverimage'],
            image1=req.POST['image1'],
            image2=req.POST['image2'],
            image3=req.POST['image3'],
            image4=req.POST['image4'],)

        return render(req,'insert.html',context)

def proj(req):
    return  render(req,'project_create_form.html')
