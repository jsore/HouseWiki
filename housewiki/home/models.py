"""
…/HouseWiki/housewiki/home/models.py
"""


from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# def get_absolute_url(list_name):
    # return reverse(f'housewiki:')


# each attribute in each defined class will have a table
# created for it by Django in the DB


class Milestone(models.Model):

    MILESTONE_STATUS_CHOICES = (('reached', 'Reached'),
                                ('not reached', 'Not Reached'))

    # to be used as title, VARCHAR in DB
    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250,
                            ##unique_for_date='Reached'
                            unique=True)

    # create a foreign key in DB using primary key of User
    creator = models.ForeignKey(User,
                                # required but also SQL standard
                                # delete Milestones on user delete
                                on_delete=models.CASCADE,
                                # the reverse relationship
                                # from User to milestone
                                related_name='milestones')

    comment = models.TextField(null=True,
                               blank=True)

    ##reached_date = models.DateTimeField(default=timezone.now)

    # saves the date automatically when creating an object
    created = models.DateTimeField(auto_now_add=True)

    # saves the date automatically when saving an object
    updated = models.DateTimeField(auto_now=True)

    status = models.CharField(max_length=20,
                              choices=MILESTONE_STATUS_CHOICES,
                              default='not reached')

    ##reached = models.BooleanField(default=False)

    class Meta:
        # recent to oldest when querying DB
        ordering = ('-created',)

    # human readable representation of this object
    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('housewiki:')



class Question(models.Model):

    QUESTION_STATUS_CHOICES = (('answered', 'Answered'),
                               ('unanswered', 'Unanswered'))

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    supplemental_example = models.TextField(null=True, blank=True)
    answer = models.TextField(null=True, blank=True)
    answered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('answered',)

    def __str__(self):
        return self.title



class WishList(models.Model):

    WISH_RANKING_CHOICES = (('dealbreaker (1)', 'Dealbreaker (1)'),
                            ('very important (2)', 'Very Important (2)'),
                            ('important (3)', 'Important (3)'),
                            ('kind of important (4)', 'Kind of Important (4)'),
                            ('almost petty (5)', 'Almost Petty (5)'),
                            ('definitely petty (6)', 'Definitely Petty (6)'))

    wish = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    ranking = models.CharField(max_length=25,
                               choices=WISH_RANKING_CHOICES,
                               default='kind of important')

    class Meta:
        ordering = ('ranking',)

    def __str__(self):
        return self.wish


class KnowledgeAndTips(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title


class ThingsToConsider(models.Model):

    CONSIDERED_RANKING_CHOICES = (('high importance (1)', 'High Importance (1)'),
                                  ('medium importance (2)', 'Medium Importance (2)'),
                                  ('low importance (3)', 'Low Importance (3)'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    ranking = models.CharField(max_length=25,
                               choices=CONSIDERED_RANKING_CHOICES,
                               default='medium importance (2)')

    class Meta:
        ordering = ('ranking',)

    def __str__(self):
        return self.title
