import zmq


def language_category(language):
    language_info = {
        "Danish": "category I",
        "Dutch": "category I",
        "French": "category I",
        "Italian": "category I",
        "Norwegian": "category I",
        "Portuguese": "category I",
        "Romanian": "category I",
        "Spanish": "category I",
        "Swedish": "category I",
        "German": "category II",
        "Indonesian": "category II",
        "Malaysian": "category II",
        "Swahili": "category II",
        "Albanian": "category III",
        "Amharic": "category III",
        "Armenian": "category III",
        "Azerbaijani": "category III",
        "Bengali": "category III",
        "Bosnian": "category III",
        "Bulgarian": "category III",
        "Burmese": "category III",
        "Croatian": "category III",
        "Czech": "category III",
        "Estonian": "category III",
        "Finnish": "category III",
        "Georgian": "category III",
        "Greek": "category III",
        "Hebrew": "category III",
        "Hindi": "category III",
        "Hungarian": "category III",
        "Icelandic": "category III",
        "Kazakh": "category III",
        "Khmer": "category III",
        "Kurdish": "category III",
        "Kyrgyz": "category III",
        "Lao": "category III",
        "Latvian": "category III",
        "Lithuanian": "category III",
        "Macedonian": "category III",
        "Mongolian": "category III",
        "Nepali": "category III",
        "Pashto": "category III",
        "Persian": "category III",
        "Dari": "category III",
        "Farsi": "category III",
        "Tajik": "category III",
        "Polish": "category III",
        "Russian": "category III",
        "Serbian": "category III",
        "Sinhala": "category III",
        "Slovak": "category III",
        "Slovenian": "category III",
        "Tagalog": "category III",
        "Thai": "category III",
        "Turkish": "category III",
        "Ukrainian": "category III",
        "Urdu": "category III",
        "Uzbek": "category III",
        "Vietnamese": "category III",
        "Xhosa": "category III",
        "Zulu": "category III",
        "Arabic": "category IV",
        "Chinese": "category IV",
        "Cantonese": "category IV",
        "Mandarin": "category IV",
        "Japanese": "category IV",
        "Korean": "category IV"
    }

    formatted_language = language.lower().title()
    return language_info.get(formatted_language, "Language not found.")


def microservice_A():
    print("Starting Microservice_A server...")
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Microservice_A server connected successfully.")

    while True:
        print("Waiting for request...")
        request = socket.recv_json()
        print("Request received. Returning language category now.")
        response = language_category(request["language"])
        print("Sending response back to client.")
        socket.send_json({"category": response})


if __name__ == "__main__":
    microservice_A()