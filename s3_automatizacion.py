import boto3
from pathlib import Path

BUCKET = "devops-bucket-481654132471"
ARCHIVO_LOCAL = "archivo_prueba.txt"
OBJETO_S3 = "pruebas/archivo_prueba.txt"

# Crear archivo local
Path(ARCHIVO_LOCAL).write_text("Archivo de prueba para S3.\n", encoding="utf-8")
print(f"Archivo local creado: {ARCHIVO_LOCAL}")

# Cliente S3
s3 = boto3.client("s3")

# Subir archivo
s3.upload_file(ARCHIVO_LOCAL, BUCKET, OBJETO_S3)
print(f"Archivo subido a s3://{BUCKET}/{OBJETO_S3}")

# Listar objetos
print("\nObjetos del bucket:")
response = s3.list_objects_v2(Bucket=BUCKET)

if "Contents" in response:
    for obj in response["Contents"]:
        print(
            f"Nombre: {obj['Key']}, "
            f"Tamaño: {obj['Size']} bytes, "
            f"Última modificación: {obj['LastModified']}"
        )
else:
    print("El bucket está vacío.")
