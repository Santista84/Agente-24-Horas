from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Rota para o webhook, onde o Twilio enviará as mensagens recebidas.
@app.route("/webhook", methods=['POST'])
def webhook():
    # Recebe a mensagem enviada para o número do WhatsApp
    incoming_msg = request.form.get('Body')
    
    # Cria a resposta
    response = MessagingResponse()
    msg = response.message()
    
    # Aqui você pode adicionar lógica para responder de acordo com a mensagem recebida
    # Por exemplo, se a mensagem for "oi", a resposta será "Olá, como posso te ajudar?"
    if 'oi' in incoming_msg.lower():
        msg.body("Olá, como posso te ajudar?")
    else:
        msg.body(f"Você disse: {incoming_msg}")
    
    return str(response)  

if __name__ == "__main__":
    app.run(debug=True)
    from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.form.get('Body')
    response = MessagingResponse()
    msg = response.message()
    
    if 'oi' in incoming_msg.lower():
        msg.body("Olá! Como posso te ajudar?")
    else:
        msg.body(f"Você disse: {incoming_msg}")
    
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)