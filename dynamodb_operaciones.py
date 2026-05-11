import boto3
import time

TABLE_NAME = "devops-tabla"

dynamodb = boto3.resource("dynamodb")

# Crear tabla
print("Creando tabla...")
table = dynamodb.create_table(
    TableName=TABLE_NAME,
    KeySchema=[
        {"AttributeName": "id", "KeyType": "HASH"}
    ],
    AttributeDefinitions=[
        {"AttributeName": "id", "AttributeType": "S"}
    ],
    BillingMode="PAY_PER_REQUEST"
)

# Esperar a que la tabla esté activa
table.wait_until_exists()
print("Tabla creada.")

# Referencia a la tabla
table = dynamodb.Table(TABLE_NAME)

# Insertar registro
print("Insertando registro...")
table.put_item(
    Item={
        "id": "1",
        "nombre": "Diego",
        "status": "Activo"
    }
)

# Actualizar status usando ExpressionAttributeNames
print("Actualizando registro...")
table.update_item(
    Key={"id": "1"},
    UpdateExpression="SET #st = :nuevo",
    ExpressionAttributeNames={
        "#st": "status"
    },
    ExpressionAttributeValues={
        ":nuevo": "Inactivo"
    }
)

# Eliminar registro
print("Eliminando registro...")
table.delete_item(
    Key={"id": "1"}
)

print("Proceso completado correctamente.")
