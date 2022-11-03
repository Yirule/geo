from qgis.core import *
from .util import *

def main(qgs: QgsApplication):
    ZELI_B = defineCrs(100002, "ZELI_B", """
        +proj=eqc
        +a=2704464.91491671
        +b=2701536.2023632993
        +units=m
        +no_defs
    """)
    print(ZELI_B.srsid())
