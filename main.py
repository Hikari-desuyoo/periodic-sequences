from binary_number import BinaryNumber
import matplotlib.pyplot as plt

# np.ndarray(shape=(2,2), dtype=float, order='F')
periodic_sequences = 0
amount = 100000
numbers = []
ratios = []
occurrences = []
all_numbers = []
periodic_sequences_list = []
# teorema de midy, estudar?

# testar comecando de outros offsets
for i in range(amount*5):
    number = i/amount
    binary_number = BinaryNumber(number)
    result = binary_number.is_periodic_sequence()
    all_numbers.append(number)
    occurrences.append(binary_number.periodic_occurrences)
    periodic_sequences_list.append(periodic_sequences)
    ratio = (periodic_sequences/i) if i != 0 else 0
    ratios.append(ratio)
    if result: 
        periodic_sequences += 1
        numbers.append(number)
    # if i!=0:
    #     if binary_number.periodic_occurrences>3:
    #         print('-')
    #         print('occurrences', binary_number.periodic_occurrences)
    #         print('fraction', binary_number.fraction_part())
    #         print('number', number)
    #         print('ratio', periodic_sequences/i) 

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

plt.title("Relações entre dizimas periódicas em binário")

plt.subplot(311)
plt.plot(all_numbers, ratios)
plt.ylabel(f"Dízimas/total(final={ratio})", rotation=0, loc='top')

plt.subplot(312)
plt.plot(all_numbers, periodic_sequences_list)
plt.ylabel('Dízimas', rotation=0, loc='top')

plt.subplot(313)
plt.plot(all_numbers, occurrences, 'b-')
plt.xlabel('Número analisado')
plt.ylabel('Repetições \nnos primeiros digitos', rotation=0, loc='top')

plt.show()