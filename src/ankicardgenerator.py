import sys
sys.dont_write_bytecode = True

from lib.card_prompt import Card_Prompt

engine = Card_Prompt("180bdc1f34ea46a48abaf34f2c121cb05391263a49a1b3c246c6241df172bf8dc06dd27d4c0b8edbc60eed6380be8b27566c6bcd7dfa34578efe5e0113605839")

try:
    notebook = engine.ask_notebook()

    glossar = engine.ask_glossar_name()

    engine.ask_number()

    layer = engine.ask_layer()

    deckname = engine.ask_deck()

    engine.next_step()

    engine.get_all_glossar_body()

    data = engine.get_glossar_entries(layer)

    test = engine.add_to_anki(data)

    for index in test:
        print("--------------------------------")
        print("test: " + index)
except KeyboardInterrupt:
    engine.exit()