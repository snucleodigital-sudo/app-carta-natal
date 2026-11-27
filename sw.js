/* Service worker de Núcleo Carta Natal: guarda la app para que funcione sin conexión.
   Al publicar cambios, sube el número de VERSION para que los teléfonos descarguen la nueva. */
const VERSION = 'v2';
const CACHE = 'carta-natal-' + VERSION;
const ARCHIVOS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './fonts/fuentes.css',
  './fonts/fraunces-latin-1.woff2',
  './fonts/fraunces-latin-ext-0.woff2',
  './fonts/inter-latin-3.woff2',
  './fonts/inter-latin-ext-2.woff2',
  './fonts/notosanssymbols-latin-6.woff2',
  './fonts/notosanssymbols-latin-ext-5.woff2',
  './fonts/notosanssymbols-symbols-4.woff2',
  './icons/favicon.svg',
  './icons/favicon-32.png',
  './icons/apple-touch-icon.png',
  './icons/icono-192.png',
  './icons/icono-512.png',
  './icons/icono-maskable-512.png',
  './lib/swisseph/src/swisseph.js',
  './lib/swisseph/wasm/swisseph.js',
  './lib/swisseph/wasm/swisseph.wasm',
  './lib/swisseph/wasm/swisseph.data.wasm',
  './data/ciudades.txt',
  './data/enciclopedia.json',
  './data/enciclopedia-pro.json'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ARCHIVOS)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(ks => Promise.all(ks.filter(k => k.startsWith('carta-natal-') && k !== CACHE).map(k => caches.delete(k))))
    .then(() => self.clients.claim()));
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== location.origin) return;
  // La página: primero internet (para ver cambios), si no hay, la copia guardada.
  if (req.mode === 'navigate') {
    e.respondWith(fetch(req).then(r => {
      if (r.ok) { const copia = r.clone(); caches.open(CACHE).then(c => c.put('./index.html', copia)); }
      return r;
    }).catch(() => caches.match('./index.html', { ignoreSearch: true })));
    return;
  }
  // Lo demás (motor, ciudades, fuentes, iconos): primero la copia guardada.
  e.respondWith(caches.match(req, { ignoreSearch: true }).then(hit => hit || fetch(req)));
});
