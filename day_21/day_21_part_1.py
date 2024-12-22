import os


def parse_input(file_path):
    # Parse the input file
    with open(file_path, 'r') as file:
        # Read the entire file
        data = file.read().strip()

        # 2. Read as a list of lines
        return data.split('\n')

        # 3. Read as a list of integers
        # return [int(line) for line in data.split('\n')]

        # 4. Read as a list of lists (e.g., for grid-like inputs)
        # return [list(line) for line in data.split('\n')]

        return data


def solve(input_data):
    numpad = {
        0: [3, 1],
        1: [2, 0],
        2: [2, 1],
        3: [2, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [0, 0],
        8: [0, 1],
        9: [0, 2],
        'A': [3, 2]
    }

    dirpad = {
        '^': [0, 1],
        '>': [1, 2],
        'v': [1, 1],
        '<': [1, 0],
        'A': [0, 2]
    }

    def get_numpad_moves(f, t):
        r_moves = numpad[t][0] - numpad[f][0]
        c_moves = numpad[t][1] - numpad[f][1]
        moves = []

        for _ in range(abs(r_moves)):
            moves.append('^' if r_moves < 0 else 'v')

        for _ in range(abs(c_moves)):
            moves.append('<' if c_moves < 0 else '>')

        return moves + ["A"]

    def get_dirpad_moves(f, t):
        r_moves = dirpad[t][0] - dirpad[f][0]
        c_moves = dirpad[t][1] - dirpad[f][1]
        moves = []

        for _ in range(abs(r_moves)):
            moves.append('^' if r_moves < 0 else 'v')

        for _ in range(abs(c_moves)):
            moves.append('<' if c_moves < 0 else '>')

        return moves + ["A"]

    # print(input_data)

    inputs = [['A' if x == 'A' else int(x) for x in input] for input in input_data]

    # print(inputs)

    cur_num = 'A'
    for line in inputs:
        all_numpad_moves = []
        print("line:", line)
        for move in line:
            all_numpad_moves += get_numpad_moves(cur_num, move)
            cur_num = move
        print(*all_numpad_moves, sep="")

        all_first_dirs = []
        cur_dir = 'A'
        for move in all_numpad_moves:
            # print(move, get_dirpad_moves(cur_dir, move))
            all_first_dirs += get_dirpad_moves(cur_dir, move)
            cur_dir = move
        print(*all_first_dirs, sep="")
        #
        all_second_dirs = []
        # cur_dir = 'A'
        for move in all_first_dirs:
            print(cur_dir, move, get_dirpad_moves(cur_dir, move))
            all_second_dirs += get_dirpad_moves(cur_dir, move)
            cur_dir = move

        print(*all_second_dirs, sep="")

        print(len(all_second_dirs))
        print("_____________")


    # cur_num = 'A'
    # cur_dir = 'A'
    # for line in inputs:
    #     print("line:", line)
    #     # # all_numpad_moves = []
    #     for move in line:
    #         numpad_moves = get_numpad_moves(cur_num, move)
    #         print("numpad_moves:", numpad_moves)
    #     #     # first_dir_moves = []

    #     #     for new_dir in numpad_moves:
    #     #         dir_moves = get_dirpad_moves(cur_dir, new_dir)
    #     #         print(new_dir, dir_moves)
    #     #         #
    #     #         #
    #     #         cur_dir = new_dir

    #         cur_num = move
    #     print("new_line________")



def main():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the input file path relative to the script's location
    input_path = os.path.join(script_dir, 'input.txt')

    # Parse input
    parsed_input = parse_input(input_path)

    # Solve and print the solution
    result = solve(parsed_input)
    print(f"Solution for Day 21, Part One: {result}")


if __name__ == '__main__':
    main()
