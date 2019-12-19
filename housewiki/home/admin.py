"""
…/HouseWiki/housewiki/home/admin.py
"""


from django.contrib import admin

# register models with the admin site
from .models import Milestone, Question, WishList


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
                    ##'reached_date',
                    'updated',
                    ##'reached',
                    'status')

    # filter-by sidebar
    list_filter = (##'reached',
                   ##'reached_date',
                   'status',)

    # search bar
    search_fields = ('title', 'comment')

    # autocreate the slug field based on title
    prepopulated_fields =  {'slug': ('title',)}

    raw_id_field = ('creator')

    # nav links to run through milestones by date
    ##date_hierarchy = 'reached_date'

    ordering = (##'reached_date',
                'status',)



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',
                    'supplemental_example',
                    'answered',
                    'answer')
    list_filter = ('answered',)
    search_fields = ('title', 'supplemental_example', 'answer')
    prepopulated_fields =  {'slug': ('title',)}



@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('wish',
                    'slug',
                    'ranking')
    list_filter = ('ranking',)
    search_fields = ('title', 'ranking')
    prepopulated_fields =  {'slug': ('wish',)}
