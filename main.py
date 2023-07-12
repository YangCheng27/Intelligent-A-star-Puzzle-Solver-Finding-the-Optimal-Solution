import heapq
import copy
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def get_manhattan_distance(from_state, to_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):

    distance = 0
    length = len(to_state)
    for i in range(length):
        for j in range(length):
            if from_state[i] == to_state[j]:
                if from_state[i] != 0 and i != j:
                    distance += abs(i // 3 - j // 3) # row
                    distance += abs(i % 3 - j % 3) # col
    return distance


def print_succ(state):
    succ_states = get_succ(state)
    for succ_state in succ_states:
        print(succ_state, "h={}".format(get_manhattan_distance(succ_state)))


def get_succ(state):

    zeroStates = []
    succ_states = []
    length = len(state)
    for i in range(length):
        if state[i] == 0:
            zeroStates.append([i // 3, i % 3])

    for zero in zeroStates:
        top = [zero[0] - 1, zero[1]]
        down = [zero[0] + 1, zero[1]]
        left = [zero[0], zero[1] - 1]
        right = [zero[0], zero[1] + 1]

        for move in top, down, left, right:
            if 2 >= move[0] >= 0 and 2 >= move[1] >= 0 and state[3*move[0] + move[1]] != 0:
                succ = copy.deepcopy(state)
                moveValue = succ[3*move[0] + move[1]]
                succ[3*zero[0] + zero[1]] = moveValue
                succ[3*move[0] + move[1]] = 0
                succ_states.append(succ)

    return sorted(succ_states)


def solve(state, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):

    open = []
    closed = set()
    trace = [] # trace exists to track the nodes we consider part of the best solution

    g = 0
    h = get_manhattan_distance(state, goal_state)
    parent_index = -1

    number = 0
    previous_number = -1
    max_length_q = 0

    # put the state node on the priority queue, called open
    # heapq.heappush(pq ,(cost, state, (g, h, parent_index), number, previous_number))
    heapq.heappush(open, (g + h, state, (g, h, parent_index), number, previous_number))
    number += 1

    # added state in tuple type to closed
    closed.add(tuple(state)) 

    # if open is empty, exit with failure
    while open:
        # update max length of queue
        max_length_q = max(max_length_q, len(open))

        # update current data
        current_data = heapq.heappop(open)
        current_state = current_data[1]
        current_g = current_data[2][0]
        current_parent_index = current_data[2][2]
        current_number = current_data[3]

        # add current state to closed when we popped it from the queue
        closed.add(tuple(current_state))

        # if node is a goal node, exit
        if current_state == goal_state: break
        # if not, keep looking at successors
        current_successors = get_succ(current_state)
        g = current_g + 1
        parent_index = current_parent_index + 1

        # previous_number for the successors should be the current number of the current data
        previous_number = current_number
        for succ in current_successors:
            # if successor not in closed --> add it to open
            if tuple(succ) not in closed:
                h = get_manhattan_distance(succ)
                heapq.heappush(open, (g + h, succ, (g, h, parent_index), number, previous_number))
                # update number
                number += 1
                
        # add the curr_entry as it is a candidate for the best solution
        trace.append(current_data) 
    
    # update final path
    final_path = [current_state]
    trace_parent_idx = current_parent_index
    trace_previous_number = current_data[4]
    while trace_parent_idx != -1:
        for data in trace:
            # finds the parent index and it's connecting number
            if data[2][2] == trace_parent_idx - 1 and data[3] == trace_previous_number: 
                # build the best final path
                final_path.append(data[1]) 
                trace_parent_idx = data[2][2]
                trace_previous_number = data[4]
                break

    move = 0
    plot_path = []
    while final_path:
        node = final_path.pop()
        plot_path.append(node)
        print(node, "h={} moves: {}".format(get_manhattan_distance(node), move))
        move += 1    
        
    print("Max queue length:", max_length_q)
    return(plot_path)


def plot_tile_puzzle(plot_path, goal_state=[1, 2, 3, 4, 5, 6, 7, 0, 0]):
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.set_title('Go Blue!', fontsize=20, weight='bold')
    grid = np.reshape(goal_state, (3, 3))
    colors = ['gray'] * 9
    cmap = ListedColormap(colors)
    data = ax.imshow(grid, cmap=cmap, interpolation='nearest', vmin=0, vmax=8)

    def mark(grid):
        for i in range(3):
            for j in range(3):
                value = grid[i, j]
                image = plt.imread('grid_images/{}.png'.format(value))
                imagebox = OffsetImage(image, zoom=0.155)
                ab = AnnotationBbox(imagebox, (j, i), frameon=False)
                ax.add_artist(ab)
        
        for i in range(3):
            for j in range(3):
                rect = Rectangle((j - 0.5, i - 0.5), 1, 1, linewidth=2, edgecolor='white', facecolor='none')
                ax.add_patch(rect)

        ax.set_xticks([])
        ax.set_yticks([])

    mark(grid)

    def update(frame):

        ax.clear()
        ax.set_aspect('equal')
        if frame == 0:
            ax.set_title("Initial State, moves: {}".format(frame), fontsize=20, weight='bold')
        else:
            ax.set_title("moves: {}".format(frame), fontsize=20, weight='bold')

        grid = np.reshape(plot_path[frame], (3, 3))
        data = ax.imshow(grid, cmap=cmap, interpolation='nearest', vmin=0, vmax=8)
        mark(grid)

        return data

    anim = FuncAnimation(fig=fig, func=update, frames=len(plot_path), interval=1000, repeat = False)
    plt.show()

if __name__ == "__main__":

    solution = solve([4,3,0,5,1,6,7,2,0])
    plot_tile_puzzle(solution)