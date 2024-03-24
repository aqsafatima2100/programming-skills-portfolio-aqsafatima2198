# Original list of places to visit
places_to_visit = ["Japan", "Italy", "New Zealand", "Egypt", "Brazil"]

# Print the list in its original order
print("Original list:", places_to_visit)

# Print the list in alphabetical order without modifying the actual list
print("Sorted list (alphabetical):", sorted(places_to_visit))

# Print the list to show it's still in its original order
print("Original list:", places_to_visit)

# Print the list in reverse alphabetical order without modifying the actual list
print("Sorted list (reverse alphabetical):", sorted(places_to_visit, reverse=True))

# Print the list to show it's still in its original order
print("Original list:", places_to_visit)

# Change the order of the list using reverse()
places_to_visit.reverse()
print("Reversed list:", places_to_visit)

# Change the order of the list again using reverse()
places_to_visit.reverse()
print("Reversed again (back to original order):", places_to_visit)

# Change the order of the list to alphabetical using sort()
places_to_visit.sort()
print("Sorted list (alphabetical):", places_to_visit)

# Change the order of the list to reverse alphabetical using sort()
places_to_visit.sort(reverse=True)
print("Sorted list (reverse alphabetical):", places_to_visit)
