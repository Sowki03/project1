from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

# Initialize the Flask app
app = Flask(__name__)

# Route to handle incoming voice calls
@app.route("/voice", methods=['POST'])
def voice():
    # Create a TwiML response object
    response = VoiceResponse()
    
    # Respond with a message for the caller
    response.say("This is Rohit. How can I help you?", voice='alice')
    
    # Return the TwiML response as an XML
    return str(response, mimetype='application/xml')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
