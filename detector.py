import sys
sys.dont_write_bytecode = True

from pathlib import Path
from alphabet import REPLACEMENTS


if __name__ == '__main__':
    # Get .txt files
    files = [file for file in Path('files').iterdir() if file.suffix == '.txt']

    # Index and show the files
    for index, file in enumerate(files, 1):
        print(f"[{index}] {file.name}")
    
    # Ask for file to read
    file = files[int(input("File: "))-1]

    # Read the file
    data = file.read_text('utf-8', 'replace')

    # Get current number of characters for future report
    characters_count = len(data)
    cyrillic_count = 0
    
    # Make red the cyrillic characters
    for cyrillic in REPLACEMENTS.values():
        data = data.replace(cyrillic, f'\033[1;31m{cyrillic}\033[0;0m')
        cyrillic_count += data.count(cyrillic)

    # Print results
    print('-'*50)
    print(data)
    print('-'*50)
    print(f"Cyrillic characters: {cyrillic_count}/{characters_count}")
