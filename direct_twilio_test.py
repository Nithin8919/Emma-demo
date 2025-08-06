#!/usr/bin/env python3
"""
Direct test of Twilio call functionality.
"""

import os
from dotenv import load_dotenv
from twilio.rest import Client

def make_call():
    """Make a test call using Twilio."""
    # Load environment variables
    load_dotenv()
    
    # Get Twilio credentials
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    from_number = os.getenv("TWILIO_FROM_NUMBER")
    to_number = "+918919288376"  # Your number
    
    if not all([account_sid, auth_token, from_number]):
        print("❌ Error: Missing Twilio credentials in .env file")
        print("Please ensure the following are set in your .env file:")
        print("- TWILIO_ACCOUNT_SID")
        print("- TWILIO_AUTH_TOKEN")
        print("- TWILIO_FROM_NUMBER")
        return
    
    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)
        
        # Message to be spoken during the call
        message = "Hello! This is a test call from the MED CALLER AI application. Thank you for testing our service."
        
        print(f"📞 Making call to: {to_number}")
        print(f"From: {from_number}")
        print(f"Message: {message}")
        
        # Make the call
        call = client.calls.create(
            to=to_number,
            from_=from_number,
            twiml=f'<Response><Say>{message}</Say></Response>'
        )
        
        print(f"\n✅ Call initiated! Call SID: {call.sid}")
        print("You should receive a call shortly.")
        
    except Exception as e:
        print(f"❌ Error making call: {e}")
        print("\nTroubleshooting steps:")
        print("1. Verify your Twilio credentials in the .env file")
        print("2. Ensure your Twilio account has sufficient balance")
        print("3. Check that the 'from' number is a valid Twilio number")
        print("4. Verify that the 'to' number is verified in your Twilio account")

if __name__ == "__main__":
    print("🚀 Testing Twilio Call Functionality")
    print("-" * 40)
    make_call()
