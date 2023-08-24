'''
Patrick Rademacher
Anthony Rhodes
Portland State University
'''
import heapq
import time



def mergeSort(arr, n): 
    # A temp_arr is created to store 
    # sorted array in merge function 
    temp_arr = [0]*n 
    return _mergeSort(arr, temp_arr, 0, n-1) 
  
# This Function will use MergeSort to count inversions 
  
def _mergeSort(arr, temp_arr, left, right): 
  
    # A variable inv_count is used to store 
    # inversion counts in each recursive call 
  
    inv_count = 0
  
    # We will make a recursive call if and only if 
    # we have more than one elements 
  
    if left < right: 
  
        # mid is calculated to divide the array into two subarrays 
        # Floor division is must in case of python 
  
        mid = (left + right)//2
  
        # It will calculate inversion counts in the left subarray 
  
        inv_count += _mergeSort(arr, temp_arr, left, mid) 
  
        # It will calculate inversion counts in right subarray 
  
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right) 
  
        # It will merge two subarrays in a sorted subarray 
  
        inv_count += merge(arr, temp_arr, left, mid, right) 
    return inv_count 
  
# This function will merge two subarrays in a single sorted subarray 

def merge(arr, temp_arr, left, mid, right): 
    i = left     # Starting index of left subarray 
    j = mid + 1 # Starting index of right subarray 
    k = left     # Starting index of to be sorted subarray 
    inv_count = 0
  
    # Conditions are checked to make sure that i and j don't exceed their 
    # subarray limits. 
  
    while i <= mid and j <= right: 
  
        # There will be no inversion if arr[i] <= arr[j] 
  
        if arr[i] <= arr[j]: 
            temp_arr[k] = arr[i] 
            k += 1
            i += 1
        else: 
            # Inversion will occur. 
            temp_arr[k] = arr[j] 
            inv_count += (mid-i + 1) 
            k += 1
            j += 1
  
    # Copy the remaining elements of left subarray into temporary array 
    while i <= mid: 
        temp_arr[k] = arr[i] 
        k += 1
        i += 1
  
    # Copy the remaining elements of right subarray into temporary array 
    while j <= right: 
        temp_arr[k] = arr[j] 
        k += 1
        j += 1
  
    # Copy the sorted subarray into Original array 
    for loop_var in range(left, right + 1): 
        arr[loop_var] = temp_arr[loop_var] 
          
          
    return inv_count 
  
def is_solvable(puzzle):   
    n = 8  
   
    if mergeSort(puzzle, n) %2 == 0:
        return True
    else:
        return False

 
# This code is contributed by ankush_953 

def out_of_place_tiles (what_it_be, what_you_want):
    
    wrong_tiles = []
    for i in range(len(what_it_be)):
        if what_it_be[i] != 0 and what_it_be[i] != what_you_want[i]:
            wrong_tiles.append(what_it_be[i])
    return  wrong_tiles

def manhatten_distance(what_it_be, what_you_want):
    wrong_tiles = out_of_place_tiles(what_it_be, what_you_want)
    tile_index = []
    for i in range(len(wrong_tiles)):
        for j in range(9):
            if wrong_tiles[i] == what_it_be[j]:
                tile_index.append(j)
    find_distance = [[], [1, 0, 1, 2, 1, 2, 3, 2, 3], [2, 1, 0, 3, 2, 1, 4, 3, 2], [1, 2, 3, 0, 1, 2, 1, 2, 3], [2, 1, 2, 1, 0, 1, 2, 1, 2], [3, 2, 1, 2, 1, 0, 3, 2, 1]]
    find_distance.append([2, 3, 4, 1, 2, 3, 0, 1, 2]) 
    find_distance.append([3, 2, 3, 2, 1, 2, 1, 0, 1])  
    find_distance.append([4, 3, 2, 3, 2, 1, 2, 1, 0])
    total_distance = 0
    for i in range(len(wrong_tiles)):
            total_distance += find_distance[wrong_tiles[i]][tile_index[i]]
    return int(total_distance)

def inversions_heuristic(puzzle):
    mergesortpuzzle = puzzle.copy()
    mergesortpuzzle.remove(0)
    n = 8
    result = mergeSort(mergesortpuzzle, n)
    return result

def print_puzzle(what_you_have, what_you_could_get):
    i = 0
    j = 0
    for k in range(3):
        while True:
            print(str(what_you_have[i]), end = " ")
            i = i + 1
            if i % 3 == 0:
                break
        print("              ", end = "")

        while True:
            print(str(what_you_could_get[j]), end = " ")
            j = j + 1
            if j % 3 == 0:
                break
        print("")

def the_path_to_totality(pathway, my_mom_or_dad, kiddo, puzzle, tracker, another_puzzle):
    
    pathway.update({kiddo: (my_mom_or_dad, another_puzzle, puzzle, tracker)})
    

def print_path(pathway, kiddo, puzzle):
    path_to_print = []
    printer = []
    puzzle_print1 = []
    puzzle_print2 = []
    counter = 0
    while kiddo != 0:
        print("\n\n")
        printer.append(str(pathway[kiddo][0]) + "--------->" + str(kiddo))
        puzzle_print1.append(pathway[kiddo][1])
        puzzle_print2.append(pathway[kiddo][2])
        kiddo = pathway[kiddo][0] 
        counter +=1
    printer.reverse()
    print(path_to_print)
    negative = -1
    print("\n")
    for i in range(len(printer)):
        print(printer[i])
        print_puzzle(puzzle_print1[negative], puzzle_print2[negative])
        negative = negative - 1
    print("Total of " + str(len(puzzle_print1)) + " steps")

rows = 3
columns = 3
possible_moves = [[1, 3], [0, 2, 4], [1,5], [0, 4, 6], [3, 1, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5,7]]





goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
count = 0
spot = 0
proceed = True

puzzle_vals = []

input("Hello, please enter your puzzle (hit enter then type the puzzle - use zero for blank): ")
for i in range(0, 9): 
    ele = int(input())
    puzzle_vals.append(ele)
mergpuzzle = puzzle_vals.copy()
mergpuzzle.remove(0)
if is_solvable(mergpuzzle) == True:
    print("Solvable puzzle - proceed if you dare")
else:
    print("sorry, puzzle is not solvable")
    proceed = False
for t in range(6):   
    #puzzle_vals = [4, 3, 2, 1, 0 , 5, 6, 7, 8]
    mergpuzzle = puzzle_vals.copy()
    mergpuzzle.remove(0)
    if is_solvable(mergpuzzle) == True:
        print("Solvable puzzle - proceed if you dare")
    else:
        print("sorry, puzzle is not solvable")
    count = 0
    tracker = 0
    heapvisited = [[len(out_of_place_tiles(puzzle_vals, goal_state)), -1, 0, 0, puzzle_vals, spot, tracker, puzzle_vals]]
    heap_unvisited = []
    node_number = 0
    
    cost = 1
    check_puzzle = [0 for h in range(9)]
    path = {}
    path[0] = []
    best_first_search_path = []
    min_cost = 999999
    node_value = 0
    spot = puzzle_vals.index(0)
    if t == 0:
        print("\n\nTILE OUT OF ORDER BFS:")
    if t == 1:
        print("\n\nMANHATTEN BFS:")
    if t == 2:
        print("INVERSIONS BFS:")
    if t == 3:
        print("\n\nTILE OUT OF ORDER A*: \n\n")
    if t == 4:
        print("\n\nMANHATTEN A*: \n\n")
    if t == 5:
        print("INVERSIONS A*:\n\n")
    while proceed == True:
        if t < 3:
            best_first_search_path.append(puzzle_vals)
            p = puzzle_vals.index(0)
            previous_index = puzzle_vals.index(0)
            for i in range(len(possible_moves[p])):
                is_possible = possible_moves[p][i]
                #print(puzzle_vals)
                previous_index = puzzle_vals.index(0)
                if is_possible != previous_index:
                    check_puzzle = puzzle_vals.copy()
                    temp = check_puzzle[p]
                    check_puzzle[p] = check_puzzle[is_possible] 
                    check_puzzle[is_possible] = temp
                    if t == 0:
                        value = len(out_of_place_tiles(check_puzzle, goal_state))
                            
                    elif t == 1:
                        value = manhatten_distance(check_puzzle, goal_state)
                    elif t == 2:
                        value = inversions_heuristic(check_puzzle)
                    if value < min_cost:
                        min_cost = value
                        backup = check_puzzle.copy()
                        
            
            puzzle_vals = backup.copy()
            p = puzzle_vals.index(0)
            count += 1
            if puzzle_vals == goal_state:
                best_first_search_path.append(check_puzzle)
                print(t)
                print(best_first_search_path)
                for o in range(len(best_first_search_path) - 1):
                    print_puzzle(best_first_search_path[o], best_first_search_path[o+1])
                print("\n\n")
                print("Total of " + str(len(best_first_search_path)) + " steps")
                break

           
            tracker += 1
            if tracker > 10000 and t < 3:
                tracker = 0
                break
        if t > 2:
            spot = heapvisited[-1][4].index(0)
            p = spot
            parent_number = heapvisited[-1][2]
            cost = heapvisited[-1][3] + 1
            for i in range(len(possible_moves[p])):
                is_possible = possible_moves[p][i]
                if tracker != 0:
                    previous_index = heapvisited[-1][7].index(0)
                else:
                    previous_index = spot
                is_possible = possible_moves[p][i]
                if is_possible != previous_index:
                  
                    check_puzzle = puzzle_vals.copy()
                    node_number += 1
                    temp = check_puzzle[p]
                    check_puzzle[p] = check_puzzle[is_possible]
                    check_puzzle[is_possible] = temp
                   
                    new_blank = 0
                    new_blank = check_puzzle.index(0)
                    if t == 3:
                        node_value = len(out_of_place_tiles(check_puzzle, goal_state)) + cost
                    elif t == 4:
                        node_value = manhatten_distance(check_puzzle, goal_state) + cost
                    elif t == 5:
                        node_value = inversions_heuristic(check_puzzle) + cost
                    if tracker != 0:
                        node = [node_value, parent_number, node_number, cost, check_puzzle, new_blank, tracker, heapvisited[-1][4]]
                        heapq.heappush(heap_unvisited, node)
                    elif tracker == 0:
                        node = [node_value, parent_number, node_number, cost, check_puzzle, spot, tracker, puzzle_vals]
                        heapq.heappush(heap_unvisited, node)
                
            bye_bye = heapq.heappop(heap_unvisited)
            
            heapvisited.append(bye_bye)
            parent_number = bye_bye[1]
            the_path_to_totality(path, bye_bye[1], bye_bye[2], bye_bye[4], tracker, bye_bye[7])
            cost = heapvisited[-1][3]
            puzzle_vals = heapvisited[-1][4]
            tracker += 1

            if len(out_of_place_tiles(puzzle_vals, goal_state)) == 0:
                print_path(path, bye_bye[2], bye_bye)
                break






    


            


    



    
        

   


