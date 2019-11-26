from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from mainapp.models import SampleGame, SampleCommand, ComingRequests, SampleQwiz, Qwestions
from adminapp.forms import GameEditForm, CommandEditForm, UserLoginForm, RequestEditForm, QwizEditForm, QwestionEditForm

from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout


class MyListView(ListView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(MyListView, self).dispatch(*args, **kwargs)


class MyCreateView(CreateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(MyCreateView, self).dispatch(*args, **kwargs)


class MyUpdateView(UpdateView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(MyUpdateView, self).dispatch(*args, **kwargs)


class MyDeleteView(DeleteView):
    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(MyDeleteView, self).dispatch(*args, **kwargs)


class GameListView(MyListView):
    model = SampleGame
    template_name = 'adminapp/games.html'


class GameCreateView(MyCreateView):
    model = SampleGame
    template_name = 'adminapp/object_create.html'
    success_url = reverse_lazy('admins:games')
    # fields = ('__all__')
    form_class = GameEditForm


class GameDeleteView(MyDeleteView):
    model = SampleGame
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admins:games')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class GameUpdateView(UpdateView):
    model = SampleGame
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admins:games')
    form_class = GameEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'game edit'
        return context


class CommandsListView(MyListView):
    model = SampleCommand
    template_name = 'adminapp/commands.html'


# def commands(request):
#     title = 'commands'
#     commands = SampleCommand.objects.all()
#     req = ComingRequests.objects.all()
#     context = {
#         'title': title,
#         'commands': commands,
#         'requests': req,
#     }
#
#     return render(request, 'adminapp/commands.html', context)


class CommandCreateView(MyCreateView):
    model = SampleCommand
    template_name = 'adminapp/object_create.html'
    success_url = reverse_lazy('admins:commands')
    # fields = ('__all__')
    form_class = CommandEditForm


class CommandDeleteView(MyDeleteView):
    model = SampleCommand
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admins:commands')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class CommandUpdateView(UpdateView):
    model = SampleCommand
    template_name = 'adminapp/object_update.html'
    success_url = reverse_lazy('admins:commands')
    form_class = CommandEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'command edit'
        return context


class RequestCreateView(MyCreateView):
    model = ComingRequests
    template_name = 'adminapp/object_create.html'
    success_url = reverse_lazy('admins:requests')
    # fields = ('__all__')
    form_class = RequestEditForm


class RequestsListView(MyListView):
    model = ComingRequests
    template_name = 'adminapp/Requests.html'


class RequestDeleteView(MyDeleteView):
    model = ComingRequests
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admins:requests')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


class QwizListView(MyListView):
    model = SampleQwiz
    template_name = 'adminapp/qwizes.html'


class QwizCreateView(MyCreateView):
    model = SampleQwiz
    template_name = 'adminapp/object_create.html'
    success_url = reverse_lazy('admins:qwiz')
    # fields = ('__all__')
    form_class = QwizEditForm


@user_passes_test(lambda x: x.is_superuser)
def qwiz_update(request, pk):
    title = 'qwiz edit'
    theme = get_object_or_404(SampleQwiz, pk=pk)
    qwestions = Qwestions.objects.filter(theme=theme)

    if request.method == 'POST':
        form = QwizEditForm(request.POST, request.FILES, instance=theme)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:qwiz_update', args=[theme.pk]))
    else:
        form = QwizEditForm(instance=theme)

    context = {
        'title': title,
        'form': form,
        'objects': qwestions,
        'qwiz': theme,
    }

    return render(request, 'adminapp/qwiz_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def qwestion_create(request, pk):
    title = 'qwestion create'
    theme = get_object_or_404(SampleQwiz, pk=pk)

    if request.method == 'POST':
        form = QwestionEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:qwiz_update', args=[theme.pk]))
    else:
        form = QwestionEditForm(initial={'theme': theme})
    context = {
        'title': title,
        'form': form,
        'theme': theme,
    }
    return render(request, 'adminapp/object_create.html', context)


@user_passes_test(lambda x: x.is_superuser)
def qwestion_update(request, pk):
    title = 'qwestion edit'
    qwestion = get_object_or_404(Qwestions, pk=pk)

    if request.method == 'POST':
        form = QwestionEditForm(request.POST, request.FILES, instance=qwestion)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:qwiz_update', args=[qwestion.theme.pk]))
    else:
        form = QwestionEditForm(instance=qwestion)

    context = {
        'title': title,
        'form': form,
        'object': qwestion,
    }

    return render(request, 'adminapp/object_update.html', context)


class QwizDeleteView(MyDeleteView):
    model = SampleQwiz
    template_name = 'adminapp/object_delete.html'
    success_url = reverse_lazy('admins:qwiz')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


# def del_qwestion(request, pk, qpk):
#     qwestion = get_object_or_404(SampleQwiz, pk=pk)
#     qwestion.delete()
#     return HttpResponseRedirect(reverse('admin:qwiz_update', args=[qpk]))


def user_login(request):
    title = 'login'
    login_form = UserLoginForm(data=request.POST or None)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('index'))

    context = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }

    return render(request, 'adminapp/login.html', context)


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
