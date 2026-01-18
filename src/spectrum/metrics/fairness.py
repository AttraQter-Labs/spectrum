from fractions import Fraction
from collections import defaultdict

def demographic_parity(outputs, groups):
    totals = defaultdict(int)
    positives = defaultdict(int)

    for o, g in zip(outputs, groups):
        totals[g] += 1
        positives[g] += int(o)

    return {g: Fraction(positives[g], totals[g]) for g in totals}
