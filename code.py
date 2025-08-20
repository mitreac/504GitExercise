def function1(a):
    '''
    Goes through each nucleotide in the sequence and counts it's frequency
    Uses a dictionary to keep track of frequency
    '''
    b = dict()
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    '''
    Main function to run the frequency function
    '''
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
