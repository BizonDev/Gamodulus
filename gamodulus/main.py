import pathlib
import os
import json

def check_folders():
    """
    check if the folders exists and creates them if not
    """
    game_path = pathlib.Path('games')
    modulo_path = pathlib.Path('modulos')
    if not game_path.exists():
        game_path.mkdir()
    if not modulo_path.exists():
        modulo_path.mkdir()

def check_settings():
    settings_path = pathlib.Path('settings.json')
    if not settings_path.exists():
        message_path = pathlib.Path('start.txt')
        with message_path.open('r',encoding='utf-8') as f:
            print(f.read())
        with settings_path.open('a',encoding='utf-8') as f:
            settings = {}
            json.dump(settings,f)
        return False
    return True

def main():
    os.chdir(pathlib.Path(__file__).parent)
    check_folders()
    check_settings()
    

if __name__=='__main__':
    main()
    input()
