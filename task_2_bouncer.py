guest_age = 18
has_ticket = True
is_vip = False

age_check = guest_age >= 18
if age_check:
    print("Guest is old enough to enter.")

if guest_age >= 18 and ( has_ticket == True):
    print("Welcome to the club!")
elif guest_age >=18 and not has_ticket:
    print("You need a ticket")
elif guest_age < 18 and is_vip:
    print("You are not old enough to enter, but you can enter as a VIP.")
else:
    print("You are not old enough to enter, please go sleep.")
