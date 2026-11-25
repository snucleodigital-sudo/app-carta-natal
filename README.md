# app-carta-natal

App web de carta natal de **Núcleo Astrológico**: bella, sencilla y sin saturar de información.

Beta publicada en https://astrologico.nucleodigital.studio/carta/ (no indexada).

## Qué hay aquí

- `index.html`: la app completa (formulario, rueda, aspectos, energías, retorno solar, perfiles).
- `lib/swisseph/`: motor de cálculo Swiss Ephemeris compilado para el navegador (paquete npm `swisseph-wasm` 0.1.0, licencia AGPL/GPL; ver `LICENSE.txt`).
- `data/ciudades.txt`: lista de ciudades (GeoNames, población ≥ 1000) con zona horaria.

Todo funciona en el navegador; no hay servidor. Para probarla en local basta servir la carpeta, por ejemplo `python3 -m http.server`.

## Licencia del motor

Swiss Ephemeris se usa bajo AGPL mientras la app sea gratuita. Antes de cobrar (versión Pro) hay que decidir entre AGPL y la licencia comercial de Astrodienst.
