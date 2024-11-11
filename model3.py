import pyautogui
import keyboard
import time


class DinoGame:
    def __init__(self):
        self.dino_location = pyautogui.Point(x=216, y=690)
        self.running = True

    def take_screenshot(self, region):
        return pyautogui.screenshot(region=region)

    def jump(self):
        pyautogui.press('space')
        print("Jumped!")

    def stop_game(self):
        self.running = False
        print("Game stopped")

    def set_dino_location(self):
        self.dino_location = pyautogui.position()
        print(f"Set starting location of Dino: {self.dino_location}")

    def detect(self, screenshot):
        for x in range(200, 420, 5):
            for y in range(110, 0, -3):
                color = screenshot.getpixel((x, y))

                if color[0] < 100 and color[1] < 100 and color[2] < 100:
                    print(f"Detected obstacle at X={x}, Y={y}")
                    self.jump()
                    return

    def play_game(self):
        print("The game starts in 5 seconds...")
        time.sleep(5)
        while self.running:
            screenshot = self.take_screenshot(region=(self.dino_location[0] + 1, self.dino_location[1] - 100, 500, 200))
            self.detect(screenshot)

    def listen_for_keys(self):
        keyboard.add_hotkey('c', self.set_dino_location)
        keyboard.add_hotkey('s', self.stop_game)

    def start(self):
        self.listen_for_keys()
        print("Press 'c' to set the dino location, and 's' to stop the game.")
        self.play_game()


if __name__ == "__main__":
    game = DinoGame()
    game.start()
