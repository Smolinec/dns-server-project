import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.dns_records import DNSZone, ARecord, MXRecord, TXTRecord

client = TestClient(app)

def test_create_zone():
    zone_data = {
        "domain": "test.com",
        "records": [
            {"name": "test.com", "type": "A", "value": "192.168.1.1", "ttl": 3600},
            {"name": "www.test.com", "type": "A", "value": "192.168.1.2", "ttl": 3600},
            {"name": "test.com", "type": "MX", "value": "mail.test.com", "priority": 10, "ttl": 3600},
            {"name": "test.com", "type": "TXT", "value": "v=spf1 -all", "ttl": 3600}
        ]
    }
    response = client.post("/zones", json=zone_data)
    assert response.status_code == 200
    assert response.json()["domain"] == zone_data["domain"]

def test_get_zone():
    response = client.get("/zones/test.com")
    assert response.status_code == 200
    assert response.json()["domain"] == "test.com"

def test_list_zones():
    response = client.get("/zones")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_zone():
    response = client.delete("/zones/test.com")
    assert response.status_code == 200
    assert response.json()["message"] == "Zóna test.com byla smazána"

def test_add_record():
    record_data = {
        "name": "test.com",
        "type": "A",
        "value": "192.168.1.3",
        "ttl": 3600
    }
    response = client.post("/zones/test.com/records", json=record_data)
    assert response.status_code == 200
    assert len(response.json()["records"]) > 0

def test_delete_record():
    response = client.delete("/zones/test.com/records", params={"name": "test.com", "type": "A"})
    assert response.status_code == 200
    assert response.json()["message"] == "Záznam test.com typu A byl smazán ze zóny test.com"