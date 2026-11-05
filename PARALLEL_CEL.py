from concurrent.futures import ThreadPoolExecutor

# Function to process each cell
def process_cell(cell):
    return sum(cell)

# Input data
data = [1, 2, 3, 4, 5, 6, 7, 8]

# Divide data into cells
cells = [data[i:i+2] for i in range(0, len(data), 2)]

# Process cells in parallel
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process_cell, cells))

# Combine results
total = sum(results)

print("Cells:", cells)
print("Cell Results:", results)
print("Final Result:", total)
