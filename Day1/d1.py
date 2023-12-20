total  = counter = 0
with open('d1.in') as file:
    lines = [i for i in file.read().strip().split("\n")]
numbers = []
new_lines = []
#--------PART ONE--------
# for line in lines:
#     counter = 0
#     for char in line:
#         if not (char.isdigit()):
#             line = line[:counter] + line[counter+1:]
#             counter -=1
#         counter += 1
#     numbers.append(line)
#     total += int(line[0] + line[-1])
#
#--------PART TWO-------- 55343

for line in lines:
    line = line.replace('one', 'o1ne')
    line = line.replace('two', 't2wo')
    line = line.replace('three', 'thr3ee')
    line = line.replace('four', 'fo4ur')
    line = line.replace('five', 'fi5ve')
    line = line.replace('six', 'si6x')
    line = line.replace('seven', 'sev7en')
    line = line.replace('eight', 'eig8ht')
    line = line.replace('nine', 'ni9ne')
    new_lines.append(line)

for line in new_lines:
    counter = 0
    for char in line:
        if not (char.isdigit()):
            line = line[:counter] + line[counter+1:]
            counter -=1
        counter += 1
    total += int(line[0] + line[-1])
print(total)