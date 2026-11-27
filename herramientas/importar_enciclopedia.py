#!/usr/bin/env python3
"""Pasa la lista de la enciclopedia (Excel) a la app.

Uso:  python3 herramientas/importar_enciclopedia.py RUTA/lista-enciclopedia.xlsx

Lee cada pestaña del Excel y escribe data/enciclopedia.json con:
  - el título y la versión gratuita de cada tema que ya tenga texto,
  - qué temas tienen ya versión Pro escrita (solo la marca, no el texto),
  - qué temas son "Solo Pro".

Los textos Pro NO se copian a la app a propósito: todo lo que está en la app
lo puede leer cualquiera. Se añadirán cuando existan cuentas Pro con servidor.

Una celda cuenta como texto si no es uno de los estados (Pendiente, Existe,
Parcial, No aplica). La dirección (columna "Dirección en la app") es la clave:
si cambias una en el Excel, la app tiene que calcular la misma.
"""
import json
import sys
from pathlib import Path

import openpyxl

ESTADOS = {"pendiente", "existe", "parcial", "no aplica", ""}
PESTANAS = ["Piezas", "Escenas", "Personaje en energía", "Personaje en escenario",
            "Encuentros (aspectos)", "Dignidades y energías", "Retorno solar"]


def es_texto(v):
    return isinstance(v, str) and v.strip().lower() not in ESTADOS


def main(xlsx, salida):
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    temas, total, con_gratis, con_pro = {}, 0, 0, 0
    for nombre in PESTANAS:
        ws = wb[nombre]
        filas = ws.iter_rows(min_row=1, values_only=True)
        cab = [str(c or "").strip() for c in next(filas)]
        col = {k: cab.index(k) for k in ("Dirección en la app", "Disponible en",
                                          "Versión gratuita (breve)", "Versión Pro (extendida)")}
        titulo_col = 1  # "Tema" o "Escena"
        for f in filas:
            ruta = f[col["Dirección en la app"]]
            if not ruta:
                continue
            total += 1
            gratis = f[col["Versión gratuita (breve)"]]
            pro = f[col["Versión Pro (extendida)"]]
            solo_pro = str(f[col["Disponible en"]] or "").strip().lower() == "solo pro"
            t = {}
            if es_texto(gratis) and not solo_pro:
                t["g"] = gratis.strip()
                con_gratis += 1
            if es_texto(pro):
                t["p"] = 1
                con_pro += 1
            if solo_pro:
                t["s"] = 1
            if t:
                t["t"] = str(f[titulo_col]).strip()
                temas[str(ruta).strip()] = t
    datos = {"version": 1, "temas": temas}
    Path(salida).write_text(json.dumps(datos, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"{total} temas leídos · {con_gratis} con versión gratuita · {con_pro} con versión Pro → {salida}")


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parent.parent
    xlsx = sys.argv[1] if len(sys.argv) > 1 else "/mnt/project-files/enciclopedia/lista-enciclopedia.xlsx"
    main(xlsx, raiz / "data" / "enciclopedia.json")
