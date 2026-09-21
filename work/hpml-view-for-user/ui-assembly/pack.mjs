import fs from 'node:fs';
import path from 'node:path';
import { build } from 'esbuild';
const dir = '.output/public';
let html = fs.readFileSync(`${dir}/index.html`, 'utf8');
const entry = html.match(/<script type="module" src="([^"]+)"[^>]*><\/script>/)[1];
const result = await build({ entryPoints: [dir + entry], bundle: true, format: 'esm', minify: true, write: false, outfile: 'preview.js', target: 'es2022' });
for (const f of result.outputFiles) {
 if (f.path.endsWith('.js')) html = html.replace(/<script type="module" src="[^"]+"[^>]*><\/script>/, () => `<script type="module">${f.text.replaceAll('</script', '<\\/script')}</script>`);
 else if (f.path.endsWith('.css')) html = html.replace('</head>', () => `<style>${f.text}</style></head>`);
}
html = html.replace(/<link[^>]+href="\/_nuxt\/[^>]+>/g, '');
const css = fs.readFileSync(path.join(dir, '_nuxt', fs.readdirSync(`${dir}/_nuxt`).find(n => n.startsWith('entry.') && n.endsWith('.css'))),'utf8');
html = html.replace('</head>', () => `<style>${css}</style></head>`);
// Inline bundles execute after SSR markup and Nuxt payload exist.
const script = html.match(/<script type="module">[\s\S]*?<\/script>/)[0];
html = html.replace(script, '').replace('</body>', () => `${script}</body>`);
fs.writeFileSync(`${dir}/view.html`, html);
console.log(JSON.stringify({bytes:Buffer.byteLength(html),file:`${dir}/view.html`,components:['UAccordion','UButton','UInput','UBadge','UAlert']}));
