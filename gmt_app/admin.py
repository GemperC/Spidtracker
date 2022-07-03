from django.contrib import admin
from .models import Project, User, Team, Tag, Issue



admin.site.register(User)
admin.site.register(Team)
admin.site.register(Tag)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'pub_date', 'owner', 'team', 'get_tags')
    ordering = ('project_name',)
    search_fields = ('project_name','pub_date', 'owner__first_name', 'tags__tag')

    def get_tags(self, obj):
        return ",\n".join([t.tag for t in obj.tags.all()])


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('issue_title',)




