from django.shortcuts import get_object_or_404, render
from .models import Route
# Create your views here.


def main(request):
    return render(request, 'route/main.html')


def routeBoard(request):
    route = Route.objects.all()
    return render(request, 'route/routeBoard.html', {'routes': route})


def routeDetail(request, route_id):
    route_detail = get_object_or_404(Route, pk=route_id)
    return render(request, 'route/routeDetail.html', {'route': route_detail})
