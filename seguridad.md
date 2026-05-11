# Seguridad en AWS

## Medidas implementadas
- Uso exclusivo del rol LabRole.
- Perfil LabInstanceProfile asignado a las instancias EC2.
- Regla SSH restringida al CIDR 10.0.0.0/16.
- Reglas HTTP (80) y HTTPS (443) configuradas.
- Verificación del límite de concurrencia de AWS Lambda.

## Límite de concurrencia de Lambda
- Límite de cuenta en Learner Lab: 400 ejecuciones concurrentes.
- Límite recomendado por función en este proyecto: 10 ejecuciones concurrentes.
