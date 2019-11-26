from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import AbstractUser
from mainapp.models import SampleGame, SampleCommand, ComingRequests, SampleQwiz, Qwestions
from django import forms


class GameEditForm(forms.ModelForm):
    class Meta:
        model = SampleGame
        # fields = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(GameEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class RequestEditForm(forms.ModelForm):
    class Meta:
        model = ComingRequests
        # fields = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(RequestEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class CommandEditForm(forms.ModelForm):
    class Meta:
        model = SampleCommand
        # fields = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(CommandEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class QwizEditForm(forms.ModelForm):
    class Meta:
        model = SampleQwiz
        # fields = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(QwizEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class QwestionEditForm(forms.ModelForm):
    class Meta:
        model = Qwestions
        # fields = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(QwestionEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = AbstractUser
        fields = ('username', 'password')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
