import pyautogui
import keyboard
import time

dino_location = pyautogui.Point(x=582, y=495)
running = True
start_time = time.time()
cooldown_time = 0.5
last_jump_time = 0


def take_screenshot(region):
    return pyautogui.screenshot(region=region)


def jump():
    global last_jump_time
    pyautogui.press('space')
    last_jump_time = time.time()
    print("Jumped!")


def stop_game():
    global running
    running = False
    print("Game stopped")


def set_dino_location():
    global dino_location
    dino_location = pyautogui.position()
    print(f"Set starting location of Dino: {dino_location}")


def detect(screenshot):
    elapsed_time = time.time() - start_time
    shift = int(elapsed_time / 5)

    obstacle_found = False

    for x in range(0 + shift, 220 + shift, 10):
        for y in range(101, 61, -5):
            color = screenshot.getpixel((x, y))

            if color[0] < 50 and not obstacle_found:
                obstacle_found = True
                print(f"Detected obstacle at X={x}, Y={y}")

            if obstacle_found and color[0] > 220:
                print(f"Detected clear space at X={x}, Y={y}")
                distance_to_clear_space = x
                return distance_to_clear_space

    return None


def jump_after_distance(distance):
    global last_jump_time
    current_time = time.time()

    if current_time - last_jump_time > cooldown_time:
        delay = distance / 10
        print(f"Preparing to jump in {delay:.2f} seconds")
        time.sleep(delay)
        jump()


def play_game():
    global running
    print("The game starts in 3 seconds...")
    time.sleep(3)
    while running:
        screenshot = take_screenshot(region=(dino_location[0] + 1, dino_location[1] - 100, 500, 200))

        distance_to_clear_space = detect(screenshot)
        if distance_to_clear_space:
            jump_after_distance(distance_to_clear_space)


def listen_for_keys():
    keyboard.add_hotkey('c', set_dino_location)
    keyboard.add_hotkey('s', stop_game)


if __name__ == "__main__":
    listen_for_keys()
    play_game()
