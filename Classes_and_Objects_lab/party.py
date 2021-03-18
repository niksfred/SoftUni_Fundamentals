class Party:
    def __init__(self):
        self.people = []

party = Party()

name = input()
while not name == "End":
    party.people.append(name)
    name = input()

#    • "Going: {people}" - the people should be separated by comma and space ", "
#    • "Total: {total_people_going}"

print(f"Going: {', '.join(party.people)}") 
print(f"Total: {len(party.people)}")
