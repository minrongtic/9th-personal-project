from django.shortcuts import get_object_or_404, render, redirect
from .models import Community
from django.utils import timezone
# Create your views here.


def communityBoard(request):
    community = Community.objects.order_by('-date')
    return render(request, 'community/communityBoard.html', {'communities': community})


def communityDetail(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community/communityDetail.html', {'community': community_detail})


def communityNew(request):
    return render(request, 'community/communityNew.html')


def communityCreate(request):
    new_community = Community()
    new_community.title = request.POST['title']
    new_community.body = request.POST['body']
    new_community.date = timezone.now()
    new_community.save()
    return redirect('community:communityBoard')


def communityEdit(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community/communityEdit.html', {'community': community_detail})


def communityUpdate(request, community_id):
    community_update = get_object_or_404(Community, pk=community_id)
    community_update.title = request.POST['title']
    community_update.body = request.POST['body']
    community_update.save()
    return redirect('community:communityBoard')


def communityDelete(request, community_id):
    community_delete = get_object_or_404(Community, pk=community_id)
    community_delete.delete()
    return redirect('community:communityBoard')
