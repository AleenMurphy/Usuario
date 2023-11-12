class Usuario:
    def __init__(self, nombre, balance=0):
        self.nombre = nombre
        self.balance = balance

    def hacer_retiro(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Error: No se puede realizar el retiro.")
            return False

    def hacer_depósito(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Depósito exitoso. Nuevo balance de {self.nombre}: ${self.balance}")
        else:
            print("Error: Monto de depósito no válido.")

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.nombre}, Balance: ${self.balance}")

    def transferir_dinero(self, otro_usuario, amount):
        if self.hacer_retiro(amount):
            otro_usuario.hacer_depósito(amount)
            print(f"Transferencia exitosa. {self.nombre} ha transferido ${amount} a {otro_usuario.nombre}")
        else:
            print("Error: No se puede realizar la transferencia.")

# Crear 3 instancias de la clase Usuario
usuario1 = Usuario("Guido van Rossum")
usuario2 = Usuario("Gerardo")
usuario3 = Usuario("Roberta")

# Usuario 1 realiza depósitos y giros
usuario1.hacer_depósito(100)
usuario1.hacer_depósito(200)
usuario1.hacer_depósito(300)
usuario1.hacer_retiro(50)
usuario1.mostrar_balance_usuario()

# Usuario 2 realiza depósitos y giros
usuario2.hacer_depósito(200)
usuario2.hacer_depósito(200)
usuario2.hacer_retiro(10)
usuario2.hacer_retiro(5)
usuario2.mostrar_balance_usuario()

# Usuario 3 realiza depósitos y giros
usuario3.hacer_depósito(300)
usuario3.hacer_retiro(20)
usuario3.hacer_retiro(10)
usuario3.hacer_retiro(50)
usuario3.mostrar_balance_usuario()

# Usuario 1 transfiere dinero al Usuario 3
usuario1.transferir_dinero(usuario3, 25)

# Mostrar balances después de la transferencia
usuario1.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()
