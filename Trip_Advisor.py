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
user_response=('yes')
user_decline=('no')
if user_response.lower() in user_response =='yes' :
    input ('Are you satisfied with your trip? ')
#code works after debugging I generate randomized choices from each list and prints are you satisfied#  
if user_response.lower() in user_response=='yes' :
    input ('Is your trip complete?')
if user_response.lower() in user_response=='yes' :
 print (daily_destination,daily_entertainment,daily_transportation,daily_restaurant)
#after yes input to questions console prints verified confirmed choices# 
if user_decline.lower() =='no':
 input ('What feature would you like to change? Destinations?, Entertainments?, Transportations?,Restaurants?')

