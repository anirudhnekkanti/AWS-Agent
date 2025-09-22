# AWS-Agent

AWS Bedrock Q&A Agent - Flask Web Application

This project provides a simple yet robust web-based chat application built with Python and Flask. It serves as a clean user interface to interact with a Question & Answer (Q&A) agent powered by Amazon Bedrock. The agent is designed to use a pre-configured Knowledge Base, allowing it to answer user questions based on your own private documents.

This application is designed for developers of all skill levels, follows industry-standard practices, and is easy to set up, run, and extend.
✨ Features

    Interactive Chat UI: A clean, modern, and responsive chat interface built with Tailwind CSS for a seamless user experience.

    Secure AWS Bedrock Integration: Securely connects to your Bedrock Agent to provide intelligent, context-aware answers from your knowledge base.

    Conversation Context: Maintains conversation context with the Bedrock Agent using session IDs, allowing for follow-up questions.

    Health Check Endpoint: Includes a /health endpoint to easily verify that the application server is running and operational.

    Configuration via Environment Variables: Securely manage your AWS credentials and Bedrock IDs without hardcoding sensitive information.

    Industry-Standard Project Structure: Organized code for better maintainability, readability, and scalability.

📂 Project Structure

The project follows a standard Flask application structure to keep code organized and intuitive.

/
├── app.py # Main Flask application: API endpoints and Bedrock connection logic.
├── templates/
│ └── index.html # Single-page HTML file for the chat user interface.
├── requirements.txt # A list of all Python dependencies for the project.
└── README.md # This documentation file.

📋 Prerequisites

Before you begin, ensure you have the following set up:

    Python 3.8+: Make sure Python is installed on your system.

    AWS Account: An active Amazon Web Services account.

    Configured AWS Bedrock Agent: You must have already created an Agent and a Knowledge Base in the Amazon Bedrock console.

    AWS CLI: The AWS Command Line Interface installed and configured with your credentials. You can set this up by running aws configure in your terminal.

    Required Bedrock IDs: From your AWS Bedrock console, you will need to copy the following values:

        Your Agent ID

        Your Agent Alias ID

🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

1. Clone the Repository

First, clone this project to your local machine (or simply create the files as laid out in the structure above).

# This is an example command.

git clone <your-repo-url>
cd <repository-folder-name>

2. Create and Activate a Virtual Environment

It is a best practice to use a virtual environment to manage project-specific dependencies.

# Create a virtual environment named 'venv'

python -m venv venv

# Activate the virtual environment

# On Windows:

venv\Scripts\activate

# On macOS/Linux:

source venv/bin/activate

3. Install Dependencies

Install all the required Python packages using the requirements.txt file.

pip install -r requirements.txt

4. Configure Environment Variables

This application uses environment variables to connect to your AWS Bedrock Agent securely. Do not hardcode these values in app.py.

Set the following variables in your terminal session:

# On macOS/Linux

export BEDROCK_AGENT_ID="YOUR_AGENT_ID_HERE"
export BEDROCK_AGENT_ALIAS_ID="YOUR_AGENT_ALIAS_ID_HERE"
export AWS_REGION="us-east-1" # Or the AWS region where your agent is deployed

# On Windows (Command Prompt)

set BEDROCK_AGENT_ID="YOUR_AGENT_ID_HERE"
set BEDROCK_AGENT_ALIAS_ID="YOUR_AGENT_ALIAS_ID_HERE"
set AWS_REGION="us-east-1"

    Note: Replace "YOUR_AGENT_ID_HERE" and "YOUR_AGENT_ALIAS_ID_HERE" with the actual IDs you copied from the Bedrock console.

▶️ How to Run the Application

Once the setup is complete, you can start the Flask development server with a single command:

python app.py

You will see output in your terminal indicating that the server is running, typically on http://127.0.0.1:5000.

Open your web browser and navigate to:
http://localhost:5000

You should now see the chat interface and can begin asking your agent questions!
🛠️ API Endpoints

The Flask application exposes the following API endpoints:

    GET /

        Description: Renders the main chat webpage (index.html).

        Response: 200 OK with the HTML content.
    GET /health

        Description: A health check endpoint to confirm the server is operational. Useful for monitoring.

        Response: 200 OK with a JSON object: {"status": "ok", "message": "Flask server is healthy"}.
    POST /ask

        Description: The primary endpoint for sending a user's question to the Bedrock Agent.

        Request Body (JSON):

        {
            "question": "What is the main topic of this document?",
            "sessionId": "some-unique-session-id"
        }

        Success Response (JSON):

        {
            "answer": "The agent's complete response will be here."
        }

        Error Response (JSON):

        {
            "error": "A descriptive error message."
        }
