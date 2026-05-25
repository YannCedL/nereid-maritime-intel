# test du tracker maritime AIS Nereid
from nereid_maritime_intel.tracker import track_vessels

def test_suivi_navires_ais():
    contract = track_vessels()
    assert contract is not None
    assert contract.result["total_vessels"] >= 1
    assert len(contract.evidence) >= 1
