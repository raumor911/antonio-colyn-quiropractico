#!/usr/bin/env python3
"""Static, dependency-free SEO/GEO/LLMO release checks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = "https://antonio-colyn-quiropractico.vercel.app/"
PHONE = "525574140935"

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.jsonld = []
        self._ld = False
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append((tag, data))
        if tag == "script" and data.get("type") == "application/ld+json":
            self._ld = True
    def handle_data(self, data):
        if self._ld:
            self.jsonld.append(data)
    def handle_endtag(self, tag):
        if tag == "script":
            self._ld = False

def one(items, msg):
    assert len(items) == 1, f"{msg}: {len(items)}"
    return items[0]

def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    page = Page()
    page.feed(html)
    tags = page.tags
    canonical = one([a.get("href") for tag,a in tags if tag == "link" and a.get("rel") == "canonical"], "Exactly one canonical")
    assert canonical == BASE, (canonical, BASE)
    assert len([1 for tag,_ in tags if tag == "h1"]) == 1, "Expected one H1"
    sections = [a.get("id") for tag,a in tags if tag == "section"]
    assert sections == ["inicio", "ayuda", "servicios", "antonio", "ubicacion"], sections
    assert len([1 for tag,_ in tags if tag == "address"]) == 1, "Semantic NAP address missing"
    assert len([1 for tag,a in tags if tag == "meta" and a.get("name") == "description" and "Iztapalapa" in a.get("content", "")]) == 1
    assert not any(tag == "meta" and a.get("name") == "robots" and "noindex" in a.get("content","") for tag,a in tags)
    assert any(tag == "a" and a.get("id") == "whatsapp-link" and "wa.me/"+PHONE in a.get("href","") for tag,a in tags), "Wrong WhatsApp"
    assert any(tag == "iframe" and "Progreso%2013" in a.get("src","") and "output=embed" in a.get("src","") for tag,a in tags), "Wrong Google Maps"
    graph = json.loads(one(page.jsonld, "Exactly one JSON-LD payload"))
    assert graph.get("@context") == "https://schema.org"
    nodes = graph["@graph"]
    ids = [n["@id"] for n in nodes]
    assert len(ids) == len(set(ids)), "Duplicate entity @id"
    business = one([n for n in nodes if n.get("@type") == "ProfessionalService"], "Business node")
    assert business["telephone"].replace(" ", "").replace("+","") == PHONE
    addr = business["address"]
    assert addr["postalCode"] == "09870"
    assert addr["streetAddress"].startswith("Progreso 13")
    assert "Tomatlán" in addr["streetAddress"]
    assert business["url"] == canonical
    assert not any(k in business for k in ("aggregateRating", "review", "openingHours", "geo")), "Unsupported claims"
    assert sorted(n["serviceType"] for n in nodes if n.get("@type") == "Service") == ["Fisioterapia", "Quiropráctica"]
    site = ET.parse(ROOT / "sitemap.xml")
    urls = [u.text for u in site.iter() if u.tag.endswith("}loc")]
    assert urls == [canonical], urls
    robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
    assert "Sitemap: "+BASE+"sitemap.xml" in robots
    assert "Disallow: /" not in robots
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    for term in ("Antonio Colyn", "Santa María Tomatlán", "Progreso 13", PHONE[2:], BASE):
        if term == PHONE[2:]:
            assert "55 7414 0935" in llms
        else:
            assert term in llms, f"Missing in llms.txt: {term}"
    for uri in [canonical, BASE+"sitemap.xml"]:
        assert urlparse(uri).scheme == "https", uri
    print("SEO local / GEO / LLMO: all static checks PASS")

if __name__ == "__main__":
    main()
