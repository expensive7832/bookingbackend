from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import serializers 
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class updateSerializer(serializers.ModelSerializer):
     
     class Meta:
        model = User
        fields = '__all__'

class signupSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    photo = serializers.ImageField()
    

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "photo"]

    def validate(self, data):
        check = User.objects.filter(email = data['email']).first()
        
        if check is not None:
            raise serializers.ValidationError("email already exist")
        
        return data
    


    def create(self, data):

        pwd = data['password']

        new_pwd = make_password(pwd)

        data['password'] = new_pwd
        
        new_user = User.objects.create(**data)
        
        
        return new_user

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def loguser(self, data):

        user = User.objects.filter(email = data['email']).first()

        if user is None:
            return "Invalid email"
        
        else:
            encpwd = getattr(user, "password")
            originalpwd = data['password']
            
            chk = check_password(originalpwd, encpwd)

            if chk:
                data = {
                    "id": getattr(user, "id"),
                    "first_name": getattr(user, "first_name"),
                    "last_name": getattr(user, "last_name"),
                    "email": getattr(user, "email"),
                    "photo": str(getattr(user, "photo")),
                }

                
                return data
            else:
                return "Invalid credentials"

                




@api_view(['POST'])
def Signup(request):
    
    try:
        serializedata = signupSerializer(data=request.data) 

        if serializedata.is_valid():
            serializedata.save()
            return Response("signup successful")
        else:
            return Response(serializedata.errors)
    except BaseException as e:
        return Response(str(e))


@api_view(['POST'])
def Login(request):
    try:
        serializerdata = loginSerializer(data = request.data)

        if serializerdata.is_valid():
         result = serializerdata.loguser(serializerdata.data)

         return Response(result)

        else:
            return Response(serializerdata.errors)

    

    except BaseException as e:
        return Response(str(e))


@api_view(['PATCH'])
def updateAccount(request, id):

    try:

        user = User.objects.filter(id = id).first()

        if user is None:
            return Response("No Account found")
        
        else:
          serializerdata = updateSerializer(user, data=request.data, partial=True)

          if serializerdata.is_valid():
              serializerdata.save()
              return Response(data = serializerdata.data)
          else:
             
              return Response(data = serializerdata.errors)

              
        

    except BaseException as e:
        return Response(str(e))


  

@api_view(['DELETE'])
def deleteAccount(request, id):

    try:
        user = User.objects.filter(id = id).first()

        if user is None:
            return Response("account not found")
        
        else:
            user.delete()
            return Response("account deleted successfully")

    except BaseException as e:
        raise Response(str(e))

 