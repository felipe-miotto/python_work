# Using the function len() to print the number of guests
# on exercise 3-5

invitees = ['Einstein', 'Ray Dalio', 'Steve Jobs', "Phillip Plein"]
message = "Hi, this is an invitation to dinner at my place, "
end_message = "Hope you can make it!"

print(f"{message}{invitees[0]}! {end_message}")
print(f"{message}{invitees[1]}! {end_message}")
print(f"{message}{invitees[2]}! {end_message}")
print(f"{message}{invitees[3]}! {end_message}")

popped_invitee = invitees.pop(2)
print(f"Unfortunately, {popped_invitee} can't make it!")

invitees.insert(2, 'Barão da Pisadinha')
print(f"{message}{invitees[0]}! {end_message}")
print(f"{message}{invitees[1]}! {end_message}")
print(f"{message}{invitees[2]}! {end_message}")
print(f"{message}{invitees[3]}! {end_message}")

total_number = len(invitees)
print(f"The number of invitees is: {total_number}")
