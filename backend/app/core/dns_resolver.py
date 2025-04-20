from dnslib.server import BaseResolver
from dnslib import DNSRecord

class CustomResolver(BaseResolver):
    def __init__(self, zones):
        self.zones = zones

    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        qtype = request.q.qtype
        
        domain_name = str(qname).rstrip('.')
        
        # Hledáme nejdelší odpovídající zónu
        matching_zone = None
        matching_zone_name = ""
        
        for zone_name, zone in self.zones.items():
            if domain_name.endswith(zone.domain) and len(zone.domain) > len(matching_zone_name):
                matching_zone = zone
                matching_zone_name = zone.domain
        
        if matching_zone:
            for record in matching_zone.records:
                if record.name == domain_name or (record.name.endswith(matching_zone.domain) and 
                                               domain_name == record.name):
                    # Kontrolujeme typ záznamu
                    if (qtype == QTYPE.A and record.type == "A") or qtype == QTYPE.ANY:
                        reply.add_answer(RR(qname, QTYPE.A, ttl=record.ttl, rdata=A(record.value)))
                    elif (qtype == QTYPE.AAAA and record.type == "AAAA") or qtype == QTYPE.ANY:
                        reply.add_answer(RR(qname, QTYPE.AAAA, ttl=record.ttl, rdata=AAAA(record.value)))
                    elif (qtype == QTYPE.MX and record.type == "MX") or qtype == QTYPE.ANY:
                        if isinstance(record, MXRecord):
                            reply.add_answer(RR(qname, QTYPE.MX, ttl=record.ttl, 
                                              rdata=MX(record.priority, record.value)))
                    elif (qtype == QTYPE.CNAME and record.type == "CNAME") or qtype == QTYPE.ANY:
                        reply.add_answer(RR(qname, QTYPE.CNAME, ttl=record.ttl, rdata=CNAME(record.value)))
                    elif (qtype == QTYPE.TXT and record.type == "TXT") or qtype == QTYPE.ANY:
                        reply.add_answer(RR(qname, QTYPE.TXT, ttl=record.ttl, rdata=TXT(record.value)))
                    elif (qtype == QTYPE.NS and record.type == "NS") or qtype == QTYPE.ANY:
                        reply.add_answer(RR(qname, QTYPE.NS, ttl=record.ttl, rdata=NS(record.value)))
        
        return reply