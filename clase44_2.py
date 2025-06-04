def log_trasaction(func):
    def wrapper():
        print("1 Log de la transacccion....")
        func()
        print("3 Log terminado....")
    return wrapper


@log_trasaction
def process_payment():
    print("2 procesando pago....")

process_payment()