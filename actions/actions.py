from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

# from rasa_core.actions.action import Action
from rasa_sdk import Action
#from rasa_sdk.forms import ( BooleanFormField, EntityFormField, FormAction, FreeTextFormField )
from rasa_sdk.events import SlotSet
# from rasa_core.events import SlotSet
import zomatopy
import json

zomato_config={ "user_key":"9336c77893ad054b9174f6d345018335"}
result_of_last_query = ""

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_restaurant'

	def filterRestaurantBasedOnBudget(self, userbudget, allRestaurants):
		rangeMin = 0
		rangeMax = 100000

		if userbudget.isdigit():
			price = int(userbudget)

			if price == 1:
				rangeMax = 299
			elif price == 2:
				rangeMin = 300
				rangeMax = 699
			elif price == 3:
				rangeMin = 700
			elif price < 300:
				rangeMax = 299
			elif price < 700 and price >= 300:
				rangeMin = 300
				rangeMax = 699
			else:
				rangeMin = 700
		else:
			# default budget
			rangeMin = 300
			rangeMax = 699

		index = 0
		count = 0
		response = ""
		global result_of_last_query
		result_of_last_query = ""

		for restaurant in allRestaurants:
			++count
			res = "[" + restaurant['restaurant']['user_rating']['aggregate_rating'] + "/5] " + restaurant['restaurant']['name'] + " in " + restaurant['restaurant']['location']['address']

			# price_range = str(restaurant['restaurant']['price_range'])
			avg_c_2 = restaurant['restaurant']['average_cost_for_two']

			# if price_range == "1":

			if avg_c_2 <= rangeMax and avg_c_2 >= rangeMin:

				# mapbybudget["1"].append(restaurant)
				# if userbudget == price_range:

				res = restaurant['restaurant']['currency'] + str(restaurant['restaurant']['average_cost_for_two']) + " " + res + "\n"
				if(index < 5):
					response = response + res

				if(index < 10):
					result_of_last_query = result_of_last_query + res
				index = index + 1

		# modifying the search results
		# if the no. of result fall short, appending the results of other price range
		if index == 0:
			response = "Oops! no restaurant found for this query. " + " search results = " + str(count)
		elif index < 5:
			# we can add restaurants from the higher range but for now i am appending an extra message
			response = response + "\n \nFor more results please search in higher budget range...\n \n"
		elif index < 10:
			result_of_last_query = result_of_last_query + "\n \nFor more results please search in higher budget range...\n \n"

		return response

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')

		zomato = zomatopy.initialize_app(zomato_config)
		location_detail=zomato.get_location(loc, 1)

		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]

		cuisines_dict={
		'american':1,
		'mexican':73,
		'italian':55,
		'chinese':25,
		'north indian':50,
		'south indian':85
		}

		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)

		d = json.loads(results)
		response=""

		if d['results_found'] == 0:
			response= "Sorry, we didn't find any results for this query."
		else:
			# dispatcher.utter_message(str(d))
			response = self.filterRestaurantBasedOnBudget(budget, d['restaurants'])

		dispatcher.utter_message(str(response))
		return [SlotSet('location',loc)]


t1_t2_cities = ["Ahmedabad","Bangalore","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune",
"Agra","Ajmer","Aligarh","Amravati","Amritsar","Asansol","Aurangabad",
"Bareilly","Belgaum","Bhavnagar","Bhiwandi","Bhopal","Bhubaneswar",
"Bikaner","Bokaro Steel City","Chandigarh","Coimbatore","Cuttack","Dehradun",
"Dhanbad","Bhilai","Durgapur","Erode","Faridabad","Firozabad","Ghaziabad",
"Gorakhpur","Gulbarga","Guntur","Gurgaon","Guwahati","Hamirpur",
"Gwalior","Hubli-Dharwad","Indore","Jabalpur","Jaipur","Jalandhar","Jammu","Jamnagar","Jamshedpur","Jhansi","Jodhpur",
"Kannur","Kanpur","Kakinada","Kochi","Kottayam","Kolhapur","Kollam","Kota","Kozhikode","Kurnool","Lucknow","Ludhiana",
"Madurai","Malappuram","Mathura","Goa","Mangalore","Meerut",
"Moradabad","Mysore","Nagpur","Nanded","Nashik","Nellore","Noida","Patna","Pondicherry","Purulia Prayagraj","Raipur","Rajkot",
"Rajahmundry","Ranchi","Rourkela","Salem","Sangli","Siliguri","Shimla"
"Solapur","Srinagar","Surat","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tiruppur",
"Ujjain","Bijapur","Vadodara","Varanasi",
"Vasai-Virar City","Vijayawada","Visakhapatnam","Vellore","Warangal"]

t1_t2_cities_list = [x.lower() for x in t1_t2_cities]

# Check if the location exists. using zomato api.if found then save it, else utter not found.
class ActionValidateLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		city = str(loc)
		# dispatcher.utter_message(city)

		if city.lower() in t1_t2_cities_list:
			return [SlotSet('location_match',"one")]
		else:
			zomato = zomatopy.initialize_app(zomato_config)

			try:
				results = zomato.get_city_ID(city)
				return [SlotSet('location_match',"one")]
			except:
				# results = "Sorry, didn’t find any such location. Can you please tell again?" + "-----" + city
				# dispatcher.utter_message(city)
				return [SlotSet('location_match',"zero")]


# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')

		# for slack handling
		if len(email.split("|")) == 2:
			email = email.split("|")[1]

		import smtplib
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls()
		s.login("<Enter_your_Email-Id>", "<Enter_your_Password>")    # Creat your dummy gmail account that can use for the credential
		SUBJECT = "Foodiebot - Provide a Good Restaurant Quickly !!"
		TEXT = "Hey Foodii ;) !\nThe details of all the restaurants you inquried, Enjoy a taste of heaven!. \n \n"
		message = 'Subject: {}\n\n{}'.format(SUBJECT,TEXT)
		global result_of_last_query
		message = message + result_of_last_query
		try:
			s.sendmail("<Enter_your_MailId>", str(email), message)
			s.quit()
		except:
			dispatcher.utter_message(email)

		result_of_last_query = ""
		return [AllSlotsReset()]

from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

class ActionRestarted(Action):
	def name(self):
		return 'action_restart'
	def run(self, dispatcher, tracker, domain):
		return[Restarted()]

class ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'
	def run(self, dispatcher, tracker, domain):
		return[AllSlotsReset()]
