import tweepy
import time
# Authenticate to Twitter
auth = tweepy.OAuthHandler("2jS2a7sMU6JidvrE4eANkn4c1", "NGKt24PE0aI5MgRY26aW5C5K0yfSujJQInVpPOYVI6oV3sZqzQ")
auth.set_access_token("1217288521565630464-20kw81QyQXr956tHfGMtswQeqdBXXV", "FyUuBHgR1i34k1sXamoaBDsKkHIXdw6146PyJEACh0iOW")

# Create API object
api = tweepy.API(auth)

#Receive Messages
while (1 == 1):
    messages  = api.list_direct_messages()
    for i in messages:
        if i.message_create["target"]["recipient_id"]== "1217288521565630464":
                api.send_direct_message(i.message_create["sender_id"],i.message_create["message_data"]["text"])
                print(i.message_create["message_data"]["text"])
                api.destroy_direct_message(i.id)
                time.sleep(108)
    


#1217288521565630464