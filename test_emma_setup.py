#!/usr/bin/env python3
"""
EMMA Setup Test Script
Tests all components of the EMMA system for the QuantumLoopAI interview
"""

import os
import sys
import asyncio
from datetime import datetime
from dotenv import load_dotenv

def test_environment_variables():
    """Test if all required environment variables are set"""
    print("🔍 Testing Environment Variables...")
    print("-" * 50)
    
    required_vars = [
        "COMPOSIO_API_KEY",
        "GOOGLE_API_KEY", 
        "LANGSMITH_API_KEY"
    ]
    
    optional_vars = [
        "TWILIO_ACCOUNT_SID",
        "TWILIO_AUTH_TOKEN",
        "TWILIO_FROM_NUMBER"
    ]
    
    all_good = True
    
    # Check required variables
    for var in required_vars:
        value = os.getenv(var)
        if value and value != f"your_{var.lower()}_here":
            print(f"✅ {var}: {'*' * 10}")
        else:
            print(f"❌ {var}: NOT SET")
            all_good = False
    
    # Check optional variables
    for var in optional_vars:
        value = os.getenv(var)
        if value and value != f"your_{var.lower()}_here":
            print(f"✅ {var}: {'*' * 10} (Optional)")
        else:
            print(f"⚠️  {var}: NOT SET (Optional)")
    
    print()
    return all_good

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing Module Imports...")
    print("-" * 50)
    
    modules_to_test = [
        ("langchain_google_genai", "Google Gemini Integration"),
        ("langgraph", "LangGraph Framework"),
        ("composio_langgraph", "Composio Integration"),
        ("twilio", "Twilio Phone Integration"),
        ("dotenv", "Environment Variables")
    ]
    
    all_good = True
    
    for module_name, description in modules_to_test:
        try:
            __import__(module_name)
            print(f"✅ {description}: {module_name}")
        except ImportError as e:
            print(f"❌ {description}: {module_name} - {e}")
            all_good = False
    
    print()
    return all_good

def test_appointment_agent():
    """Test if the appointment agent can be imported and configured"""
    print("🔍 Testing Appointment Agent...")
    print("-" * 50)
    
    try:
        # Test imports
        from src.appointment_agent.configuration import Configuration
        from src.appointment_agent.state import AppointmentAgentState
        from src.appointment_agent.graph import appointment_agent_graph
        from src.appointment_agent.nodes.generate_response import model
        
        print("✅ Appointment Agent imports: SUCCESS")
        
        # Test configuration
        config = Configuration()
        print("✅ Configuration: SUCCESS")
        
        # Test state
        state = AppointmentAgentState()
        print("✅ State management: SUCCESS")
        
        # Test graph compilation
        if appointment_agent_graph:
            print("✅ Graph compilation: SUCCESS")
        
        # Test model initialization
        if model:
            print("✅ Model initialization: SUCCESS")
        
        print("✅ Appointment Agent: FULLY FUNCTIONAL")
        return True
        
    except Exception as e:
        print(f"❌ Appointment Agent Error: {e}")
        return False

def test_react_agent():
    """Test if the react agent can be imported and configured"""
    print("🔍 Testing React Agent...")
    print("-" * 50)
    
    try:
        # Test imports
        from src.react_agent.configuration import Configuration
        from src.react_agent.state import ReactAgentState
        from src.react_agent.graph import react_agent_graph
        
        print("✅ React Agent imports: SUCCESS")
        
        # Test configuration
        config = Configuration()
        print("✅ Configuration: SUCCESS")
        
        # Test state
        state = ReactAgentState()
        print("✅ State management: SUCCESS")
        
        # Test graph compilation
        if react_agent_graph:
            print("✅ Graph compilation: SUCCESS")
        
        print("✅ React Agent: FULLY FUNCTIONAL")
        return True
        
    except Exception as e:
        print(f"❌ React Agent Error: {e}")
        return False

def test_composio_integration():
    """Test Composio integration"""
    print("🔍 Testing Composio Integration...")
    print("-" * 50)
    
    try:
        from composio_langgraph import Action, ComposioToolSet
        
        # Test ComposioToolSet initialization
        api_key = os.getenv("COMPOSIO_API_KEY")
        if not api_key or api_key == "your_composio_api_key_here":
            print("❌ COMPOSIO_API_KEY not set")
            return False
        
        toolset = ComposioToolSet(api_key=api_key)
        print("✅ ComposioToolSet initialization: SUCCESS")
        
        # Test getting tools
        tools = toolset.get_tools(
            actions=[
                Action.GOOGLECALENDAR_FIND_FREE_SLOTS,
                Action.GOOGLECALENDAR_CREATE_EVENT,
                Action.GMAIL_CREATE_EMAIL_DRAFT
            ]
        )
        
        if tools:
            print(f"✅ Composio tools loaded: {len(tools)} tools")
            for tool in tools:
                print(f"   - {tool.name}")
        else:
            print("❌ No Composio tools loaded")
            return False
        
        print("✅ Composio Integration: FULLY FUNCTIONAL")
        return True
        
    except Exception as e:
        print(f"❌ Composio Integration Error: {e}")
        return False

def test_google_gemini():
    """Test Google Gemini model"""
    print("🔍 Testing Google Gemini Model...")
    print("-" * 50)
    
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key or api_key == "your_google_api_key_here":
            print("❌ GOOGLE_API_KEY not set")
            return False
        
        # Test model initialization
        model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
        print("✅ Model initialization: SUCCESS")
        
        # Test simple response
        response = model.invoke("Hello, can you confirm you're working?")
        if response and response.content:
            print("✅ Model response: SUCCESS")
            print(f"   Response: {response.content[:100]}...")
        else:
            print("❌ Model response: FAILED")
            return False
        
        print("✅ Google Gemini Model: FULLY FUNCTIONAL")
        return True
        
    except Exception as e:
        print(f"❌ Google Gemini Error: {e}")
        return False

def test_phone_integration():
    """Test phone call integration"""
    print("🔍 Testing Phone Call Integration...")
    print("-" * 50)
    
    try:
        from src.appointment_agent.tools.make_confirmation_call import make_confirmation_call
        
        # Test function import
        print("✅ Confirmation call function: SUCCESS")
        
        # Test function call (will be mocked if no Twilio credentials)
        result = make_confirmation_call("+1234567890", "Test appointment")
        
        if result:
            print("✅ Confirmation call function: SUCCESS")
            print(f"   Status: {result.get('status', 'unknown')}")
        else:
            print("❌ Confirmation call function: FAILED")
            return False
        
        print("✅ Phone Call Integration: FUNCTIONAL (Mocked if no Twilio)")
        return True
        
    except Exception as e:
        print(f"❌ Phone Call Integration Error: {e}")
        return False

def test_docker_setup():
    """Test Docker setup"""
    print("🔍 Testing Docker Setup...")
    print("-" * 50)
    
    try:
        import subprocess
        
        # Check if Docker is running
        result = subprocess.run(["docker", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Docker: INSTALLED")
            print(f"   Version: {result.stdout.strip()}")
        else:
            print("❌ Docker: NOT INSTALLED")
            return False
        
        # Check if docker-compose is available
        result = subprocess.run(["docker", "compose", "version"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Docker Compose: AVAILABLE")
        else:
            print("❌ Docker Compose: NOT AVAILABLE")
            return False
        
        print("✅ Docker Setup: READY")
        return True
        
    except Exception as e:
        print(f"❌ Docker Setup Error: {e}")
        return False

async def run_full_test():
    """Run all tests"""
    print("=" * 80)
    print("🏥 EMMA SYSTEM TEST")
    print("QuantumLoopAI Interview Preparation")
    print("=" * 80)
    print()
    
    # Load environment variables
    load_dotenv()
    
    tests = [
        ("Environment Variables", test_environment_variables),
        ("Module Imports", test_imports),
        ("Appointment Agent", test_appointment_agent),
        ("React Agent", test_react_agent),
        ("Composio Integration", test_composio_integration),
        ("Google Gemini Model", test_google_gemini),
        ("Phone Call Integration", test_phone_integration),
        ("Docker Setup", test_docker_setup)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n🧪 Running: {test_name}")
        print("=" * 60)
        
        try:
            if asyncio.iscoroutinefunction(test_func):
                result = await test_func()
            else:
                result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append((test_name, False))
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 TEST RESULTS SUMMARY")
    print("=" * 80)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status}: {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! EMMA is ready for the interview!")
    elif passed >= total * 0.8:
        print("⚠️  Most tests passed. Some setup may be needed.")
    else:
        print("❌ Multiple tests failed. Setup required before interview.")
    
    print("\n📋 NEXT STEPS:")
    if passed < total:
        print("1. Set up missing API keys in .env file")
        print("2. Install missing dependencies")
        print("3. Configure Composio integration")
        print("4. Test Docker deployment")
    else:
        print("1. Run: docker compose up")
        print("2. Access: http://localhost:8123")
        print("3. Test the live demo")
        print("4. Practice the interview script")
    
    print("\n🚀 Ready for QuantumLoopAI interview!")

if __name__ == "__main__":
    asyncio.run(run_full_test()) 