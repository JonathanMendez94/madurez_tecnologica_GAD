from .forms import *
from .models import *
import six
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import datetime
from django.core.exceptions import ObjectDoesNotExist
import random
from django.db.models import Sum, Q, Count, F, FloatField, ExpressionWrapper
import json


# Create your views here.
def encuesta(request, encuesta):
    qs3 = list(Encuestas.objects.filter(idencuesta=encuesta).values())
    tipo = qs3[0]
    nombre = tipo['nombre']
    if (tipo['nombre'] == 'Top Down'):
        if request.user.is_authenticated:
            current_user = request.user
            user_id = current_user.id
            valorgd = GadSerUser.objects.filter(user_id=user_id).values('gad_ser__gad__id_gad',
                                                                        'gad_ser__servicios__servicio')
            vag = valorgd[0]
            gad = vag['gad_ser__gad__id_gad']
            quiz_form = Name2Form(gad)
            if request.method == 'POST':
                post_data = request.POST
                question_id = int(post_data['servicio'])
                return redirect('preguntas', encuesta=1, serv=int(question_id))
        form = NameForm()
    else:
        # button-up
        r1 = random.randint(0, 100000)
        if request.method == 'POST':
            form = NameForm(request.POST)
            if form.is_valid():
                # obtener valor del gad
                valor = form.cleaned_data['GAD']
                # consultar GAD en la bd
                qs1 = list(Gad.objects.filter(gad=valor).values())
                # obtener id del GAD
                valor2 = qs1[0]
                # cargar otro formulario
                quiz_form = Name2Form(valor2['id_gad'])
                post_data = request.POST
                resp = dict(six.iterlists(post_data))
                if (len(resp) > 2):
                    # gad_servicio
                    resp1 = resp['servicio']
                    hol = GadsServicios.objects.get(idgadservicio=int(resp1[0]))
                    # ***************************
                    a = User(username="username" + str(r1), first_name="first_name" + str(r1),
                             last_name="last_name" + str(r1), email="email" + str(r1) + "@gmail.com",
                             date_joined=datetime.datetime.now())
                    a.set_password("password1" + str(r1))
                    a.is_superuser = False
                    a.is_staff = True
                    a.is_active = True
                    a.save()
                    aa = AuthUser.objects.get(username="username" + str(r1), first_name="first_name" + str(r1),
                                              last_name="last_name" + str(r1), email="email" + str(r1) + "@gmail.com")
                    gas = GadSerUser(gad_ser=hol, user=aa)
                    gas.save()
                    user = authenticate(username="username" + str(r1), password="password1" + str(r1))
                    login(request, user)
                    if request.method == 'POST':
                        post_data = request.POST
                        resp = dict(six.iterlists(post_data))
                        question_id = int(post_data['servicio'])
                    return redirect('preguntas2', encuesta=2, serv=int(question_id))
        else:
            quiz_form = Name2Form(0)
            form = NameForm()
    return render(request, 'encuesta/cuestionario.html',
                  {'form': form, 'tipoEncuesta': tipo, 'ser': quiz_form, 'nombre': nombre})


def pregunta(request, encuesta, serv):
    try:
        # 1-15 TOP DOWN
        question_number = 0
        mensajeBool = False
        mensaje = ''
        fecha = datetime.datetime.now()
        preguntas = []
        # nombre del cuestionario
        cuestio = Encuestas.objects.filter(idencuesta=encuesta).values('nombre')
        # consultar preguntas respuesta del tipo cuestionario
        preg = list(PreguntasRespuestas.objects.select_related('pregunta').filter(pregunta__encuesta=encuesta).values(
            'pregunta').distinct().values())
        nuevo = list(cuestio)
        # nombre cuestionario dict
        valore = nuevo[0]
        for i in preg:
            preguntas.append(i['pregunta_id'])
        # preguntas unicas
        preg = list(set(preguntas))
        if request.user.is_authenticated:
            current_user = request.user
            user_id = current_user.id
            user_nombre = current_user.username
            valorgd = GadSerUser.objects.filter(user_id=user_id, gad_ser=serv).values('gad_ser__gad__gad',
                                                                                      'gad_ser__servicios__servicio')
            vaw = GadSerUser.objects.get(user=user_id, gad_ser=serv)
            vag = valorgd[0]
            gad = vag['gad_ser__gad__gad']
            serv = vag['gad_ser__servicios__servicio']
        # si el usuario no es funcionario
        if request.method == 'POST':
            post_data = request.POST
            resp = dict(six.iterlists(post_data))
            catResp = len(PreguntasRespuestas.objects.filter(pregunta=int(resp['question_number'][0])).values())
            question_id = int(post_data['question_number'])
            if 'respuesta' in resp:
                respuetas = resp['respuesta']
                if catResp > 2 or catResp < 3 and len(respuetas) < 2 or question_id == 37:
                    for i in range(len(respuetas)):
                        respuesta = int(respuetas[i])
                        res = PreguntasRespuestas.objects.get(idpreguntaresp=respuesta)
                        f = Fichas(fecha=fecha, gad_servi_usuario=vaw, pregunta_respuesta=res)
                        f.save()
                    if (valore['nombre'] == 'Top Down'):
                        num = 0
                    else:
                        num = 15
                    if question_id == 1 and respuesta == 112:
                        question_number = 3 - 1
                    elif question_id == 3 and respuesta == 13:
                        question_number = 6 - 1
                    elif question_id == 4 and respuesta == 17:
                        question_number = 10 - 1
                    elif question_id == 5 and respuesta == 18:
                        question_number = 9 - 1
                    elif question_id == 6 and respuesta == 19:
                        question_number = 10 - 1
                    elif question_id == 7 and respuesta == 21:
                        question_number = 10 - 1
                    elif question_id == 8 and respuesta == 23:
                        question_number = 10 - 1
                    elif question_id == 17 and respuesta == 42:
                        question_number = 4 - 1
                    elif question_id == 26 and respuesta == 66:
                        question_number = 13 - 1
                    elif question_id == 28 and respuesta == 69:
                        question_number = 15 - 1
                    elif question_id == 30 and respuesta == 74:
                        question_number = 17 - 1
                    elif question_id == 34 and respuesta == 84:
                        question_number = 21 - 1
                    elif question_id == 36 and respuesta == 90:
                        question_number = 23 - 1
                    else:
                        question_number = question_id - num
                else:
                    valor = preg.index(int(post_data['question_number']))
                    question_number = valor
                    mensajeBool = True
                    mensaje = "Seleccionar una opción"
            else:
                valor = preg.index(int(post_data['question_number']))
                question_number = valor
                mensajeBool = True
                mensaje = "Seleccionar respuesta"
        if (valore['nombre'] == 'Top Down'):
            quiz_form = PreguntaTop(preg[question_number])
            pregunta = Preguntas.objects.filter(idpregunta=preg[question_number]).values('pregunta')
        else:
            quiz_form = PreguntaBotton(preg[question_number])
            pregunta = Preguntas.objects.filter(idpregunta=preg[question_number]).values('pregunta')

    except:
        return redirect('gracias')
    return render(request, 'encuesta/preguntas.html',
                  {"question_form": quiz_form,
                   'question_number': preg[question_number],
                   'preguntas': pregunta,
                   'cuestionario': valore['nombre'],
                   'gad': gad,
                   'serv': serv,
                   'nombre': user_nombre,
                   'mensajeBool': mensajeBool,
                   'mensaje': mensaje})


def index(request):
    return render(request, 'encuesta/index.html')


def index2(request):
    return render(request, 'encuesta/index2.html')


def gracias(request):
    return render(request, 'encuesta/gracias.html')


def signup(request):
    mensaje = ""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            GADf = form.cleaned_data.get('GAD')
            ga = Gad.objects.filter(gad=GADf).values("id_gad")
            gan = ga[0]
            try:
                servicios = list(GadsServicios.objects.filter(gad=gan['id_gad']).values('servicios_id'))
                if (len(servicios) > 0):
                    # crear usuario
                    a = User(username=username, first_name=first_name, last_name=last_name, email=email,
                             date_joined=datetime.datetime.now())
                    a.set_password(password1)
                    a.is_superuser = False
                    a.is_staff = True
                    a.is_active = True
                    a.save()
                    aa = AuthUser.objects.get(username=username, first_name=first_name, last_name=last_name,
                                              email=email)
                    for i in servicios:
                        hol = GadsServicios.objects.get(gad=gan['id_gad'], servicios=i['servicios_id'])
                        gas = GadSerUser(gad_ser=hol, user=aa)
                        gas.save()
                    user = authenticate(username=username, password=password1)
                    login(request, user)
                    return redirect('index2')
                else:
                    mensaje = "Comunicarse con administrador. Municipio o Servicio no registrado"
            except ObjectDoesNotExist:
                mensaje = "Comunicarse con administrador. Municipio o Servicio no registrado"
    else:
        form = SignUpForm()
    return render(request, 'encuesta/signup.html', {'form': form, 'mensaje': mensaje})


def resultado(request):
    dato = {}
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # obtener valor del gad
            valor = form.cleaned_data['GAD']
            # consultar GAD en la bd
            qs1 = list(Gad.objects.filter(gad=valor).values())
            # obtener id del GAD
            valor2 = qs1[0]
            # consultando fichas
            # primero consultando el gad
            fichas2 = Fichas.objects.filter(gad_servi_usuario__gad_ser__gad=valor2['id_gad']). \
                values('gad_servi_usuario__gad_ser__servicios__servicio',
                       'gad_servi_usuario__gad_ser__idgadservicio'). \
                annotate(Top_Down=Sum('pregunta_respuesta__valor',
                                      filter=Q(pregunta_respuesta__pregunta__encuesta__nombre='Top Down')),
                         valT=Count('gad_servi_usuario', distinct=True)). \
                annotate(Bottom_Up=Sum('pregunta_respuesta__valor',
                                       filter=Q(pregunta_respuesta__pregunta__encuesta__nombre='Bottom Up')),
                         valB=Count('gad_servi_usuario', distinct=True)). \
                annotate(Bottom_Up_Total=ExpressionWrapper(F('Bottom_Up') / F('valB'), output_field=FloatField())). \
                annotate(Top_Down_Total=ExpressionWrapper(F('Top_Down') / F('valT'), output_field=FloatField())).                \
                annotate(Total=ExpressionWrapper((F('Bottom_Up_Total')+F('Top_Down_Total'))/2, output_field=FloatField())).order_by('-Total')
            dato = fichas2
    else:
        form = NameForm()
    return render(request, 'encuesta/resultado.html',
                  {'form': form, 'dato': dato})


def grafica(request, cuestionario, GadServ):
    ficha = (Fichas.objects.filter(gad_servi_usuario__gad_ser__idgadservicio=GadServ,
                                   pregunta_respuesta__pregunta__encuesta__nombre=cuestionario). \
             values('pregunta_respuesta__pregunta__categoria__categoria'). \
             annotate(Total=Sum('pregunta_respuesta__valor'),
                      valB=Count('gad_servi_usuario', distinct=True)). \
             annotate(val = ExpressionWrapper(F('Total') / F('valB'), output_field=FloatField())))
    return render(request, 'encuesta/graficas.html', {'dato': json.dumps(list(ficha)),'lista':ficha})
