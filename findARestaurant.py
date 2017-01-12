from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
import httplib
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "RESTKBENVR0VH4D22Z34YAWCVPUAO0SXWRP0X0LJCZJKHHSD"
foursquare_client_secret = "NQSRZMMRDZ5WQSXVU31ANQABEXPC0JNV5GZD3FWW2NI0DLVE"

def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
        lat, long = getGeocodeLocation(location)

	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
        url = ('https://api.foursquare.com/v2/venues/search?ll=%s,%s&client_id=%s&client_secret=%s&query=%s'%(lat,long,foursquare_client_id,foursquare_client_secret,mealType))
        h = httplib2.Http()
        response, content = h.request(url, 'GET')
        result = json.loads(content[1])

        if result['response']['venues']:
                #3. Grab the first restaurant
                restaurant = result['response']['venues'][0]
                venue_id = restaurant['id'] 
                restaurant_name = restaurant['name']
                restaurant_address = restaurant['location']['formattedAddress']
                address = ""
		# The address is a list of entries as opposed to a single string. Thus each entry i is concatenated with next one by adding space in below lines
                for i in restaurant_address:
                        address += i + " "
                restaurant_address = address
                #4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
                pic_url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&client_secret=%s&v=20161212'%(venue_id,oursquare_client_id,oursquare_client_secret))
                h2 = httplib2.Http()
                response2, content2 = h2.request(url,'GET')
                result2 = json.loads(content2[1])
                #5. Grab the first image
                if result2['response']['photos']['item']
                        first_photo = result2['response']['photos']['items'][0]
                        prefix = first_photo['prefix']
                        suffix = first_photo['suffix']
                        size = "300x300"
                        photo_url = prefix + size + suffix
                else:
                        #6. If no image is available, insert default a image url
                        default_photo_url = ('https://upload.wikimedia.org/wikipedia/en/d/db/Despicable_Me_Poster.jpg')
                        photo_url = default_photo_url
                #7. Return a dictionary containing the restaurant name, address, and image url
                restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
                print "Restaurant Name: %s" % restaurantInfo['name']
                print "Restaurant Address: %s" % restaurantInfo['address']
                print "Image: %s \n" % restaurantInfo['image']
                return restaurantInfo

        else:
                print "No Restaurants found for %s" %location
                return "no location found"



if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")
       







