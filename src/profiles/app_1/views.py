from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions


# Create your views here.
class HelloApiViews(APIView):  
    """Test api views"""

    serializer_class= serializers.HelloSerializer

    def get(self,request,format=None):
        """ Returns lsit of api features"""
        
        an_apiview =  [
            'Uses http mehtods as fucntion (get,post,put,delete,patch)',
            'it is similar to a traditional Django View',
            'GIves us the most control over our logic',
            'Its mapped manually to the URLS',
        ]

        
        return Response({'message':'Hello','apiview':an_apiview })

    def post(self,request):
        """Creates hello message with our Name"""

        serializer =serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message = ' hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """put method"""

        return Response({'message':'put'})


    def patch(self,request,pk=None): 
        """patch method"""

        return Response({'message':'patch'})

    def delete(self,request,pk=None):
        """delete method"""

        return Response({'message':'delete'})


class HelloViewSets(viewsets.ViewSet):
    """Test API VIEWSETS"""

    serializer_class= serializers.HelloSerializer

    def list(self,request):
        """create hello message"""

        a_view= [ 
            '1',
            '2',
            '3'
        ]
        return Response({'message':'Hellow','a_view':a_view })

    def create(self,request):
        """create a new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name= serializer.data.get('name')
            message = ' hello {0}'.format(name)
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self,request,pk=None):
        """GET method objetcs by id"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """put method"""

        return Response({'http_method':'put'})


    def partial_update(self,request,pk=None): 
        """patch method"""

        return Response({'http_method':'patch'})

    def destroy(self,request,pk=None):
        """delete method"""

        return Response({'http_method':'DELETE'})

class UserProfileViewSets(viewsets.ModelViewSet):
    """Handles creating , Reading and Updating User profiles"""

    serializer_class=serializers.UserSerailiser
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes     = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)



class LoginViewSet(viewsets.ViewSet):
    """Checks emails and passwords and returns an auth Token"""
    serializer_class = AuthTokenSerializer

    def create(self,request):
        """Use ObtainAuthToken APIview to validate and create a token"""


        return ObtainAuthToken().post(request)

class ProfileFeedItmeViewSet(viewsets.ModelViewSet):
    """handles creating and updating of profile feed items"""


    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)



    def perform_create(self,serializer):
        """Sets the user profile to the logged in user """

        serializer.save(user_profile=self.request.user)
