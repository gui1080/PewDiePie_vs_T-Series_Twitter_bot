import urllib.request
import json
import time
from time import gmtime, strftime
import tweepy as tp
import numpy
from stuff import first_data_update
from stuff import data

# bug to be fixed: hours are delayed!
# future update: do a basic user interface

# Creating array for data analysis
subgap_arr = []

# we have not tweeted yet
tweet_counter = 0

print("Twitter Bot is running!")

# Google's API key
key = " YOUR OWN KEY HERE "

# The truth
good_content = "PewDiePie"
bad_content = "tseries"

# credentials to login to twitter api
consumer_key = ' YOUR OWN CREDENTIAL HERE '
consumer_secret = ' YOUR OWN CREDENTIAL HERE '
access_token = ' YOUR OWN CREDENTIAL HERE '
access_secret = ' YOUR OWN CREDENTIAL HERE '

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# creating the first data update
subgap_last_update = first_data_update(key, good_content, bad_content);
time.sleep(30)

# Time input

print("Enter (in minutes) the loop duration: ")
loop_time = input()

print("Enter (in minutes) the interval between your tweets: ")
tweet_interval = input()

# creating time
actual_time = (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
fobj_out = open("Subscriber_log - " + str(actual_time) + ".txt", "w")

# defining time loop
t_end = time.time() + (60 * (int(loop_time)))

#-----------------------------------------------------------------------BOT TWEET LOOP----------------------------------------------------------------------------------------------------------------

while time.time() < t_end:

  #PEWDIEPIE DATA

  pewds_subs = data(key, good_content)
  print("PewDiePie's subscribers: " + (str(pewds_subs)))

  #TSERIES DATA

  tseries_subs = data(key, bad_content)
  print("T-Series's subscribers: " + (str(tseries_subs)))

  # time!

  print("Local Time:")
  actual_time = (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
  print(actual_time)

  # Subscriber Difference
  current_subgap = (int(pewds_subs)) - (int(tseries_subs))
  print("Subgap:" + str(current_subgap))

  if subgap_last_update == current_subgap:
    # (since we can't actually spam the same message at twitter)
    print("No sub gap changes, wait for next iteration!")

  elif subgap_last_update > current_subgap:
    # subscriber difference is decreasing!
    print("Subscriber difference is decreasing! Attention all gamers!")
    api.update_status("ATTENTION!\nThe sub gap is decreasing!\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)

  elif subgap_last_update < current_subgap:
    # subscriber difference is increasing!
    print("Subscriber difference is increasing! Epic gamer moment!")
    api.update_status("ATTENTION!\nThe sub gap is increasing!\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)

  elif current_subgap < 30000:
    if subgap_last_update < current_subgap:
      # low sub gap tweet 1
      print("The end is near fellow gamers! Sub gap is below 30k!")
      api.update_status("Keep it up! The sub gap is increasing!\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)

    elif subgap_last_update > current_subgap:
      # low sub gap tweet 2
      print("The end is near! Sub gap is below 30k!")
      api.update_status("Attention! The sub gap is decreasing!\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)

  elif current_subgap < 20000:
    # low sub gap tweet 3
    print("The end is near fellow gamers! Sub gap is below 20k!")
    api.update_status("WE NEED YOUR HELP @elonmusk and @MrBeastYT\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)


  elif current_subgap < 10000:
    # low sub gap tweet 4
    print("The end is near fellow gamers! Sub gap is below 10k!")
    api.update_status("It's almost over! Sub gap is below 10k!\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)

  elif current_subgap < 1000:
    # low sub gap tweet 5
    print("The end is near fellow gamers! Sub gap is below 1000!")
    api.update_status("It's almost over! Sub gap is below 1000! T-Series can win at any time!!!!\nThe subscriber difference between PewDiePie and T-series is only %s!!!\n\n#SubscribetoPewdiepie" % current_subgap)


  elif current_subgap < 0:
    # T-Series is winning
    tseries_is_winning = (current_subgap * (-1))

    print("This is It.")
    api.update_status("It's over!\nT-Series is %s subscribers ahead of PewDiePie!\n\n#SubscribetoPewdiepie" % tseries_is_winning)


  # update subgap to next iteration
  subgap_last_update = current_subgap

  # add subgap to array (data analysis later, maybe)
  subgap_arr.append(current_subgap)

  # saving at a document
  fobj_out.write("Subscriber gap between T_Series and Pewdiepie at " + str(actual_time) )
  fobj_out.write(str(subgap_arr[tweet_counter]))

  # updating counter
  tweet_counter = tweet_counter + 1

  # (*60 to avoid spam)
  time.sleep((int(tweet_interval)) * 60)

#-----------------------------------------------------------------------END OF BOT TWEET LOOP-----------------------------------------------------------------------------------------------------

print("This Twitter bot is not running anymore :( ")

print("Number of times you tweeted: ")
print(tweet_counter)
# Remember to clean your account everyday! Nobody likes spam!
