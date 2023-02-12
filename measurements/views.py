from .logic import logic_measurements as ml
from variables.logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Path params (/id)
@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        variable_dto = vl.get_variable(json.loads(request.body)["variable"])
        if variable_dto:
            measurement_dto = ml.create_measurement(json.loads(request.body))
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            return HttpResponse(status=404)

    if request.method == 'DELETE':
        ml.delete_measurement(json.loads(request.body))
        return HttpResponse(status=200)

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ml.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        measurement_dto = ml.update_measurement(pk, json.loads(request.body))
        variable = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(variable, 'application/json')
    
    if request.method == 'DELETE':
        ml.delete_measurement(pk)
        return HttpResponse(status=200)