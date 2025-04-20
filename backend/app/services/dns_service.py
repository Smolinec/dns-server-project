from typing import Dict, List, Union
from fastapi import HTTPException
from backend.app.models.dns_records import DNSZone, ARecord, AAAARecord, MXRecord, CNAMERecord, TXTRecord, NSRecord, DNSRecordCreate

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

    def add_record(self, domain: str, record: DNSRecordCreate) -> DNSZone:
        # Implementace přidání záznamu
        if domain not in self.zones:
            raise HTTPException(status_code=404, detail=f"Zone {domain} not found")
        zone = self.zones[domain]
        record_type = record.type.upper()
        if record_type == 'A':
            zone.records.append(ARecord(**record.dict()))
        elif record_type == 'AAAA':
            zone.records.append(AAAARecord(**record.dict()))
        elif record_type == 'MX':
            zone.records.append(MXRecord(**record.dict()))
        elif record_type == 'CNAME':
            zone.records.append(CNAMERecord(**record.dict()))
        elif record_type == 'TXT':
            zone.records.append(TXTRecord(**record.dict()))
        elif record_type == 'NS':
            zone.records.append(NSRecord(**record.dict()))
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported record type: {record_type}")
        return zone

    def delete_record(self, domain: str, name: str, record_type: str) -> None:
        if domain not in self.zones:
            raise HTTPException(status_code=404, detail=f"Zone {domain} not found")
        initial_count = len(self.zones[domain].records)
        self.zones[domain].records = [r for r in self.zones[domain].records if not (r.name == name and r.type == record_type)]
        if len(self.zones[domain].records) == initial_count:
            raise HTTPException(status_code=404, detail=f"Record {name} of type {record_type} not found in zone {domain}")