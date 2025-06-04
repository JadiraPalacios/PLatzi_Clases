class Counter:
    cuenta = 0

    @classmethod
    def incrementar(cls):
        cls.cuenta += 1
Counter.incrementar()
Counter.incrementar()
print(Counter.cuenta)