import io
import fitz # PyMuPDF
import zipfile
import streamlit as st

from PIL import Image

st.title("PDF to PNG Converter", anchor=False)

uploaded_file = st.file_uploader("", type=["pdf"])
print(type(uploaded_file))
if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    with st.spinner("Converting PDF to PNGs ..."):
        pdf_bytes = uploaded_file.read() # Read uploaded PDF file as bytes
        doc = fitz.open(stream=pdf_bytes, filetype="pdf") # Open PDF in memory
        zip_buffer = io.BytesIO() # Create an in-memory buffer for ZIP file

        # Open ZIP file in append mode with compression
        with zipfile.ZipFile(zip_buffer, "a", zipfile.ZIP_DEFLATED) as zip_file:
# Loop through each page in the PDF
            for page_num in range(len(doc)):
                page = doc.load_page(page_num) # Load page by index
                pix = page.get_pixmap(dpi=200) # Render page as image at 200 DPI
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples) # Convert to PIL Image
                
# Display the PNG image in the Streamlit app
                st.image(img, caption=f"Page {page_num+1}", use_container_width=True)

                # Save the image as PNG into in-memory buffer
                img_bytes = io.BytesIO()
                img.save(img_bytes, format="PNG")

                # Write PNG file into the ZIP archive with page-specific filename
                zip_file.writestr(f"page_{page_num + 1}.png", img_bytes.getvalue())

        zip_buffer.seek(0)
        st.download_button(
            label="📥 Download All PNGs as ZIP",
            data=zip_buffer,
            file_name="converted_images.zip",
            mime="application/zip"
        )