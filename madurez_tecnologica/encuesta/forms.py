from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NameForm(forms.Form):
    GAD = forms.ModelChoiceField(queryset=Gad.objects.all(), label='GAD')
    GAD.widget.attrs.update({'class': 'form-control form-control-user',
                             'placeholder': 'Ingresar municipio'})

class Name2Form(forms.Form):
    servicio = forms.ModelChoiceField(queryset=Gad.objects.none())
    servicio.widget.attrs.update({'class': 'form-control form-control-user'})
    def __init__(self, question):
        super(Name2Form, self).__init__()
        valor = GadsServicios.objects.prefetch_related('servicios').filter(gad_id=question)
        self.fields['servicio'].queryset = valor
        self.fields['servicio'].empty_label = None

class PreguntaTop(forms.Form):
    respuesta = forms.ModelChoiceField(
        queryset=PreguntasRespuestas.objects.none(),
        required=True,
        widget=forms.CheckboxSelectMultiple)

    def __init__(self, question):
        super(PreguntaTop, self).__init__()
        valor = PreguntasRespuestas.objects.select_related('pregunta').filter(pregunta__encuesta=1, pregunta=question)
        self.fields['respuesta'].queryset = valor
        self.fields['respuesta'].empty_label = None


class PreguntaBotton(forms.Form):
    respuesta = forms.ModelChoiceField(
        queryset=PreguntasRespuestas.objects.none(),
        widget=forms.CheckboxSelectMultiple, empty_label=None)

    def __init__(self, question, *args, **kwargs):
        super(PreguntaBotton, self).__init__(*args, **kwargs)
        valor = PreguntasRespuestas.objects.prefetch_related('pregunta').filter(pregunta__encuesta=2,
                                                                                pregunta=question)
        self.fields['respuesta'].queryset = valor
        self.fields['respuesta'].empty_label = None

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    GAD = forms.ModelChoiceField(queryset=Gad.objects.all(), label='GAD')
    GAD.widget.attrs.update({'class': 'form-control form-control-user',
                             'placeholder': 'Ingresar municipio'})

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','GAD')
