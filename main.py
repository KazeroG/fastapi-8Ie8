from fastapi import FastAPI, Request
from pydantic import BaseModel
from weasyprint import HTML

app = FastAPI()


class HTMLRequest(BaseModel):
    html: str


@app.post('/convert')
async def convert_to_pdf(request: Request, html_request: HTMLRequest):
    html_content = html_request.html
    pdf_bytes = HTML(string=html_content).write_pdf()
    return pdf_bytes
