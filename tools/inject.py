#!/usr/bin/env python3
"""Add the web-app manifest + offline service worker to the game HTML.
Usage: python3 tools/inject.py path/to/exported_artifact.html  (writes ./index.html)"""
import sys, re
src = open(sys.argv[1], encoding='utf-8').read()
src = re.sub(r'\n?<!--HIGHER-APP-->.*?<!--/HIGHER-APP-->\n?', '', src, flags=re.S)
snip = ('<!--HIGHER-APP--><link rel="manifest" href="manifest.webmanifest">'
        '<meta name="theme-color" content="#0a0e28"><link rel="icon" href="icons/icon-192.png">'
        '<link rel="apple-touch-icon" href="icons/icon-192.png">'
        '<script>if("serviceWorker" in navigator&&location.protocol==="https:")'
        'navigator.serviceWorker.register("sw.js").catch(function(){});</script><!--/HIGHER-APP-->')
i = src.lower().find('</head>')
src = src[:i] + snip + '\n' + src[i:] if i >= 0 else snip + '\n' + src
open('index.html', 'w', encoding='utf-8').write(src)
print('index.html written,', len(src), 'bytes')
