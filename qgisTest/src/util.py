from qgis.core import *

def defineCrs(id: int, name: str, proj: str):
    reg = QgsCoordinateReferenceSystemRegistry()

    crs = QgsCoordinateReferenceSystem()
    crs.createFromProj(proj)
    reg.updateUserCrs(id, crs, name)
    return crs.fromSrsId(id)