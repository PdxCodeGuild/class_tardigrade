from typing import Counter
import webbrowser
import os
import folium
import geocoder

g = geocoder.arcgis(input('city:   '))
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
            route()
        else:
            print("Please try again")
            menu()



def place():
    
    g = geocoder.arcgis(input('Enter a city:   '))
    # m = folium.Map(location=[g.lat, g.lng], zoom_start=12)
    m.save("index.html")
    webbrowser.open('index.html')


def pins():
    
    p = geocoder.arcgis(input('Enter a pin location:   '))
    lati =p.lat
    lon= p.lng
    # m = folium.Map(location=[lati, lon], zoom_start=15)
    Counter = 1
    Counter+=1
    folium.Marker([lati, lon], tooltip='{Counter}').add_to(m)

    m.save("index.html")


def route():
    p = geocoder.arcgis(input('Enter a pin location:   '))
    lati =p.lat
    lon= p.lng

    loc = [(lati, lon),
       (lati, lon)]

    folium.PolyLine(loc,
                    color='red',
                    weight=12,
                    opacity=1).add_to(m)
    m.save("index.html")


main()