# Intentify
Translate network security natural-language requirements into a compact, validated intent JSON.

## Quick start
1. Create a virtual environment and activate it.
2. Install requirements: `pip install -r requirements.txt`
3. Edit `config.py` if you want to change the model or device.
4. Run: `streamlit run app.py`

## Files
- app.py: Streamlit frontend
- translate.py: LLM integration and prompt templates
- schema.json: JSON Schema for intents
- config.py: model configuration
- requirements.txt: Python dependencies
