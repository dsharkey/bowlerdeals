from django.shortcuts import render_to_response
from django.http import Http404
from models import Deal



def detail(request, deal_id):
    d = get_object_or_404(Deal, pk=deal_id)
    return render_to_response('detail.html', {'deal': d})