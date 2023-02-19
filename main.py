class Asiento:
  def __init__(self, color, precio, registro):
    self.color = color
    self.precio = precio
    self.registro = registro

  def cambiarColor(self, color):
    coloresPosibles = ["rojo", "verde", "amarillo", "negro", "blanco"]
    if color in coloresPosibles:
        self.color = color

class Auto:
  cantidadCreados = 0
  def __init__(self, modelo, precio, asientos, marca, motor, registro):
    self.modelo = modelo
    self.precio = precio
    self.asientos = asientos
    self.marca = marca
    self.motor = motor
    self.registro = registro
    

  def cantidadAsientos(self):
    contador = 0
    for asiento in self.asientos: 
      if isinstance(asiento, Asiento):
        contador += 1
    return contador

  def verificarIntegridad(self):
    for asiento in self.asientos:
        if ((asiento != None) and (asiento.registro != self.registro) and (self.motor.registro != self.registro)):
          return "Las piezas no son originales"
    return "Auto original"

class Motor:
  def __init__(self, numeroCilindros, tipo, registro):
    self.numeroCilindros = numeroCilindros
    self.tipo = tipo
    self.registro = registro

  def cambiarRegistro(self, registro):
    self.registro = registro

  def asignarTipo(self, tipo):
    tipoMotor = ["electrico", "gasolina"]
    if tipo in tipoMotor:
      self.tipo = tipo