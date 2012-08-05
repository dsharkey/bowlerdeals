from django.shortcuts import render_to_response
from django.http import Http404
from models import Deal



def detail(request, deal_id):
    try:
        d = Deal.objects.get(pk=deal_id)
    except Deal.DoesNotExist:
        raise Http404
    return render_to_response('deal/detail.html', {'deal': d})