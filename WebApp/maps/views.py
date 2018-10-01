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

        #myRoute = direction['routes'][0]['legs'][0]['steps'][1]['start_location']


        weather_list=[]

        #for i in direction['routes'][0]['legs'][0]['steps']:
        for x in direction['routes'][0]['legs'][0]['steps']:
            lat = str(x['start_location']['lat'])
            lon = str(x['start_location']['lng'])
            lat_param = quote(lat)
            lon_param = quote(lon)
            req = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat_param + "&lon=" + lon_param + "&appid=66b64cfa937f31bbd5cb328cdad938a0"
            weather_response = urllib.request.urlopen(req).read()
            weather_res = json.loads(weather_response)
            weather_list.append(weather_res['weather'][0]['main'])


        #print(weather_list)

        #print(str(myRoute))

        destination={}
        origin={}
        destination['query'] = y
        origin['query'] =x
        direction['request'] = {'destination': destination, 'origin': origin, 'travelMode': "DRIVING"}


        #Now, Calling the Weather API to fetch the weather details
        lat_param, lon_param = fetch_latlong(x_param, gmaps)
        request2 = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat_param + "&lon=" + lon_param + "&appid=66b64cfa937f31bbd5cb328cdad938a0"
        weather_response = urllib.request.urlopen(request2).read()
        weatherresponse_start = json.loads(weather_response)
        weather_start = weatherresponse_start['weather'][0]['main']


        lat_param, lon_param = fetch_latlong(y_param, gmaps)
        #request3 = "https://api.openweathermap.org/data/2.5/weather?q=" + y_param + "&appid=66b64cfa937f31bbd5cb328cdad938a0"
        request3 = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat_param + "&lon=" + lon_param + "&appid=66b64cfa937f31bbd5cb328cdad938a0"
        weather_response = urllib.request.urlopen(request3).read()
        weatherresponse_destination = json.loads(weather_response)
        weather_destination = weatherresponse_destination['weather'][0]['main']


        #return HttpResponse(json.dumps(direction))
        #return render(request, self.template_name, args)


        print(weather_list)

        if(directions_result is None):
            return render(request, self.template_name, {'form': form, 'flag': 0})
        else:
            return render(request, self.template_name, {'form': form, 'response': json.dumps(direction), 'flag': 1, 'start': start, 'end': destination, 'start_weather': weather_start, 'destination_weather': weather_destination, 'weather_list': weather_list})

def search(request):
    return render(request, 'maps/map.html', context=None)


def fetch_latlong(loc, gmaps):
    geocode_result = gmaps.geocode(loc)
    lat = geocode_result[0]["geometry"]["location"]["lat"]
    lon = geocode_result[0]["geometry"]["location"]["lng"]

    lat = str(lat)
    lon = str(lon)
    lat_param = quote(lat)
    lon_param = quote(lon)

    return lat_param, lon_param