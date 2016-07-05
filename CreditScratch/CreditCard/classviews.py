from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from CreditCard.models import *
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator


@method_decorator(login_required,name="dispatch")
class CardList(ListView):
    model=CardDetails
    template_name = 'CreditCard/CardDetails.html'
    context_object_name = "Cardlist"


@method_decorator(login_required,name="dispatch")
class CardUpdate(UpdateView):
    model=CardDetails
    fields=['nickName','nameOnCard','expireDate','type','cardNumber']
    success_url = '/credit/CardDetails/'


@method_decorator(login_required,name="dispatch")
class CardDelete(DeleteView):
    model=CardDetails
    success_url = '/creditCardDetails/'



@method_decorator(login_required,name="dispatch")
class Cardcreate(CreateView):
    model=CardDetails
    fields =['nickName','nameOnCard','expireDate','type','cardNumber']
    success_url = '/credit/CardDetails/'