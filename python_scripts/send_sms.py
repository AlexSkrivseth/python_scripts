# The Basic code to send an sms

from twilio.rest import Client

def send_message(x):
    # These need to be changed to enviromental variables
    account_sid = ''
    auth_token = ''

    client = Client(account_sid, auth_token)

    message = client.messages.create(
                      body = x,
                      #Phone number also need to be change to enviromental variables
                      from_ = '',
                      to = ''
                  )
    print(message.sid)
m = input("What do you want to say?:")
message = str(m)
send_message(message)
