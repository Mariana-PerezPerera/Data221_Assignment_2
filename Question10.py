#create a function that will search within the text files:
#the function will return a list of numbers for the lines that will contain the certain keyword:
def find_lines_containing(filename, keyword):
    #creating an empty list that will have the matches:
    matches = []

#opening the rile in read mode:
    with open(filename, "r") as file:
        #making sure it starts at line 1:
        for line_number, line in enumerate(file, start=1):
            if keyword.lower() in line.lower():
                matches.append((line_number, line.strip()))

    return matches

#now we have to test the function from above:
final_results = find_lines_containing("sample-file.txt", "lorem")

#now we will print how many matching lines were found in the file:
print(f"Number of matching lines: {len(final_results)}")

#and print the first 3 matching lines as well:
print("First 3 matching lines:")
for line_number, line_text in final_results[:3]:
    print(f"{line_number}: {line_text}")
