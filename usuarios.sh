UARIO="devops_user"

echo "Creando usuario..."
sudo useradd $USUARIO

echo "Asignando contraseña..."
echo "$USUARIO:DevOps123" | sudo chpasswd

echo "Agregando usuario al grupo docker..."
sudo usermod -aG docker $USUARIO

echo "Asignando permisos sobre environment..."
sudo chown -R $USUARIO:$USUARIO ~/environment

echo "Restaurando permisos a ec2-user..."
sudo chown -R ec2-user:ec2-user ~/environment

echo "Proceso completado."
