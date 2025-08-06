#!/usr/bin/env python3
"""
Test script to directly test the make_confirmation_call functionality.
"""

import os
import sys
from dotenv import load_dotenv

# Add src to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.appointment_agent.tools.make_confirmation_call import make_confirmation_call

def main():
    """Test the make_confirmation_call function directly."""
    # Load environment variables
    load_dotenv()
    
    # Test phone number - replace with your number
    phone_number = "+918919288376"
    
    print(f"📞 Testing call to: {phone_number}")
    
    # Test the call
    result = make_confirmation_call(
        phone_number=phone_number,
        instructions="This is a test call from the MED CALLER AI application. "
                   "Thank you for testing our service."
    )
    
    print("\n📞 Call result:")
    print(json.dumps(result, indent=2))
    
    if result.get("status") == "queued":
        print("\n✅ Call was successfully queued! You should receive a call shortly.")
    else:
        print("\n❌ There was an issue making the call. Please check the error message above.")

if __name__ == "__main__":
    main()
