importar  openai

abierto _ api_key  =  "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"

conversación  =  "Humano: Hola, ¿quién eres? \n AI: Soy una IA creada por OpenAI. ¿Cómo puedo ayudarte hoy?"
imprimir ( conversación )

yo  =  1
mientras ( yo  !=  0 ):
    pregunta  =  entrada ( "Humano:" )
    conversación  +=  " \n Humano:"  +  pregunta  +  " \n AI:"
    respuesta  =  openai . Finalización . crear (
        motor  =  "davinci" ,
        aviso  =  conversación ,
        temperatura  =  0,9 ,
        max_tokens  =  150 ,
        top_p  =  1 ,
        frecuencia_penalización  =  0 ,
        presencia_penalización  =  0.6 ,
        detener  = [ " \n " , " Humano:" , " AI:" ]
    )
    respuesta  =  respuesta . opciones [ 0 ]. texto _ tira ()
    conversación  +=  respuesta
    imprimir ( "AI:"  +  respuesta )