from flask import Flask, render_template,jsonify
from flask import flash,request	
from flask_cors import CORS
import json

app=Flask(__name__,static_folder='./frontend/dist/static',template_folder='./frontend/dist')

cors=CORS(app,resources={r"/api/*": {"origins":"*"}} )
app.secret_key="super secret key"

@app.route('/api/chatbot')
def mensaje():
    return jsonify('Hola desde python como nuevo mensaje')



#estas librearrias son para el uso de machine learning o inteligencia artificial
import os.path as path
import nltk
#esto permite transformar palabras  osea quita algunas letras demas para que sea entendible a los datos que hay en el json
from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer()
#es una libreria de python
import numpy
import tflearn 
# libreroa conocida creaada por brain google
import tensorflow
import json 
# se usa para aleatoriedad , en este programa se suara para escger una respuesta aleatoria
import random
import pickle
#nltk.download('punkt')
#abrimos el archivo json con nombre de archivo con el utf-8 permitira palabras ya sea con tildes y otros caracteres
with open("contenido.json" ,encoding='utf-8') as  archivo:
   datos=json.load(archivo)
#intentar cargar esas variable sy si no cargan es porque no existe el archivo y crearemos lo identado de except
try:
	with open("variables.pickle","rb") as archivoPickle:
		palabras,tags,entrenamiento,salida=	pickle.load()

except:
	palabras=[]
	tags=[]
	auxX=[]
	auxY=[]
	#esta es la línea comentada nos permite trabajar con lenguaje natural , 
	 #  	lo separa en palabras, nos separar en tokens 
	  # 	es decir en palabras , reconocera los puntos
	   #	 especiales como signo de admiracion y exclamacion
	for contenido in datos["contenido"]:
	   for patrones in contenido ["patrones"]:
	   	     #esta variable nos va ah permitir por el momento solo la palabra
	   	     #word_tokenize toamra la frase y la separar en palabras 
	       auxPalabra =nltk.word_tokenize(patrones)
	       #a las palanras le añadimos otras palabras
	       palabras.extend(auxPalabra)
	       #aqui seran los tokens de entrada
	       auxX.append(auxPalabra)
	       #aqui agregamos los tags de nuestro contenido
	       auxY.append(contenido["tag"])

	       if contenido ["tag"] not in tags:
	       	   tags.append(contenido["tag"])
	#usaremos stemmer y su metodo stem le pasaremos una palabra en miniscula "lower" recorremos toda nuestra lista de palabras
	#con el  "for"  , siempre y cuando sea diferente del signo de pregunta
	#dependediendo de la palabras stemmer le quitara algunas letras  aqui mas explicado este metodo ->https://www.nltk.org/howto/stem.html
	palabras=[stemmer.stem(w.lower()) for w in palabras if w!="?"]
	#aqui ordenamos las palabras
	#sorted nos regresa una lista ordenan
	palabras = sorted(list(set(palabras)))
	#Nos devuelve los tags ordenados
	tags=sorted(tags)

	entrenamiento=[]
	salida=[]

	salidaVacia=[0 for _ in range(len(tags))]
	#enumerate nos permite tener la palabra y el indice es decir la lista con indices
	for x, documento in enumerate(auxX):
		cubeta=[]
		auxPalabra=[stemmer.stem(w.lower()) for w in documento]
	   #aqui usaremos la cubeta[]
		for w in palabras:
	    	 if w in auxPalabra:
	    		#añadimos a la cubeta siu es elemento esta
	    	    	cubeta.append(1)
	    	 else:
	    		    cubeta.append(0)

		filaSalida=salidaVacia[:]
	     #vamos a obtenrer el indice 
	#obtenemos el indeice de los tags repetidos, ingresaremos por cada indice un 1
		filaSalida[tags.index(auxY[x])]=1
		entrenamiento.append(cubeta)
		salida.append(filaSalida)

	#creamos nuestros datos para el entrenamiento de la red neuronal tanto las caracterisitcas como las etiquetas entrenamiento y salida respectivamente
	entrenamiento= numpy.array(entrenamiento)
	salida=numpy.array(salida)
with open("variables.pickle","wb") as archivoPickle:
    pickle.dump((palabras,tags,entrenamiento,salida),archivoPickle)



#resetea nuestro espacio de trabajo para empezar el incio de entrenamiento
tensorflow.reset_default_graph()
#la entrada de datos para ele entrenamiento se detalla la longitud ya sea una matris o vector
red=tflearn.input_data(shape=[None,len(entrenamiento[0])])
#la cantidad de 10 enuronas es de manera relativa depende de  uno mismo cuantas neuronas quiere ponerlo para que entrene
#ademas le podemos poner el numero de capas considerables
red=tflearn.fully_connected(red,10)
red=tflearn.fully_connected(red,10 	)
#aqui usamos la salida que este caso son el numero de clases o tema a quese abarca como saludo ,despedida,etc 
#y la funcion de activacion softmax sirve para que nos devuelva un 1 a la mayor posibilidad o presicion de clase y al resto devolvera 0
red=tflearn.fully_connected(red,len(salida[0]),activation='softmax')
#nos permitira ver que tan eficas o preciso es una clasificacion
red=tflearn.regression(red)
#aqui moldeamos al la red de neuronas
modelo=tflearn.DNN(red)
#para evitar la carga y entrenamiento de la neurona y no perder tiempo hacemos un try para cargar si el modelo entrenado ya existe


if path.exists("modelo.tflearn.meta"):
	modelo.load("modelo.tflearn")
else:
	#aqui entrenamos a la red neuronal
	#el numero de epocas tambien es importante para que itere
	#batch_size son la cantidad de entradas que usara por cada iteracion en este caso son palabras o tokens
	#el show_metrics es para que muestre el valor de presicion de entrenamiento
    modelo.fit(entrenamiento,salida,n_epoch=1500, batch_size=80,show_metric=True)
    modelo.save("modelo.tflearn")

def mainBot(mensaje):
	#while True:
		#entrada=input("Tu: ")
		cubeta=[0 for _ in range(len(palabras))]
		#se encarga de sepaar las palabras o frases que escribiremos 
		entradaProcesada= nltk.word_tokenize(mensaje)
		#convertimso a palabra en minusculas para que no halla problemas  y a entrada le ingresamos todo lo tokenizado o 
		#que mejr dicho que ah sido enlistado en palabras
		entradaProcesada=[stemmer.stem(palabra.lower()) for palabra in entradaProcesada]
        #ahora identificamos palabra por palabra
		for palabraIndividual in entradaProcesada:
		             #enumaermos las lista de palabras
		    for i,palabra in enumerate(palabras):
		        if palabra==palabraIndividual:
		        	  cubeta[i] =1
		resultados= modelo.predict([numpy.array(cubeta)])
		print(resultados)
		resultadosIndices= numpy.argmax(resultados)
		tag=tags[resultadosIndices]

		for tagAux in datos["contenido"]:
		   	 if tagAux['tag']==tag:
		   	 	respuesta=tagAux["respuestas"]

		return random.choice(respuesta)




@app.route('/api/mensaje_chatbot',methods=['POST'])
def mensaje_chatbot():
    #mensajillo= json.loads(request.json)
    data = request.get_json()
    #received_json_data = json.loads(request.body.decode("utf-8"))
    mensajillo=data['user']
    mensaje_respuesta = mainBot(mensajillo)
    data={'user':mensajillo ,
            'boot': mensaje_respuesta
    }
    return jsonify( data) 

@app.route('/',defaults={'path':''})

@app.route('/<path:path>')
def render_vue(path):
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)