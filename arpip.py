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

# @prefix bf:
ns_bf = rdflib.Namespace('http://id.loc.gov/ontologies/bibframe/')
nm.bind('bf', ns_bf)

# @prefix:bibo
ns_bibo = rdflib.Namespace('http://purl.org/ontology/bibo/')
nm.bind('bibo', ns_bibo)

# @prefix:dct
ns_dct = rdflib.Namespace('http://purl.org/dc/terms/')
nm.bind('dct', ns_dct)

# @prefix:ex
ns_ex = rdflib.Namespace('http://example.org/')
nm.bind('ex', ns_ex)

# @prefix:fabio:
ns_fabio = rdflib.Namespace('http://purl.org/spar/fabio/')
nm.bind('fabio', ns_fabio)

s = rdflib.URIRef('https://datadryad.org/dataset/doi:10.5061/dryad.wstqjq2nj')
p = ns_dct.creator

g.add((s, p, ns_ex.ManuelGil))
g.add((s, p, ns_ex.MassimoMaiolo))
g.add((s, p, ns_ex.GholamhosseinJowkar))
g.add((s, p, ns_ex.JūlijaPečerska))
g.add((s, p, ns_ex.MariaAnisimova))

g.add((s, RDF.type, ns_fabio.Dataset))

s = rdflib.URIRef('https://doi.org/10.1093/sysbio/syac050')
p = RDF.type

g.add((s, p, ns_dct.BibliographicResource))
g.add((s, p, ns_bibo.Article))

for s, p, o in g:
    print(s, p, o)