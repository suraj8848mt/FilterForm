from django.db.models import Q
from django.shortcuts import render
from .models import Journal, Category


def is_valid_queryparam(param):
    return param != '' and param is not None


def bootstrapfilter(request):
    qs = Journal.objects.all()
    categories = Category.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    view_count_min = request.GET.get('view_count_min')
    view_count_max = request.GET.get('view_count_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
    reviewed = request.GET.get('reviewed')
    not_Reviewed = request.GET.get('notReviewed')
    print(
        title_contains_query,
        id_exact_query,
        title_or_author_query,
        view_count_max,
        view_count_min,
        date_max,
        date_min,
        category,
        reviewed,
        )

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    if is_valid_queryparam(id_exact_query):
        qs = qs.filter(id__exact=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__name__icontains=title_or_author_query)
                       ).distinct()

    if is_valid_queryparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)

    if is_valid_queryparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)

    if is_valid_queryparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)

    if is_valid_queryparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)

    if reviewed == 'on':
        qs = qs.filter(reviewed=True)
    elif not_Reviewed == 'on':
        qs = qs.filter(reviewed=False)

    context = {
        'queryset': qs,
        'categories': categories
    }
    return render(request, "bootstrap_form.html", context)
