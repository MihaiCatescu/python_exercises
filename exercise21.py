'''
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions"
for the development and functioning of living organisms.

If you want to know more http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one
side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never
empty or there is no DNA at all (again, except for Haskell).
'''

def DNA_strand(dna):
    dna = list(dna)
    new_strand = ''
    for i in dna:
        if i == "A":
            new_strand += "T"
        elif i == "T":
            new_strand += "A"
        elif i == "C":
            new_strand += "G"
        elif i == "G":
            new_strand += "C"
    print(new_strand)


DNA_strand("TTTT")
