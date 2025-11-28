# Intentify

**Short:** Translate network security requirements written in natural language into a compact, validated intent JSON format. Powered by Hugging Face models + Streamlit.

## Why
Demonstrates NL → intent translation and schema validation - core capabilities for intent-based security. Small, explainable, and fast to demo.

## Features
- Streamlit web UI for live translation
- Uses Hugging Face text2text model (configurable)
- JSON Schema validation and error reporting
- Example prompts and prompt templates
- Export intent JSON for downstream tools

## Quick Start (local)
1. Clone:
   git clone https://github.com/zain-ramzan/intentify.git
2. Create venv and install:
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Put your HF model name in `config.py` (default: "google/flan-t5-large")
4. Run:
   streamlit run app.py

## Usage
- Type a security requirement (e.g., "Block SSH from finance VLAN to internet")
- Click Translate
- Inspect the generated intent JSON and schema validation results

## Evaluation ideas
- Exact-match rate vs. a gold intent set
- Schema validation rate (% of outputs that pass)
- Human evaluation: 5-point correctness scale

## Files
- `app.py` - Streamlit app
- `translate.py` - LLM integration + prompt templates
- `schema.json` - JSON Schema for intent format
- `requirements.txt`

## Notes
- For demo, small instruction-tuned HF models work (FLAN-T5). For better performance use an LLM accessible on GPU.
