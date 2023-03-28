destinations=['Downtown Miami','Palm Beach','Ft Lauderdale','Miami Beach']
import random
daily_destination= random.choice (destinations)

restaurants=['Red Cow','Rock and Roll Ribs','Mint','News Cafe']
import random
daily_restaurant= random.choice (restaurants)

transportations=['lyft','uber','metro rail','taxi']
import random
daily_transportation= random.choice (transportations)

entertainments=['Arena Concert','Amphitheatre Concert','Arena Concert','Outdoor Concert']

daily_entertainment= random.choice (entertainments)

print (daily_destination,daily_entertainment,daily_transportation,daily_restaurant)
user_confirm='yes'
user_decline='no' 

user_response=input('Are you satisfied with your trip?')
if user_response==user_confirm:
    user_response=input('Is your trip complete?')
    if user_response==user_confirm:
        print (daily_destination,daily_entertainment,daily_transportation,daily_restaurant)
if user_response==user_decline:
     user_response=input ('What feature would you like to change? Destinations?, Entertainments?, Transportations?,Restaurants?')
     if user_response.lower()== 'destinations':
       print(random.choice (destinations))
     if user_response.lower()== 'restaurants':
       print (random.choice (restaurants))
     if user_response.lower()== 'transportations':
      print (random.choice (transportations))
      if user_response.lower()== 'entertainments':
          print (random.choice (entertainments))
          if user_response==user_confirm:
             input('Iyour trip complete?')
             if user_response==user_confirm:
                print (daily_destination,daily_entertainment,daily_transportation,daily_restaurant)
                #revision once I refreshed functions not complete


    
   

