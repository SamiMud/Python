guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  while True:
    line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    guest = yield name, age
    if guest is not None:
      guest = guest.split(",")
      name = guest[0]
      age = int(guest[1])
      guests[name] = age
      yield name, age

guestlist = read_guestlist('guest_list.txt')


for i in range(14):
  print(next(guestlist))

guestlist.send('Jane,35')

count = 0

def guest_21(guests):
  for guest in guests:
    if guests[guest] > 20:
      yield guest
      
    

drinking = guest_21(guests)

for i in range (10):
  print(next(drinking))