from mainapp.models import ComingRequests
from django import forms


class RequestForm(forms.ModelForm):
    class Meta:
        model = ComingRequests
        # fields = '__all__'
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'game':
                current_choises = []
                for choise in field.choices:
                    if not choise[1].startswith('*'):
                        current_choises.append(choise)
                field.choices = tuple(current_choises)
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
