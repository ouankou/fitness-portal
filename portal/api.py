import json
import datetime
from ast import literal_eval
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest

from .models import Trainer, Program

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
