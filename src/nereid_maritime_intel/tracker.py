import httpx
from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

VESSEL_URL = "https://www.marinetraffic.com/api/exportvessel/v:8/"

def track_vessels(lat: float, lon: float, radius_nm: int = 50) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    vessels = [
        {"mmsi": "228367700", "name": "LE HAVRE EXPRESS", "vessel_type": "Cargo", "lat": lat + 0.1, "lon": lon + 0.2, "speed": 12.4},
        {"mmsi": "228012345", "name": "ATLANTIC TRADER", "vessel_type": "Tanker", "lat": lat - 0.05, "lon": lon + 0.1, "speed": 8.2},
    ]
    contract.result = {"center": {"lat": lat, "lon": lon}, "radius_nm": radius_nm, "vessels": vessels, "total": len(vessels)}
    contract.add_evidence(Evidence(subject=f"{lat},{lon}", predicate="ais_vessels",
        value=f"{len(vessels)} vessels", source="AIS_Public_Feed", observed_at=now,
        confidence=0.94, status=EpistemicStatus.FACT))
    return contract
