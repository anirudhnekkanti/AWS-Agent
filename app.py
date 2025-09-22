import os
import boto3
from flask import Flask, request, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# --- AWS Bedrock Agent Configuration ---
# It's recommended to use environment variables for these settings
# for better security and flexibility.
AGENT_ID = os.environ.get("BEDROCK_AGENT_ID")
AGENT_ALIAS_ID = os.environ.get("BEDROCK_AGENT_ALIAS_ID")
# Default to us-east-1 if not set
REGION_NAME = os.environ.get("AWS_REGION", "us-east-1")

# --- Boto3 Bedrock Agent Runtime Client ---
# Create a Bedrock Agent Runtime client
try:
    bedrock_agent_runtime = boto3.client(
        'bedrock-agent-runtime',
        region_name=REGION_NAME
    )
except Exception as e:
    print(f"Error creating Boto3 client: {e}")
    bedrock_agent_runtime = None


@app.route('/')
def index():
    """
    Renders the main chat interface page.
    """
    return render_template('index.html')


@app.route('/health')
def health_check():
    """
    Provides a simple health check endpoint to confirm the server is running.
    """
    return jsonify({"status": "ok", "message": "Flask server is healthy"}), 200


@app.route('/ask', methods=['POST'])
def ask_agent():
    """
    Receives a question from the user, invokes the Bedrock Agent,
    and returns the agent's response.
    """
    # Basic validation
    if not AGENT_ID or not AGENT_ALIAS_ID:
        return jsonify({"error": "Bedrock Agent ID or Alias ID not configured on the server."}), 500

    if not bedrock_agent_runtime:
        return jsonify({"error": "Boto3 client is not initialized. Check server logs."}), 500

    data = request.get_json()
    user_question = data.get('question')
    # Use a session ID for context
    session_id = data.get('sessionId', 'default-session')

    if not user_question:
        return jsonify({"error": "Question is required."}), 400

    try:
        # Invoke the AWS Bedrock Agent
        response = bedrock_agent_runtime.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=user_question
        )

        # The response is a streaming body. We need to read and decode it.
        response_body = ""
        for event in response.get('completion', []):
            chunk = event.get('chunk', {})
            if 'bytes' in chunk:
                response_body += chunk['bytes'].decode('utf-8')

        return jsonify({"answer": response_body})

    except Exception as e:
        print(f"Error invoking Bedrock Agent: {e}")
        return jsonify({"error": f"An error occurred while communicating with the Bedrock Agent: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask app
    # Debug mode should be False in a production environment
    app.run(host='0.0.0.0', port=5000, debug=True)
