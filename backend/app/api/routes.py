from fastapi import APIRouter, HTTPException
from typing import List
from app.models.dns_records import DNSZone, DNSRecordCreate
from app.services.dns_service import DNSService

router = APIRouter()
dns_service = DNSService()

@router.get("/zones", response_model=List[DNSZone])
def list_zones():
    return dns_service.list_zones()

@router.post("/zones", response_model=DNSZone)
def create_zone(zone: DNSZone):
    return dns_service.create_zone(zone)

@router.get("/zones/{domain}", response_model=DNSZone)
def get_zone(domain: str):
    return dns_service.get_zone(domain)

@router.delete("/zones/{domain}")
def delete_zone(domain: str):
    dns_service.delete_zone(domain)
    return {"message": f"Zone {domain} deleted"}

@router.post("/zones/{domain}/records", response_model=DNSZone)
def add_record(domain: str, record: DNSRecordCreate):
    return dns_service.add_record(domain, record)

@router.delete("/zones/{domain}/records")
def delete_record(domain: str, name: str, type: str):
    dns_service.delete_record(domain, name, type)
    return {"message": f"Record {name} of type {type} deleted from zone {domain}"}