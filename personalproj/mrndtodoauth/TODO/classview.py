from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
from django.utils.decorators import method_decorator
from django.http import Http404
from django.core.exceptions import PermissionDenied


@method_decorator(login_required,name="dispatch")
class TodoListView(ListView):
    model=TodoList
    context_object_name = "list"

    def get_queryset(self):
        k = self.request.user
        if k:
            return TodoList.objects.all().filter(user=k)


@method_decorator(login_required,name="dispatch")
class TodoItemList(ListView):
    context_object_name = "itemlist"

    def get_context_data(self, **kwargs):
        context= super(TodoItemList, self).get_context_data(**kwargs)
        context['username'] = self.request.user
        return context

    def get_queryset(self):
        k=self.kwargs.get('id')
        if k:
            try:
                list_object = TodoList.objects.all().filter(pk=k)[0]
            except IndexError:
                raise Http404

            if list_object.user.username==self.request.user.username:
                return TodoItem.objects.all().filter(li_id__exact=k)
            else:
                raise PermissionDenied


@method_decorator(login_required,name="dispatch")
class TodoListCreate(CreateView):
    model = TodoList
    fields = ['name','created']
    template_name = 'TODO/todolist_form.html'
    success_url = '/todo/todolist/'

    def form_valid(self, form):
        user_name = self.request.user
        user_object = User.objects.all().filter(username__exact=user_name)[0]
        form.instance.user = user_object
        return super(TodoListCreate, self).form_valid(form)


@method_decorator(login_required,name="dispatch")
class TodoItemCreate(CreateView):
    model=TodoItem
    fields=['description','duedate','completed','created']
    template_name = 'TODO/todoitem_form.html'

    def get_template_names(self):
        list_object=TodoList.objects.all().filter(pk=self.kwargs.get('id'))[0]
        user_name=list_object.user.username
        if user_name==self.request.user.username:
            return super(TodoItemCreate, self).get_template_names()
        else: raise PermissionDenied

    def form_valid(self, form):
        list_id=self.kwargs.get('id')
        list_object = TodoList.objects.get(pk=list_id)
        form.instance.li = list_object
        return super(TodoItemCreate, self).form_valid(form)

    def get_success_url(self):
        return '/todo/todolist/' + self.kwargs.get('id') + '/items/'


@method_decorator(login_required,name="dispatch")
class TodoListUpdate(UpdateView):
    model = TodoList
    fields = ['name', 'created']
    success_url = '/todo/todolist/'

    def get_object(self, queryset=None):
        update_list_id = self.kwargs.get('pk')
        list_object = TodoList.objects.all().filter(pk=update_list_id)[0]
        if list_object.user.username == self.request.user.username:
            return super(TodoListUpdate, self).get_object(queryset)
        else:
            raise PermissionDenied


@method_decorator(login_required,name="dispatch")
class TodoItemUpdate(UpdateView):
    model=TodoItem
    fields = ['description', 'created', 'duedate', 'completed']

    def get_object(self, queryset=None):
        item_id=self.kwargs.get('pk')
        item_object=TodoItem.objects.all().filter(pk=item_id)[0]
        if item_object.li.pk == int(self.kwargs.get('listid')):
            list_object = TodoList.objects.all().filter(pk=self.kwargs.get('listid'))[0]
            if list_object.user.username == self.request.user.username:
                return super(TodoItemUpdate, self).get_object(queryset)
        raise PermissionDenied

    def get_success_url(self):
        return '/todo/todolist/' + self.kwargs.get('listid') + '/items/'


@method_decorator(login_required,name="dispatch")
class TodoListDelete(DeleteView):
    model=TodoList
    success_url = '/todo/todolist/'

    def get_object(self, queryset=None):
        delete_list_id = self.kwargs.get('pk')
        list_object = TodoList.objects.all().filter(pk=delete_list_id)[0]
        if list_object.user.username == self.request.user.username:
            return super(TodoListDelete, self).get_object(queryset)
        else:
            raise PermissionDenied


@method_decorator(login_required,name="dispatch")
class TodoItemDelete(DeleteView):
    model=TodoItem

    def get_object(self, queryset=None):
        item_id=self.kwargs.get('pk')
        item_object=TodoItem.objects.all().filter(pk=item_id)[0]
        if item_object.li.pk == int(self.kwargs.get('listid')):
            list_object = TodoList.objects.all().filter(pk=self.kwargs.get('listid'))[0]
            if list_object.user.username == self.request.user.username:
                return super(TodoItemDelete, self).get_object(queryset)
        raise PermissionDenied

    def get_success_url(self):
        return '/todo/todolist/' + self.kwargs.get('listid') + '/items/'


