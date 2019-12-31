"""
…/HouseWiki/housewiki/home/views.py

Defines logic for consuming requests, returns a rendered
template after passing any required variables and data to
the template.
"""


from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from .models import Property, Milestone, Question, WishList, KnowledgeAndTips, ThingsToConsider

# having some issues with template data inheritance
# aware that this isn't ideal but i'm okay with it for now
milestone_list = Milestone.objects.order_by('-created')[:1]
question_list = Question.objects.order_by('-created')[:1]
wishlist_list = WishList.objects.order_by('-created')[:1]
knowledge_and_tips_list = KnowledgeAndTips.objects.order_by('-created')[:1]
things_to_consider_list = ThingsToConsider.objects.order_by('-created')[:1]
property_list = Property.objects.order_by('ranking')

def dashboard(request):

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
                  {'property_list': property_list,
                   'milestone_list': milestone_list,
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


def questions(request):

    context_object_name = 'questions'



    template_name = 'housewiki/questions/index.html'
    # questions = Question.objects.order_by('-created')[1:]
    # questions = queryset.order_by('-created')[1:]
    # paginated_questions = Question.objects.order_by('-created')
    question_list_all = Question.objects.all()

    # paginate_by = 25
    # paginator = Paginator(question_list_all, 20)
    # paginator = Paginator(question_list_all, 10)
    ## paginator = Paginator(question_list_all, 1)
    # try:
    ## page = request.GET.get('page')

    ## try:
    ##   paginated_questions = paginator.get_page(page)
    ## except PageNotAnInteger:
        # If page is not an integer deliver the first page
        ## paginated_questions = paginator.get_page(1)
    ## except EmptyPage:
        ## if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            ## return HttpResponse('')
        # If page is out of range deliver last page of results
        ## paginated_questions = paginator.get_page(paginator.num_pages)

    #if request.is_ajax():
    #    return render(request,
    #                  'images/image/list_ajax.html'
    #                  {…})

    return render(request,
                  'housewiki/questions/index.html',
                  {'question_list_all': question_list_all,
                   ##'paginated_questions': paginated_questions,
                   'property_list': property_list,
                   'milestone_list': milestone_list,
                   'wishlist_list': wishlist_list,
                   'things_to_consider_list': things_to_consider_list,
                   'knowledge_and_tips_list': knowledge_and_tips_list})


class HousePicturesView(ListView):
    model = Property
    # template_name = 'housewiki/dashboard/homes.html'
    template_name = 'housewiki/dashboard/index.html'

# class MilestoneView(ListView):
#
#     queryset = Milestone.objects.all()
#     context_object_name = 'milestones'
#     paginate_by = 4
#     template_name = 'home/dashboard/milestones.html'

