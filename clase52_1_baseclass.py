class BaseClass:
    def __init__(self):
        self._variable_protegida = "Valor protegido"
    
    def _metodo_protegido(self):
        print("Este es un método protegido")

base=BaseClass()
print(base._variable_protegida)
base._metodo_protegido()