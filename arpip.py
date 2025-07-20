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

# @prefix bf:
ns_bf = rdflib.Namespace('http://id.loc.gov/ontologies/bibframe/')
nm.bind('bf', ns_bf)

# @prefix:bibo
ns_bibo = rdflib.Namespace('http://purl.org/ontology/bibo/')
nm.bind('bibo', ns_bibo)

# @prefix:fabio:
ns_fabio = rdflib.Namespace('http://purl.org/spar/fabio/')
nm.bind('fabio', ns_fabio)

uri = 'https://datadryad.org/dataset/doi:10.5061/dryad.wstqjq2nj'
s = rdflib.URIRef(uri)

p = RDF.type

o = ns_fabio.Dataset

g.add((s, p, o))

for s, p, o in g:
    print(s, p, o)