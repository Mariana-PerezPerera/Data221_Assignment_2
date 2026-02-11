import string
from collections import defaultdict

#open and read the text file:
with open ("sample-file.txt", 'r') as file:
    lines = file.readlines()

#make a dictionary to group lines by their normalized form
normalized_groups = defaultdict(list)

#now we have to process each line:
for index, line in enumerate(lines, start=1):
    #we have to ignore the blank lines:
    if not line.strip():
        continue
    #convert them all to lowercase
    normalized = line.lower()
    #now we have to remove all the white space
    normalized = "".join(normalized.split())
    #now we have to remove the punctuation:
    normalized = normalized.translate(str.maketrans("", "", string.punctuation))

    #we have to store the original line back with the line number
    normalized_groups[normalized].append((index, line.strip()))

#now we have to keep only the groups that have more than one line
sets_near_duplicates = [group for group in normalized_groups.values() if len(group) > 1]

#now we have to print the number of near-duplicate sets:
print(f"Number of near-duplicate sets: {len(sets_near_duplicates)}\n")

#now we will print the first 2 near duplicate sets:
for set_number, duplicate_sets in enumerate(sets_near_duplicates[:2], start=1):
    print(f"Set {set_number}:")

    for line_number, original_line in duplicate_sets:
        print(f"{line_number}: {original_line}")
    print()