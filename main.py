#importamos mongoclient para conectar a Mongodb
from pymongo import MongoClient

# Conectamos a MongoDB
client = MongoClient("mongodb://localhost:27017")

# Crear la base de datos 'university' y las colecciones
db = client["university"]
students_collection = db["students"]
teachers_collection = db["teachers"]

# 1. Insertar 20 estudiantes
students = [
    {"name": f"Student {i+1}", "age": 20 + (i % 5), "career": f"Career {i+1}", 
     "email": f"student{i+1}@university.com", "address": f"Address {i+1}", "gender": "M" if i % 2 == 0 else "F"}
    for i in range(20)
]

students_collection.insert_many(students)

# 2. Insertar 10 profesores
teachers = [
    {"name": f"Teacher {i+1}", "age": 30 + (i % 10), "career": f"Career {i+1}", 
     "email": f"teacher{i+1}@university.com", "address": f"Address {i+1}", "gender": "M" if i % 2 == 0 else "F", 
     "profession": f"Profession {i+1}"}
    for i in range(10)
]

teachers_collection.insert_many(teachers)

# 3. Actualizar la edad de 5 estudiantes
for i in range(1, 6):
    students_collection.update_one(
        {"name": f"Student {i}"},
        {"$set": {"age": 25}}  # Actualizamos la edad
    )

# 4. Eliminar el campo 'email' de 3 profesores
for i in range(1, 4):
    teachers_collection.update_one(
        {"name": f"Teacher {i}"},
        {"$unset": {"email": ""}}  # Eliminamos el campo 'email'
    )

# 5. Mostrar la lista de los estudiantes después de las modificaciones
updated_students = students_collection.find()

print("List of students after updates:")
for student in updated_students:
    print(student)