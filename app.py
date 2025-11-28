import streamlit as st
import json
from translate import translate_text, get_generator
from jsonschema import validate, ValidationError

st.set_page_config(page_title="Intentify", layout="wide")
st.title("Intentify — NL → Intent translator")
st.write("Type a network security requirement and get a validated intent JSON.")

nl = st.text_area("Natural language requirement", height=150,
                  value="Block SSH from the finance VLAN to the internet.")
model_override = st.text_input("Model override (optional)")

if st.button("Translate"):
    with st.spinner("Translating..."):
        gen = get_generator()
        raw = translate_text(nl, gen=gen)
        st.subheader("Raw LLM output")
        st.code(raw)
        try:
            parsed = json.loads(raw)
            st.subheader("Parsed JSON")
            st.json(parsed)
            with open("schema.json") as f:
                schema = json.load(f)
            validate(parsed, schema)
            st.success("Schema validation: OK")
        except json.JSONDecodeError as e:
            st.error(f"Could not parse JSON: {e}")
        except ValidationError as e:
            st.error(f"Schema validation failed: {e.message}")
