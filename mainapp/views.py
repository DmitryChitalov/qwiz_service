from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from mainapp.models import SampleGame, SampleCommand, SampleQwiz, Qwestions
from mainapp.forms import RequestForm
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import JsonResponse
from datetime import date

from django.core.mail import mail_admins

def index(request):
    context = {
        'title': 'Homepage',
    }
    return render(request, 'mainapp/index.html', context)


def games(request):
    games = SampleGame.objects.filter().order_by('date')[:4]
    coming_games = []
    for game in games:
        if game.date > date.today():
            coming_games.append(game)
    if not coming_games:
        coming_games = [None, None]
    if len(coming_games) < 2:
        other = [None]
    else:
        other = coming_games[1:]

    context = {
        'coming_game': coming_games[0],
        'other_games': other,
        'title': 'Games',
    }
    return render(request, 'mainapp/games.html', context)


def galery(request):
    context = {
        'title': 'Galery',
    }
    return render(request, 'mainapp/galery.html', context)


def leadboard(request):
    commands = SampleCommand.objects.order_by('-points')[:25]
    for i, command in enumerate(commands):
        command.num = i+1

    context = {
        'commands': commands,
        'title': 'Leadboard',
    }
    return render(request, 'mainapp/leadboard.html', context)


def victorina(request):
    qwiz = SampleQwiz.objects.all()
    context = {
        'qwizes': qwiz,
        'title': 'Victorina',
    }
    return render(request, 'mainapp/victorina.html', context)


def registration(request):
    title = 'register'

    if request.method == 'POST':
        data = request.POST
        register_form = RequestForm(data)
        if register_form.is_valid():
            # mail_admins(f"Заявка на игру {data['game']}",
            #           f"""Почта: {data['mail']}. \n
            #             Телефон: {data['phone']}. \n
            #             Имя капитана: {data['capitan_name']}. \n
            #             Название комады: {data['command_name']} x {data['members']} участников \n""",)
            register_form.save()
            return HttpResponseRedirect(reverse('success'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        register_form = RequestForm()

    context = {
        'title': title,
        'form': register_form,
    }
    return render(request, 'mainapp/registration.html', context)


def success(request):
    context = {
        'title': 'registration success',
    }
    return render(request, 'mainapp/success.html', context)


def qwestions(request, pk):
    if request.is_ajax():
        qwiz = get_object_or_404(SampleQwiz, pk=pk)
        qwestions = Qwestions.objects.filter(theme=qwiz)
        result = []
        for qwestion in qwestions:
            result.append(qwestion.to_json())

        return JsonResponse({'result': result})


