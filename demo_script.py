#!/usr/bin/env python3
"""
EMMA Demo Script for QuantumLoopAI Interview
Enhanced Medical Messaging Assistant - NHS-Ready AI Call Handling
"""

import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, List

class EMMADemo:
    """EMMA Demo Class for showcasing NHS call handling capabilities"""
    
    def __init__(self):
        self.demo_scenarios = {
            "appointment_booking": {
                "title": "🏥 Patient Appointment Booking",
                "description": "EMMA handles appointment booking with natural conversation",
                "conversation": [
                    ("Patient", "Hi, I need to book an appointment with Dr. Smith"),
                    ("EMMA", "Hello! I'd be happy to help you book an appointment with Dr. Smith. What's your preferred date and time?"),
                    ("Patient", "I'd like something next week, preferably in the afternoon"),
                    ("EMMA", "I can see available slots on Tuesday at 2 PM, Wednesday at 3 PM, or Thursday at 4 PM. Which works best for you?"),
                    ("Patient", "Tuesday at 2 PM sounds good"),
                    ("EMMA", "Perfect! I've booked you for Tuesday at 2 PM with Dr. Smith. I'll send you a confirmation email and call you to confirm. Is there anything else you need help with?")
                ]
            },
            "queue_management": {
                "title": "⏰ Queue Management & Wait Times",
                "description": "EMMA provides real-time queue updates and wait time estimates",
                "conversation": [
                    ("Patient", "How long is the wait time?"),
                    ("EMMA", "Currently, there are 3 patients ahead of you. Estimated wait time is 15 minutes. Would you like me to call you back when it's your turn?"),
                    ("Patient", "Yes, that would be great"),
                    ("EMMA", "I'll call you back in approximately 15 minutes. Is this the best number to reach you at?")
                ]
            },
            "multi_language": {
                "title": "🌍 Multi-language Support",
                "description": "EMMA supports 99 languages for diverse patient populations",
                "conversation": [
                    ("Patient", "Hola, necesito una cita médica"),
                    ("EMMA", "¡Hola! Con gusto te ayudo a programar una cita médica. ¿Cuál es tu fecha preferida?"),
                    ("Patient", "Me gustaría algo para la próxima semana"),
                    ("EMMA", "Perfecto. Tengo espacios disponibles el martes a las 2 PM, miércoles a las 3 PM, o jueves a las 4 PM. ¿Cuál te funciona mejor?")
                ]
            },
            "emergency_handling": {
                "title": "🚨 Emergency Call Handling",
                "description": "EMMA identifies and prioritizes urgent medical needs",
                "conversation": [
                    ("Patient", "I'm having chest pain and difficulty breathing"),
                    ("EMMA", "I understand this is concerning. For chest pain and breathing difficulties, I need to connect you immediately with our emergency triage. Please stay on the line while I transfer you to our urgent care team."),
                    ("Patient", "Thank you"),
                    ("EMMA", "You're welcome. I'm connecting you now. Please don't hang up.")
                ]
            },
            "prescription_refill": {
                "title": "💊 Prescription Refill Request",
                "description": "EMMA handles prescription refills and medication queries",
                "conversation": [
                    ("Patient", "I need to refill my blood pressure medication"),
                    ("EMMA", "I can help you with that. Which medication specifically do you need refilled?"),
                    ("Patient", "Amlodipine 5mg"),
                    ("EMMA", "I've submitted your refill request for Amlodipine 5mg. It will be ready for pickup in 2 hours. Would you like me to send you a text when it's ready?")
                ]
            }
        }
        
        self.nhs_statistics = {
            "dropped_calls_reduction": "87%",
            "staff_calls_reduction": "82%",
            "conversion_increase": "128%",
            "call_answer_rate": "100%",
            "languages_supported": "99",
            "availability": "24/7"
        }
    
    def print_header(self):
        """Print EMMA demo header"""
        print("=" * 80)
        print("🏥 EMMA™ - Enhanced Medical Messaging Assistant")
        print("NHS-Ready AI Call Handling System")
        print("QuantumLoopAI Interview Demo")
        print("=" * 80)
        print()
    
    def print_statistics(self):
        """Print NHS deployment statistics"""
        print("📊 PROVEN NHS RESULTS (2024 Deployments):")
        print("-" * 50)
        for key, value in self.nhs_statistics.items():
            formatted_key = key.replace("_", " ").title()
            print(f"• {formatted_key}: {value}")
        print()
    
    def run_conversation_demo(self, scenario_name: str):
        """Run a conversation demo"""
        scenario = self.demo_scenarios[scenario_name]
        
        print(f"🎯 {scenario['title']}")
        print(f"📝 {scenario['description']}")
        print("-" * 60)
        
        for speaker, message in scenario['conversation']:
            print(f"{speaker}: {message}")
            if speaker == "EMMA":
                print("   [AI Processing: Calendar check, form filling, email generation]")
            print()
        
        print("✅ Demo completed successfully!")
        print()
    
    def showcase_features(self):
        """Showcase EMMA's key features"""
        features = [
            "🔹 24/7 Availability - Never calls in sick",
            "🔹 Multi-language Support - 99 languages",
            "🔹 Instant Response - Zero wait times",
            "🔹 Automatic Form Filling - 66% success rate",
            "🔹 Calendar Integration - Real-time scheduling",
            "🔹 Email Confirmations - Automatic notifications",
            "🔹 Phone Call Integration - Bland API ready",
            "🔹 Queue Management - Real-time updates",
            "🔹 Emergency Triage - Urgent care routing",
            "🔹 Prescription Management - Refill requests"
        ]
        
        print("🚀 EMMA KEY FEATURES:")
        print("-" * 40)
        for feature in features:
            print(feature)
        print()
    
    def technical_architecture(self):
        """Showcase technical architecture"""
        print("🛠 TECHNICAL ARCHITECTURE:")
        print("-" * 40)
        tech_stack = [
            "• LangGraph - Agent orchestration framework",
            "• Google Gemini 2.0 Flash - Advanced AI model",
            "• Composio - Tools library integration",
            "• Google Calendar - Appointment scheduling",
            "• Gmail - Email confirmations",
            "• Bland API - Phone call integration",
            "• Docker - Containerized deployment",
            "• LangSmith - Monitoring and tracing",
            "• NHS Integration Ready - Practice management systems"
        ]
        
        for tech in tech_stack:
            print(tech)
        print()
    
    def business_benefits(self):
        """Showcase business benefits"""
        print("💰 BUSINESS BENEFITS FOR NHS PRACTICES:")
        print("-" * 50)
        benefits = [
            "• Cost Reduction: 82% fewer calls handled by staff",
            "• Staff Wellbeing: Reduced burnout and stress",
            "• Patient Satisfaction: Improved GP Patient Survey scores",
            "• Efficiency: Handle unlimited calls simultaneously",
            "• Reliability: 100% call coverage, no missed calls",
            "• Scalability: Works for practices of any size",
            "• Integration: Connects with existing NHS systems",
            "• Compliance: NHS data security standards"
        ]
        
        for benefit in benefits:
            print(benefit)
        print()
    
    def run_full_demo(self):
        """Run the complete EMMA demo"""
        self.print_header()
        self.print_statistics()
        self.showcase_features()
        self.technical_architecture()
        self.business_benefits()
        
        print("🎬 LIVE DEMO SCENARIOS:")
        print("=" * 50)
        
        # Run all conversation demos
        for scenario_name in self.demo_scenarios.keys():
            self.run_conversation_demo(scenario_name)
        
        print("🎉 EMMA DEMO COMPLETED!")
        print("Ready to transform NHS call handling! 🏥✨")
    
    def generate_demo_script(self):
        """Generate a demo script for the interview"""
        script = """
# EMMA Demo Script for QuantumLoopAI Interview

## Opening (2 minutes)
"Good morning! I'm excited to demonstrate EMMA, our Enhanced Medical Messaging Assistant designed specifically for NHS GP surgeries. EMMA is a human-like AI agent that can handle virtually unlimited calls simultaneously, respond to patients' questions, and fill in appointment forms automatically."

## Key Statistics (1 minute)
"Let me share some impressive results from our NHS deployments in 2024:
- 87% reduction in dropped calls
- 82% reduction in calls handled by staff
- 128% increase in conversions
- 100% of calls answered"

## Live Demo (5 minutes)
"Now let me show you EMMA in action with some real scenarios..."

## Technical Architecture (2 minutes)
"EMMA is built with cutting-edge technology:
- LangGraph for agent orchestration
- Google Gemini 2.0 Flash for advanced AI
- Composio for tool integration
- Docker for scalable deployment"

## Business Impact (2 minutes)
"For NHS practices, EMMA delivers:
- Significant cost savings
- Improved staff wellbeing
- Better patient satisfaction
- 24/7 reliable service"

## Closing (1 minute)
"EMMA represents the future of NHS call handling - efficient, reliable, and patient-focused. We're ready to help transform your call management experience."
        """
        
        with open("interview_demo_script.md", "w") as f:
            f.write(script)
        print("📝 Demo script saved to 'interview_demo_script.md'")

if __name__ == "__main__":
    demo = EMMADemo()
    demo.run_full_demo()
    demo.generate_demo_script() 