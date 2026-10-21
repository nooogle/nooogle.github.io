#!/usr/bin/env python3
"""Rebuild hiragana/sw.js, the offline cache list.

Run it from the top of the repo whenever you add, rename or remove a file in hiragana/,
or change any voice clips. Pass a new version name so phones fetch the new set:

    python3 tools/make_sw.py hiragana hiragana/sw.js 2026-10-21b
"""
import sys, json, os
root, out, version = sys.argv[1], sys.argv[2], sys.argv[3]
files = ['./']
for d in ['', 'css', 'js', 'js/screens', 'vendor', 'icons', 'audio']:
    p = os.path.join(root, d)
    for f in sorted(os.listdir(p)):
        full = os.path.join(p, f)
        if os.path.isfile(full) and f.split('.')[-1] in ('html', 'css', 'js', 'mjs', 'mp3', 'png', 'webmanifest') and f != 'sw.js':
            files.append(os.path.join(d, f) if d else f)
sw = """// Offline cache for Hiragana drill: every page, script, stylesheet and voice clip is stored on the phone.
// Pages, scripts and styles are fetched fresh whenever there's signal (and the saved copy is updated),
// so code updates arrive straight away and old and new files never get mixed.
// Voice clips are taken from the cache first. Change VERSION when the clips change, or files are added.
// A preview copy (under /preview/) keeps its own caches, so it can never clear the real app's.
const PREFIX=self.registration.scope.includes('/preview/')?'hiragana-preview-':'hiragana-';
const VERSION=PREFIX+'%s';
const FILES=%s;
self.addEventListener('install',e=>{e.waitUntil(caches.open(VERSION).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith(PREFIX)&&k!==VERSION&&(PREFIX!=='hiragana-'||!k.startsWith('hiragana-preview-'))).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const req=e.request,url=new URL(req.url);
  if(req.method!=='GET'||url.origin!==location.origin)return;
  if(url.pathname.includes('/audio/')){ // clips: cache first
    e.respondWith(caches.match(req).then(hit=>hit||fetch(req)));
    return;
  }
  // everything else: network first, saved copy when offline
  e.respondWith(fetch(req).then(r=>{if(r.ok){const copy=r.clone();caches.open(VERSION).then(c=>c.put(req,copy));}return r;})
    .catch(()=>caches.match(req,{ignoreSearch:true}).then(hit=>hit||(req.mode==='navigate'?caches.match('./'):undefined))));
});
""" % (version, json.dumps(files, separators=(',', ':'), ensure_ascii=False))
open(out, 'w').write(sw)
print(len(files), 'files:', [f for f in files if not f.startswith('audio/')])
