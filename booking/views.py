from rest_framework.response import Response
from .models import Department
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Appointment
# Create your views here.

class dptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

@api_view(['GET'])
def getDepartment(request):

    dpt = Department.objects.all()

    serializerdata = dptSerializer(dpt, many=True)


    return Response(serializerdata.data)



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = "__all__"

@api_view(['POST'])
def InsertAppointment(request):

    serializerdata = AppointmentSerializer(data = request.data)

    if serializerdata.is_valid():
        serializerdata.save()
        return Response("success")
    else:
        return Response(serializerdata.errors)
