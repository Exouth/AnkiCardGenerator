import sys
from lib.prompting import Prompt
from lib.joplin_api import JoplinAPI
from lib.anki_api import AnkiAPI

class Card_Prompt:

    def __init__(self, joplin_api):
        self.glossar_id = ""
        self.number = ""
        self.notebook_id = ""
        self.anki_deck = ""
        self.__prompt_instance = Prompt()
        self.__api_instance = JoplinAPI(joplin_api)
        self.__anki_instance = AnkiAPI()
    
    def ask_notebook(self):
        foldername = self.__prompt_instance.promp_user_return("What is the Name of the Notebook?", "You set the Notebook to")

        for folder in self.__api_instance.get_all_folders()["items"]:
            if folder["title"] == foldername:
                self.notebook_id = folder["id"]

        return foldername
    
    def ask_glossar_name(self):
        glossar_name = self.__prompt_instance.promp_user_return("What is the Note Name of the Glossar?", "You set the Note Name to")

        self.glossar_id = self.__api_instance.find_glossar_id(self.notebook_id, glossar_name)

        return glossar_name

    def ask_number(self):
        self.number = self.__prompt_instance.promp_user_return("What is the Number of Glossar Entry?", "You set the Number to")
        return self.number
    
    def ask_layer(self):
        layer = self.__prompt_instance.promp_user_return("What is the Layer in the Glossar Entry?", "You set the Layer to")
        return layer
    
    def ask_deck(self):
        self.anki_deck = self.__prompt_instance.promp_user_return("What is the Deck Name in Anki?", "You set the Deck Name to")
        return self.anki_deck
    
    def get_all_glossar_body(self):
        glossar_text = self.__api_instance.get_note_text(self.glossar_id)
        return glossar_text
    
    def next_step(self):
        self.__prompt_instance.prompt_user("Are you ready to go to the next step? Click a Button")
        self.__prompt_instance.send_logo()

    def get_glossar_entries(self, layer):
        body = self.get_all_glossar_body()

        i = 0
        markdown_body = body["body"]

        if layer == "1":
            markdown_body = markdown_body.strip().split("\n\n")
            splitted = self.number.split(".")[1]

            for index in markdown_body:
                if splitted in index:
                    i += 1
                    break

                i += 1

            return markdown_body[i]
        
        elif layer == "2":
            markdown_body = markdown_body.strip().split("\n    \n")

            for index in markdown_body:
                if self.number in index:
                    i += 1
                    break

                i += 1     

            markdown_body = markdown_body[i].split("- # **")

            if "# **" in markdown_body[0]:
                markdown_body = markdown_body[0].split("# **")

            return markdown_body[0]
    
    def add_to_anki(self, data):
        clean = []

        splitted = data.split("\n")

        for index in splitted:
            if "-" in index:
                clean.append(index)

        for defintion in clean:
            current = defintion.split("**")

            glossar_defintion = current[1].strip()
            glossar_explaination = current[2].strip()

            self.__anki_instance.add_card(self.anki_deck, glossar_defintion, glossar_explaination)
    
    def exit(self):
        self.__prompt_instance.write_message("Exam sucessfully generated! Exiting now!")
        sys.exit(1)