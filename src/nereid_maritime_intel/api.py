# API FastAPI pour le moteur Nereid Maritime Intel
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .tracker import track_vessels

app = FastAPI(
    title="Nereid Maritime Intel API",
    description="Moteur de Suivi Maritime & Positions Navires AIS Live",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert directement la carte maritime leaflet
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Nereid API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Nereid", "version": "1.0.0"}

@app.get("/api/v1/vessels", response_model=ResultContract)
def get_vessels(
    lat: float = Query(49.49),
    lon: float = Query(0.10),
    radius_nm: int = Query(50)
):
    return track_vessels(lat, lon, radius_nm)
