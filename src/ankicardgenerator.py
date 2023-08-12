import sys
sys.dont_write_bytecode = True

from lib.card_prompt import Card_Prompt

engine = Card_Prompt()

try:
    obsidian_path = engine.ask_obsidian_path()

    glossar = engine.ask_note()

    engine.ask_start_topic()
    engine.ask_end_topic()

    deckname = engine.ask_deck()

    engine.next_step()

    path = engine.get_obsidian_path()

    data = engine.get_glossar_entries(path)

    engine.add_to_anki(data)
except KeyboardInterrupt:
    engine.exit()