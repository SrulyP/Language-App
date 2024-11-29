import zmq

print("Starting Microservice_B server...")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")
print("Microservice_B server connected successfully.")


def language_hours(language):
    language_info = {
        "Danish": "600",
        "Dutch": "600",
        "French": "600",
        "Italian": "600",
        "Norwegian": "600",
        "Portuguese": "600",
        "Romanian": "600",
        "Spanish": "600",
        "Swedish": "600",
        "German": "900",
        "Indonesian": "900",
        "Malaysian": "900",
        "Swahili": "900",
        "Albanian": "1,100",
        "Amharic": "1,100",
        "Armenian": "1,100",
        "Azerbaijani": "1,100",
        "Bengali": "1,100",
        "Bosnian": "1,100",
        "Bulgarian": "1,100",
        "Burmese": "1,100",
        "Croatian": "1,100",
        "Czech": "1,100",
        "Estonian": "1,100",
        "Finnish": "1,100",
        "Georgian": "1,100",
        "Greek": "1,100",
        "Hebrew": "1,100",
        "Hindi": "1,100",
        "Hungarian": "1,100",
        "Icelandic": "1,100",
        "Kazakh": "1,100",
        "Khmer": "1,100",
        "Kurdish": "1,100",
        "Kyrgyz": "1,100",
        "Lao": "1,100",
        "Latvian": "1,100",
        "Lithuanian": "1,100",
        "Macedonian": "1,100",
        "Mongolian": "1,100",
        "Nepali": "1,100",
        "Pashto": "1,100",
        "Persian": "1,100",
        "Dari": "1,100",
        "Farsi": "1,100",
        "Tajik": "1,100",
        "Polish": "1,100",
        "Russian": "1,100",
        "Serbian": "1,100",
        "Sinhala": "1,100",
        "Slovak": "1,100",
        "Slovenian": "1,100",
        "Tagalog": "1,100",
        "Thai": "1,100",
        "Turkish": "1,100",
        "Ukrainian": "1,100",
        "Urdu": "1,100",
        "Uzbek": "1,100",
        "Vietnamese": "1,100",
        "Xhosa": "1,100",
        "Zulu": "1,100",
        "Arabic": "2,200",
        "Chinese": "2,200",
        "Cantonese": "2,200",
        "Mandarin": "2,200",
        "Japanese": "2,200",
        "Korean": "2,200"
    }

    language = language.lower().title()
    return language_info.get(language, "Language not found.")


while True:
    print("Waiting for request...")
    request = socket.recv_json()
    print("Request received. Returning hours now.")
    response = language_hours(request["language"])
    print("Sending response back to client.")
    socket.send_json({"hours": response})