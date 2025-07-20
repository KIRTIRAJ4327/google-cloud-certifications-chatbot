# Google Cloud Certifications Chatbot

This is a Streamlit-based chatbot that helps users with questions about Google Cloud Certifications. The chatbot can answer questions about the certification process, exam details, project ideas, and provide information about different certification paths and benefits.

## Features

- Interactive Streamlit web interface
- AI-powered responses about Google Cloud Certifications
- Vector search capabilities with Vertex AI
- Knowledge base management

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy `env_template.txt` to `env.txt`
   - Fill in your actual API keys and project details in `env.txt`

4. Run the application:
   ```bash
   streamlit run streamlit.py
   ```

## Files

- `streamlit.py` - Main Streamlit application
- `ai.py` - AI helper functions
- `search.py` - Search functionality
- `knowledge_base.py` - Knowledge base management
- `vertexai_vectorsearch.py` - Vector search with Vertex AI
- `requirements.txt` - Python dependencies
- `env_template.txt` - Environment variables template

## Requirements

- Python 3.x
- Google Cloud Platform account with API access
- Required API keys and project configuration (see `env_template.txt`) 