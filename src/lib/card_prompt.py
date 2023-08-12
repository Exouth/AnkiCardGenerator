import sys
from lib.prompting import Prompt
from lib.obsidian_api import ObsidianAPI
from lib.anki_api import AnkiAPI

class Card_Prompt:

    def __init__(self):
        self.notebook_id = ""
        self.anki_deck = ""
        self.start_topic = ""
        self.end_topic = ""
        self.general_path = ""
        self.__prompt_instance = Prompt()
        self.__api_instance = ObsidianAPI()
        self.__anki_instance = AnkiAPI()
    
    def ask_obsidian_path(self):
        self.general_path = self.__prompt_instance.promp_user_return("What is the Path to Obsidian?", "You set the Path to Obsidian to")
        return self.general_path
    
    def get_obsidian_path(self):
        complete_path = self.__api_instance.findNote(self.general_path, self.notebook_id)
        return complete_path
    
    def get_glossar_entries(self, complete_path):
        data = self.__api_instance.get_glossar_entries(complete_path, self.start_topic, self.end_topic)
        return data

    def ask_note(self):
        self.notebook_id = self.__prompt_instance.promp_user_return("What is the Note called in Obsidian?", "You set the Note Name to")
        return self.notebook_id
    
    def ask_start_topic(self):
        self.start_topic = self.__prompt_instance.promp_user_return("What is the Start Topic or the Topic you want to read out?", "You set the Start Topic to")
        return self.start_topic
    
    def ask_end_topic(self):
        self.end_topic = self.__prompt_instance.promp_user_return("Which is the next Topic, to see where the Start Topic ends?", "You set the End Topic to")
        return self.end_topic
    
    def ask_deck(self):
        self.anki_deck = self.__prompt_instance.promp_user_return("What is the Deck Name in Anki?", "You set the Deck Name to")
        return self.anki_deck
    
    def next_step(self):
        self.__prompt_instance.prompt_user("Are you ready to go to the next step? Click a Button")
        self.__prompt_instance.send_logo()
    
    def add_to_anki(self, data):
        for key, value in data.items():
            self.__anki_instance.add_card(self.anki_deck, key, value)
    
    def exit(self):
        self.__prompt_instance.write_message("Exam sucessfully generated! Exiting now!")
        sys.exit(1)