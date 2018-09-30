from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.generic import TemplateView
from maps.inputform import InputForm
from django.http import HttpResponseRedirect
from urllib.parse import quote

import googlemaps
import json

import urllib.request

import requests
from datetime import datetime



#def index(request):
#    if request.method == "GET":
#        return render(request, 'maps/index.html', context=None)
#    if request.method == "GET":
#        return render(request, 'maps/map.html', context=None)

class HomeView(TemplateView):
    template_name = 'maps/index.html'

    def get(self, request):
        form = InputForm()
        return render(request, self.template_name, {'form' : form, 'flag': -1})

    def post(self, request):

        form = InputForm(request.POST)

        if form.is_valid():
            start = form.cleaned_data['Start']
            destination = form.cleaned_data['End']
            #return HttpResponseRedirect('/search/')

        args = {'form': form, 'start': start, 'end': destination}


        gmaps = googlemaps.Client(key='AIzaSyBQThVIW-tNgV4Yth_Evk_vbLS4cVQgjgU')

        directions_result = gmaps.directions(request.POST['Start'], request.POST['End'], mode="driving", departure_time=datetime.now())

        #request = https://maps.googleapis.com/maps/api/directions/json?origin=start&destination=destination&key=AIzaSyBQThVIW-tNgV4Yth_Evk_vbLS4cVQgjgU

        #response = requests.get(
         #   'https://maps.googleapis.com/maps/api/directions/json?origin=start&destination=destination&key=AIzaSyBQThVIW-tNgV4Yth_Evk_vbLS4cVQgjgU')
        #direction = json.loads(response.text)


        x = str(request.POST['Start'])
        y= str(request.POST['End'])

        print(x)
        print(y)
        x_param = quote(x)
        y_param = quote(y)

        request1 = "https://maps.googleapis.com/maps/api/directions/json?origin=" + x_param + "&destination=" + y_param + "&key=AIzaSyBQThVIW-tNgV4Yth_Evk_vbLS4cVQgjgU"
        #request1 = 'https://maps.googleapis.com/maps/api/directions/json?origin=buffalo&destination=chicago&key=AIzaSyBQThVIW-tNgV4Yth_Evk_vbLS4cVQgjgU'
        print(request1)
        #print(request)
        response = urllib.request.urlopen(request1).read()
        direction = json.loads(response)
        print(direction)


        destination={}
        origin={}
        destination['query'] = y
        origin['query'] =x
        direction['request'] = {'destination': destination, 'origin': origin, 'travelMode': "DRIVING"}



        #return HttpResponse(json.dumps(direction))
        #return render(request, self.template_name, args)

        if(directions_result is None):
            return render(request, self.template_name, {'form': form, 'flag': 0})
        else:
            return render(request, self.template_name, {'form': form,'response': json.dumps(direction), 'flag': 1, 'start': start, 'end': destination})
            #return render(request, self.template_name,
             #             {'form': form, 'response': json_data, 'flag': 1, 'start': start,
              #             'end': destination})

def search(request):
    return render(request, 'maps/map.html', context=None)




