#!/usr/bin/env python3
"""
Test script to verify the project setup and basic functionality.
Run this to check if all required APIs are configured correctly.
"""

import os
import sys
import dotenv
from pathlib import Path

# Add src to path
sys.path.append(str(Path(__file__).parent / "src"))

def test_environment_variables():
    """Test if all required environment variables are set."""
    print("🔍 Testing environment variables...")
    
    required_vars = [
        "COMPOSIO_API_KEY",
        "GOOGLE_API_KEY", 
        "LANGSMITH_API_KEY"
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if not value or value == "your_api_key_here":
            missing_vars.append(var)
        else:
            print(f"✅ {var}: {'*' * len(value)}")
    
    if missing_vars:
        print(f"❌ Missing or invalid environment variables: {missing_vars}")
        return False
    else:
        print("✅ All required environment variables are set!")
        return True

def test_composio_setup():
    """Test Composio setup."""
    print("\n🔍 Testing Composio setup...")
    
    try:
        from composio_langgraph import ComposioToolSet, Action
        
        # Initialize ComposioToolSet
        api_key = os.getenv("COMPOSIO_API_KEY")
        composio_toolset = ComposioToolSet(api_key=api_key)
        
        # Test getting tools
        tools = composio_toolset.get_tools(
            actions=[
                Action.GOOGLECALENDAR_FIND_FREE_SLOTS,
                Action.GOOGLECALENDAR_CREATE_EVENT,
                Action.GMAIL_CREATE_EMAIL_DRAFT
            ]
        )
        
        print(f"✅ Composio tools loaded: {len(tools)} tools")
        for tool in tools:
            print(f"   - {tool.name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Composio setup failed: {e}")
        return False

def test_google_model():
    """Test Google Gemini model access."""
    print("\n🔍 Testing Google Gemini model...")
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
        print("✅ Google Gemini model initialized successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Google Gemini model failed: {e}")
        return False

def test_confirmation_call():
    """Test the confirmation call tool (without Bland API)."""
    print("\n🔍 Testing confirmation call tool...")
    
    try:
        from appointment_agent.tools.make_confirmation_call import make_confirmation_call
        
        # Test the function
        result = make_confirmation_call("+1234567890", "Test confirmation call")
        
        if result.get("status") == "success":
            print("✅ Confirmation call tool works (mocked mode)")
            return True
        else:
            print(f"❌ Confirmation call tool failed: {result}")
            return False
            
    except Exception as e:
        print(f"❌ Confirmation call tool error: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Testing MED CALLER AI Setup\n")
    print("=" * 50)
    
    # Load environment variables
    dotenv.load_dotenv()
    
    tests = [
        test_environment_variables,
        test_composio_setup,
        test_google_model,
        test_confirmation_call
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your setup is ready to run.")
        print("\nNext steps:")
        print("1. Run: docker compose up")
        print("2. Access: http://localhost:8123")
    else:
        print("⚠️  Some tests failed. Please check the configuration.")
        print("\nMake sure you have:")
        print("- COMPOSIO_API_KEY set and apps configured")
        print("- GOOGLE_API_KEY set")
        print("- LANGSMITH_API_KEY set")

if __name__ == "__main__":
    main() 