from ..models import Measurement
from ..models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(measurement_pk):
    measurements = Measurement.objects.get(pk=measurement_pk)
    return measurements

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    if "value" in new_measurement:
        measurement.value = new_measurement["value"]
    if "unit" in new_measurement:
        measurement.unit = new_measurement["unit"]
    if "variable" in new_measurement:
        variable_id = Variable.objects.get(pk=new_measurement["variable"])
        measurement.variable = variable_id
    if "place" in new_measurement:
        measurement.place = new_measurement["place"]
    measurement.save()
    return measurement

def create_measurement(measurement):
    variable_id = Variable.objects.get(pk=measurement["variable"])
    measurement = Measurement(variable=variable_id, value=measurement["value"], place=measurement["place"], unit=measurement["unit"])
    measurement.save()
    return measurement

def delete_measurement(measurement_pk):
    measurement = get_measurement(measurement_pk)
    measurement.delete()
    return measurement