import heapq

def min_cost(cable_lengths):
    
    # Create a heap from the cable lengths
    heap = [cable for cable in cable_lengths]
    heapq.heapify(heap)
    
    total_cost = 0
    
    while len(heap) > 1:
        # Select the two cables with the shortest length
        cable1 = heapq.heappop(heap)
        cable2 = heapq.heappop(heap)
        
        # Connect the two cables and calculate the cost
        new_cable = cable1 + cable2
        total_cost += new_cable
        
        # Add the new cable to the heap
        heapq.heappush(heap, new_cable)
    
    return total_cost

# Example usage
cable_lengths = [10, 2, 8, 5]
min_cost_value = min_cost(cable_lengths)
print("Minimum total cost:", min_cost_value)