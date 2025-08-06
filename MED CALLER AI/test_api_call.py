#!/usr/bin/env python3
"""
Test script to interact with the LangGraph API and test the Twilio call functionality.
"""

import requests
import json
import time

BASE_URL = "http://localhost:8123"

def test_api():
    """Test the API endpoints and make a test call."""
    print("🚀 Testing LangGraph API...")
    
    # 1. Check if server is running
    try:
        response = requests.get(f"{BASE_URL}/ok", timeout=5)
        if response.status_code == 200:
            print("✅ Server is running and healthy")
        else:
            print(f"❌ Server health check failed (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Server connection failed: {e}")
        return False
    
    # 2. Create an assistant
    try:
        print("\n🔄 Creating assistant...")
        response = requests.post(
            f"{BASE_URL}/assistants",
            json={
                "graph_id": "react_agent",
                "name": "Test Call Assistant",
                "description": "Assistant for testing call functionality"
            },
            timeout=10
        )
        
        if response.status_code == 200:
            assistant = response.json()
            assistant_id = assistant["assistant_id"]
            print(f"✅ Created assistant: {assistant_id}")
        else:
            print(f"❌ Failed to create assistant: {response.text}")
            return False
            
        # 3. Create a thread
        print("\n🔄 Creating thread...")
        response = requests.post(
            f"{BASE_URL}/threads",
            json={"assistant_id": assistant_id},
            timeout=10
        )
        
        if response.status_code == 200:
            thread = response.json()
            thread_id = thread["thread_id"]
            print(f"✅ Created thread: {thread_id}")
        else:
            print(f"❌ Failed to create thread: {response.text}")
            return False
            
        # 4. Create a run with a message to trigger the call
        print("\n📞 Testing call functionality...")
        response = requests.post(
            f"{BASE_URL}/threads/{thread_id}/runs",
            json={
                "assistant_id": assistant_id,
                "input": {
                    "messages": [
                        {
                            "role": "user",
                            "content": "Please call me at +918919288376 to confirm my appointment"
                        }
                    ]
                }
            },
            timeout=30
        )
        
        if response.status_code == 200:
            print("✅ Message sent successfully")
            print("The agent should now process the request and make a call to +91 8919288376")
            print("Please check your phone for the call.")
            return True
        else:
            print(f"❌ Failed to send message: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        return False

if __name__ == "__main__":
    test_api()
