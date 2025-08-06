import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")

def make_confirmation_call(phone_number: str, instructions: str = None):
    """
    Makes a confirmation call for a dental appointment using the Twilio API.
    
    Parameters:
        phone_number (str): The recipient's phone number (E.164 format).
        instructions (str, optional): Additional instructions to include in the call.
    
    Returns:
        dict: The API response as a dictionary (call SID and status).
    """
    if not (TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN and TWILIO_FROM_NUMBER):
        return {
            "status": "error",
            "message": "Twilio credentials are not set in environment variables."
        }
    
    # Default confirmation message
    confirmation_message = (
        "Hello! This is a call from your Dental Clinic. "
        "This is a confirmation of your upcoming dental appointment. "
        "Please arrive 10 minutes before your scheduled time. "
        "If you need to reschedule or cancel, please call us at least 24 hours in advance. "
        "Thank you and we look forward to seeing you soon!"
    )
    
    # Add any additional instructions if provided
    if instructions and isinstance(instructions, str):
        confirmation_message += f" Additional instructions: {instructions}"
    
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=phone_number,
            from_=TWILIO_FROM_NUMBER,
            twiml=f'<Response><Say voice="Polly.Joanna">{confirmation_message}</Say></Response>',
            timeout=30,  # Wait up to 30 seconds for the call to be answered
            status_callback=f"{os.getenv('APP_URL', '')}/call-status",  # Optional: for call status updates
            status_events=['initiated', 'ringing', 'answered', 'completed']
        )
        
        return {
            "status": "success",
            "call_sid": call.sid,
            "call_status": call.status,
            "message": "Appointment confirmation call initiated"
        }
        
    except Exception as e:
        # Log the error and return a user-friendly message
        error_message = str(e)
        print(f"Error making call to {phone_number}: {error_message}")
        
        # Provide more specific error messages for common issues
        if "not a valid phone number" in error_message.lower():
            error_message = "The provided phone number is not valid. Please check the number and try again."
        elif "calls to this number are not allowed" in error_message.lower():
            error_message = "Calls to this number are not allowed. Please verify the number with Twilio."
            
        return {
            "status": "error",
            "message": f"Failed to make the call: {error_message}",
            "error_type": type(e).__name__
        }