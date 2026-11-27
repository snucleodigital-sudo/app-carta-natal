# app-carta-natal

App web de carta natal de **Núcleo Astrológico**: bella, sencilla y sin saturar de información.

Beta publicada en https://astrologico.nucleodigital.studio/carta/ (no indexada).

## Qué hay aquí

- `index.html`: la app completa (formulario, rueda, aspectos, energías, retorno solar, perfiles).
- `lib/swisseph/`: motor de cálculo Swiss Ephemeris compilado para el navegador (paquete npm `swisseph-wasm` 0.1.0, licencia AGPL/GPL; ver `LICENSE.txt`).
- `data/ciudades.txt`: lista de ciudades (GeoNames, población ≥ 1000) con zona horaria.
- `manifest.webmanifest`, `sw.js`, `icons/`: lo que hace la app instalable y que funcione sin conexión.
- `fonts/`: Fraunces, Inter y Noto Sans Symbols servidas desde aquí (licencia SIL OFL), para no depender de Google Fonts sin conexión.
- `.htaccess`: tipos de archivo, caché y https para Hostinger.
- `data/enciclopedia.json`: los textos gratuitos de la enciclopedia que la app muestra (se genera, no se edita a mano).
- `herramientas/`: scripts de mantenimiento. **No se suben a Hostinger.**

## Enciclopedia

Cada elemento de la carta abre su lectura: la escena (Personaje + Energía + Escenario) y, debajo, lo que la completa (encuentros, las piezas de la escena, dignidad y retrogradación). En el retorno solar, el planeta en la casa del retorno y la superposición con la casa natal.

Cada tema se busca por su **Dirección en la app** de la lista de la enciclopedia (Excel, que se guarda fuera del repositorio). Si tiene versión gratuita, se muestra; si no, aparece «Próximamente». La versión Pro solo se anuncia: sus textos no se copian a la app porque todo lo que está en la app lo puede leer cualquiera. Llegarán con las cuentas Pro.

Para actualizar los textos después de editar el Excel:

```
python3 herramientas/importar_enciclopedia.py RUTA/lista-enciclopedia.xlsx
```

y luego subir `VERSION` en `sw.js`. Si cambias una dirección en el Excel, también hay que cambiarla en `RUTA` dentro de `index.html`.

## App instalable y sin conexión

La primera visita guarda todo (unos 7 MB) en el teléfono o el ordenador. Después la app abre y calcula cartas sin internet.

**Al publicar cambios**, sube el número `VERSION` al principio de `sw.js` (v1 → v2…). Si no, quien ya la tenga instalada seguirá viendo partes antiguas.

Para que se pueda instalar necesita https y estar en la raíz de su (sub)dominio o carpeta; todas las rutas son relativas.

Todo funciona en el navegador; no hay servidor. Para probarla en local basta servir la carpeta, por ejemplo `python3 -m http.server`.

## Licencia del motor

Swiss Ephemeris se usa bajo AGPL mientras la app sea gratuita. Antes de cobrar (versión Pro) hay que decidir entre AGPL y la licencia comercial de Astrodienst.
