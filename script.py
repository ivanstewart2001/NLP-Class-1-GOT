import os

current_directory = os.getcwd()

file_path = os.path.join(current_directory, 'textFile.txt')

list_length = 0
lines_with_phrase_count_1 = 0
lines_with_phrase_count_2 = 0
lines_with_phrase_count_3 = 0

with open(file_path, 'r') as file:
    lines = file.readlines()

    list_length = len(lines)

    for line in lines:
        if 'arya and sansa' in line.lower():
            lines_with_phrase_count_1 += 1


print("Number of lines: ", list_length)
print('Number of times Arya and Sansa mentioned: ', lines_with_phrase_count_1)
