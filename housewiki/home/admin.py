"""
…/HouseWiki/housewiki/home/admin.py
"""


from django.contrib import admin
from django.utils.text import slugify

# register models with the admin site
from .models import Property, Milestone, Question, WishList, KnowledgeAndTips, ThingsToConsider


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):

    # property_string = Property.class_string(Property)

    list_display = ('floorplan_name',
                    'community_name',
                    'builder_name',
                    'ranking',
                    'cover',
                    'floorplan_link',
                    'square_footage',
                    'bedrooms',
                    'bathrooms',
                    'garage',
                    'optional_floorplan_info',
                    'standout_features',
                    'desired_options',
                    'rounded_total_price',
                    # 'property_string',
                    # 'class_string',
                    # '__str__',
                    'string_property',
                    'slug')

    list_filter = ('ranking', 'builder_name', 'community_name')
    search_fields = ('floorplan_name', 'bedrooms', 'rounded_total_price')
    # prepopulated_fields = {'property_slug': ('class_string',),
    #                        'class_string': ('class_string')}

    # string = Property.class_string
    # prepopulated_fields = {'slug': ('floorplan_name',)}
    # prepopulated_fields = {'slug': (self.__str__(Property),)}
    # prepopulated_fields = {'slug': ('__str__',)}
    # prepopulated_fields = {'slug': ('string_property',)}

    # prepopulated_fields = {'slug': ('-'.join(('floorplan_name',
    #                                           'community_name',
    #                                           'builder_name')),)}

    ordering = ('ranking',)


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


@admin.register(KnowledgeAndTips)
class KnowledgeAndTipsAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',
                    'created')
    list_filter = ('created',)
    search_fields = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ThingsToConsider)
class ThingsToConsiderAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'slug',
                    'created')
    list_filter = ('created',)
    search_fields = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}

