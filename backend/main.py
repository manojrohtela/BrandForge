from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from brandforge.api import router as brandforge_router

app = FastAPI(title="BrandForge API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True,
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(brandforge_router, prefix="/api/brandforge")

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
