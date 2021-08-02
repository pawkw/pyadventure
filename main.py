from pyadventure.AdvObject import *


def get_root(location: AdvObject):
    result = None
    while True:
        parent = location.get_parent()
        if parent is None:
            result = location
            break
        location = parent
    return result


def describe_contents(item: AdvObject, spaces=1):
    print(" " * spaces,item.article, item.get_description())
    if item.has_children():
        if item.surface:
            print(" " * (spaces + 2), "on top you see:")
        elif item.container:
            if (item.openable and item.open) or item.openable is False:
                print(" " * (spaces + 2), "inside you see:")
            else:
                return
        for child in item.get_children():
            describe_contents(child, spaces + 2)


def describe_location(location):
    root: AdvObject = get_root(location)
    print("\nLocation: {}".format(root.get_description()))
    if root.has_children():
        print("You see:")
        for child in root.get_children():
            describe_contents(child)


if __name__ == '__main__':
    room = AdvObject("Mysterious Room")
    room.location = True

    basket = AdvObject("basket")
    basket.add_vocab("basket")
    basket.container = True
    basket.openable = True
    basket.open = False  # Redundant
    basket.set_parent(room)

    red_ball = AdvObject("red ball")
    red_ball.add_vocab("red", "ball")
    red_ball.set_parent(basket)

    green_ball = AdvObject("green ball")
    green_ball.add_vocab("green", "ball")
    green_ball.set_parent(room)

    player_location = room
    describe_location(player_location)
    basket.open = True
    describe_location(player_location)

