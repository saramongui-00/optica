from enum import Enum

class AppointmentState(str, Enum):
    AGENDADA = "Agendada"
    CANCELADA = "Cancelada"
    EN_PROCESO = "En proceso"