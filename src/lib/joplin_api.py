import requests

class JoplinAPI:

    def __init__(self, token, api_url = "http://localhost:41184"):
        self.token = token
        self.api_url = api_url

    def request(self, path, parameter = ""):
        response = requests.get(f"{self.api_url}/{path}?token={self.token}{parameter}")
        notes = response.json()

        return notes

    def get_all_notes(self):
        return self.request("notes")
    
    def get_all_folders(self):
        return self.request("folders")
    
    def get_all_notes_infolder(self, id):
        return self.request(id + "/notes")
    
    def get_note_text(self, id):
        return self.request(f"notes/{id}", "&fields=body")
    
    def find_glossar_id(self, notebook_id, glossar_name):
        glossar_id = ""
        page = 1

        while True:
            response = self.request("folders/" + notebook_id + "/notes", f"&page={page}")

            for note in response["items"]:
                if note["title"] == glossar_name:
                    glossar_id = note["id"]
                    break

            if not response["has_more"]:
                break

            page += 1

        return glossar_id