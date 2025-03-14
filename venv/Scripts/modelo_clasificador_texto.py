from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# 1. Datos de entrenamiento (ejemplos de mensajes y sus etiquetas)
mensajes = [
    'Recuerda que tu clase de matemáticas comienztua a las 9 AM', 
    'Nuevo curso sobre programación en Python disponible', 
    'Tu sesión de tutoría de física ha sido reprogramada', 
    '¡Inscríbete ahora al curso de marketing digital!', 
    'Hoy tenemos examen de álgebra, prepárate bien',
    'Se ha publicado un nuevo módulo sobre inteligencia artificial', 
    'Recordatorio: la clase de biología es este viernes', 
    '¿Te gustaría unirte al curso de desarrollo web?', 
    'El profesor acaba de subir las notas del último examen', 
    'Importante: actualización de horarios para clases de arte'
]

etiquetas = ['recordatorio', 'curso', 'cambio', 'curso', 'recordatorio', 
             'curso', 'recordatorio', 'curso', 'notificación', 'es informativo']

#  2. Preparar datos con TfidfVectorizer (vectorización avanzada)
vectorizer = TfidfVectorizer()  
X = vectorizer.fit_transform(mensajes) 
y = etiquetas
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#  4. Crear y entrenar el modelo Naive Bayes
modelo = MultinomialNB()
modelo.fit(X_train, y_train)

#  5. Evaluar el modelo
y_pred = modelo.predict(X_test)
prec = accuracy_score(y_test, y_pred)
print(f'Precisión del modelo: {prec}')
print(classification_report(y_test, y_pred))

#  6. Clasificación de nuevos mensajes
while True:
    mensaje_usuario = input("\nIngresa un mensaje para clasificar (o escribe 'salir' para terminar): ")
    
    if mensaje_usuario.lower() == 'salir':
        print("Saliendo del programa...")
        break 
    
    # Convertimos el mensaje del usuario a formato TF-IDF
    mensaje_vec = vectorizer.transform([mensaje_usuario])
    categoria = modelo.predict(mensaje_vec)[0]
    
    print(f"El mensaje '{mensaje_usuario}' es clasificado como: {categoria}")
