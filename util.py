def getTextUser(message):
    text = ""
    typeMessage = message["type"]

    if typeMessage == "text":
        text = (message["text"])["body"]
    elif typeMessage == "interactive":
        interactiveObject = message["interactive"]
        typeInteractive = interactiveObject["type"]

        if typeInteractive == "button_reply":
            text = (interactiveObject["button_reply"])["title"]
        elif typeInteractive == "list_reply":
            text = (interactiveObject["list_reply"])["title"]
        else:
            print("sin mensaje")
    else:
        print("sin mensaje")
    return text

# METODO PARA DEFINIR UN MENSAJE TIPO TEXTO


def TextMessage(text, number):
    data = {
        "messaging_product": "whatsapp",
        # "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
                # "preview_url": false,
                "body": text
        }
    }
    return data


def TextFormatMessage(number):
    data = {
        "messaging_product": "whatsapp",
        # "recipient_type": "individual",
        "to": number,
        "type": "text",
        "text": {
                # "preview_url": false,
                "body": "*informacion importante*\n_Si te llamas Thomás te gusta CR7_\n~Pero te gusta messi en secreto~\n```todo en diferentes formatos mi prro :v```"
        }
    }
    return data


def ImageMessage(number):
    data = {
        "messaging_product": "whatsapp",
        # "recipient_type": "individual",
        "to": number,
        "type": "image",
        "image": {
                # "preview_url": false,
                "link": "https://i.imgflip.com/7yzooq.jpg"
        }
    }
    return data


def AudioMessage(number):
    data = {
        "messaging_product": "whatsapp",
        # "recipient_type": "individual",
        "to": number,
        "type": "audio",
        "audio": {
                # "preview_url": false,
                "link": "https://samplelib.com/lib/preview/mp3/sample-3s.mp3"
        }
    }
    return data


def VideoMessage(number):
    data = {
        "messaging_product": "whatsapp",
        # "recipient_type": "individual",
        "to": number,
        "type": "video",
        "video": {
                # "preview_url": false,
                "link": "https://samplelib.com/lib/preview/mp4/sample-5s.mp4",
            "caption": "Prueba video"
        }
    }
    return data


def DocumentMessage(number):
    data = {
        "messaging_product": "whatsapp",
        # "recipient_type": "individual",
        "to": number,
        "type": "document",
        "document": {
                # "preview_url": false,
                "link": "https://education.github.com/git-cheat-sheet-education.pdf",
            "caption": "Github cheat Sheet Inglés"
        }
    }
    return data


def ButtonMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": number,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {
                "text": "escoge algun boto a manera de prueba"
            },
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "001",
                            "title": "si"
                        }
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "002",
                            "title": "no"
                        }
                    }
                ]
            }
        }
    }
    return data


def ListMessage(number):
    data = {
        "messaging_product": "whatsapp",
        "to": number,
        "type": "interactive",
                "interactive": {
                    "type": "list",
                    "body": {
                        "text": "✅ I have these options"
                    },
                    "footer": {
                        "text": "Select an option"
                    },
                    "action": {
                        "button": "See options",
                        "sections": [
                            {
                                "title": "Buy and sell products",
                                "rows": [
                                    {
                                        "id": "main-buy",
                                        "title": "Buy",
                                        "description": "Buy the best product your home"
                                    },
                                    {
                                        "id": "main-sell",
                                        "title": "Sell",
                                        "description": "Sell your products"
                                    }
                                ]
                            },
                            {
                                "title": "📍center of attention",
                                "rows": [
                                    {
                                        "id": "main-agency",
                                        "title": "Agency",
                                        "description": "Your can visit our agency"
                                    },
                                    {
                                        "id": "main-contact",
                                        "title": "Contact center",
                                        "description": "One of our agents will assist you"
                                    }
                                ]
                            }
                        ]
                    }
                }
    }
    return data
