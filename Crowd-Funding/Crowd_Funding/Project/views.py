from django.shortcuts import render,HttpResponseRedirect
from Users.models import *


# Create your views here.
# from .models import

def pro(request):
    if request.method == 'POST':
        user = getUser(request)
        newproject = Projects.objects.create(
            title=request.POST['title'], category=request.POST['category'],
            total_target=request.POST['total'],
            start_date=request.POST['start'], end_date=request.POST['end'],
            details=request.POST['desc'], user=user

        )
        tags = request.POST['tag']
        list_tags = list(tags.split(" "))
        images = request.FILES.getlist('photo')
        if newproject:
            for image in images:
                photo = Image.objects.create(
                    images=image,
                    project=newproject
                )
            for tag in list_tags:
                newtag = ProjectsTages.objects.create(
                    tags=tag,
                    project=newproject
                )

        return HttpResponseRedirect("added........")
    else:
        context={}
        user = Register.objects.get(id=request.session['user_id'])
        context['img'] = user.profile_img
        return render(request, 'project_create_form.html',context)




def mytag(obj1,obj2):
    return (obj1+obj2)

def getUser(request):
    user = Register.objects.get(id=request.session['user_id'])
    return user
def show_projects(req):
    context = {}
    user = getUser(req)
    projects = Projects.objects.all()
    context['projects'] = projects
    context['user'] = user

    if (req.method == 'GET'):
        return render(req, 'projects.html', context)
    else:
        project = Projects.objects.get(id=req.POST['project_id'])
        comment.objects.create(
            project_id=project,
            Comend_name=req.POST['Comend_name'],
            comment_body=req.POST['comment_body'],
        )
        return render(req, 'projects.html', context)

def reportss(req):
    context = {}
    user = getUser(req)
    projects = Projects.objects.all()
    project = Projects.objects.get(id=req.POST['project_id'])
    context['projects'] = projects
    context['user'] = user
    reports.objects.create(
        project_id=project,
        user_name=req.POST['user_name'],
        report_body=req.POST['Report_body'],
    )
    return render(req, 'projects.html', context)

def cartegory(req,category_name):
    context = {}
    categoryr = Projects.objects.filter(category=category_name)
    context['projects'] = categoryr

    return render(req, 'projects.html', context)