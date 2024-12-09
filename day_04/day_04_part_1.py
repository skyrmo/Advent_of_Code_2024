import os

def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        # return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        return [list(line) for line in data.split('\n')]

        return data

def solve(input_data):
    grid = input_data
    h, w = len(grid), len(grid[0])
    result = 0
    dirs = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))

    for r in range(h):
        for c in range(w):
            if grid[r][c] == 'X':
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= h or nc < 0 or nc >= w:
                        continue
                    if grid[nr][nc] != 'M':
                        continue

                    nr_3 = nr + dr
                    nc_3 = nc + dc

                    if nr_3 < 0 or nr_3 >= h or nc_3 < 0 or nc_3 >= w:
                        continue
                    if grid[nr_3][nc_3] != 'A':
                        continue

                    nr_4 = nr_3 + dr
                    nc_4 = nc_3 + dc

                    if nr_4 < 0 or nr_4 >= h or nc_4 < 0 or nc_4 >= w:
                        continue
                    if grid[nr_4][nc_4] != 'S':
                        continue

                    result += 1
    return result

def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 04, Part One: {result}")

if __name__ == '__main__':
    main()
