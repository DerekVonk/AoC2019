from itertools import product


def process_intcode(noun: int, verb: int, data):
    codes = data.copy()
    codes[1] = noun
    codes[2] = verb
    op_pos = 0
    while codes[op_pos] != 99:
        output_pos = data[op_pos + 3]
        if codes[op_pos] == 1:
            codes[output_pos] = codes[data[op_pos + 1]] + codes[data[op_pos + 2]]
        elif codes[op_pos] == 2:
            codes[output_pos] = codes[data[op_pos + 1]] * codes[data[op_pos + 2]]
        else:
            raise ValueError('incorrect op-code found', codes[0])
        op_pos += 4
    return codes[0]


input_data = '1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,' \
             '6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,' \
             '1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,' \
             '1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0'
input_list = [int(i) for i in input_data.split(',')]

print(f"1. {process_intcode(12, 2, input_list)}")

for n, v in product(range(0, 100), range(0, 100)):
    if process_intcode(n, v, input_list) == 19690720:
        print(f"2. {100 * n + v}")
        break

