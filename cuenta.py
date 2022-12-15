class Usuario:
    def __init__(self,nombre,apellido,cedula,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad   
class Cuenta (Usuario):
    def __init__(self, nombre, apellido, cedula, edad, saldo):
        super().__init__(nombre, apellido, cedula, edad)
        self.saldo = saldo
    def getNombre(self):
        return self.nombre 
    def getApellido(self):
        return self.apellido
    def getCedula(self):
        return self.cedula
    def getEdad(self):
        return self.edad
    def setNombre(self, nombre):
        self.nombre = nombre
    def setApellido(self, apellido):
        self.apellido = apellido
    def setCedula(self, cedula):
        self.cedula = cedula
    def setEdad(self, edad):
        self.edad = edad
    def mostrar(self,beneficio = False, pbeneficio = 0.0):
        if beneficio:
            saldoConBeneficio=self.saldo*(1+pbeneficio)
            detalles = str(f"Usuario: {self.apellido} {self.nombre}, CC {self.cedula} , saldo en cuenta: {self.saldo}, saldo mas beneficio: {saldoConBeneficio}")
        else:
            detalles = str(f"Usuario: {self.apellido} {self.nombre}, CC {self.cedula} , saldo en cuenta: {self.saldo}")
        return detalles 
    def ingresar(self,monto):
        if monto > 0:
            self.saldo=self.saldo+monto
        else:
            print("El monto a ingresar debe ser mayor a cero(0)")        
    def retirar(self,monto):
        if monto > 0:
            self.saldo=self.saldo-monto
        else:
            print("El monto a retirar debe ser mayor a cero(0)")   
class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, saldo):
        super().__init__(nombre, apellido, cedula, edad, saldo)
    def validarUsuario(self):
        if self.edad > 17 and self.edad < 28:
            return super().mostrar(True,0.05)
        else:
            self.mostrar()
b = Beneficio("javier","V",123,20,420000)
print(b.mostrar())
print(b.validarUsuario())