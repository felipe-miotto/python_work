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

# ? Continuação 3-5

print("Wow, I found a bigger dinner table!")

invitees.insert(0, 'Stuart')
invitees.insert(2, 'Clay')
invitees.append('John')

print(f"{message}{invitees[0]}! {end_message}")
print(f"{message}{invitees[1]}! {end_message}")
print(f"{message}{invitees[2]}! {end_message}")
print(f"{message}{invitees[3]}! {end_message}")
print(f"{message}{invitees[4]}! {end_message}")
print(f"{message}{invitees[5]}! {end_message}")
print(f"{message}{invitees[6]}! {end_message}")

# ? Continuação 3-6

print("Damn it! Last minute change of plans... Table for 2 only =(")
message_2 = "Sorry, last minute change. Hope we can reschedule another time,"
popped_invitee_1 = invitees.pop(1)
print(f"{message_2} {popped_invitee_1}!")

popped_invitee_2 = invitees.pop(3)
print(f"{message_2} {popped_invitee_2}!")

popped_invitee_3 = invitees.pop(4)
print(f"{message_2} {popped_invitee_3}!")

popped_invitee_4 = invitees.pop(1)
print(f"{message_2} {popped_invitee_4}!")

popped_invitee_5 = invitees.pop(2)
print(f"{message_2} {popped_invitee_5}!")

message_3 = "Even though the table is small, I'll love if you can come, "
print(f"{message_3} {invitees[0]}!")
print(f"{message_3} {invitees[1]}!")

del invitees[0]
del invitees[0]
print(invitees)
