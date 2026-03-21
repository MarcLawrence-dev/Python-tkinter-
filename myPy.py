userInput = input("Write your text: ")
print("Write your slices (start:end): ")
sliceList = []
for x in range(2):
    userSlice = input(f"Slice {x+1}: ")
    sliceList.append(userSlice)

# Parse and apply slices
for i, slice_str in enumerate(sliceList):
    parts = slice_str.split(":")
    start = int(parts[0]) if parts[0] else None
    end = int(parts[1]) if len(parts) > 1 and parts[1] else None
    sliced_text = userInput[start:end]
    print(f"Slice {i+1} ({slice_str}): {sliced_text}")