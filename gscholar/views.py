from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
#
from .models import Organization
import json

def index(request):
    template = loader.get_template('gscholar/index.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello, world. You're at the polls index.")

def get_orgs(request):
    mimetype = 'application/json'
    #
    if not request.is_ajax():
        data = 'fail'
        return HttpResponse(data, mimetype)
    #
    q = request.GET.get('term', '')
    orgs = Organization.objects.filter(email_domain__icontains = q )[:20]
    #
    ret = []
    for org in orgs:
        org_json = {}
        org_json['value'] = org.email_domain
        org_json['label'] = org.email_domain
        ret.append(org_json)
    #
    data = json.dumps(ret)
    return HttpResponse(data, mimetype)

