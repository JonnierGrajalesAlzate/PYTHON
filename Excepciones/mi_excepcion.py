#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"cometiste el siguiente error: {err}")
        

#crer excepciones y lanzarlas
#raise MiExcepcion("error en tal cosa")

#manejandola
try: 
    raise MiExcepcion("jajaja,sornero")
except:
    print("como vas a cometer ese error")