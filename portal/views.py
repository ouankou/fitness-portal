import json
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import logout as user_logout, authenticate, login as user_login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Trainer, Client, Program, ClientSubscribedProgram


def index(request, **kwargs):
    if not request.user.is_authenticated:
        return render(request, "welcome.html", context=kwargs)
    else:
        if request.user.is_superuser:
            return render_admin_index(request, **kwargs)
        elif request.user.is_staff:
            return render_trainer_index(request, **kwargs)
        else:
            return render_client_index(request, **kwargs)


def render_admin_index(request, **kwargs):
    pending_applications = Trainer.objects.filter(is_approved=False).all()
    context = {"application_list": pending_applications}
    return render(request, "administrator/index.html", context=context)


def render_client_index(request, username=None, **kwargs):
    username = username if username else request.user.username
    client = Client.objects.filter(user__username=username).first()
    programs = Program.objects.filter(is_active=True).all()
    if client is not None:
        context = {"client": client, "programs": programs}
        return render(request, "client/index.html", context)
    return HttpResponseBadRequest()


def render_trainer_index(request, username=None, **kwargs):
    username = username if username else request.user.username
    trainer = Trainer.objects.filter(user__username=username).first()
    if trainer is not None:
        client_program_list = ClientSubscribedProgram.objects.filter(program__trainer_id=trainer.id).all()
        client_information = {}
        for client_program in client_program_list:
            if not client_information.get(client_program.client_id):
                client_information[client_program.client_id] = {
                    "name": client_program.client.user.get_full_name(),
                    "purpose": client_program.client.purpose_text,
                    "client_since": client_program.joined_on,
                    "program_completed": 1 if client_program.completed_on is not None else 0
                }
            elif client_information.get(client_program.client_id):
                if client_information[client_program.client_id]["client_since"] > client_program.joined_on:
                    client_information[client_program.client_id]["client_since"] = client_program.joined_on
                if client_program.completed_on is not None:
                    client_information[client_program.client_id]["program_completed"] += 1

        context = {"trainer": trainer, "client_information": client_information}
        return render(request, "trainer/index.html", context)
    return HttpResponseBadRequest()


def trainer_application(request, **kwargs):
    if request.method == "POST":
        try:
            data = request.POST.dict()
            # import remote_pdb; remote_pdb.set_trace(host='0.0.0.0', port=4444)
            user = User(username=data['username'], email=data['email'], password=data['password'])
            user.is_staff = True
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.set_password(data['password'])
            if user:
                user.save()

            trainer = Trainer.objects.create(
                user=user,
                years_of_previous_experience=data['years_of_experience'],
                charge=data['charge'],
                locations_served=data['location_served'],
                certification=data['certifications']
            )
            if trainer:
                trainer.save()
                context = {"message": "Your application is under review. We will get back to you shortly!"}
                return render(request, "welcome.html", context=context)
        except Exception:
            return HttpResponseBadRequest()

    context = {
        "location_options": Trainer.LOCATION_CHOICES_MAP,
        "certification_options": Trainer.CERTIFICATION_CHOICE_MAP
    }
    return render(request, "signups/trainer.html", context=context)


def client_signup(request, **kwargs):
    if request.method == "POST":
        # try:
        data = request.POST.dict()
        # import remote_pdb; remote_pdb.set_trace(host='0.0.0.0', port=4444)
        user = User(username=data['username'], email=data['email'], password=data['password'])
        user.is_staff = False
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.set_password(data['password'])
        if user:
            user.save()
        client = Client.objects.create(
            user=user,
            purpose=data['purpose'],
            starting_weight=data['current_weight'],
            current_weight=data['current_weight'],
            target_weight=data["target_weight"],
            blood_group=data['blood_group'],
            height_in_feet=data['height_in_feet'],
            arm_size=data['arm_size'],
            chest_size=data['chest_size'],
            leg_size=data['leg_size'],
            health_issues=data['health_issues']
        )
        if client is not None:
            client.save()
            context = {"message": "Your account has been created "}
            return index(request, **context)
    return render(request, "signups/client.html")


def login(request, **kwargs):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            user_login(request, user)
        return JsonResponse({"is_authenticated": True if user else False})
    else:
        return HttpResponseBadRequest()


def logout(request, **kwargs):
    user_logout(request)
    return redirect("/")
