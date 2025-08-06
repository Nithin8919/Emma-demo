# MED CALLER AI Setup Guide

## Quick Setup (Without Bland API)

### 1. Create Environment File

Create a `.env` file in the project root with your API keys:

```bash
# Required API Keys
COMPOSIO_API_KEY=your_composio_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here

# Optional - Leave empty if not using Bland for phone calls
BLAND_API_KEY=

# Database and Redis (for Docker setup)
REDIS_URI=redis://langgraph-redis:6379
DATABASE_URI=postgres://postgres:postgres@langgraph-postgres:5432/postgres?sslmode=disable
```

### 2. Install Dependencies

```bash
# Install Python dependencies
pip install -e .

# Or using uv (recommended)
uv pip install -e .
```

### 3. Setup Composio

```bash
# Install Composio CLI
pip install composio

# Add Google Calendar
composio add googlecalendar

# Add Gmail
composio add gmail

# Enable Gmail triggers
composio triggers enable GMAIL_NEW_GMAIL_MESSAGE
```

### 4. Test Your Setup

```bash
# Run the test script
python test_setup.py
```

### 5. Start the Application

```bash
# Using Docker (recommended)
docker compose up

# Or using LangGraph CLI
langgraph up
```

### 6. Access the Application

- **LangGraph Studio**: http://localhost:8123
- **API Endpoint**: http://localhost:8123

## API Keys Required

### 1. Composio API Key
- **Get it from**: https://composio.dev
- **Used for**: Google Calendar and Gmail integration
- **Setup**: Run `composio add googlecalendar gmail`

### 2. Google API Key
- **Get it from**: https://aistudio.google.com/
- **Used for**: Gemini 2.0 Flash model
- **Setup**: Enable Gemini API in Google AI Studio

### 3. LangSmith API Key
- **Get it from**: https://smith.langchain.com/
- **Used for**: Monitoring and tracing
- **Setup**: Create account and get API key

## What Works Without Bland API

✅ **Fully Functional:**
- Appointment scheduling with Google Calendar
- Email confirmations via Gmail
- AI conversation with Gemini model
- Docker deployment

⚠️ **Mocked (No Real Calls):**
- Phone confirmation calls (logged instead of made)

## Testing the Setup

Run the test script to verify everything works:

```bash
python test_setup.py
```

Expected output:
```
🚀 Testing MED CALLER AI Setup
==================================================
🔍 Testing environment variables...
✅ COMPOSIO_API_KEY: ****************
✅ GOOGLE_API_KEY: ****************
✅ LANGSMITH_API_KEY: ****************
✅ All required environment variables are set!

🔍 Testing Composio setup...
✅ Composio tools loaded: 3 tools
   - GOOGLECALENDAR_FIND_FREE_SLOTS
   - GOOGLECALENDAR_CREATE_EVENT
   - GMAIL_CREATE_EMAIL_DRAFT

🔍 Testing Google Gemini model...
✅ Google Gemini model initialized successfully!

🔍 Testing confirmation call tool...
✅ Confirmation call tool works (mocked mode)

==================================================
📊 Test Results: 4/4 tests passed
🎉 All tests passed! Your setup is ready to run.
```

## Troubleshooting

### Common Issues:

1. **Composio Authentication Failed**
   ```bash
   composio auth
   ```

2. **Google Calendar Not Found**
   - Check calendar ID in Google Calendar settings
   - Ensure calendar is shared with the authenticated account

3. **Docker Issues**
   ```bash
   docker system prune
   docker compose down
   docker compose up
   ```

4. **Port Already in Use**
   ```bash
   # Check what's using port 8123
   lsof -i :8123
   # Kill the process or change port in compose.yaml
   ```

## Next Steps

Once setup is complete:

1. **Test the appointment agent** by sending messages
2. **Configure calendar settings** for your dental clinic
3. **Customize email templates** for confirmations
4. **Add Bland API** later for real phone calls

## Support

If you encounter issues:
1. Check the test script output
2. Verify all API keys are correct
3. Ensure Composio apps are properly configured
4. Check Docker logs: `docker compose logs` 