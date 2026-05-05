class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        """
        Constructor de la clase CuentaBancaria.

        Args:
            titular (str): Nombre del titular de la cuenta.
            saldo_inicial (float): Saldo inicial de la cuenta (por defecto 0).
        """
        self._titular = titular
        self._saldo = 0.0  # Inicializamos a 0 para luego usar el setter con validación
        self.saldo = saldo_inicial  # Usamos la propiedad para establecer el saldo inicial

    # Propiedad titular (solo lectura)
    @property
    def titular(self):
        """Devuelve el titular de la cuenta (solo lectura)."""
        return self._titular

    # Propiedad saldo (lectura y escritura controlada)
    @property
    def saldo(self):
        """Devuelve el saldo actual de la cuenta."""
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """
        Establece el saldo de la cuenta con validación de no negatividad.
        
        Args:
            valor (float): Nuevo saldo.
            
        Raises:
            ValueError: Si el valor es negativo.
        """
        if valor < 0:
            raise ValueError("El saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, cantidad):
        """
        Incrementa el saldo si la cantidad es positiva.
        
        Args:
            cantidad (float): Cantidad a depositar.
            
        Returns:
            bool: True si el depósito fue exitoso, False en caso contrario.
        """
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """
        Disminuye el saldo solo si hay suficiente dinero y la cantidad es positiva.
        
        Args:
            cantidad (float): Cantidad a retirar.
            
        Returns:
            bool: True si el retiro fue exitoso, False en caso contrario.
        """
        if cantidad > 0 and self._saldo >= cantidad:
            self._saldo -= cantidad
            return True
        return False


# Ejemplo de uso y prueba de la clase
if __name__ == "__main__":
    # Crear una cuenta bancaria
    cuenta = CuentaBancaria("Ana Pérez", 1000)
    
    print(f"Titular: {cuenta.titular}")          # Solo lectura
    print(f"Saldo inicial: {cuenta.saldo}")      # 1000
    
    # Intentar modificar el titular (no se puede)
    # cuenta.titular = "Otro"  # Esto lanzará AttributeError
    
    # Depositar dinero
    print("\n--- Depósitos ---")
    exito = cuenta.depositar(500)
    print(f"Depósito de 500: {'Exitoso' if exito else 'Fallido'}")
    print(f"Saldo después del depósito: {cuenta.saldo}")  # 1500
    
    exito = cuenta.depositar(-200)
    print(f"Depósito de -200: {'Exitoso' if exito else 'Fallido'}")  # Fallido
    print(f"Saldo después de depósito inválido: {cuenta.saldo}")  # 1500
    
    # Retirar dinero
    print("\n--- Retiros ---")
    exito = cuenta.retirar(300)
    print(f"Retiro de 300: {'Exitoso' if exito else 'Fallido'}")
    print(f"Saldo después del retiro: {cuenta.saldo}")  # 1200
    
    exito = cuenta.retirar(2000)
    print(f"Retiro de 2000: {'Exitoso' if exito else 'Fallido'}")  # Fallido
    print(f"Saldo después de retiro inválido: {cuenta.saldo}")  # 1200
    
    # Intentar establecer saldo negativo mediante la propiedad
    print("\n--- Intento de saldo negativo ---")
    try:
        cuenta.saldo = -500
    except ValueError as e:
        print(f"Error: {e}")  # El saldo no puede ser negativo
    
    print(f"Saldo final: {cuenta.saldo}")  # 1200