from multiprocessing import context
from django.shortcuts import render,  get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
import json
from rest_framework import viewsets
from .serializers import ProjectSerializer,UserSerializer,TagSerializer,TeamSerializer,BugTagSerializer,IssueSerializer

from requests import request
from authlib.integrations.django_client import OAuth
from django.conf import settings
from urllib.parse import quote_plus, urlencode
from .models import Project, Team, User, Issue
from .forms import ProjectForm, IssueForm, ProjectURLForm
from rest_framework.views import APIView



def index(request):
    return render(
        request,
        "index.html",
        context={
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        },
    )

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("projects")))

def logout(request):
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("index")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )


def all_projects(request):
    project_list = Project.objects.all()
    team_list = Team.objects.all()

    #check if the project form was filled
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects')
    else:
        form = ProjectForm
        context = {'project_list': project_list, 'team_list': team_list, 'form':form}
        return render(request, 'projects.html',context)



def showproject(request, project_id):
    project = Project.objects.get(pk=project_id)

    #update project information
    editPform = ProjectForm(request.POST or None, instance=project)
    if editPform.is_valid():
        editPform.save()
        return HttpResponseRedirect('/projects/'+str(project_id))

    #check if the issue form was filled
    if request.method == "POST":
        form = IssueForm(request.POST, initial={'project': project})
        if form.is_valid():
            form = form.save()
            return HttpResponseRedirect('/projects/'+str(project_id))
    else:
        form = IssueForm(initial={'project': project})
        issues_list = Issue.objects.filter(project=project)

        context = {'form':form, 'project': project, 'issues_list': issues_list, 'editPform':editPform}
        return render(request, 'showproject.html',context)

def delete_project(request, project_id):
    project = Project.objects.get(pk=project_id)
    project.delete()
    return redirect('projects')

def delete_issue(request, project_id,issue_id):
    issue = Issue.objects.get(pk=issue_id)
    issue.delete()
    return redirect('/projects/'+str(project_id))


def updateissue(request, project_id,issue_id):
    issue = Issue.objects.get(pk=issue_id)
    #update issue information
    editSform = IssueForm(request.POST or None, instance=issue)
    if editSform.is_valid():
        editSform.save()
        return HttpResponseRedirect('/projects/'+str(project_id))
    else:
        context = {'editSform':editSform}
        return render(request, 'updateissue.html',context)


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class IssueView(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def project_readme(request,project_id):
    project = Project.objects.get(pk=project_id)

    projectURLForm = ProjectURLForm(request.POST or None, instance=project)
    if projectURLForm.is_valid():
        projectURLForm.save()
        return HttpResponseRedirect('/projects/'+str(project_id)+'/readme')

    else:
        context= {'project': project, 'projectURLForm':projectURLForm}
        return render(request, 'project_readme.html',context)