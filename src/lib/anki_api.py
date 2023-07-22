import requests

class AnkiAPI:

    def __init__(self, api_url = "http://localhost:8765"):
        self.api_url = api_url
    
    def __request(self, action, params):
        payload = {
            "action": action,
            "version": 6,
            "params": params
        }

        response = requests.post(self.api_url, json=payload)
        return response.json()
    
    def add_card(self, card_name, front, back):
        note = {
            "note": {
                "deckName": card_name,
                "modelName": "Basic (and reversed card)",
                "fields": {
                    "Front": front,
                    "Back": back
                }
            }
        }
        
        response = self.__request("addNote", note)

        return response
    
    def add_deck(self, deck_name):
        deck = { "deck": deck_name }

        response = self.__request("createDeck", deck)

        return response