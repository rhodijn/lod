#!/usr/bin/env python3

#   ###################
#   ##                 ##
#   ##               ##
#     ######       ##
#       ##       ######
#     ##               ##
#   ##                 ##
#     ###################


import rdflib
from rdflib.namespace import RDF


g = rdflib.Graph()
nm = g.namespace_manager
triples = []

# @prefix bibo: <http://purl.org/ontology/bibo/> .
ns_bibo = rdflib.Namespace('http://purl.org/ontology/bibo/')
nm.bind('bibo', ns_bibo)

# @prefix dc: <http://purl.org/dc/elements/1.1/> .
ns_dc = rdflib.Namespace('http://purl.org/dc/elements/1.1/')
nm.bind('dc', ns_dc)

# @prefix dcat: <http://www.w3.org/ns/dcat#> .
ns_dcat = rdflib.Namespace('http://www.w3.org/ns/dcat#')
nm.bind('dcat', ns_dcat)

# @prefix dct: <http://purl.org/dc/terms/> .
ns_dct = rdflib.Namespace('http://purl.org/dc/terms/')
nm.bind('dct', ns_dct)

# @prefix ex: <http://example.org/> .
ns_ex = rdflib.Namespace('http://example.org/')
nm.bind('ex', ns_ex)

# @prefix fabio: <http://purl.org/spar/fabio/> .
ns_fabio = rdflib.Namespace('http://purl.org/spar/fabio/')
nm.bind('fabio', ns_fabio)

# @prefix foaf: <http://xmlns.com/foaf/0.1/> .
ns_foaf = rdflib.Namespace('http://xmlns.com/foaf/0.1/')
nm.bind('foaf', ns_foaf)

# @prefix owl: <http://www.w3.org/2002/07/owl#> .
ns_owl = rdflib.Namespace('http://www.w3.org/2002/07/owl#')
nm.bind('owl', ns_owl)

# @prefix prism: <http://prismstandard.org/namespaces/basic/2.1/> .
ns_prism = rdflib.Namespace('http://prismstandard.org/namespaces/basic/2.1/')
nm.bind('prism', ns_prism)

# @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
ns_xsd = rdflib.Namespace('http://www.w3.org/2001/XMLSchema#')
nm.bind('xsd', ns_xsd)


#dataset
s = rdflib.URIRef('https://datadryad.org/dataset/doi:10.5061/dryad.wstqjq2nj')
p = ns_dct.creator

g.add((s, p, ns_ex.ManuelGil))
g.add((s, p, ns_ex.MassimoMaiolo))
g.add((s, p, ns_ex.GholamhosseinJowkar))
g.add((s, p, ns_ex.JūlijaPečerska))
g.add((s, p, ns_ex.MariaAnisimova))

g.add((s, RDF.type, ns_fabio.Dataset))


# article
s = rdflib.URIRef('https://doi.org/10.1093/sysbio/syac050')


p = RDF.type

g.add((s, p, ns_dct.BibliographicResource))
g.add((s, p, ns_bibo.Article))


# related appendices
s = rdflib.URIRef('https://doi.org/10.5281/zenodo.7078704')


d = g.serialize(format='ttl')
print(d)

# generate json-ld file
context = {
        '@language': 'en',
        'wtm': 'http://purl.org/heals/food/',
        'ind': 'http://purl.org/heals/ingredient/',
    }

data = g.serialize(
    format='json-ld',
    context=context,
    indent=2,
    encoding='utf-8',
    )

with open('arpip.jsonld', 'wb') as f:
    f.write(data)