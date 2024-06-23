# This code is very hacked together, please don't read it
flag = "BEGINNER{pr0oF_by_in$pec7ion}"

import random
sorted_labels = sorted(set(flag))

letter_to_code = {}

for i, letter in enumerate(sorted_labels):
    code = chr(ord('a') + i) + ":\n"
    code += f"\tli\t$t1, {ord(letter)}\n"
    code += "\tlb\t$t2, userinput($t0)\n\tbne\t$t1, $t2, bad\n\taddi\t$t0, $t0, 1\n"

    letter_to_code[letter] = code

for i, letter in enumerate(flag[:-1]):
    goto_label = chr(ord('a') + sorted_labels.index(flag[i+1]))

    if letter in flag[(i+1):]:
        index_of_reoccurence = flag[(i+1):].find(letter) + i
        upperbound_i_for_goto = random.randint(i+1, index_of_reoccurence+1)

        letter_to_code[letter] += f"\tble\t$t0, {upperbound_i_for_goto}, {goto_label}\n"
    else:
        letter_to_code[letter] += f"\tb\t{goto_label}\n"

letter_to_code[flag[-1]] += "\tb\tgood\n"

machine_code = ""
for sorted_label in sorted_labels:
    machine_code += letter_to_code[sorted_label] + "\n"

print(f"\tb\t{chr(ord('a') + sorted_labels.index(flag[0]))}")
print(machine_code)
