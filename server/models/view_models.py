from pydantic import BaseModel, Field
from datetime import date


class VM_aviso_fecha(BaseModel):
    fecha_desde : str
    fecha_hasta : str