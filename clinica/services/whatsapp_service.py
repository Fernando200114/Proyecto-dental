from twilio.rest import Client
from dotenv import load_dotenv
import os 

# account_sid = os.getenv('account_sid')
# auth_token = os.getenv('auth_token')

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')

load_dotenv()
client = Client(account_sid, auth_token)

def enviar_whatsapp(numero, mensaje):

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=mensaje,
        to=f"whatsapp:{numero}"
    )

    return message.sid