from xml.etree.ElementInclude import include
from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('projects',views.ProjectView)
router.register('issues',views.IssueView)
router.register('user',views.UserView)

urlpatterns = [
    path('api/',include(router.urls)),
    path('', views.index, name='index'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path("projects", views.all_projects, name="projects"),
    path("projects/<project_id>/", views.showproject, name="showproject"),
    path("projects/<project_id>/issues/<issue_id>", views.updateissue, name="updateissue"),
    path('delete_project/<project_id>', views.delete_project, name= "delete_project"),
    path('delete_issue/<project_id>/<issue_id>', views.delete_issue, name= "delete_issue"),
    path('projects/<project_id>/readme/', views.project_readme, name= "project_readme"),
    
]