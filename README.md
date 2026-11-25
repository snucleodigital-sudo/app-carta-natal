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

## App instalable y sin conexión

La primera visita guarda todo (unos 7 MB) en el teléfono o el ordenador. Después la app abre y calcula cartas sin internet.

**Al publicar cambios**, sube el número `VERSION` al principio de `sw.js` (v1 → v2…). Si no, quien ya la tenga instalada seguirá viendo partes antiguas.

Para que se pueda instalar necesita https y estar en la raíz de su (sub)dominio o carpeta; todas las rutas son relativas.

Todo funciona en el navegador; no hay servidor. Para probarla en local basta servir la carpeta, por ejemplo `python3 -m http.server`.

## Licencia del motor

Swiss Ephemeris se usa bajo AGPL mientras la app sea gratuita. Antes de cobrar (versión Pro) hay que decidir entre AGPL y la licencia comercial de Astrodienst.
