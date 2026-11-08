"""Builds the GitHub Pages index.html (repo root) from src/index.html."""
import pathlib
src = pathlib.Path(__file__).with_name("index.html").read_text()
out = pathlib.Path(__file__).parent.parent
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#090B0E">
<meta name="description" content="Daily recovery for serious athletes: readiness, stretch routines, sleep and hydration.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Morrow">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
<script>window.MORROW_SITE=true;</script>
'''
body = src.replace('<div id="app"></div>', '</head>\n<body>\n<div id="app"></div>', 1)
tail = '''
<script>
if('serviceWorker' in navigator){addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}))}
</script>
</body>
</html>
'''
(out / 'index.html').write_text(head + body + tail)
print('built', out / 'index.html')
