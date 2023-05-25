from MainService import MainService

_ms = MainService()

input("Aperte qualquer tecla para continuar ")
while(True):
    userText = _ms.getText()
    
    if userText.startswith("pergunte "):

        response = _ms.makeQuestion(userText)
        _ms.getAudio("Veja alguns resultados que eu encontrei")
        print("Resposta: " + response)


