from transformers import pipeline
from config import MODEL, DEVICE

_GEN = None
def get_generator():
    global _GEN
    if _GEN is None:
        _GEN = pipeline("text2text-generation", model=MODEL, device=DEVICE)
    return _GEN

PROMPT = """You are a translator that converts short natural-language network security requirements
into a compact JSON intent with keys: action, protocol, source, destination, scope.
Example:
NL: "Block SSH from finance VLAN to internet."
JSON: {"action":"deny","protocol":"ssh","source":"vlan_finance","destination":"internet","scope":"outbound"}

Now translate this:
{}

Return only valid JSON.
"""

def translate_text(text, gen=None, max_length=256):
    if gen is None:
        gen = get_generator()
    prompt = PROMPT.format(text.strip())
    out = gen(prompt, max_length=max_length, do_sample=False)[0].get("generated_text","")
    return out.strip()
