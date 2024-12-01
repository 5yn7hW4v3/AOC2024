import os

left = []
right = []
sum = 0

input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
with open(input_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        split1 = line.split('   ')
        left.append(int(split1[0]))
        trimmed = split1[1].strip()
        right.append(int(trimmed))
file.close()

left.sort()
right.sort()

for i in range(len(left)):
    count = 0
    for j in range(len(right)):
        if left[i] == right[j]:
            count += 1
    sum += left[i] * count

print(sum)