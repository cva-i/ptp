from pydantic import BaseModel, Field

class PDFRequest(BaseModel):
    pdf: str = Field(..., description="Base64 encoded PDF content")
    dpi: int = Field(200, ge=72, le=600, description="DPI for output images")
