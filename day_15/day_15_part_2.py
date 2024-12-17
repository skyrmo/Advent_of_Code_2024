import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        # return data


def solve(input_data):
    dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    lookup = {"^": 0, ">": 1, "v": 2, "<": 3}
    moves = [lookup[x] for x in input_data[1] if x != "\n"]

    small_grid = [list(line) for line in input_data[0].split("\n")]
    small_h, small_w = len(small_grid), len(small_grid[0])

    grid = [['.'] * small_w * 2 for _ in range(small_h)]

    start_pos = [-1, -1]
    for r in range(small_h):
        for c in range(small_w):
            if small_grid[r][c] == '@':
                start_pos = [r, 2 * c]
                grid[r][c * 2] = '@'
            elif small_grid[r][c] == '#':
                grid[r][c * 2] = '#'
                grid[r][c * 2 + 1] = '#'
            elif small_grid[r][c] == 'O':
                grid[r][c * 2] = '['
                grid[r][c * 2 + 1] = ']'

    # def move_left(r, c):
    #     pos_to_check = [(r, c - 1)]
    #
    #     while pos_to_check:
    #         nr, nc = pos_to_check.pop()
    #
    #         if grid[nr][nc] == '#':
    #             return r, c
    #
    #         elif grid[nr][nc] == ']':
    #             pos_to_check.append((nr, nc - 2))
    #
    #         elif grid[nr][nc] == '.':
    #             for i in range(nc, c - 1):
    #                 grid[r][i] = grid[r][i + 1]
    #             grid[r][c] = '.'
    #             grid[r][c - 1] = '@'
    #             return r, c - 1

    # def move_right(r, c):
    #     pos_to_check = [(r, c + 1)]
    #
    #     while pos_to_check:
    #         nr, nc = pos_to_check.pop()
    #         print(nr, nc)
    #
    #         if grid[nr][nc] == '#':
    #             return r, c
    #
    #         elif grid[nr][nc] == '[':
    #             pos_to_check.append((nr, nc + 2))
    #
    #         elif grid[nr][nc] == '.':
    #             for i in range(nc, c, -1):
    #                 grid[r][i] = grid[r][i - 1]
    #             grid[r][c] = '.'
    #             grid[r][c + 1] = '@'
    #             return r, c + 1

    def move_up(r, c):
        pos_to_check = [(r - 1, c)]
        moves = []
        # seen = set([(r, c)])

        while pos_to_check:
            nr, nc = pos_to_check.pop()

            if grid[nr][nc] == '#':
                return r, c

            elif grid[nr][nc] == '[':
                pos_to_check.append((nr, nc))
                pos_to_check.append((nr, nc + 1))
                moves.append((nr, nc))

            elif grid[nr][nc] == ']':
                pos_to_check.append((nr, nc))
                pos_to_check.append((nr, nc - 1))
                moves.append((nr, nc - 1))

        # while moves:
        #     (fr, fc), (tr, tc) = moves.pop()
        #     grid[tr][tc] = grid[fr][fc]

        # grid[r][c] = '.'
        return r - 1, c

    r, c = start_pos
    for move_no, move in enumerate(moves):
        # print(f"Move:{move_no + 1}-{move}---------")
        # for row in grid:
        #     print("".join(row))

        if move == 0:
            r, c = move_up(r, c)

        # if move == 1:
        #     r, c = move_right(r, c)
        # elif move == 2:
        #     r, c = move_down(r, c)
        # if move == 3:
        #     r, c = move_left(r, c)

        # for row in grid:
        #     print("".join(row))
        # print(f"------------------------\n")


def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 15, Part Two: {result}")


if __name__ == '__main__':
    main()
