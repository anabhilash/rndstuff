from django.template import loader,context
from django.http import HttpResponse

from models import *
# Create your views here.

def getcollege(request,location):
    template=loader.get_template('clg.html')
    result=template.render(context={'colleges':College.objects.filter(location__iexact=location)})
    return HttpResponse(result)