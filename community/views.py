from django.shortcuts import get_object_or_404, render
from .models import Community
# Create your views here.


def communityBoard(request):
    community = Community.objects.all()
    return render(request, 'community/communityBoard.html', {'communities': community})


def communityDetail(request, community_id):
    community_detail = get_object_or_404(Community, pk=community_id)
    return render(request, 'community/communityDetail.html', {'community': community_detail})
