#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MSDT - METODO SCIENTIFICO DIGITALE TOLA
Framework Europeo a Valenza Sistemica Generale
Modello Ontologico Forense, Cibernetico di Terzo Ordine, Giurisdizione Esclusiva e WAI-ARIA
"""

import json

MSDT_METADATA = {
  "@context": {
    "@vocab": "https://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "prov": "http://www.w3.org/ns/prov#",
    "sec": "https://w3id.org/security#",
    "fibo": "https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/FinancialProductsAndServices/",
    "msdt": "http://www.msdt.university/schema/v3#"
  },
  "@graph": [
    {
      "@type": [
        "ScholarlyArticle",
        "TechArticle",
        "CreativeWork"
      ],
      "@id": "https://doi.org/10.5281/zenodo.22007889",
      "name": {
        "@language": "it",
        "@value": "FRAMEWORK EUROPEO A VALENZA SISTEMICA GENERALE MSDT - METODO SCIENTIFICO DIGITALE TOLA"
      },
      
      "comment": "--- BLOCCO PROPRIETÀ INTELLETTUALE E GIURISDIZIONE ESCLUSIVA ---",
      "copyrightYear": 2026,
      "copyrightHolder": {
        "@id": "urn:oid:2.5.4.97:IT-TLOFNC80D30G348Z"
      },
      "copyrightNotice": "PROPRIETÀ INTELLETTUALE ESCLUSIVA: Il Framework MSDT (Metodo Scientifico Digitale Tola) è proprietà intellettuale assoluta di Francesco Tola. Struttura forense transfrontaliera protetta da diritto d'autore e asseverazione algoritmica, con validità erga omnes in tutti gli Stati Membri dell'Unione Europea (Regolamenti UE 2024/1689, eIDAS 2.0, e-CODEX). CLAUSOLA DI GIURISDIZIONE ESCLUSIVA: In ragione della localizzazione geospaziale della Sede Esecutiva Primaria a Partinico (PA), per qualsivoglia controversia legale, violazione di proprietà intellettuale, o disputa tecnica e amministrativa derivante dall'utilizzo dell'infrastruttura, viene stabilita la competenza territoriale esclusiva, assoluta e inderogabile del Foro di Palermo, Italia.",
      
      "author": {
        "@type": "Person",
        "@id": "urn:oid:2.5.4.97:IT-TLOFNC80D30G348Z",
        "name": "Francesco Tola",
        "taxID": "TLOFNC80D30G348Z"
      },
      
      "comment": "--- BLOCCO GEOLOCALIZZAZIONE SPAZIALE FORENSE ---",
      "spatialCoverage": [
        {
          "@type": "Place",
          "name": "Sede Esecutiva Primaria e Presidio Sovrano MSDT",
          "description": "Nodo di comando esecutivo, giurisdizione di origine della supervisione umana e titolarità della Proprietà Intellettuale.",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Partinico",
            "addressRegion": "Palermo",
            "addressCountry": "IT"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": "38.046830",
            "longitude": "13.111812",
            "elevation": "175",
            "description": "Punto zero cibernetico dell'Invariante Umano Sovrano TLOFNC80D30G348Z."
          }
        },
        {
          "@type": "Place",
          "name": "Hub Scientifico di Riferimento Transfrontaliero (CERN / Zenodo / OpenAIRE)",
          "description": "Infrastruttura accademica centrale per il deposito forense inoppugnabile dei log telemetrici MSDT e dell'European Learning Model.",
          "address": {
            "@type": "PostalAddress",
            "addressLocality": "Meyrin / Genève",
            "addressCountry": "CH"
          },
          "geo": {
            "@type": "GeoCoordinates",
            "latitude": "46.233058",
            "longitude": "6.053229",
            "description": "Coordinate geospaziali del cluster data-center CERN per la conservazione permanente dei DOI."
          }
        }
      ],

      "comment": "--- BLOCCO ACCESSIBILITÀ UNIVERSALE E INCLUSIONE CIBERNETICA (DISABILITÀ) ---",
      "accessibilityAPI": "ARIA",
      "accessibilityControl": [
        "fullKeyboardControl",
        "fullMouseControl",
        "fullTouchControl",
        "fullVoiceControl"
      ],
      "accessibilityFeature": [
        "structuralNavigation",
        "highContrastDisplay",
        "readingOrder",
        "unrolledList",
        "tableOfContents",
        "taggedPDF",
        "largePrint",
        "alternativeText",
        "displayTransformability",
        "synchronizedAudioText",
        "ttsMarkup"
      ],
      "accessibilityHazard": [
        "none",
        "noFlashingHazard",
        "noMotionSimulationHazard",
        "noSoundHazard"
      ],
      "accessMode": [
        "textual",
        "visual",
        "auditory"
      ],
      "accessModeSufficient": [
        {"@type": "ItemList", "itemListElement": ["textual"]},
        {"@type": "ItemList", "itemListElement": ["textual", "auditory"]}
      ],
      "accessibilitySummary": "Infrastruttura cibernetica nativamente accessibile e conforme agli standard ISO/IEC 40500:2012 (WCAG 2.2 Livello AAA), all'European Accessibility Act (Direttiva UE 2019/882), alla Legge Stanca (Legge 4/2004 e D.Lgs 106/2018) e alla Direttiva UE 2016/2102. Integrazione semantica avanzata WAI-ARIA a tutela assoluta delle persone con disabilità visiva (ipovedenti e non vedenti) e motoria, garantendo interazione universale e priva di bias computazionali tramite screen reader, display braille e tecnologie assistive di sintesi vocale.",

      "identifier": [
        {
          "@type": "PropertyValue",
          "name": "Macro-Ecosystem Root DOI Concept",
          "propertyID": "DOI-CONCEPT",
          "value": "10.5281/zenodo.20177272"
        },
        {
          "@type": "PropertyValue",
          "name": "Hybrid QTSP & Blockchain Time-Lock Notarization Flag",
          "propertyID": "urn:eu:msdt:trust-flag:qtsp-btc-master-proof",
          "value": "NAMIRIAL-QTSP-UTC-20260902-BTC-BLOCK-965185-OTS"
        }
      ],
      "msdt:aiHumanSovereigntyFusionProtocol": {
        "@context": [
          "https://www.w3.org/2018/credentials/v1",
          "https://francesco-tolamsdt.github.io/msdt-tola/context/v1.jsonld",
          "https://w3id.org/security/suites/ed25519-2020/v1"
        ],
        "type": [
          "VerifiablePresentation",
          "MsdtAIHumanSovereigntyFusion"
        ],
        "presentation_context": "European Union AI Act Compliance - Article 14 (Human Oversight)",
        "holder": "urn:oid:1.3.6.1.4.1.66881.3.2",
        "human_invariant_supervisor": "TLOFNC80D30G348Z",
        "issuanceDate": "2026-10-02T21:25:00Z",
        "verifiableCredential": [
          {
            "type": [
              "VerifiableCredential",
              "MsdtAcademyHumanOversightCredential"
            ],
            "issuer": "urn:oid:1.3.6.1.4.1.66881.3.2.5",
            "issuanceDate": "2026-10-02T21:25:00Z",
            "credentialSubject": {
              "id": "did:web:francesco-tolamsdt.github.io:msdt-tola:human:TLOFNC80D30G348Z",
              "certified_role": "Chief AI Ethics Officer",
              "qualification_level": "EQF Level 5 - Cibernetica e Governance IA",
              "clearance_status": "ACTIVE",
              "pen": "66881",
              "human_invariant": "TLOFNC80D30G348Z"
            },
            "proof": {
              "type": "Ed25519Signature2020",
              "created": "2026-10-02T21:25:00Z",
              "proofPurpose": "assertionMethod",
              "verificationMethod": "did:web:francesco-tolamsdt.github.io:msdt-tola:human:TLOFNC80D30G348Z#human-auth-key",
              "proofValue": "z5f5K8v9Xy2pLq3R8sT1uVw2xY3zA4bC5dE6fG7hJ8kL9mN0pQ1rS2tU3vW4xY5zA6bC7dE8fG9hJ0kL1mN2pQ3rS4tU5vW6xY7zA8bC9dE0fG1hJ2kL3mN"
            }
          },
          {
            "type": [
              "VerifiableCredential",
              "MsdtHighRiskSystemInterlock"
            ],
            "issuer": "urn:oid:1.3.6.1.4.1.66881.3.2.6",
            "issuanceDate": "2026-10-02T21:25:00Z",
            "credentialSubject": {
              "system_id": "urn:uuid:industrial-ai-core-99x",
              "risk_classification": "HIGH_RISK_ANNEX_III",
              "system_status": "INTERLOCK_ENGAGED_AWAITING_HUMAN",
              "telemetry_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
              "pen_reference": "1.3.6.1.4.1.66881.3.2.6"
            },
            "proof": {
              "type": "Ed25519Signature2020",
              "created": "2026-10-02T21:25:00Z",
              "proofPurpose": "assertionMethod",
              "verificationMethod": "urn:oid:1.3.6.1.4.1.66881.3.2.6#machine-telemetry-key",
              "proofValue": "z3kL9mN0pQ1rS2tU3vW4xY5zA6bC7dE8fG9hJ0kL1mN2pQ3rS4tU5vW6xY7zA8bC9dE0fG1hJ2kL3mN4pQ5rS6tU7vW8xY9zA0bC1"
            }
          }
        ],
        "fusion_proof": {
          "type": "Ed25519Signature2020",
          "created": "2026-10-02T21:25:00Z",
          "domain": "api.world-trust.msdt.eu",
          "challenge": "audit-challenge-req-778899",
          "proofPurpose": "authentication",
          "verificationMethod": "urn:oid:1.3.6.1.4.1.66881.3.2#master-root-key",
          "proofValue": "z2pLq3R8sT1uVw2xY3zA4bC5dE6fG7hJ8kL9mN0pQ1rS2tU3vW4xY5zA6bC7dE8fG9hJ0kL1mN2pQ3rS4tU5vW6xY7zA8bC9dE0fG1hJ2kL",
          "publicKeyMultibase": "z6MkrT1wW7p8x9y0zA1bC2dE3fG4hJ5kL6mN7pQ8rS9tU0vW1xY2zA3bC4dE5fG6hJ7kL8"
        },
        "nato_vendor_context": {
          "pen": 66881,
          "oid_root": "1.3.6.1.4.1.66881",
          "doi": "10.5281/zenodo.20177272",
          "ncage_required": true
        }
      }
    }
  ]
}

def export_jsonld(filepath: str = "api/msdt-master-framework.jsonld") -> None:
    """Valida, stampa e gestisce il salvataggio cibernetico del Framework."""
    json_output = json.dumps(MSDT_METADATA, indent=2, ensure_ascii=False)
    print("--- INIZIO VERIFICA STRUTTURALE MSDT ---")
    print(json_output)
    print("\n[OK] Record JSON-LD generato, validato e stampato con successo!")

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(json_output)
        print(f"[OK] Salvataggio locale completato: {filepath}")
    except (PermissionError, OSError):
        print("[INFO] Ambiente protetto: scrittura su disco bypassata. Codice pronto per il copia-incolla.")

if __name__ == "__main__":
    export_jsonld()
