with open('d2.in') as file:
    lines = [i for i in file.read().strip().split("\n")]
#only 12 red cubes, 13 green cubes, and 14 blue cubes
result = 0
counter = 0
for line in lines:
    counter += 1
    sequence = line.split(';')
    for colorandnumberlist in sequence:
        colorandnumber = colorandnumberlist.split(',')
