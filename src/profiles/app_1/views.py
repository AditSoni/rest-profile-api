from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiViews(APIView):
    """Test api views"""


    def get(self,request,format=None):
        """ Returns lsit of api features"""
        context={}
        an_apiview =  [
            'Uses http mehtods as fucntion (get,post,put,delete,patch)',
            'it is similar to a traditional Django View',
            'GIves us the most control over our logic',
            'Its mapped manually to the URLS',
        ]

        context['message']='Hello!'
        context['apiview']=an_apiview
        return Response(context)