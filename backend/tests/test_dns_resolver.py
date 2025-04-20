import pytest
from app.core.dns_resolver import CustomResolver
from app.models.dns_records import DNSZone, ARecord, MXRecord

@pytest.fixture
def setup_dns_resolver():
    resolver = CustomResolver()
    example_zone = DNSZone(
        domain="example.com",
        records=[
            ARecord(name="example.com", value="192.168.1.1", ttl=3600),
            ARecord(name="www.example.com", value="192.168.1.2", ttl=3600),
            MXRecord(name="example.com", value="mail.example.com", priority=10, ttl=3600),
        ]
    )
    resolver.zones[example_zone.domain] = example_zone
    return resolver

def test_a_record_resolution(setup_dns_resolver):
    resolver = setup_dns_resolver
    request = DNSRecord.question("example.com", QTYPE.A)
    reply = resolver.resolve(request, None)
    assert reply.rr and len(reply.rr) == 1
    assert reply.rr[0].rdata == A("192.168.1.1")

def test_mx_record_resolution(setup_dns_resolver):
    resolver = setup_dns_resolver
    request = DNSRecord.question("example.com", QTYPE.MX)
    reply = resolver.resolve(request, None)
    assert reply.rr and len(reply.rr) == 1
    assert reply.rr[0].rdata == MX(10, "mail.example.com")

def test_non_existent_record(setup_dns_resolver):
    resolver = setup_dns_resolver
    request = DNSRecord.question("nonexistent.example.com", QTYPE.A)
    reply = resolver.resolve(request, None)
    assert not reply.rr  # No records should be found

def test_www_a_record_resolution(setup_dns_resolver):
    resolver = setup_dns_resolver
    request = DNSRecord.question("www.example.com", QTYPE.A)
    reply = resolver.resolve(request, None)
    assert reply.rr and len(reply.rr) == 1
    assert reply.rr[0].rdata == A("192.168.1.2")