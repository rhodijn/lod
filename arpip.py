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

o = rdflib.Literal('ARPIP: Ancestral sequence Reconstruction with insertions and deletions under the Poisson Indel Process', datatype=rdflib.XSD.string)
g.add((s, ns_dct.title, o))

g.add((s, ns_fabio.hasPublicationYear, rdflib.Literal(2022, datatype=rdflib.XSD.integer)))

g.add((s, ns_dct.modified, rdflib.Literal('2022-07-26', datatype=rdflib.XSD.date)))

p = ns_dct.relation
g.add((s, p, rdflib.URIRef('https://doi.org/10.1093/sysbio/syac050')))
g.add((s, p, rdflib.URIRef('https://doi.org/10.5281/zenodo.7078704')))

g.add((s, rdflib.RDF.type, ns_fabio.Dataset))
g.add((s, ns_bibo.numPages, rdflib.Literal(12, datatype=rdflib.XSD.integer)))
g.add((s, ns_bibo.pageStart, rdflib.Literal(307, datatype=rdflib.XSD.integer)))
g.add((s, ns_bibo.pageEnd, rdflib.Literal(318, datatype=rdflib.XSD.integer)))
g.add((s, ns_bibo.pages, rdflib.Literal('307-318', datatype=rdflib.XSD.string)))

p = ns_dct.subject
g.add((s, p, rdflib.Literal('computer and information sciences', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('ancestral sequences', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('coronaviridae', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('dynamic programming', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('evolutionary stochastic process', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('indel', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('joint ancestral sequence reconstruction', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('maximum likelihood ancestral reconstruction', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('Poisson indel Process', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('SARS-CoV', datatype=rdflib.XSD.string)))

o = rdflib.Literal('Modern phylogenetic methods allow inference of ancestral molecular sequences given an alignment and phylogeny relating present day sequences. This provides insight into the evolutionary history of molecules, helping to understand gene function and to study biological processes such as adaptation and convergent evolution across a variety of applications. Here we propose a dynamic programming algorithm for fast joint likelihood-based reconstruction of ancestral sequences under the Poisson Indel Process (PIP). Unlike previous approaches, our method, named ARPIP, enables the reconstruction with insertions and deletions based on an explicit indel model. Consequently, inferred indel events have an explicit biological interpretation. Likelihood computation is achieved in linear time with respect to the number of sequences. Our method consists of two steps, namely finding the most probable indel points and reconstructing ancestral sequences. First, we find the most likely indel points and prune the phylogeny to reflect the insertion and deletion events per site. Second, we infer the ancestral states on the pruned subtree in a manner similar to FastML. We applied ARPIP on simulated datasets and on real data from the Betacoronavirus genus. ARPIP reconstructs both the indel events and substitutions with a high degree of accuracy. Our method fares well when compared to established state-of-the-art methods such as FastML and PAML. Moreover, the method can be extended to explore both optimal and suboptimal reconstructions, include rate heterogeneity through time and more. We believe it will expand the range of novel applications of ancestral sequence reconstruction.', datatype=rdflib.XSD.string)
g.add((s, ns_dct.abstract, o))

o = rdflib.Literal('Jowkar, Gholamhossein; Pečerska, Jūlija; Maiolo, Massimo et al. (2022). ARPIP: Ancestral sequence Reconstruction with insertions and deletions under the Poisson Indel Process [Dataset]. Dryad. https://doi.org/10.5061/dryad.wstqjq2nj', datatype=rdflib.XSD.string)
g.add((s, ns_dct.bibliographicCitation, o))

g.add((s, ns_dct.license, rdflib.URIRef('https://creativecommons.org/publicdomain/zero/1.0/')))
g.add((s, ns_dct.license, rdflib.Literal('Public Domain', datatype=rdflib.XSD.string)))

g.add((s, ns_dct.hasPart, rdflib.URIRef('https://datadryad.org/downloads/file_stream/1688696')))
g.add((s, ns_dct.hasPart, rdflib.URIRef('https://datadryad.org/downloads/file_stream/1688697')))

g.add((s, ns_ex.fundedBy, rdflib.URIRef('http://viaf.org/viaf/150746866')))


# article
s = rdflib.URIRef('https://doi.org/10.1093/sysbio/syac050')
p = ns_dct.creator
g.add((s, p, ns_ex.ManuelGil))
g.add((s, p, ns_ex.MassimoMaiolo))
g.add((s, p, ns_ex.GholamhosseinJowkar))
g.add((s, p, ns_ex.JūlijaPečerska))
g.add((s, p, ns_ex.MariaAnisimova))

g.add((s, ns_bibo.issn, rdflib.Literal('1063-5157', datatype=rdflib.XSD.string)))

g.add((s, ns_bibo.volume, rdflib.Literal(72, datatype=rdflib.XSD.integer)))

g.add((s, ns_dc.title, rdflib.Literal('ARPIP: Ancestral Sequence Reconstruction with Insertions and Deletions under the Poisson Indel Process', datatype=rdflib.XSD.string)))

g.add((s, ns_dct.issued, rdflib.Literal('2022-03', datatype=rdflib.XSD.gYearMonth)))

p = ns_dct.subject
g.add((s, p, rdflib.Literal('computer and information sciences', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('ancestral sequences', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('coronaviridae', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('dynamic programming', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('evolutionary stochastic process', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('indel', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('joint ancestral sequence reconstruction', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('maximum likelihood ancestral reconstruction', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('Poisson indel Process', datatype=rdflib.XSD.string)))
g.add((s, p, rdflib.Literal('SARS-CoV', datatype=rdflib.XSD.string)))

o = rdflib.Literal('Modern phylogenetic methods allow inference of ancestral molecular sequences given an alignment and phylogeny relating present day sequences. This provides insight into the evolutionary history of molecules, helping to understand gene function and to study biological processes such as adaptation and convergent evolution across a variety of applications. Here we propose a dynamic programming algorithm for fast joint likelihood-based reconstruction of ancestral sequences under the Poisson Indel Process (PIP). Unlike previous approaches, our method, named ARPIP, enables the reconstruction with insertions and deletions based on an explicit indel model. Consequently, inferred indel events have an explicit biological interpretation. Likelihood computation is achieved in linear time with respect to the number of sequences. Our method consists of two steps, namely finding the most probable indel points and reconstructing ancestral sequences. First, we find the most likely indel points and prune the phylogeny to reflect the insertion and deletion events per site. Second, we infer the ancestral states on the pruned subtree in a manner similar to FastML. We applied ARPIP on simulated datasets and on real data from the Betacoronavirus genus. ARPIP reconstructs both the indel events and substitutions with a high degree of accuracy. Our method fares well when compared to established state-of-the-art methods such as FastML and PAML. Moreover, the method can be extended to explore both optimal and suboptimal reconstructions, include rate heterogeneity through time and more. We believe it will expand the range of novel applications of ancestral sequence reconstruction.', datatype=rdflib.XSD.string)
g.add((s, ns_dct.abstract, o))

o = rdflib.Literal('Modern phylogenetic methods allow inference of ancestral molecular sequences given an alignment and phylogeny relating present-day sequences. This provides insight into the evolutionary history of molecules, helping to understand gene function and to study biological processes such as adaptation and convergent evolution across a variety of applications. Here, we propose a dynamic programming algorithm for fast joint likelihood-based reconstruction of ancestral sequences under the Poisson Indel Process (PIP). Unlike previous approaches, our method, named ARPIP, enables the reconstruction with insertions and deletions based on an explicit indel model. Consequently, inferred indel events have an explicit biological interpretation. Likelihood computation is achieved in linear time with respect to the number of sequences. Our method consists of two steps, namely finding the most probable indel points and reconstructing ancestral sequences. First, we find the most likely indel points and prune the phylogeny to reflect the insertion and deletion events per site. Second, we infer the ancestral states on the pruned subtree in a manner similar to FastML. We applied ARPIP (Ancestral Reconstruction under PIP) on simulated data sets and on real data from the Betacoronavirus genus. ARPIP reconstructs both the indel events and substitutions with a high degree of accuracy. Our method fares well when compared to established state-of-the-art methods such as FastML and PAML. Moreover, the method can be extended to explore both optimal and suboptimal reconstructions, include rate heterogeneity through time and more. We believe it will expand the range of novel applications of ancestral sequence reconstruction. [Ancestral sequences; dynamic programming; evolutionary stochastic process; indel; joint ancestral sequence reconstruction; maximum likelihood; Poisson Indel Process; phylogeny; SARS-CoV.]', datatype=rdflib.XSD.string)
g.add((s, ns_dct.bibliographicCitation, o))

g.add((s, ns_dct.license, rdflib.URIRef('https://creativecommons.org/licenses/by-nc/4.0/')))
g.add((s, ns_dct.license, rdflib.Literal('Creative Commons CC BY-NC', datatype=rdflib.XSD.string)))

g.add((s, ns_dct.relation, rdflib.URIRef('https://doi.org/10.5061/dryad.wstqjq2nj')))

g.add((s, rdflib.RDF.type, ns_dct.BibliographicResource))
g.add((s, rdflib.RDF.type, ns_bibo.Article))


# related appendices
s = rdflib.URIRef('https://doi.org/10.5281/zenodo.7078704')
g.add((s, ns_dct.relation, rdflib.URIRef('https://doi.org/10.5061/dryad.wstqjq2nj')))

g.add((s, ns_dct.hasFormat, rdflib.URIRef('https://zenodo.org/records/7078704/files/ARPIP_appendices.pdf?download=1')))

g.add((s, ns_dct.isPartof, rdflib.URIRef('https://doi.org/10.5061/dryad.wstqjq2nj')))

g.add((s, rdflib.RDF.type, ns_dct.BibliographicResource))
g.add((s, rdflib.RDF.type, ns_bibo.Article))


# appendices in PDF format
s = rdflib.URIRef('https://zenodo.org/records/7078704/files/ARPIP_appendices.pdf?download=1')
g.add((s, ns_dct.hasFormat, rdflib.Literal('application/pdf', datatype=rdflib.XSD.string)))

g.add((s, ns_owl.hasChecksum, rdflib.Literal('0c1f6e998da89735e3bb5200f8d81977', datatype=rdflib.XSD.string)))

g.add((s, rdflib.RDF.type, ns_bibo.Document))


# creator Manuel Gil
s = ns_ex.ManuelGil
g.add((s, ns_foaf.givenName, rdflib.Literal('Manuel', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.familyName, rdflib.Literal('Gil', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.mbox, rdflib.URIRef('mailto:manuel.gil@zhaw.ch')))
g.add((s, ns_ex.worksFor, rdflib.URIRef('http://viaf.org/viaf/152303235')))
g.add((s, ns_ex.workplaceHomepage, rdflib.URIRef('https://www.zhaw.ch/de/ueber-uns/person/giln')))
g.add((s, rdflib.RDF.type, ns_foaf.Person))


# creator Massimo Maiolo
s = ns_ex.MassimoMaiolo
g.add((s, ns_foaf.givenName, rdflib.Literal('Massimo', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.familyName, rdflib.Literal('Maiolo', datatype=rdflib.XSD.string)))
g.add((s, ns_owl.sameAs, rdflib.URIRef('https://orcid.org/0000-0001-5858-4185')))
g.add((s, rdflib.RDF.type, ns_foaf.Person))


# creator Gholamhossein Jowkar
s = ns_ex.GholamhosseinJowkar
g.add((s, ns_foaf.givenName, rdflib.Literal('Gholamhossein', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.familyName, rdflib.Literal('Jowkar', datatype=rdflib.XSD.string)))
g.add((s, ns_owl.sameAs, rdflib.URIRef('https://orcid.org/0000-0002-3512-0032')))
g.add((s, rdflib.RDF.type, ns_foaf.Person))


# creator Jūlija Pečerska
s = ns_ex.JūlijaPečerska
g.add((s, ns_foaf.givenName, rdflib.Literal('Jūlija', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.familyName, rdflib.Literal('Pečerska', datatype=rdflib.XSD.string)))
g.add((s, ns_owl.sameAs, rdflib.URIRef('https://orcid.org/0000-0002-3499-6200')))
g.add((s, ns_foaf.mbox, rdflib.URIRef('mailto:julija.pecerska@zhaw.ch')))
g.add((s, ns_ex.worksFor, rdflib.URIRef('http://viaf.org/viaf/152303235')))
g.add((s, ns_ex.workplaceHomepage, rdflib.URIRef('https://www.zhaw.ch/de/ueber-uns/person/pece')))
g.add((s, rdflib.RDF.type, ns_foaf.Person))


# creator Maria Anisimova
s = ns_ex.MariaAnisimova
g.add((s, ns_foaf.givenName, rdflib.Literal('Maria', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.familyName, rdflib.Literal('Anisimova', datatype=rdflib.XSD.string)))
g.add((s, ns_foaf.mbox, rdflib.URIRef('mailto:maria.anisimova@zhaw.ch')))
g.add((s, ns_ex.worksFor, rdflib.URIRef('http://viaf.org/viaf/152303235')))
g.add((s, ns_ex.workplaceHomepage, rdflib.URIRef('https://www.zhaw.ch/de/ueber-uns/person/anis')))
g.add((s, rdflib.RDF.type, ns_foaf.Person))


# readme in Markdown format
s = rdflib.URIRef('https://datadryad.org/downloads/file_stream/1688696')
g.add((s, ns_dcat.byteSize, rdflib.Literal('9.34 KB', datatype=rdflib.XSD.byte)))
g.add((s, ns_dcat.hasFormat, rdflib.Literal('.md', datatype=rdflib.XSD.string)))
g.add((s, rdflib.RDF.type, ns_fabio.Document))
g.add((s, rdflib.RDF.type, ns_fabio.InstructionManual))


# serialize turtle
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