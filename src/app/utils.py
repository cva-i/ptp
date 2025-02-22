from pdf2image import convert_from_bytes
import base64
from io import BytesIO
from PIL import Image

def image_to_base64(image: Image.Image) -> str:
    """
    Converts a PIL Image to a base64 encoded PNG string.
    """
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def pdf_to_pngs(pdf_content: bytes, dpi: int = 200) -> list[str]:
    """
    Converts PDF content to a list of base64 encoded PNG images.
    """
    images = convert_from_bytes(
        pdf_content,
        dpi=dpi,
        fmt='png',
    )
    return [image_to_base64(image) for image in images]
