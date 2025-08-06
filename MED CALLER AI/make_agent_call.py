#!/usr/bin/env python3
"""
Script to interact with the appointment agent and trigger a call.
"""

import requests
import json

BASE_URL = "http://localhost:8123"

def create_assistant():
    """Create an assistant for the appointment agent."""
    payload = {
        "graph_id": "react_agent",
        "name": "Appointment Caller",
        "description": "Assistant for making appointment confirmation calls"
    }
    
    response = requests.post(f"{BASE_URL}/assistants", json=payload, timeout=10)
    response.raise_for_status()
    return response.json()["assistant_id"]

def create_thread(assistant_id):
    """Create a new conversation thread."""
    response = requests.post(
        f"{BASE_URL}/threads",
        json={"assistant_id": assistant_id, "metadata": {}},
        timeout=10
    )
    response.raise_for_status()
    return response.json()["thread_id"]

def send_message(thread_id, message):
    """Send a message to the agent and get the response."""
    response = requests.post(
        f"{BASE_URL}/threads/{thread_id}/messages",
        json={"content": message},
        timeout=30
    )
    response.raise_for_status()
    return response.json()

def main():
    """Main function to run the appointment call."""
    try:
        print("🚀 Setting up appointment call...")
        
        # Create assistant and thread
        assistant_id = create_assistant()
        thread_id = create_thread(assistant_id)
        
        # Start the conversation
        print("🤖 Assistant: Hello! I can help you schedule an appointment. "
              "Please provide your name and preferred date and time.")
        
        # Simulate a conversation that would lead to a call
        messages = [
            "I'd like to schedule an appointment",
            "My name is Nitin",
            "I'm available tomorrow at 2 PM",
            "Please call me at +91 8919288376 to confirm"
        ]
        
        for msg in messages:
            print(f"\n👤 You: {msg}")
            response = send_message(thread_id, msg)
            
            # Print the agent's response
            if "messages" in response:
                for msg in response["messages"]:
                    if msg["role"] == "assistant":
                        print(f"🤖 Assistant: {msg['content']}")
        
        print("\n✅ Check your phone! The agent should be calling you shortly.")
        
    except Exception as e:
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
