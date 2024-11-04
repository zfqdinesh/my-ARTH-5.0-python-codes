from twilio.rest import Client
import os




account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')


# Initialize Twilio client
client = Client(account_sid, auth_token)


    


def msg():
    message = client.messages.create(
        body=input("type msg"),
        from_=twilio_number,
        to=input("send to")
     )
    print(message.sid)

def call():
    call = client.calls.create(
    to=input("call to"),
    from_=twilio_number,
    url='https://handler.twilio.com/twiml/EH8541890a30b247c75131c571a3811a90'
    )
    print(call.sid)

def main():
    while 1:

        print("enter your choice")
        print("1.for msg")
        print("2.for call")
        print("q.for quit the loop")

        choice=input("enter")
        if choice=='1':
            msg()

        elif choice=='2':
            call()
        elif choice=='q':
            break
        else :
            print("invalid input")

if __name__ == '__main__':
    main()