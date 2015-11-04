from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from minimixer_manager.serializers import UserSerializer, RecipeSerializer, RecipeInstructionSerializer
from minimixer_manager.models import Recipe, RecipeIngredient, Ingredient
from minimixer_manager.permissions import IsOwner
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
import serial
import Adafruit_BBIO.UART as UART
import time

# Create your views here.

# Model Viewset for the recipe model. Allows
class RecipeViewSet(viewsets.ModelViewSet):

    # Define the queryset to act on for the recipe models
    queryset = Recipe.objects.all()

    # Define the serializer used to serialize/de-serialize the data
    serializer_class = RecipeSerializer

    # Define the permissions required for Account view requests to be provided
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Define the queryset to be provided for the authenticated user to act on
    def get_queryset(self):
        return self.request.user.recipe_set.all()

# Modell Viewset for the User model.
class UserViewSet(viewsets.ModelViewSet):
    model = User
    # Serializer used to delete the User model (Destroying main user account).
    serializer_class = UserSerializer

    # All requests to the user view must be authenticated
    permission_classes = [IsAuthenticated]

    # The queryset to act on will be all user object of the requested user.
    queryset = User.objects.all()
    def get_queryset(self):
        return User.objects.filter(username=self.request.user)


# Define the POST view to create a new main user account
@api_view(['POST'])
# Exempt csrf tokens in the headers as they are not needed for this request
@csrf_exempt
def create_auth(request):

    # User serializer for the incoming create account request
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['username'],
            serialized.init_data['email'],
            serialized.init_data['password']
        )
        return Response(status=status.HTTP_201_CREATED)
    else:
        # User account already exists.
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

# Tempurature status check
@api_view(['GET'])
@csrf_exempt
def get_temp(request):
    w1="/sys/bus/w1/devices/28-000006deecc1/w1_slave"
    raw = open(w1, "r").read()
    temp = str(float(raw.split("t=")[-1])/1000*9/5+32)
    content = {'tempurature': temp}
    return Response(content)

# Order a drink.
class OrderManager(GenericAPIView):
    def get(self, request, format=None):
        return Response(request.data)

    def get_serializer_class(self):
        return RecipeInstructionSerializer
    def post(self, request, format=None):

            serializer = RecipeInstructionSerializer(data=request.data)
            num_parallel = request.data.get('num_parallel')
            print num_parallel
            pump_a = request.data.get('pump_a')
            print pump_a
            pump_b = request.data.get('pump_b')
            pump_c = request.data.get('pump_c')
            pump_d = request.data.get('pump_d')
            pump_e = request.data.get('pump_e')
            pump_f = request.data.get('pump_f')
            #instruction = "R" + str(num_parallel) + "0A" + str(pump_a) + "B" + str(pump_b) + "C" + str(pump_c) + "D" + str(pump_d) + "E" + str(pump_e) + "F" + str(pump_f)
            #print instruction

            if serializer.is_valid():
                #serializer.save()

                #UART.setup("UART1")
                ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
                ser.close()
                ser.open()
                print "Response" + ser.read(10)
                ser.write("R")
                print "Response " + ser.read(10)
                ser.write(str(num_parallel))
                print "Response " + ser.read(10)
                ser.write("0")
                print "Response " + ser.read(10)
                ser.write("A")
                print "Response " + ser.read(10)
                ser.write(str(pump_a))
                print "Response " + ser.read(10)
                ser.write("B")
                print "Response " + ser.read(10)
                ser.write(str(pump_b))
                print "Response " + ser.read(10)
                ser.write("C")
                print "Response " + ser.read(10)
                ser.write(str(pump_c))
                print "Response " + ser.read(10)
                ser.write("D")
                print "Response " + ser.read(10)
                ser.write(str(pump_d))
                print "Response " + ser.read(10)
                ser.write("E")
                print "Response " + ser.read(10)
                ser.write(str(pump_e))
                print "Response " + ser.read(10)
                ser.write("F")
                print "Response " + ser.read(10)
                ser.write(str(pump_f))
                print "Response " + ser.read(10)
                print "got here"

                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
