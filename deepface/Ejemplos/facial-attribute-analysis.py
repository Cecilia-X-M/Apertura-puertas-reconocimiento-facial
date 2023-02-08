from deepface import DeepFace
obj = DeepFace.analyze (img_path = "/home/cecilia/Documents/GitHub/Apertura-puertas-reconocimiento-facial/deepface/Faces/aigenerated1.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)
print("El resultado del analisis es:")
print(obj)
