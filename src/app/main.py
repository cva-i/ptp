from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from typing import List
from app.utils import pdf_to_pngs
import base64
import yaml

app = FastAPI(
    title="PDF to PNG Converter",
    description="API for converting PDFs to PNG images",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc"
)

class PDFRequest(BaseModel):
    pdf: str
    dpi: int = 200

@app.post("/convert", response_model=List[str])
async def convert_pdf(request: PDFRequest):
    """
    Convert PDF to PNG images
    
    - **pdf**: Base64 encoded PDF content
    - **dpi**: Output resolution (72-600 DPI)
    """
    try:
        if not request.pdf:
            raise HTTPException(status_code=400, detail="Empty PDF content")
            
        pdf_bytes = base64.b64decode(request.pdf)
        return pdf_to_pngs(pdf_bytes, request.dpi)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/openapi.yaml", include_in_schema=False)
async def get_openapi_yaml():
    
    openapi_schema = app.openapi()
    yaml_str = yaml.dump(openapi_schema, sort_keys=False)
    return Response(content=yaml_str, media_type="application/yaml")
