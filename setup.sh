o "Actualizando paquetes..."
sudo yum update -y

echo "Instalando dependencias..."
sudo yum install git -y
sudo yum install vim -y
sudo yum install docker -y
sudo yum install python3 -y
sudo yum install cronie -y

echo "Instalando boto3..."
pip3 install boto3

echo "Iniciando Docker..."
sudo service docker start

echo "Configuración completada."
