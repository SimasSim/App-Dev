def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:  # Change "<=" to ">=" for descending order
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# Load data
data = []
with open("p2.txt", 'r') as fin:
    for line in fin:
        data.append(int(line.strip()))

print("Unsorted Array")
print(len(data), "items")

size = len(data)
quickSort(data, 0, size - 1)

# Count duplicates
duplicates = {}
for i in range(len(data) - 1):  # Prevent out-of-range error
    if data[i] == data[i + 1]:
        if data[i] not in duplicates:
            duplicates[data[i]] = 1
        else:
            duplicates[data[i]] += 1

# Calculate total duplicate occurrences
count_duplicates = sum(duplicates.values())

print("Sorted in descending order")
print("Found", count_duplicates, "duplicates")
