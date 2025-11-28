# Intentify (Natural Language to Network Intent Translator)

A compact tool and demo that converts administrator natural-language security requirements into a simple, structured intent language (JSON). Built with Hugging Face LLMs for translation, JSON Schema for validation, and Streamlit for an interactive web demo. Purpose: show an end-to-end NL→Intent pipeline and demonstrate prompt engineering + basic assurance via schema checks.

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
