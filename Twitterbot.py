import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("2jS2a7sMU6JidvrE4eANkn4c1", "NGKt24PE0aI5MgRY26aW5C5K0yfSujJQInVpPOYVI6oV3sZqzQ")
auth.set_access_token("1217288521565630464-fjvMRgQxpzqZ6a2QlCHjMaIak5CDbp", "LGZ0tUr9mArog7SOoCiBcFQYHXiJ27PPhHZQF5v8HxPhK")

# Create API object
api = tweepy.API(auth)

#Receive Messages
response_list = api.list_direct_messages

for i in response_list:
    print(i)
