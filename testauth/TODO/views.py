from django.template import loader,context
from django.http import HttpResponse

from models import *

def getlist(request):
    lists = TodoList.objects.values()
    lists = lists.values('item_id', 'name', 'created')
    template = loader.get_template("lists.html")
    result = template.render(context={"lists":lists})
    return HttpResponse(result)

def gettodoitem(request,uid):
    item = TodoItem.objects.filter(id__exact=uid)
    item = item.values()[0]
    template = loader.get_template("todoitem.html")
    result = template.render(context={"items":item})
    return HttpResponse(result)