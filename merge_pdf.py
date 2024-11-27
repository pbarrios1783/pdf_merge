import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Configuración de la página
st.set_page_config(page_title="Merge PDFs App", layout="centered")

# Título de la App
st.title("📎 Merge PDFs Tool")

st.write("Sube múltiples archivos PDF y combínalos en un solo documento.")

# Subida de archivos
uploaded_files = st.file_uploader("Selecciona los archivos PDF", type="pdf", accept_multiple_files=True)

if st.button("Combinar PDFs"):
    if uploaded_files:
        merger = PdfMerger()

        for uploaded_file in uploaded_files:
            merger.append(uploaded_file)

        # Guardar el archivo combinado en memoria
        merged_pdf = BytesIO()
        merger.write(merged_pdf)
        merger.close()
        merged_pdf.seek(0)

        # Descargar el archivo combinado
        st.download_button(
            label="Descargar PDF Combinado",
            data=merged_pdf,
            file_name="merged_document.pdf",
            mime="application/pdf",
        )
        st.success("¡Tus PDFs han sido combinados exitosamente!")
    else:
        st.warning("Por favor, sube al menos dos archivos PDF.")
