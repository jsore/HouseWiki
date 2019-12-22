"""
…/HouseWiki/housewiki/home/views.py

Defines logic for consuming requests, returns a rendered
template after passing any required variables and data to
the template.
"""


from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Milestone, Question, WishList, KnowledgeAndTips, ThingsToConsider


def dashboard(request):

    # grab all of our objects for an overview
    milestone_list = Milestone.objects.order_by('-created')[:1]
    question_list = Question.objects.order_by('-created')[:1]
    wishlist_list = WishList.objects.order_by('-created')[:1]
    knowledge_and_tips_list = KnowledgeAndTips.objects.order_by('-created')[:1]
    things_to_consider_list = ThingsToConsider.objects.order_by('-created')[:1]



    # instantiate Paginator class with the number of objects
    # to display per page
    ##paginated_milestones = Paginator(milestone_list, 4)
    ##paginated_questions = Paginator(question_list, 4)
    ##paginated_wishes = Paginator(wishlist_list, 4)

    # 'page' GET param indicates the current page number
    ##page = request.GET.get('page')


    # get objects for current page with Paginator.page()
    ##try:
    ##    milestones = paginated_milestones.page(page)
    ##    questions = paginated_questions.page(page)
    ##    wishes = paginated_wishes.page(page)


    return render(request,
                  'housewiki/dashboard/index.html',
                  {'milestone_list': milestone_list,
                   'question_list': question_list,
                   'wishlist_list': wishlist_list,
                   'things_to_consider_list': things_to_consider_list,
                   'knowledge_and_tips_list': knowledge_and_tips_list})


def all_milestones(request):
    queryset = Milestone.objects.all()
    # context variable for the queryset results
    context_object_name = 'milestones'
    paginate_by = 25
    template_name = 'housewiki/milestones/index.html'


# class MilestoneView(ListView):
#
#     queryset = Milestone.objects.all()
#     context_object_name = 'milestones'
#     paginate_by = 4
#     template_name = 'home/dashboard/milestones.html'

