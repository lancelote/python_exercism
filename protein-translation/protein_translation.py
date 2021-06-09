from enum import Enum
from itertools import takewhile
from textwrap import wrap
from typing import Dict
from typing import List

Codon = str


class Protein(Enum):
    STOP = 0
    METHIONINE = 1
    PHENYLALANINE = 2
    LEUCINE = 3
    SERINE = 4
    TYROSINE = 5
    CYSTEINE = 6
    TRYPTOPHAN = 7


ProteinToCodons: Dict[Protein, List[Codon]] = {
    Protein.STOP: ["UAA", "UAG", "UGA"],
    Protein.METHIONINE: ["AUG"],
    Protein.LEUCINE: ["UUA", "UUG"],
    Protein.PHENYLALANINE: ["UUU", "UUC"],
    Protein.SERINE: ["UCU", "UCC", "UCA", "UCG"],
    Protein.TYROSINE: ["UAU", "UAC"],
    Protein.CYSTEINE: ["UGU", "UGC"],
    Protein.TRYPTOPHAN: ["UGG"],
}

CodonToProtein: Dict[Codon, Protein] = {
    codon: protein
    for protein, codons in ProteinToCodons.items()
    for codon in codons
}


def is_not_stop(codon: Codon) -> bool:
    return CodonToProtein[codon] is not Protein.STOP


def proteins(strand: str) -> List[str]:
    return [
        CodonToProtein[codon].name.capitalize()
        for codon in takewhile(is_not_stop, wrap(strand, 3))
    ]
