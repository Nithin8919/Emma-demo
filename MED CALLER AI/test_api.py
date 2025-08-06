#!/usr/bin/env python3
"""
Test script to verify the LangGraph API is working.
"""

import requests
import json

def test_api():
    """Test the LangGraph API endpoints."""
    base_url = "http://localhost:8123"
    
    print("🔍 Testing LangGraph API...")
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/ok", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running and healthy")
            return True
        else:
            print(f"❌ Server health check failed (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Server connection failed: {e}")
        return False

def test_react_agent():
    """Test the react_agent graph."""
    base_url = "http://localhost:8123"
    
    print("\n🔍 Testing react_agent...")
    
    # First, create an assistant
    assistant_payload = {
        "graph_id": "react_agent",
        "name": "Test React Agent",
        "description": "Test assistant for react_agent"
    }
    
    try:
        # Create assistant
        response = requests.post(
            f"{base_url}/assistants",
            json=assistant_payload,
            timeout=10
        )
        
        if response.status_code == 200:
            assistant = response.json()
            assistant_id = assistant["assistant_id"]
            print(f"✅ Created assistant: {assistant_id}")
            
            # Create a thread
            thread_payload = {
                "metadata": {"test": "true"}
            }
            
            response = requests.post(
                f"{base_url}/threads",
                json=thread_payload,
                timeout=10
            )
            
            if response.status_code == 200:
                thread = response.json()
                thread_id = thread["thread_id"]
                print(f"✅ Created thread: {thread_id}")
                
                # Test the assistant with a message
                run_payload = {
                    "assistant_id": assistant_id,
                    "input": {
                        "messages": [
                            {"role": "user", "content": "Hello! Can you help me?"}
                        ]
                    }
                }
                
                response = requests.post(
                    f"{base_url}/threads/{thread_id}/runs/wait",
                    json=run_payload,
                    timeout=30
                )
                
                if response.status_code == 200:
                    print("✅ react_agent is working!")
                    print("Response received successfully")
                    return True
                else:
                    print(f"❌ react_agent run failed (Status: {response.status_code})")
                    print(f"Response: {response.text}")
                    return False
            else:
                print(f"❌ Thread creation failed (Status: {response.status_code})")
                return False
        else:
            print(f"❌ Assistant creation failed (Status: {response.status_code})")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ react_agent test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🚀 Testing MED CALLER AI API\n")
    print("=" * 50)
    
    # Test basic API
    api_working = test_api()
    
    if api_working:
        # Test react_agent
        agent_working = test_react_agent()
        
        print("\n" + "=" * 50)
        if agent_working:
            print("🎉 All tests passed! Your MED CALLER AI is working!")
            print("\nYou can now:")
            print("1. Access the API at http://localhost:8123")
            print("2. Use the react_agent for general assistance")
            print("3. Add the appointment_agent later for scheduling")
            print("\nTo use the API:")
            print("- Create assistants: POST /assistants")
            print("- Create threads: POST /threads")
            print("- Run assistants: POST /threads/{thread_id}/runs/wait")
        else:
            print("⚠️  API is running but agent test failed")
    else:
        print("❌ API is not working properly")

if __name__ == "__main__":
    main() 