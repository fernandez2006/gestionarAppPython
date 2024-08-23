from sqlalchemy import create_engine, event 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

#conexion a la  BD
#NOMBREBD
dataBaseName="gestionbd"

#usuarioBD
userName="root"
#contraseña del usuario
userPassword=""

#puerto de conexion 
conexionPort="3306"

#servidor conexion
serverConexion="localhost"

#creando la conexion 
connectionToDataBase=f"mysql+mysqlconnector://{userName}:{userPassword}@{serverConexion}:{conexionPort}/{dataBaseName}"

Engine=create_engine(connectionToDataBase)
sessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=Engine)