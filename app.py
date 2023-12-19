from flask import Flask, request
import util
import whatsappservice

app = Flask(__name__)
@app.route('/welcome', methods=['GET'])
def index():
    return "bienvenido esta vaina va viento en popa"

@app.route('/whatsapp', methods=['GET'])
def VerificarToken():
    
    try:
        accessToken = "AquiVaElTokenDeWppApi"
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if token != None and challenge != None and token == accessToken:
            return challenge
        else:
            return "", 400
    except:
        return "", 400

@app.route('/whatsapp', methods=['POST'])
def MensajeRecibido():

    try:
        body = request.get_json()
        entry = (body["entry"])[0]
        changes = (entry["changes"])[0]
        value = changes["value"]
        message = (value["messages"])[0]
        number = message["from"]

        text = util.getTextUser(message)
        GenerarMensaje(text, number)
        print(text)

        return "EVENT_RECEIVED" # siempre el objeto tiene que retornar eso, lo dice en la documentacion 
    except:
        return "EVENT_RECEIVED"
    
def GenerarMensaje(text, number):
    
    if "text" in text:
        data = util.TextMessage("Text", number)
    if "format" in text:
        data = util.TextFormatMessage(number)
    if "image" in text:
        data = util.ImageMessage(number)
    if "video" in text:
        data = util.VideoMessage(number)
    if "audio" in text:
        data = util.AudioMessage(number)
    if "document" in text:
        data = util.DocumentMessage(number)
    if "button" in text:
        data = util.ButtonMessage(number)
    if "list" in text:
        data = util.ListMessage(number)
    whatsappservice.enviarMensajeWhatsapp(data)

if(__name__ == "__main__"):
    app.run()