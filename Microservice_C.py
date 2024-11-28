import zmq

print("Starting Microservice_C server...")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")
print("Microservice_C server connected successfully.")


language_hours = {}


def total_hours(request):
    """Handles the different actions sent by the main program."""
    inc_or_reset = request.get("inc_or_reset")
    language = request.get("language")

    # Initialize hours for the language if it doesn't exist in the database
    if language not in language_hours:
        language_hours[language] = 0

    if inc_or_reset == "get_hours":
        # Return the current hours for the language
        return {"hours": language_hours[language]}
    elif inc_or_reset == "reset_hours":
        # Reset the hours for the language
        language_hours[language] = 0
        return {"status": "success", "hours": 0}
    elif inc_or_reset == "add_hours":
        # Add hours to the language
        additional_hours = request.get("hours", 0)
        language_hours[language] += additional_hours
        return {"hours": language_hours[language]}


while True:
    print("Waiting for request...")
    request = socket.recv_json()
    print("Request received. Returning hours changed now.")
    response = total_hours(request)
    print("Sending response back to client.")
    socket.send_json(response)