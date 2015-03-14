
import utils

data = utils.load_data('p059_cipher.txt')
data = data.strip().split(',')
data = [int(d) for d in data]

aint = ord('a')
ascii_lower = range(aint, aint+26)

def decrypt(int_seq, key):
    new_int_seq = []
    count = 0
    for i in int_seq:
        # Here's the XOR
        new_int_seq.append(i ^ key[count%3])
        count += 1
    return new_int_seq

for c1 in ascii_lower:
    for c2 in ascii_lower:
        for c3 in ascii_lower:
            new_seq = decrypt(data, (c1, c2, c3))
            nsstr = ''.join(chr(i) for i in new_seq)
            if ' the ' in nsstr and ' and ' in nsstr:
                print(sum(new_seq))

