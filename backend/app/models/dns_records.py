from pydantic import BaseModel, Field, validator
from typing import List, Union

class DNSRecordBase(BaseModel):
    name: str
    ttl: int = Field(default=3600, ge=0)

class ARecord(DNSRecordBase):
    type: str = "A"
    value: str

    @validator('value')
    def validate_ipv4(cls, v):
        parts = v.split('.')
        if len(parts) != 4:
            raise ValueError('Invalid IPv4 address')
        for part in parts:
            try:
                num = int(part)
                if num < 0 or num > 255:
                    raise ValueError('Invalid IPv4 address')
            except ValueError:
                raise ValueError('Invalid IPv4 address')
        return v

class AAAARecord(DNSRecordBase):
    type: str = "AAAA"
    value: str

class MXRecord(DNSRecordBase):
    type: str = "MX"
    value: str
    priority: int = Field(default=10, ge=0)

class CNAMERecord(DNSRecordBase):
    type: str = "CNAME"
    value: str

class TXTRecord(DNSRecordBase):
    type: str = "TXT"
    value: str

class NSRecord(DNSRecordBase):
    type: str = "NS"
    value: str

class DNSZone(BaseModel):
    domain: str
    records: List[Union[ARecord, AAAARecord, MXRecord, CNAMERecord, TXTRecord, NSRecord]] = []