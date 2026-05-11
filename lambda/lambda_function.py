import json
import random

def lambda_handler(event, context):
    mensajes = [
        "Microservicio DevOps funcionando correctamente.",
        "Despliegue exitoso en AWS Lambda.",
        "API Gateway conectado con Lambda.",
        "Proyecto DevOps ejecutándose en la nube.",
        "Automatización y microservicios en AWS."
    ]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "mensaje": random.choice(mensajes),
            "servicio": "microservicio-devops"
        })
    }
