from django.db.models import Q
from django.shortcuts import render
from .models import Journal


def is_valid_queryparam(param):
    return param != '' and param is not None


def bootstrapfilter(request):
    qs = Journal.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('id_exact')
    title_or_author_query = request.GET.get('title_or_author')
    print(title_contains_query, id_exact_query, title_or_author_query)

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)

    if is_valid_queryparam(id_exact_query):
        qs = qs.filter(id__exact=id_exact_query)

    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query)
                       | Q(author__name__icontains=title_or_author_query)
                       ).distinct()

    context = {
        'queryset': qs
    }
    return render(request, "bootstrap_form.html", context)
