# Original list of people to invite to dinner
invitees = ["Albert ", "Ayub", "Ronaldo", "Samia"]

# Print an invitation message to each person
for person in invitees:
    print("Dear", person + ",\nYou are cordially invited to dinner. Please join us for an evening of great food and conversation!\n")

# Print a message saying that only two people can be invited for dinner
print("Unfortunately, due to space constraints, we can only invite two people for dinner.\n")

# Remove guests from the list until only two names remain
while len(invitees) > 2:
    removed_person = invitees.pop()
    print("Sorry", removed_person + ", we can't invite you to dinner this time.\n")

# Print a message to each of the two remaining people still on the list
for person in invitees:
    print("Dear", person + ",\nYou are still invited to dinner!\n")

# Remove the last two names from the list
del invitees[:]

# Print the list to confirm it's empty
print("Final list of invitees:", invitees)
