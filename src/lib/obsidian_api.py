import os

class ObsidianAPI:

    def __init__(self):
        self.note_path = ""

    def findNote(self, path, name):
        for root, dirs, files in os.walk(path):
            if name in files:
                note_path = os.path.join(root, name)
                return note_path
        return None
    
    def get_glossar_entries(self, complete_path, start_topic, end_topic):
        with open(complete_path, 'r') as file:
            note = file.read()

        start_index = note.find(start_topic)
        end_index = note.find(end_topic)

        section = note[start_index:end_index]

        dictionary = {}
        for line in section.split("\n"):
            if ":" in line:
                term, description = line.split(":", 1)
                dictionary[term.replace("**", "").strip()] = description.replace("**", "").strip()

        return dictionary
