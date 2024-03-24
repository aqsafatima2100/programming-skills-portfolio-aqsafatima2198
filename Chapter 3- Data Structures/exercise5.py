# Original list of people to invite to dinner
invitees = ["Albert", "Ayub", "Ronaldo"]

# Print an invitation message to each person
for person in invitees:
    print("Dear", person + ",\nYou are cordially invited to dinner. Please join us for an evening of great food and conversation!\n")

# Print the name of the guest who can't make it
guest_cant_make_it = "Albert "
print(guest_cant_make_it, "can't make it to the dinner.\n")

# Modify the list, replacing the guest who can't make it with a new person
new_invitee = "Samia"
invitees.remove(guest_cant_make_it)
invitees.append(new_invitee)

# Print a second set of invitation messages to each remaining person in the list
for person in invitees:
    print("Dear", person + ",\nYou are cordially invited to dinner. Please join us for an evening of great food and conversation!\n")
