from typing import Dict, List, Union
from fastapi import HTTPException
from backend.app.models.dns_records import DNSZone, ARecord, AAAARecord, MXRecord, CNAMERecord, TXTRecord, NSRecord

class DNSService:
    def __init__(self):
        self.zones: Dict[str, DNSZone] = {}

    def create_zone(self, zone: DNSZone) -> DNSZone:
        if zone.domain in self.zones:
            raise HTTPException(status_code=400, detail=f"Zone {zone.domain} already exists")
        self.zones[zone.domain] = zone
        return zone

    def get_zone(self, domain: str) -> DNSZone:
        if domain not in self.zones:
            raise HTTPException(status_code=404, detail=f"Zone {domain} not found")
        return self.zones[domain]

    def delete_zone(self, domain: str) -> None:
        if domain not in self.zones:
            raise HTTPException(status_code=404, detail=f"Zone {domain} not found")
        del self.zones[domain]

    def add_record(self, domain: str, record: Union[ARecord, AAAARecord, MXRecord, CNAMERecord, TXTRecord, NSRecord]) -> DNSZone:
        if domain not in self.zones:
            raise HTTPException(status_code=404, detail=f"Zone {domain} not found")
        self.zones[domain].records.append(record)
        return self.zones[domain]

    def delete_record(self, domain: str, name: str, record_type: str) -> None:
        if domain not in self.zones:
            raise HTTPException(status_code=404, detail=f"Zone {domain} not found")
        initial_count = len(self.zones[domain].records)
        self.zones[domain].records = [r for r in self.zones[domain].records if not (r.name == name and r.type == record_type)]
        if len(self.zones[domain].records) == initial_count:
            raise HTTPException(status_code=404, detail=f"Record {name} of type {record_type} not found in zone {domain}")