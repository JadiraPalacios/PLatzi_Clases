"""Implementar una clase CuentaBancaria con un método protegido para
actualizar el saldo y un método privado para registrar las transacciones
internamente."""

class CuentaBancaria:
    def __init__(self, saldo_inicial=0):
        self._saldo = saldo_inicial  # Atributo protegido
        self.__transacciones = []  # Atributo privado

    def _actualizar_saldo(self, cantidad):
        self._saldo += cantidad

    def __registrar_transaccion(self, transaccion):
        self.__transacciones.append(transaccion)
    
    def tansaccion(self, cantidad):
        self._actualizar_saldo(cantidad)
        self.__registrar_transaccion(f"Depósito: +{cantidad}")

    def print_transacciones(self):
        print("Transacciones:", self.__transacciones)
# Ejemplo de uso
        
cuenta1 = CuentaBancaria(1000)
print("Saldo inicial:", cuenta1._saldo)  # Accediendo al atributo protegido
cuenta1.tansaccion(500)
print("Saldo depués del primer deposito:", cuenta1._saldo)  # Accediendo al atributo protegido
cuenta1.print_transacciones()  # Imprimir las transacciones realizadas
cuenta1.tansaccion(-100)  # Realizar un retiro
print("Saldo después de un retiro:", cuenta1._saldo)  # Accediendo al atributo protegido
cuenta1.print_transacciones()  # Imprimir las transacciones realizadas
# print(cuenta1.__transacciones)  # Esto generará un error porque __transacciones es privado