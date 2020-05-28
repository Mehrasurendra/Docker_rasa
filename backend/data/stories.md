<!-- good bye stories -->
## Complete path 1
* goodbye
    - utter_goodbye
	- action_restart

## Complete path 2
* goodbye
    - utter_goodbye
	- action_restart
    - action_restart

## Complete path 3
* goodbye
    - utter_goodbye
	- action_restart

## Complete path 4
* goodbye
    - utter_goodbye
	- action_restart

## Complete path 5
* goodbye
    - utter_goodbye
	- action_restart

## Complete path 6
* goodbye
    - utter_goodbye
	- action_restart

<!-- good bye stories -->


<!-- deny stories -->
## Complete path 7
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 8
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 9
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 10
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 11
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 12
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 13
* deny
    - utter_no_email_sent
	- action_restart

## Complete path 14
* deny
    - utter_no_email_sent
	- action_restart
<!-- deny stories -->


<!-- stories starting with only bare inform with complete information and email -->
## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_2
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "kanpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_3
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "jaipur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_4
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_5
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_6
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart
<!-- stories starting with only bare inform with complete information and email -->

<!-- stories starting with only bare inform with complete information and no email -->
## interactive_story_7
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_8
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_9
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_10
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_11
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_12
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_13
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_14
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_15
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_16
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_17
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_18
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_19
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_20
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_21
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_22
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_23
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

<!-- stories starting with only bare inform with complete information and no email -->





<!-- stories starting with location inform with complete information and sent email -->
## interactive_story_24
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_25
* greet
    - utter_greet
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
     - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_26
* greet
    - utter_greet
* inform{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "prateekvikam@asdasd.com"}
    - slot{"email": "prateekvikram@asdasd.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_27
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_28
* greet
    - utter_greet
* inform{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_29
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_30
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_31
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_32
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_33
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_34
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart
<!-- stories starting with location inform with complete information and sent email -->


<!-- stories starting with location inform with complete information and no sent email -->
## interactive_story_35
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_36
* greet
    - utter_greet
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_37
* greet
    - utter_greet
* inform{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Amritsar"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_38
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_39
* greet
    - utter_greet
* inform{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nagpur"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_40
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_41
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_42
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_43
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_44
* greet
    - utter_greet
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_45
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_46
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_47
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_48
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_49
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_50
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_51
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_52
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_53
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_54
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_55
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_56
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_57
* greet
    - utter_greet
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_58
* greet
    - utter_greet
* inform{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Jalandhar"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart


<!-- stories starting with location inform with complete information and no sent email -->


<!-- stories starting with cuisine inform with complete information and sent email -->

## interactive_story_59
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_60
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* send_email{"email": "zjiom@gmail.co.in"}
    - slot{"email": "zjiom@gmail.co.in"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_61
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_62
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_63
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_64
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_65
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_66
* greet
    - utter_greet
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* inform{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_67
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_68
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_69
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_70
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_71
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart
<!-- stories starting with cuisine inform with complete information and sent email -->

<!-- stories starting with cuisine inform with complete information and no sent email -->

## interactive_story_72
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_73
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_74
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_75
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_76
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_77
* greet
    - utter_greet
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_78
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chennai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_79
* greet
    - utter_greet
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* inform{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Gwalior"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_80
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_81
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_82
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_83
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_84
* greet
    - utter_greet
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* inform{"location": "Surat"}
    - slot{"location": "Surat"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Surat"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

<!-- stories starting with cuisine inform with complete information and no sent email -->



<!-- stories starting with cuisine and location inform, with complete information and sent email -->
## interactive_story_85
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Chandigarh"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Chandigarh"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Chandigarh"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_86
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_87
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart


## interactive_story_88
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_89
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_90
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_91
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_92
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_93
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_94
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_95
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_96
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_97
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_98
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_99
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_100
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_101
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Guwahati"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Guwahati"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Guwahati"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_102
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_103
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_104
* greet
    - utter_greet
* inform{"cuisine": "italian", "location": "Patna"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_105
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_106
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_107
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

## interactive_story_108
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
	- action_restart

<!-- stories starting with cuisine and location inform, with complete information and sent email -->


<!-- stories starting with cuisine and location inform, with complete information and no sent email -->

## interactive_story_109
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patna"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_110
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Bhopal"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bhopal"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bhopal"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart

## interactive_story_111
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* deny
    - utter_no_email_sent
	- action_restart


## interactive_story_112
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart


## interactive_story_113
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Kozhikode"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kozhikode"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Kozhikode"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart


## interactive_story_114
* greet
    - utter_greet
* inform{"cuisine": "north indian", "location": "mumbai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* deny
    - utter_no_email_sent
	- action_restart
<!-- stories starting with cuisine and location inform, with complete information and no sent email -->

<!-- misc -->
## interactive_story_115
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_116
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_117
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_118
* greet
    - utter_greet
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_119
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_120
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_121
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_122
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_123
* greet
    - utter_greet
* inform
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart


<!-- misc -->
<!-- leave in between -->


## interactive_story_124
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_125
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_126
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart

## interactive_story_127
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* goodbye
    - utter_goodbye
	- action_restart
	- action_restart


## interactive_story_128
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_129
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_130
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_131
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_132
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_133
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_134
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "noida"}
    - slot{"location": "noida"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* inform{"budget": "701"}
    - slot{"budget": "701"}
    - utter_searching
    - action_restaurant
    - slot{"location": "noida"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_135
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_136
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_137
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* goodbye
    - utter_goodbye
	- action_restart

## interactive_story_138
* greet
    - utter_greet
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* goodbye
    - utter_goodbye
	- action_restart

<!-- leave in between -->




<!-- condition checkpoints -->

## interactive_story_139
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_140
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_141
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart

## interactive_story_142
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_143
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_144
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart


## interactive_story_145
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_146
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_147
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_148
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_149
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_150
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_151
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_152
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_153
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart

## interactive_story_154
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_155
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_156
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart


## interactive_story_157
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_158
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_159
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_160
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_161
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_162
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_163
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_164
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_165
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart

## interactive_story_166
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_167
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* goodbye
    - utter_goodbye
    - action_restart


## interactive_story_168
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhsdadi"}
    - slot{"location": "delhsdadi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "dlehi"}
    - slot{"location": "dlehi"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* deny
    - utter_goodbye
    - action_restart


## interactive_story_169
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_170
* greet
    - utter_greet
* inform{"location": "Bangalorety"}
    - slot{"location": "Bangalorety"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Banglaore"}
    - slot{"location": "Banglaore"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "uyhbkjn@gmail.com"}
    - slot{"email": "uyhbkjn@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_171
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_172
* greet
    - utter_greet
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* inform{"location": "Nashiq"}
    - slot{"location": "Nashiq"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashiqw"}
    - slot{"location": "Nashiqw"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Nashik"}
    - utter_ask_for_email_to_send
* send_email{"email": "asdsdad@gmail.com"}
    - slot{"email": "asdsdad@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_173
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_174
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "Patnait"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patnaii"}
    - slot{"location": "Patnaii"}
    - action_check_location
    - slot{"location_match": "zero"}
    - utter_location_not_found
* inform{"location": "Patna"}
    - slot{"location": "Patna"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_budget
* inform{"budget": "399"}
    - slot{"budget": "399"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

<!-- condition checkpoints -->

<!-- all the information in one go -->

## interactive_story_175
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_176
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_177
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_178
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_179
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_180
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_181
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart


## interactive_story_182
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_183
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_184
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_185
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_186
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_187
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_188
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_189
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_190
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_191
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_192
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_193
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_194
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_195
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_196
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_197
* greet
    - utter_greet
* inform{"cuisine": "chinese", "location": "delhi", "budget": "399"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"budget": "399"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "Patna"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

<!-- all information in one go. -->



<!-- starting with budget and location -->

## interactive_story_198
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_199
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_200
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_201
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_202
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_203
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_204
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_205
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_206
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_207
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_208
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_209
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_210
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_211
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_212
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_213
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_214
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_215
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_216
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_217
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_218
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_219
* greet
    - utter_greet
* inform{"location": "delhi", "budget": "2000"}
    - slot{"location": "delhi"}
    - slot{"budget": "2000"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

<!-- starting with cuisine and budget -->

## interactive_story_220
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_221
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_222
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_223
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_224
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_225
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_226
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_227
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_228
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_229
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_230
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_231
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_232
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_233
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_234
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_235
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_236
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_237
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_238
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_239
* greet
    - utter_greet
* inform{"cuisine": "chinese", "budget": "2000"}
    - slot{"cuisine": "chinese"}
    - slot{"budget": "2000"}
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "surendramehra40@gmail.com"}
    - slot{"email": "surendramehra40@gmail.com"}
    - action_send_email
    - utter_email_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* inform
    - utter_ask_location
* inform{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location_match": "one"}
    - utter_ask_cuisine
* inform{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* inform{"budget": "699"}
    - slot{"budget": "699"}
    - utter_searching
    - action_restaurant
    - slot{"location": "delhi"}
    - utter_ask_for_email_to_send
