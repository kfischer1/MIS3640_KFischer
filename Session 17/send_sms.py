# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACbd62608fcc1c7c46e8464b59b59a9b25"
auth_token = "YYYYYYYYYYYYYYYYYY"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+17816352371", from_="+17812857043",
                                     body="Hello from Kiley Fischer!")

print(message.sid)
