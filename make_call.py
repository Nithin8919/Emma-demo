#!/usr/bin/env python3
"""
Simple script to make a Twilio phone call.
"""

import os
import dotenv
from twilio.rest import Client

def make_call(to_number):
    """Make a phone call using Twilio."""
    # Load environment variables
    dotenv.load_dotenv()
    
    # Get Twilio credentials from environment variables
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM_NUMBER")
    
    if not all([account_sid, auth_token, from_number]):
        print("❌ Error: Missing Twilio credentials in environment variables")
        return False
    
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Message to be spoken during the call
        message = "Hello! This is a test call from the MED CALLER AI application. Thank you for using our service."
        
        print(f"📞 Making call to: {to_number}")
        print(f"From: {from_number}")
        print(f"Message: {message}")
        
        # Make the call
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml=f'<Response><Say>{message}</Say></Response>'
        )
        
        print(f"✅ Call initiated! Call SID: {call.sid}")
        return True
        
    except Exception as e:
        print(f"❌ Error making call: {e}")
        return False

if __name__ == "__main__":
    # Replace with your phone number in E.164 format
    PHONE_NUMBER = "+918919288376"  # Using the number you provided
    make_call(PHONE_NUMBER)
