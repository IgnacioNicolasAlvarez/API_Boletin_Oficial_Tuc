from typing import Optional
from pydantic import BaseModel, Field


class AvisoSchema(BaseModel):
    _id: str = Field(None)
    texto: str = Field(None)
    nro_boletin: str = Field(None)
    fecha_aviso: str = Field(None)
    nro_aviso: str = Field(None)
    id_tipo_aviso: str = Field(None)
    razon_social: str = Field(None)
    id_tipo_sociedad: str = Field(None)
    titulo: str = Field(None)
    fechaConstitucion: str = Field(None)
    id_titulo: str = Field(None)
    CUIT: str = Field(None)
    capitalSocial: str = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "_id": "a123b456e789d7a8s7d8s9d87as897d89as7d987as9d87",
                "texto": "POR 5 DIAS - VICENTE TRAPANI S.A. Convocatoria. Se convoca a Asamblea General "
                         "Ordinaria de accionistas de VICENTE TRAPANI S.A. para el da viernes 19 de Junio de "
                         "2020, a las 09:00 horas a realizarse en el local social de Los Nogales - "
                         "Departamento Taf Viejo, Provincia de Tucumn, para tratar el siguiente Orden del Da: "
                         "1.- Designacin de dos accionistas para firmar el Acta de Asamblea, conjuntamente "
                         "con la Presidente. 2 - Consideracin de la prrroga para el llamado a Asamblea "
                         "dispuesta por el Directorio por no contar con la documentacin del Art. 234 de la "
                         "Ley General de Sociedades No. 19550. 3- Consideracin de los documentos a que se "
                         "refiere el Art. 234, Inc. 1 de la Ley General de Sociedades N 19.550, "
                         "correspondientes al Ejercicio N 42 cerrado el 31 de Diciembre de 2019. 4.- "
                         "Consideracin de la gestin de los miembros del Directorio y Sindicatura. Su "
                         "tratamiento y aprobacin. 5.- Consideracin de las remuneraciones al Directorio y "
                         "Sindicatura. Ratificacin por sobre los topes del Art. 261 de la Ley General de "
                         "Sociedades N 19.550, en su caso. Su aprobacin. 6.- Asignacin de Resultados. Su "
                         "Aprobacin. 7.- Fijacin del nmero de Directores Titulares y Suplentes con que "
                         "funcionar El Directorio, por tres ejercicios, por vencimiento de los mandatos de "
                         "los actuales Directores. 8.- Eleccin de los Directores Titulares y Suplentes de "
                         "acuerdo al nmero fijado segn punto anterior. 9.- Eleccin de Sndico Titular y "
                         "Suplente, por 3 (tres) ejercicios, por vencimiento de los mandatos de los actuales "
                         "Sndicos. Nota: El Directorio informa a los Sres. Accionistas que de acuerdo a las "
                         "disposiciones de la Ley General de Sociedades N 19.550 respecto a acreditar su "
                         "titularidad, atento a que todas las acciones son nominativas no endosables, "
                         "quedan exceptuados de la obligacin de depositarlas pero deben cursar comunicacin "
                         "para que se las inscriba en el Libro de Asistencia con no menos de tres das hbiles "
                         "de anticipacin a la fecha de la Asamblea. Dicha notificacin debe ser enviada a la "
                         "Direccin de la empresa en su Sede Social en Los Nogales, Departamento Taf Viejo, "
                         "Provincia de Tucumn, en das hbiles dentro del horario de 10 a 17 hs.Asimismo el "
                         "Directorio informa a los Sres. Accionistas que la documentacin relacionada con la "
                         "Asamblea a la que se convoca, est disponible en su Sede Social en Los Nogales, "
                         "Departamento Taf Viejo, de donde podrn retirarla en das hbiles en el horario de 10 "
                         "a 17 Hs. El Directorio, p. VICENTE TRAPANI S.A. Silvia Susana Trapani, Presidente. "
                         "DNI 16.526.470. E 01 y V 05/06/2020. $ 4.471,25. Aviso N 230.997.",
                "nro_boletin": "29745",
                "fecha_aviso": "2020-06-01",
                "nro_aviso": "230997",
                "id_tipo_aviso": "2",
                "razon_social": "VICENTE TRAPANI S.A",
                "id_tipo_sociedad": "2",
                "titulo": "5",
                "fechaConstitucion": "2020-06-05",
                "id_titulo": "5",
                "CUIT": "",
                "capitalSocial": "0"}
        }


class UpdateAvisoModel(BaseModel):
    texto: Optional[str]
    nro_boletin: Optional[str]
    fecha_aviso: Optional[str]
    nro_aviso: Optional[str]
    id_tipo_aviso: Optional[str]
    razon_social: Optional[str]
    id_tipo_sociedad: Optional[str]
    titulo: Optional[str]
    fechaConstitucion: Optional[str]
    id_titulo: Optional[str]
    CUIT: Optional[str]
    capitalSocial: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "texto": "POR 5 DIAS - VICENTE TRAPANI S.A. Convocatoria. Se convoca a Asamblea General "
                         "Ordinaria de accionistas de VICENTE TRAPANI S.A. para el da viernes 19 de Junio de "
                         "2020, a las 09:00 horas a realizarse en el local social de Los Nogales - "
                         "Departamento Taf Viejo, Provincia de Tucumn, para tratar el siguiente Orden del Da: "
                         "1.- Designacin de dos accionistas para firmar el Acta de Asamblea, conjuntamente "
                         "con la Presidente. 2 - Consideracin de la prrroga para el llamado a Asamblea "
                         "dispuesta por el Directorio por no contar con la documentacin del Art. 234 de la "
                         "Ley General de Sociedades No. 19550. 3- Consideracin de los documentos a que se "
                         "refiere el Art. 234, Inc. 1 de la Ley General de Sociedades N 19.550, "
                         "correspondientes al Ejercicio N 42 cerrado el 31 de Diciembre de 2019. 4.- "
                         "Consideracin de la gestin de los miembros del Directorio y Sindicatura. Su "
                         "tratamiento y aprobacin. 5.- Consideracin de las remuneraciones al Directorio y "
                         "Sindicatura. Ratificacin por sobre los topes del Art. 261 de la Ley General de "
                         "Sociedades N 19.550, en su caso. Su aprobacin. 6.- Asignacin de Resultados. Su "
                         "Aprobacin. 7.- Fijacin del nmero de Directores Titulares y Suplentes con que "
                         "funcionar El Directorio, por tres ejercicios, por vencimiento de los mandatos de "
                         "los actuales Directores. 8.- Eleccin de los Directores Titulares y Suplentes de "
                         "acuerdo al nmero fijado segn punto anterior. 9.- Eleccin de Sndico Titular y "
                         "Suplente, por 3 (tres) ejercicios, por vencimiento de los mandatos de los actuales "
                         "Sndicos. Nota: El Directorio informa a los Sres. Accionistas que de acuerdo a las "
                         "disposiciones de la Ley General de Sociedades N 19.550 respecto a acreditar su "
                         "titularidad, atento a que todas las acciones son nominativas no endosables, "
                         "quedan exceptuados de la obligacin de depositarlas pero deben cursar comunicacin "
                         "para que se las inscriba en el Libro de Asistencia con no menos de tres das hbiles "
                         "de anticipacin a la fecha de la Asamblea. Dicha notificacin debe ser enviada a la "
                         "Direccin de la empresa en su Sede Social en Los Nogales, Departamento Taf Viejo, "
                         "Provincia de Tucumn, en das hbiles dentro del horario de 10 a 17 hs.Asimismo el "
                         "Directorio informa a los Sres. Accionistas que la documentacin relacionada con la "
                         "Asamblea a la que se convoca, est disponible en su Sede Social en Los Nogales, "
                         "Departamento Taf Viejo, de donde podrn retirarla en das hbiles en el horario de 10 "
                         "a 17 Hs. El Directorio, p. VICENTE TRAPANI S.A. Silvia Susana Trapani, Presidente. "
                         "DNI 16.526.470. E 01 y V 05/06/2020. $ 4.471,25. Aviso N 230.997.",
                "nro_boletin": "29745",
                "fecha_aviso": "2020-06-01",
                "nro_aviso": "230997",
                "id_tipo_aviso": "2",
                "razon_social": "VICENTE TRAPANI S.A",
                "id_tipo_sociedad": "2",
                "titulo": "5",
                "fechaConstitucion": "2020-06-05",
                "id_titulo": "5",
                "CUIT": "",
                "capitalSocial": "0"}
        }


def response_model(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def error_response_model(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }
