from random import choices, uniform, randint
import pyautogui
import pydirectinput
from time import sleep

screen_width, screen_height = pyautogui.size()


def get_store_button_position():
    return screen_width - 300, screen_height - 50


def get_camera_direction():
    camera_x = 0
    camera_y = 0
    half_screen_width = screen_width / 2
    half_screen_height = screen_height / 2

    directions = ["up", "down", "left", "right"]
    direction_index = randint(0, 3)

    direction = directions[direction_index]

    if (direction == "up"):
        camera_y = -screen_height
        camera_x = randint(half_screen_width - half_screen_width / 2,
                          half_screen_width + half_screen_width / 2)

    if (direction == "down"):
        camera_y = screen_height
        camera_x = randint(half_screen_width - half_screen_width / 2,
                          half_screen_width + half_screen_width / 2)

    if (direction == "left"):
        camera_x = -screen_width
        camera_y = randint(half_screen_height - half_screen_height / 2,
                          half_screen_height + half_screen_height / 2)

    if (direction == "right"):
        camera_x = screen_width
        camera_y = randint(half_screen_height - half_screen_height / 2,
                          half_screen_height + half_screen_height / 2)
    return camera_x, camera_y


def get_screen_random_position():
    x = randint(300, screen_width - 300)
    y = randint(300, screen_height - 300)
    return x, y


def get_random_hero_position(hero_index=None):

    if hero_index is None:
        hero_index = randint(0, 9)

    radiant_first_hero = 770
    dire_first_hero = 290
    acc = 80

    position_hero = radiant_first_hero + (hero_index * acc)

    if hero_index > 4:
        position_hero += dire_first_hero

    return position_hero, 30


def get_random_hero_item_position():
    x = 1530
    y = screen_height - 150

    accX = 90
    accY = 60

    item_random_index = randint(0, 5)
    item_index = item_random_index

    if item_random_index > 2:
        item_index -= 3
        y += accY

    x += accX * item_index

    return x, y


def move_to_store_button():
    pyautogui.moveTo(*get_store_button_position(), duration=0.5)


def move_camera():
    try:
        pyautogui.moveTo(*get_camera_direction(), duration=0.5)
    except pyautogui.FailSafeException as ex:
        print("error al mover camera", ex)
    finally:
        # Mueve el mouse a otra posición despúes de mover la cámara
        sleep(uniform(0.5, 1.25))
        pyautogui.moveTo(*get_screen_random_position(), duration=0.5)

        move_camera = choices([0, 1], [0.3, 0.7])[0]

        if(move_camera):
            click_on_terrain()


def click_on_terrain(button="right", maxClicks=3):
    clicks = randint(1, maxClicks)
    pyautogui.moveTo(*get_screen_random_position(), duration=0.5)
    pyautogui.click(button=button, clicks=clicks, interval=0.35)


def follow_hero():
    pyautogui.moveTo(800, screen_height - 150, duration=0.5)
    pyautogui.doubleClick(interval=0.35)


def level_up():
    ability_index = randint(1, 4)
    ability_position = ability_index * 85
    pyautogui.moveTo(1000 + ability_position, screen_height - 225, duration=0.5)
    pyautogui.click()


def cast_ability():
    ability_index = randint(1, 4)
    ability_position = ability_index * 85
    pyautogui.moveTo(1000 + ability_position, screen_height - 150, duration=0.5)
    pyautogui.click()

    if (randint(0, 1)):
        click_on_terrain(button="left", maxClicks=1)


def make_hi5():
    pyautogui.moveTo(1525, screen_height - 225, duration=0.5)
    pyautogui.click()


def fortify():
    pyautogui.moveTo(370, screen_height - 50, duration=0.5)
    pyautogui.click()


def buy_ward():
    move_to_store_button()
    pyautogui.click()
    pyautogui.moveTo(screen_width - 500, 300, duration=0.5)
    pyautogui.click(button="right")
    move_to_store_button()
    pyautogui.click()
    click_on_terrain(maxClicks=1)


def attack():
    pydirectinput.press("a")
    pyautogui.moveTo(*get_screen_random_position(), duration=0.5)
    pyautogui.click()


def point_hero_item(hero_index=None):

    pyautogui.moveTo(
        *get_random_hero_position(hero_index=hero_index), duration=0.5)

    pyautogui.click()

    pyautogui.moveTo(*get_random_hero_item_position(), duration=0.5)

    pydirectinput.keyDown('alt')
    pyautogui.doubleClick(interval=0.25)
    pydirectinput.keyUp('alt')


def tip_hero():

    hero_position = list(get_random_hero_position())
    hero_position[1] += 70

    pyautogui.moveTo(
        *hero_position, duration=0.5)

    pydirectinput.keyDown('alt')
    pyautogui.click()
    pydirectinput.keyUp('alt')


def say_something():
    """
        - -> ?
        . -> :
        / -> _
    """
    phrases = [
        "hasta ahora no ganamos- .sleeping. .sleeping.",
        "arcontes siendo arcontes na mas wa decir",
        "tanto juegan y son arcontes? xddddddddd .axe/laugh. .axe/laugh.",
        "xdddd",
        "xd",
        ".sleeping..sleeping.",
        ".cny/rat..cny/rat..cny/rat.",
        "el chiste se cuenta solo",
        "para eso mid-",
        "para eso sacas hc- tmr hasta mi sobrino juega mejor",
        "chipi chipi chapa chapa dubi dubi daba daba",
        "no debi buscar partida .c"
    ]

    phrase = phrases[randint(0, len(phrases) - 1)]

    pydirectinput.press("enter")

    for letter in phrase:
        if letter in ".-/":
            pydirectinput.keyDown("shift")
            pydirectinput.press(letter)
            pydirectinput.keyUp("shift")
        else:
            pydirectinput.press(letter)

    pydirectinput.press("enter")


def wait_next_movement():
    seconds = uniform(1.5, 3.5)
    sleep(seconds)


def get_action():
    actions = [
        {
            "action": move_camera,
            "weight": 0.30
        },
        {
            "action": click_on_terrain,
            "weight": 0.30
        },
        {
            "action": follow_hero,
            "weight": 0.15
        },
        {
            "action": level_up,
            "weight": 0.123
        },
        {
            "action": cast_ability,
            "weight": 0.123
        },
        {
            "action": make_hi5,
            "weight": 0.123
        },
        {
            "action": fortify,
            "weight": 0.123
        },
        {
            "action": buy_ward,
            "weight": 0.083
        },
        {
            "action": attack,
            "weight": 0.043
        },
        {
            "action": point_hero_item,
            "weight": 0.043
        },
        {
            "action": tip_hero,
            "weight": 0.043
        },
        {
            "action": say_something,
            "weight": 0.043
        }
    ]

    weights = list(map(lambda item: item["weight"], actions))

    action_index = choices(range(0, len(actions)), weights)[0]

    return actions[action_index]["action"]


timer = None


def take_action():
    action = get_action()
    action()


sleep(10)

while True:
    take_action()
    wait_next_movement()
