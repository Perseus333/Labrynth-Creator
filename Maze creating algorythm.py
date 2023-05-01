import random


def create_basic_maze(maze_length=21, maze_height=21):
    maze = [['#'] * maze_length for _ in range(maze_height)]  # Chat GPT
    return maze


def print_maze(maze):
    for row in maze:
        better_row = ''
        for square in row:
            better_row += (str(square) + ' ')
        print(better_row)


def add_paths(maze, start_reps=100, end_reps=100):
    maze_len = len(maze[0])
    maze_height = len(maze)

    start = random.randrange(maze_len - 2)
    maze[0][start + 1], maze[1][start + 1] = '·', '·'

    end = random.randrange(maze_len - 2)
    maze[maze_height-1][end + 1], maze[maze_height-2][end + 1] = '·', '·'

    directions = ['u', 'd', 'l', 'r']  # For up, down, left and right
    start_paths = [[0, start], [1, start]]
    end_paths = [[maze_height - 1, end], [maze_height - 2, end]]

    start_reps_done = 0
    end_reps_done = 0

    while start_reps_done < start_reps:

        prev_square = list(start_paths[-1])
        # print(prev_square)

        choose_direction = random.choice(directions)
        # print(choose_direction)

        next_square = None

        if choose_direction == 'u':
            if prev_square[0] > 1:  # So that it doesn't go off the maze
                if maze[prev_square[0] - 1][prev_square[1]] != '·':
                    # print(maze[prev_square[0] - 1][prev_square[1]])  # So that it doesn't go to a path square
                    if maze[prev_square[0] - 1][prev_square[1] - 1] != '·':  # Check up left
                        if maze[prev_square[0] - 1][prev_square[1] + 1] != '·':  # Check up right
                            next_square = [prev_square[0] - 1, prev_square[1]]

        elif choose_direction == 'd':
            if prev_square[0] < maze_height - 2:  # So that it doesn't go down the maze
                if maze[prev_square[0] + 1][prev_square[1]] != '·':  # So that it doesn't go to a path square
                    # print(maze[prev_square[0] - 1][prev_square[1]])
                    if maze[prev_square[0] + 1][prev_square[1] - 1] != '·':  # Check down left
                        if maze[prev_square[0] + 1][prev_square[1] + 1] != '·':  # Check down right
                            next_square = [prev_square[0] + 1, prev_square[1]]

        elif choose_direction == 'l':
            if prev_square[1] > 1:  # So that it doesn't go left the maze
                if maze[prev_square[0]][prev_square[1] - 1] != '·':  # So that it doesn't go to a path square
                    # print(maze[prev_square[0] - 1][prev_square[1]])
                    if maze[prev_square[0] - 1][prev_square[1] - 1] != '·':  # Check up left
                        if maze[prev_square[0] + 1][prev_square[1] - 1] != '·':  # Check down left
                            next_square = [prev_square[0], prev_square[1] - 1]

        else:  # Which means 'r' was chosen
            if prev_square[1] < maze_len - 2:  # So that it doesn't go left the maze
                if maze[prev_square[0]][prev_square[1] + 1] != '·':  # So that it doesn't go to a path square
                    # print(maze[prev_square[0] - 1][prev_square[1]])
                    if maze[prev_square[0] - 1][prev_square[1] + 1] != '·':  # Check up right
                        if maze[prev_square[0] + 1][prev_square[1] + 1] != '·':  # Check down right
                            next_square = [prev_square[0], prev_square[1] + 1]

        if next_square is not None:
            maze[next_square[0]][next_square[1]] = '·'
            start_paths.append(next_square)
            # print(next_square)

        start_reps_done += 1

    # End Reps
    # ...

    while end_reps_done < end_reps:

        prev_square = list(end_paths[-1])
        # print(prev_square)

        choose_direction = random.choice(directions)
        # print(choose_direction)

        next_square = None

        if choose_direction == 'u':
            if prev_square[0] > 1:  # So that it doesn't go off the maze
                if maze[prev_square[0] - 1][prev_square[1]] != '·':
                    # print(maze[prev_square[0] - 1][prev_square[1]])  # So that it doesn't go to a path square
                    if maze[prev_square[0] - 1][prev_square[1] - 1] != '·':  # Check up left
                        if maze[prev_square[0] - 1][prev_square[1] + 1] != '·':  # Check up right
                            next_square = [prev_square[0] - 1, prev_square[1]]

        elif choose_direction == 'd':
            if prev_square[0] < maze_height - 2:  # So that it doesn't go down the maze
                if maze[prev_square[0] + 1][prev_square[1]] != '·':  # So that it doesn't go to a path square
                    # print(maze[prev_square[0] - 1][prev_square[1]])
                    if maze[prev_square[0] + 1][prev_square[1] - 1] != '·':  # Check down left
                        if maze[prev_square[0] + 1][prev_square[1] + 1] != '·':  # Check down right
                            next_square = [prev_square[0] + 1, prev_square[1]]

        elif choose_direction == 'l':
            if prev_square[1] > 1:  # So that it doesn't go left the maze
                if maze[prev_square[0]][prev_square[1] - 1] != '·':  # So that it doesn't go to a path square
                    # print(maze[prev_square[0] - 1][prev_square[1]])
                    if maze[prev_square[0] - 1][prev_square[1] - 1] != '·':  # Check up left
                        if maze[prev_square[0] + 1][prev_square[1] - 1] != '·':  # Check down left
                            next_square = [prev_square[0], prev_square[1] - 1]

        else:  # Which means 'r' was chosen
            if prev_square[1] < maze_len - 2:  # So that it doesn't go left the maze
                if maze[prev_square[0]][prev_square[1] + 1] != '·':  # So that it doesn't go to a path square
                    # print(maze[prev_square[0] - 1][prev_square[1]])
                    if maze[prev_square[0] - 1][prev_square[1] + 1] != '·':  # Check up right
                        if maze[prev_square[0] + 1][prev_square[1] + 1] != '·':  # Check down right
                            next_square = [prev_square[0], prev_square[1] + 1]

        if next_square is not None:
            maze[next_square[0]][next_square[1]] = '·'
            end_paths.append(next_square)

        end_reps_done += 1

    # ---
    # Connect two sides

    start_x = start_paths[-1][1]
    start_y = start_paths[-1][0]

    end_x = end_paths[-1][1]
    end_y = end_paths[-1][0]

    if start_y < end_y:
        connect_y_pos = True
    else:
        connect_y_pos = False

    if start_x < end_x:
        connect_x_pos = True
    else:
        connect_x_pos = False

    start_x_connects = [start_x]
    start_y_connects = [start_y]

    end_x_connects = [end_x]
    end_y_connects = [end_y]

    while start_y_connects[-1] != end_y_connects[-1]:
        if connect_y_pos:
            end_y_connects.append(end_y_connects[-1]-1)
        else:
            end_y_connects.append(end_y_connects[-1]+1)
        # print(f'End Y connects {end_y_connects[-1]}')
        # print(f'End X {end_x}')
        maze[end_y_connects[-1]][end_x] = '·'

    while start_x_connects[-1] != end_x_connects[-1]:
        if connect_x_pos:
            end_x_connects.append(end_x_connects[-1] - 1)
        else:
            end_x_connects.append(end_x_connects[-1] + 1)

        maze[end_y_connects[-1]][end_x_connects[-1]] = '·'

        # print_maze(maze)
        # print('---')

    return maze


basic_maze = create_basic_maze()
maze_with_paths = add_paths(basic_maze)
print_maze(maze_with_paths)
