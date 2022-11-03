from qgis.core import *
from src.main import main

QgsApplication.setPrefixPath("c:\program files\qgis 3.26.3")
qgs = QgsApplication([], True)
qgs.initQgis()

main(qgs)

qgs.exitQgis()