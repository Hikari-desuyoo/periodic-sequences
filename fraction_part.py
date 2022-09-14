class FractionPart:
    def __init__(self, sequence, identifier=None):
        self.sequence = str(sequence)
        self.id=identifier
        self.process()

    def get_id(self):
        return self.id

    def period_length(self):
        if not self.period: return 0
        return len(self.period)

    def process(self):
        sequence_list = self.group_periodic_sequences()
        self.period_occurrences = 0
        self.period = None
        if len(sequence_list) == 1: return

        first_sequence = sequence_list[0]
        if first_sequence == '0': return
        self.period = self.get_ordered_period(sequence_list)

        for sequence in sequence_list:
            if sequence != first_sequence:
                break
            self.period_occurrences += 1

    def group_periodic_sequences(self):
        reversed_sequence = self.sequence[::-1]
        sequence_list = list(reversed_sequence)
        last_sequence_list = []
        while True:
            last_sequence_list = sequence_list
            sequence_list = self.merge_common_sequences(sequence_list)   
            if len(sequence_list)<=len(last_sequence_list):
                break
        sequence_list = self.separate_last_sequences(sequence_list)
        print(sequence_list)
        return sequence_list

    def get_ordered_period(self, sequence_list):
        unordered_period = sequence_list[0]
        not_period = ""
        for sequence in sequence_list:
            if sequence != unordered_period:
                not_period = sequence
                break
            
        if not not_period: return unordered_period[::-1]
        
        ordered_period = unordered_period
        for i, digit in enumerate(not_period):
            if not i<len(unordered_period):
                break

            if digit == unordered_period[i]:
                ordered_period = ordered_period[1:] + digit
        
        return ordered_period[::-1]


    def separate_last_sequences(self, sequence_list):
        first_sequence = sequence_list[0]
        separated = []
        for element in sequence_list:
            if element == first_sequence:
                separated.append(first_sequence)
            elif element.startswith(first_sequence):
                separated.append(first_sequence)
                separated.append(element[len(first_sequence):])
            else:
                separated.append(element)

        return separated  

    def merge_common_sequences(self, sequence_list):
        first_sequence = sequence_list[0]
        merged = []
        for element in sequence_list:
            if element == first_sequence:
                merged.append(element)
            else:
                merged[-1] += element
        return merged  