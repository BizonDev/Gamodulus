import pathlib


def main():
    # search for folders
    game_path = pathlib.Path('games')
    modulo_path = pathlib.Path('modulos')
    if not game_path.exists():
        game_path.mkdir()
    if not modulo_path.exists():
        modulo_path.mkdir()
    

if __name__=='__main__':
    main()
    input()
