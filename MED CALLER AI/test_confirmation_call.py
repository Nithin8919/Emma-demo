#!/usr/bin/env python3
"""
Test script for the updated make_confirmation_call function.
"""

import sys
import os
from dotenv import load_dotenv

# Add the src directory to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(project_root, 'src')
sys.path.insert(0, src_path)

# Now import the function
try:
    from appointment_agent.tools.make_confirmation_call import make_confirmation_call
    
    def test_confirmation_call():
        """Test the confirmation call functionality."""
        # Load environment variables
        load_dotenv()
        
        # Test with your phone number
        phone_number = "+918919288376"
        
        print(f"📞 Testing confirmation call to: {phone_number}")
        print("This will make an actual phone call with the updated message.")
        
        # Additional instructions can be added here
        additional_instructions = "Please bring your ID and insurance card if applicable."
        
        # Make the call
        result = make_confirmation_call(
            phone_number=phone_number,
            instructions=additional_instructions
        )
        
        print("\n📞 Call result:")
        print(f"Status: {result.get('status')}")
        if result.get('status') == 'success':
            print(f"Call SID: {result.get('call_sid')}")
            print(f"Call status: {result.get('call_status')}")
            print("✅ You should receive a call shortly with the updated message.")
        else:
            print(f"❌ Error: {result.get('message')}")
            if 'error_type' in result:
                print(f"Error type: {result.get('error_type')}")
    
    if __name__ == "__main__":
        test_confirmation_call()
        
except ImportError as e:
    print(f"❌ Error importing make_confirmation_call: {e}")
    print("Make sure you're running this from the project root directory.")
    print("Current working directory:", os.getcwd())
    print("Python path:", sys.path)
