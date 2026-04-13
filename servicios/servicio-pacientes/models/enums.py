from enum import Enum

class Sexo(str, Enum):
    F = "Femenino"
    M = "Masculino"
    N = "No especificado"

class EstadoCivil(str, Enum):
    SOLTERO = "Soltero/a"
    CASADO = "Casado/a"
    SEPARADO = "Separado/a"
    DIVORVIADO = "Divorciado/a"
    VIUDA = "Viudo/a"
    UNION_LIBRE = "Unión libre"