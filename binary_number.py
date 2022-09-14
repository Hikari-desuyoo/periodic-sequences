import struct

class BinaryNumber:
    def __init__(self, float_value):
        self.float_value = float_value
        
    def ieee754(self, long=True):
        if not getattr(self, 'ieee754_value', None):
            self.ieee754_value = ''.join('{:0>8b}'.format(c) for c in struct.pack('!d', self.float_value))
        return self.ieee754_value

    def fraction_part(self):
        return self.ieee754()[12:12+40]

    def is_periodic_sequence(self):
        reversed_fraction = self.fraction_part()[::-1]
        pack = list(reversed_fraction)
        last_pack = []
        while last_pack != pack:
            last_pack = pack
            pack = self.pack_sequences_together(pack)
        periodic_occurrences = pack.count(pack[-1])
        self.periodic_occurrences = periodic_occurrences
        return (set(pack) != {'0'}) and periodic_occurrences>3

    def pack_sequences_together(self, array):
        track_digit = array[0]
        packs = []
        for element in array:
            if element == track_digit:
                packs.append(element)
            else:
                packs[-1] += element
        return packs

if __name__ == '__main__':
    import sys
    for i in range(1000):
        i = 2**i
        i = float(f"0.{i}")
        result = BinaryNumber(i).is_periodic_sequence()
        if not result: print(i, result) 

