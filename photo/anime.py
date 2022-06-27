import sys
from random import randint
import requests
# third-party imports
from py3pin.Pinterest import Pinterest

# Test
print("email: " + sys.argv[1])
# print("password: " + sys.argv[2])
print("username: " + sys.argv[3])
print('********************************************************************************')

pinterest = Pinterest(email=sys.argv[1],
                      password=sys.argv[2],
                      username=sys.argv[3],
                      cred_root='cred_root')

pinterest.login()

# Get all boards
boards = pinterest.boards_all()

#Get anime board id
animeBoardId = ""
for board in boards:
    if board.get('name') == "Anime":
        animeBoardId = board.get('id')
        break

# Get all pins in the Anime board
pins = pinterest.board_feed(board_id=animeBoardId)

# Get random pin
pin = pins[randint(0, len(pins) - 1)]

# Get pin's image url
pinInfo = pinterest.load_pin(pin_id=pin.get('id'))
p = pinInfo.get('images')
print(p)
imageUrl = pinInfo.get('images').get('474x').get('url')

print(imageUrl)

# Download image
image = requests.get(imageUrl)

file = open("../img/cover.jpg", "wb")
file.write(image.content)
file.close()

