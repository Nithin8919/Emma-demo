#!/usr/bin/env python3
"""
Test script to verify Twilio phone call functionality.
"""

import os
import sys
import dotenv
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

def test_twilio_setup():
    """Test if Twilio credentials are properly configured."""
    print("🔍 Testing Twilio setup...")
    
    # Load environment variables
    dotenv.load_dotenv()
    
    required_vars = [
        "TWILIO_ACCOUNT_SID",
        "TWILIO_AUTH_TOKEN", 
        "TWILIO_FROM_NUMBER"
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value or value == "your_twilio_account_sid":
            missing_vars.append(var)
        else:
            print(f"✅ {var}: {'*' * len(value)}")
    
    if missing_vars:
        print(f"❌ Missing Twilio environment variables: {missing_vars}")
        return False
    else:
        print("✅ All Twilio environment variables are set!")
        return True

def test_twilio_call():
    """Test the Twilio confirmation call functionality."""
    print("\n🔍 Testing Twilio confirmation call...")
    
    try:
        from appointment_agent.tools.make_confirmation_call import make_confirmation_call
        
        # Test the function with a mock call
        result = make_confirmation_call("+1234567890", "Test confirmation call from Twilio")
        
        if result.get("status") == "success":
            print("✅ Twilio confirmation call tool works!")
            print(f"Call SID: {result.get('call_sid', 'N/A')}")
            print(f"Call Status: {result.get('call_status', 'N/A')}")
            return True
        else:
            print(f"❌ Twilio call failed: {result.get('message', 'Unknown error')}")
            return False
            
    except Exception as e:
        print(f"❌ Twilio call test error: {e}")
        return False

def main():
    """Run all Twilio tests."""
    print("🚀 Testing Twilio Phone Call Integration\n")
    print("=" * 50)
    
    # Test Twilio setup
    setup_ok = test_twilio_setup()
    
    if setup_ok:
        # Test Twilio call functionality
        call_ok = test_twilio_call()
        
        print("\n" + "=" * 50)
        if call_ok:
            print("🎉 Twilio integration is working!")
            print("\nYour phone call functionality is ready!")
            print("The appointment agent can now make real confirmation calls.")
        else:
            print("⚠️  Twilio setup is correct but call test failed.")
            print("Check your Twilio credentials and account status.")
    else:
        print("❌ Twilio setup is incomplete.")
        print("Please configure your Twilio environment variables.")

if __name__ == "__main__":
    main() 