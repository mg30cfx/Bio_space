file = open('./rosalind1.txt', 'r')
string = file.read()
freq = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
for i in string:
    freq[i] = freq[i] + 1

print freq['A'], freq['C'], freq['G'], freq['U']
