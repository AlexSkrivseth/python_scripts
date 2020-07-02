# The Basic code to send an sms

from twilio.rest import Client

def send_message(x):
    # These need to be changed to enviromental variables
    account_sid = 'ACfcb6b435b76307064f38cf284157dc5d'
    auth_token = 'ab5f2559a1821edfd8246993cfee0786'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
                      body = x,
                      #Phone number also need to be change to enviromental variables
                      from_ = '+17082219671',
                      to = '+12085972537'
                  )
    print(message.sid)
m = input("What do you want to say?:")
message = str(m)
send_message(message)
