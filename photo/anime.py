import sys
import os
from random import randint
import requests
# third-party imports
from py3pin.Pinterest import Pinterest

# Checking if the user has entered the required arguments.
if len(sys.argv) < 4:
    print("Usage: python3 " + sys.argv[0] + " <pinterest email> <pinterest password> <pinterest username>")
    sys.exit(1)

pinterest = Pinterest(email=sys.argv[1],
                      password=sys.argv[2],
                      username=sys.argv[3],
                      cred_root='cred_root')

# It's logging in to the Pinterest account.
pinterest.login()

# Get all boards
boards = pinterest.boards_all()

# Get anime board id
animeBoardId = ""
for board in boards:
    # Checking if the board name is Random "Anime".
    if board.get('name') == "Random Anime":
        animeBoardId = board.get('id')
        break

# Get all pins in the Anime board
pins = pinterest.board_feed(board_id=animeBoardId)

# The directory where the image will be saved.
saveDir = "../img/"

# The cache directory.
cacheDir = "cache/"

while len(pins) > 2:
    # Get random pin
    pin = pins[randint(0, len(pins) - 1)]

    # Get pin's image url
    pinInfo = pinterest.load_pin(pin_id=pin.get('id'))
    imageUrl = pinInfo.get('images').get('474x').get('url')

    print(imageUrl)

    # Download image
    image = requests.get(imageUrl)

    # Checking if the cache directory exists. If it doesn't, it creates it.
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)

    # Checking if the save directory exists. If it doesn't, it creates it.
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # Save image to cache directory
    file = open(cacheDir + "cover.jpg", "wb")
    file.write(image.content)
    file.close()

    # Reopen the image in a read mode.
    file = open(cacheDir + "cover.jpg", "rb")

    # Compare image with the previous one
    path = saveDir + "cover.jpg"
    if os.path.exists(path) and file.read() == open(path, "rb").read():
        print("Same image")
        # Close file
        file.close()
        # Delete file from cache
        os.remove(cacheDir + "cover.jpg")
        # It's skipping the rest of the code in the loop and going back to the top.
        continue

    # It's deleting the old image and replacing it with the new one.
    if os.path.exists(path):
        os.remove(path)
    os.rename(cacheDir + "cover.jpg", path)

    # Close file
    file.close()

    # Remove cache directory
    os.rmdir(cacheDir)

    # Break the loop
    break

print("Done ☺")
