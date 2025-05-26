# Tips/Hints
#Define your function as follows
from typing import List
import heapq
def battle(monsters: List[int]) -> None:
    #If theres no input, then nobody wins by deafult LOL
    if not monsters:
        print("Nobody won!")
        return
    # We create a max heap by inverting the element's sign since heapq is min-heap by default in the land of python.
    max_heap = [-power for power in monsters]
    heapq.heapify(max_heap)
    #Another one to actually do the battling since the other one just in case theres no arguments for the battle.
    while len(max_heap) > 1:
        # put the two strongest monsters in combat with each other
        first_monster = -heapq.heappop(max_heap)
        second_monster = -heapq.heappop(max_heap)
        
        #Battle outcome: Stronger monster loses power when they win and we push the power back into the heap.
        if first_monster != second_monster:
            remaining_power = abs(first_monster - second_monster)
            heapq.heappush(max_heap, -remaining_power)
    
    # If one monster remains, print: “I have won, but at what cost?” and the oher one is If no monsters remain, print: “Nobody won!” 
    if max_heap:
        print("I have won, but at what cost?")
    else:
        print("Nobody won!")