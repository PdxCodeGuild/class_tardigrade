from typing import Counter
import webbrowser
import os
import folium
import geocoder
import geojson
import requests
import openrouteservice
import pandas
import secrets

g = geocoder.arcgis('Enter a start city:')
m = folium.Map(location=[g.lat, g.lng], zoom_start=15)
# folium.Marker(
#    [45.3288, -121.6625], popup="<i>Mt. Hood Meadows</i>", tooltip='hello'
# ).add_to(m)
# folium.Marker(
#     [45.3311, -121.7113], popup="<b>Timberline Lodge</b>", tooltip='hi'
# ).add_to(m)
# m.save("index.html")
# webbrowser.open('index.html')

def main():
   menu()

def menu():
    print()
    while True:
        choice = int(input("""
                        1: Choose your city
                        2: Save your spot
                        3: Make a path

                        Please choose: """))

        if choice == 1:
            place()
        elif choice == 2:
            pins()
        elif choice == 3:
            routes()
        else:
            print("Please try again")
            menu()



def place():
    
    g = geocoder.arcgis(input('Enter a city:   '))
    
    m = folium.Map(location=[g.lat, g.lng], zoom_start=12)
    m.save("dex.html")
    webbrowser.open('dex.html')
    
Counter = 0

def pins():
    global Counter
    p = geocoder.arcgis(input('Enter a pin location:   '))
    lati =p.lat
    lon= p.lng
    # m = folium.Map(location=[lati, lon], zoom_start=15)
    Counter+=1
    folium.Marker([lati, lon], tooltip=f'{Counter}').add_to(m)

    m.save("dex.html")
    return p
def routes():
        city = input('city:   ')
        g = geocoder.arcgis(city)
        g2 = geocoder.arcgis(input('city:   '))
        
        client = openrouteservice.Client(key=secrets.secret_key)
        # coordinates =[(g.lat, g.lng), (g2.lat, g2.lng)]
        coordinates =[ (g.lng, g.lat), (g2.lng, g2.lat)]

        
        

        m = folium.Map(location=[g.lat, g.lng], zoom_start=15)
        folium.Marker([g.lat,g.lng], popup=g, tooltip=g).add_to(m)
        folium.Marker([g2.lat,g2.lng], popup=g2, tooltip=g2).add_to(m)
        # folium.PolyLine([(g.lat,g.lng),(g2.lat,g2.lng)],
        #                     color='red',
        #                     weight=1,
        #                     opacity=1).add_to(m)


        route = client.directions(coordinates=coordinates, profile='driving-car', format='geojson')
        # One of [“driving-car”, “driving-hgv”, “foot-walking”, “foot-hiking”, “cycling-regular”, “cycling-road”,”cycling-mountain”, “cycling-electric”,]. Default “driving-car”.
        folium.GeoJson(route, name='route').add_to(m)
        folium.Marker([g.lat,g.lng], popup=g, tooltip=g).add_to(m)
        folium.Marker([g2.lat,g2.lng], popup=g2, tooltip=g2).add_to(m)
        
        print(route['features'][0]['properties']['segments'][0]['distance']*0.000621371, 'miles')
        print(route['features'][0]['properties']['segments'][0]['duration']*0.000277778, 'hours\n')

        m.save("dex.html")


        webbrowser.open('dex.html')
        




main()
