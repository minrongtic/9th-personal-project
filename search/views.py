from django.shortcuts import render
from route.models import Route
from django.db.models import Q, query
# Create your views here.


def searchResult(request):
    query = request.GET.get('kw')
    routes = Route.objects.all()

    context = dict()
    context['query'] = query
    context['routes'] = routes

    if query:
        routes.filter(Q(fin__icontains=query) | Q(via__icontains=query))
    return render(request, 'search/search.html', context=context)
