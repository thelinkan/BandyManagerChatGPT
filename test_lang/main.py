import json

class Game:
    def __init__(self):
        self.language = "en"

    def load_translations(self):
        try:
            with open(f"translations/{self.language}.json", "r", encoding="utf-8") as file:
                self.translations = json.load(file)
        except FileNotFoundError:
            with open("translations/en.json", "r", encoding="utf-8") as file:
                self.translations = json.load(file)

    def set_language(self, language):
        self.language = language
        self.load_translations()

    def get_translation(self, key):
        return self.translations.get(key, key)

    def play(self):
        print(self.get_translation("welcome_message"))
        print(self.get_translation("instructions"))
        print(self.get_translation("good_luck"))

game = Game()
game.set_language("sv")
game.play()