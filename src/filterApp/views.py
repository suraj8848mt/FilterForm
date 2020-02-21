from django.shortcuts import render


def bootstrapfilter(request):
    return render(request, "bootstrap_form.html", {})
