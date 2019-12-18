from django.contrib import admin

# register models with the admin site
from .models import Milestone, Question


# use a decorator instead of admin.site.register(<Model>)
# to customize how models are displayed
@admin.register(Milestone)
class MilestoneAdmin(admin.ModelAdmin):

    # attributes for setting name of fields, what to show for
    # each Milestone object
    list_display = ('title',
                    'slug',
                    'comment',
                    'created',
                    #'reached_date',
                    'updated',
                    #'reached',
                    'status')

    # filter-by sidebar
    list_filter = (#'reached',
                   #'reached_date',
                   'status',)

    # search bar
    search_fields = ('title', 'comment')

    # autocreate the slug field based on title
    prepopulated_fields =  {'slug': ('title',)}

    raw_id_field = ('creator')

    # nav links to run through milestones by date
    # date_hierarchy = 'reached_date'

    ordering = ('status',
                #'reached_date'
                )


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'supplemental_example',
                    'answered',
                    'answer')
    list_filter = ('answered',)
    search_fields = ('title', 'supplemental_example', 'answer')