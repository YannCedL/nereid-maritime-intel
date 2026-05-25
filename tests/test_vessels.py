from nereid_maritime_intel.tracker import track_vessels

def test_track_vessels():
    c = track_vessels(43.3, 5.37, 30)
    assert "vessels" in c.result
    assert c.result["total_vessels"] > 0
    assert c.confidence > 0.9
