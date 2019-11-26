import json
import datetime
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest

from .models import Trainer, Program, ClientSubscribedProgram, Client

SUCCESS_STATUS = "success"
ERROR_STATUS = "error"


def prepare_response_data(status, data):
    return {"status": status, "data": data}


def prepare_list_as_data_table_col_format(columns):
    column_data = []
    for col in columns:
        column_data.append({
            "title": col,
            "defaultContent": "-",
        })
    return column_data


def pending_trainer_applications(request, **kwargs):
    pending_applications = Trainer.objects.filter(is_approved=False).all()
    # import remote_pdb; remote_pdb.set_trace(host='0.0.0.0', port=4444)
    data = {"data": [], "columns": []}
    columns = ["", "Name", "Email", "Experience (Years)", "Certifications", "Charge/Month", "Application Submitted"]
    counter = 1
    for application in pending_applications:
        prepared_row = [
            "<input type='checkbox' class='app-row' data-username='" + application.user.username + "' data-row='"
            + str(counter) + "'>",
            application.full_name,
            application.user.email,
            application.years_of_previous_experience,
            application.certification,
            application.charge,
            application.applied_on,
        ]
        data["data"].append(prepared_row)
        counter += 1

    data["columns"] = prepare_list_as_data_table_col_format(columns)
    return JsonResponse(prepare_response_data(SUCCESS_STATUS, data))


@csrf_exempt
def trainer_application_decision(request, decision, **kwargs):
    if request.method == "POST":
        data = request.POST.dict()
        application_list = literal_eval(data['applications'])
        trainers = Trainer.objects.filter(user__username__in=application_list).all()
        is_approved = False
        if decision == "accept":
            is_approved = True

        for trainer in trainers:
            trainer.is_approved = is_approved
            trainer.approved_on = datetime.date.today()
            trainer.save()

        return JsonResponse({"status": "success", "message": "{0} trainer application/s {1}!".format(
            len(trainers), decision
        )})

    return HttpResponseBadRequest({"status": "error", "message": "Bad Request"})


def add_program(request, trainer_username, **kwargs):
    if request.method == "POST":
        data = json.loads(request.body)
        trainer = Trainer.objects.filter(user__username=trainer_username).first()
        if trainer.is_approved:
            program = Program.objects.create(
                trainer=trainer,
                name=data['name'],
                code=data['code'],
                overview=data['overview'],
                details=data['details'],
                material_1=data['material_1'],
                material_2=data['material_2'],
                material_3=data['material_3']
            )
            if program:
                program.save()
                message = {"message": "Program added successfully!"}
                return JsonResponse(prepare_response_data(SUCCESS_STATUS, message))

    return HttpResponseBadRequest()


def program_list(request, **kwargs):
    programs = Program.objects.filter(is_active=True).all()
    client_id = int(request.GET.get("client_id"))
    client_subscribed_program_list = ClientSubscribedProgram.objects.filter(client_id=client_id).values_list('program_id')
    data = {"data": [], "columns": []}
    columns = ["", "Trainer", "Name", "Code", "Overview", "Subscription", "Join"]
    counter = 1
    for program in programs:
        is_program_subscribed = (program.id,) in client_subscribed_program_list
        button_class = "btn-primary" if is_program_subscribed else "btn-success"
        button_label = "Joined" if is_program_subscribed else "Join"
        prepared_row = [
            counter,
            program.trainer.full_name,
            program.name,
            program.code,
            program.overview,
            program.subscription_count,
            "<button type='button' id='program-id-" + str(program.id) + "' "
            "class='btn " + button_class + " join-program' "
            "data-joined='" + str(is_program_subscribed) + "'"
            "data-program_id='" + str(program.id) + "'>" + button_label + "</button>"
        ]
        data["data"].append(prepared_row)
        counter += 1

    data["columns"] = prepare_list_as_data_table_col_format(columns)
    return JsonResponse(prepare_response_data(SUCCESS_STATUS, data))


@csrf_exempt
def client_joining_program(request, program_id, client_id, **kwargs):
    if request.method == "POST":
        client_subscribed_program = ClientSubscribedProgram.objects.create(
            program_id=program_id,
            client_id=client_id
        )
        if client_subscribed_program:
            client_subscribed_program.save()
            data = {"id": client_subscribed_program.id}
            return JsonResponse(prepare_response_data(SUCCESS_STATUS, data))
    return HttpResponseBadRequest()


def get_client_subscribed_program_list(request, client_id, **kwargs):
    client_subscribed_programs = ClientSubscribedProgram.objects.filter(client_id=client_id).all()

    data = {"data": [], "columns": []}
    columns = ["", "Name", "Code", "Trainer", "Overview", "Joined"]
    counter = 1

    for cs_program in client_subscribed_programs:

        prepared_row = [
            counter,
            cs_program.program.name,
            cs_program.program.code,
            cs_program.program.trainer.full_name,
            cs_program.program.overview,
            cs_program.joined_on
        ]
        data["data"].append(prepared_row)
        counter += 1

    data["columns"] = prepare_list_as_data_table_col_format(columns)
    return JsonResponse(prepare_response_data(SUCCESS_STATUS, data))
