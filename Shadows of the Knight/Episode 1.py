import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [100, 100]
n = int(40)  # maximum number of turns before game over.
x0, y0 = [5, 98]

# game loop
search_area = {'w': w, 'h': h}


def search(bomb_dir, left_x, bottom_y, right_x, top_y):
    print("x:", left_x, right_x)
    print("y", top_y, bottom_y)

    x_distance = abs(right_x - left_x)
    y_distance = abs(bottom_y - top_y)
    x = 0
    y = 0

    if "U" == bomb_dir:
        if y_distance / 2 <= 1:
            y = top_y + 1
        else:
            y = top_y + y_distance // 2
        x = left_x
        print(x, y)
        new_bomb_dir = input()
        if "D" == new_bomb_dir:
            search(new_bomb_dir, x, bottom_y, x, y)
        elif "U" == new_bomb_dir:
            search(new_bomb_dir, x, y, x, top_y)
    elif "UR" == bomb_dir:
        if y_distance / 2 <= 1:
            y = top_y + 1
        else:
            y = top_y + y_distance // 2
        if x_distance / 2 <= 1:
            x = left_x + 1
        else:
            x = left_x + x_distance // 2
        print(x, y)
        new_bomb_dir = input()
        if "D" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, bottom_y, right_x, y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, bottom_y, x, y)
            else:
                search(new_bomb_dir, x, bottom_y, x, y)
        elif "U" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, y, right_x, top_y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, y, x, top_y)
            else:
                search(new_bomb_dir, x, y, x, top_y)
        elif "R" in new_bomb_dir:
            search(new_bomb_dir, x, y, right_x, y)
        elif "L" in new_bomb_dir:
            search(new_bomb_dir, left_x, y, x, y)
    elif "UL" == bomb_dir:
        if y_distance / 2 <= 1:
            y = top_y + 1
        else:
            y = top_y + y_distance // 2
        if x_distance / 2 <= 1:
            x = right_x - 1
        else:
            x = right_x - x_distance // 2
        print(x, y)
        new_bomb_dir = input()
        if "D" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, bottom_y, right_x, y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, bottom_y, x, y)
            else:
                search(new_bomb_dir, x, bottom_y, x, y)

        elif "U" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, y, right_x, top_y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, y, x, top_y)
            else:
                search(new_bomb_dir, x, y, x, top_y)
        elif "R" in new_bomb_dir:
            search(new_bomb_dir, x, y, right_x, y)
        elif "L" in new_bomb_dir:
            search(new_bomb_dir, left_x, y, x, y)


    elif "D" == bomb_dir:
        if y_distance // 2 <= 1:
            y = top_y + 1
        else:
            y = top_y + y_distance // 2
        x = left_x
        print(x, y)
        new_bomb_dir = input()
        if "D" in new_bomb_dir:
            search(new_bomb_dir, x, bottom_y, x, y)
        elif "U" in new_bomb_dir:
            search(new_bomb_dir, x, y, x, top_y)

    elif "DR" == bomb_dir:
        if y_distance // 2 <= 1:
            y = top_y + 1
        else:
            y = top_y + y_distance // 2
        if x_distance / 2 <= 1:
            x = left_x + 1
        else:
            x = left_x + x_distance // 2
        print(x, y)
        new_bomb_dir = input()
        # search(new_bomb_dir, x, bottom_y, right_x, y)
        if "D" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, bottom_y, right_x, y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, bottom_y, x, y)
            else:
                search(new_bomb_dir, x, bottom_y, x, y)
        elif "U" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, y, right_x, top_y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, y, x, top_y)
            else:
                search(new_bomb_dir, x, y, x, top_y)
        elif "R" in new_bomb_dir:
            search(new_bomb_dir, x, y, right_x, y)
        elif "L" in new_bomb_dir:
            search(new_bomb_dir, left_x, y, x, y)
    elif "DL" == bomb_dir:
        if y_distance // 2 <= 1:
            y = top_y + 1
        else:
            y = top_y + y_distance // 2
        if x_distance / 2 <= 1:
            x = right_x - 1
        else:
            x = right_x - x_distance // 2
        print(x, y)
        new_bomb_dir = input()
        # search(new_bomb_dir, x, bottom_y, right_x, y)
        if "D" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, bottom_y, right_x, y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, bottom_y, x, y)
        elif "U" in new_bomb_dir:
            if "R" in new_bomb_dir:
                search(new_bomb_dir, x, y, right_x, top_y)
            elif "L" in new_bomb_dir:
                search(new_bomb_dir, left_x, y, x, top_y)
        elif "R" in new_bomb_dir:
            search(new_bomb_dir, x, y, right_x, y)
        elif "L" in new_bomb_dir:
            search(new_bomb_dir, left_x, y, x, y)
    elif "R" == bomb_dir:
        if x_distance / 2 <= 1:
            x = left_x + 1
        else:
            x = left_x + x_distance // 2
        y = bottom_y
        print(x, y)
        new_bomb_dir = input()
        # search(new_bomb_dir, x, y, right_x, y)
        if "R" in new_bomb_dir:
            search(new_bomb_dir, x, y, right_x, y)
        elif "L" in new_bomb_dir:
            search(new_bomb_dir, left_x, y, x, y)

    elif "L" == bomb_dir:
        if x_distance / 2 <= 1:
            x = right_x - 1
        else:
            x = right_x - x_distance // 2
        y = bottom_y
        print(x, y)
        new_bomb_dir = input()
        # search(new_bomb_dir, x, y, right_x, y)
        if "R" in new_bomb_dir:
            search(new_bomb_dir, x, y, right_x, y)
        elif "L" in new_bomb_dir:
            search(new_bomb_dir, left_x, y, x, y)


while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # print("4 8")
    # print(bomb_dir)
    if "U" in bomb_dir:
        if "R" in bomb_dir:
            search(bomb_dir, x0, y0, w, 0)
        elif "L" in bomb_dir:
            search(bomb_dir, 0, y0, x0, 0)
        else:
            search(bomb_dir, x0, y0, x0, 0)
    elif "D" in bomb_dir:
        if "R" in bomb_dir:
            search(bomb_dir, x0, h, w, y0)
        elif "L" in bomb_dir:
            search(bomb_dir, 0, h, x0, y0)
        else:
            search(bomb_dir, x0, h, x0, y0)
    elif "R" in bomb_dir:
        search(bomb_dir, x0, y0, w, y0)
    else:
        search(bomb_dir, 0, y0, x0, y0)

    # the location of the next window Batman should jump to.
    # print("0 0")
    # print("3 1")
