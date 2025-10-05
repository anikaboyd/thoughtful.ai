# app.py
import io
import pandas as pd
import streamlit as st

# import your sorter
from package_sorter import sort  # expects sort(width, height, length, mass)

st.set_page_config(page_title="Package Sorter", page_icon="📦", layout="centered")
st.title("📦 Package Sorter")

st.caption("Classifies packages as STANDARD, SPECIAL, or REJECTED")
with st.expander("how it works", expanded=False):
    st.write("Bulky if volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm; heavy if mass ≥ 20 kg. "
             "Both bulky and heavy → REJECTED, either one → SPECIAL, else STANDARD.")

tab1, tab2 = st.tabs(["Single package", "Batch CSV"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        width  = st.number_input("Width (cm)",  min_value=0.0, step=1.0, value=50.0)
        height = st.number_input("Height (cm)", min_value=0.0, step=1.0, value=50.0)
    with col2:
        length = st.number_input("Length (cm)", min_value=0.0, step=1.0, value=50.0)
        mass   = st.number_input("Mass (kg)",   min_value=0.0, step=0.5, value=10.0)

    if st.button("Classify"):
        try:
            label = sort(width, height, length, mass)
            st.success(f"Result: **{label}**")
        except Exception as e:
            st.error(f"Error: {e}")

with tab2:
    st.write("Upload a CSV with columns: width,height,length,mass")
    file = st.file_uploader("CSV file", type=["csv"])
    if file is not None:
        try:
            df = pd.read_csv(file)
            required = ["width", "height", "length", "mass"]
            missing = [c for c in required if c not in df.columns]
            if missing:
                st.error(f"Missing columns: {missing}")
            else:
                out = df.copy()
                out["classification"] = [
                    sort(float(w), float(h), float(l), float(m))
                    for w, h, l, m in zip(out["width"], out["height"], out["length"], out["mass"])
                ]
                st.dataframe(out, use_container_width=True)
                # download
                buf = io.StringIO()
                out.to_csv(buf, index=False)
                st.download_button("Download results CSV", buf.getvalue(), "sorted_packages.csv", "text/csv")
        except Exception as e:
            st.error(f"Error reading or processing CSV: {e}")
