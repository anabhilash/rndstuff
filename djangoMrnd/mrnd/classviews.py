from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView,DeleteView
from mrnd.models import *


class Collegelist(ListView):
    model = College
    template_name = "mrnd/mycollegelist.html"
    context_object_name = "clglist"

    def get_context_data(self, **kwargs):
        context = super(Collegelist, self).get_context_data(**kwargs)
        context['now'] = "abhilash"
        return context

    def get(self, request, *args, **kwargs):
        return super(Collegelist, self).get(request, *args, **kwargs)

    def get_queryset(self):
        location=self.kwargs.get('location')

        if location:
            return College.objects.filter(location__iexact=location)
        else :
            location = self.request.GET.get('location')
            if location:
                return College.objects.filter(location__iexact=location)
            else:
                return College.objects.all()


class TestDetailView(DetailView):
    model=College
    template_name = "mrnd/college_detail.html"
    context_object_name = "clgdetail"
    def get_object(self, queryset=None):
        acronym=self.kwargs.get('acronym')
        if acronym:
            return College.objects.get(acronym__iexact=acronym)
        else:
            return College.objects.get(pk=self.kwargs["pk"])




class TestCreateViewCollege(CreateView):
    model=College
    fields=['name','acronym','location','contact']
    success_url = '/mrnd/college/'

class TestCreateViewStudent(CreateView):
    model = Student
    fields = ['name', 'email', 'dbfolder', 'dropped', 'college']
    success_url = '/mrnd/college/'

class TestUpdateViewCollege(UpdateView):
    model=College
    fields=['name','acronym','location','contact']
    def get_object(self, queryset=None):
        id=self.kwargs.get('id')
        if id:
            return College.objects.get(pk=id)
        else:
            return None

class TestDeleteViewCollege(DeleteView):
    model=College
    template_name = "mrnd/college_confirm_detail.html"
    success_url = "/mrnd/college"