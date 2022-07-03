import profile
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(models.Model):
    first_name= models.CharField(max_length=30)
    last_name= models.CharField(max_length=30)
    email_address= models.EmailField(max_length=300)
    user_profile = models.URLField('user profile address', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Team(models.Model):
    team_name = models.CharField(max_length=256, default='Team Name')
    #manager = models.ForeignKey(User, blank=True, related_name='manager of the group', on_delete=models.DO_NOTHING)
    team_members = models.ManyToManyField(User, blank= True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.team_name


class Tag(models.Model):
    tag = models.CharField(max_length=256)

    def __str__(self):
        return self.tag

class BugTag(models.Model):
    tag = models.CharField(max_length=256)

    def __str__(self):
        return self.tag







# the projects
class Project(models.Model):
    project_name = models.CharField(max_length=30) # assin the name of the project
    pub_date = models.DateTimeField(blank = True, null=True)
    owner = models.ForeignKey(User, blank = True, null=True, on_delete=models.DO_NOTHING)
    description = models.TextField(blank= True, max_length=100)
    team = models.ForeignKey(Team, blank = True, null=True, on_delete=models.DO_NOTHING, db_constraint=False)
    tags= models.ManyToManyField(Tag, blank = True)
    githubURL = models.URLField(blank = True, null=True)


    def __str__(self):
        return self.project_name



class Issue(models.Model):

    class SEVERITY_CHOICES(models.TextChoices):
        ENHANCMENT= "1", 'enhancment'
        MINOR="2",'minor' 
        MAJOR="3",'major'
        CRITICAL="4", 'critical'
        BLOCKER= "5",'blocker'
        

    issue_title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pud_date = models.DateTimeField(blank = True, null=True)
    issue_creator = models.ForeignKey(User, blank = True, null=True, on_delete=models.DO_NOTHING, related_name='%(class)s_issue_creator')
    issue_solver = models.ForeignKey(User, blank = True, null=True, on_delete=models.DO_NOTHING, related_name='%(class)s_issue_solver')
    bug_tags = models.ManyToManyField(BugTag, blank = True)
    severity = models.CharField(max_length=15, choices=SEVERITY_CHOICES.choices, null=True ,blank = True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE,null = True)


    def __str__(self):
        return self.issue_title


