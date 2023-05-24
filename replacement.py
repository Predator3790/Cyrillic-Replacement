import sys
sys.dont_write_bytecode = True

from pathlib import Path
from alphabet import REPLACEMENTS


if __name__ == '__main__':

    # Get .txt files
    files = [file for file in Path('files').iterdir() if file.suffix == '.txt' and not file.stem.endswith('cyrillic')]

    # Iterate through files directory
    for file in files:
        # Read file content
        data = file.read_text('utf-8', 'replace')
        
        # Replace latin letters with cyrillic ones
        for latin, cyrillic in REPLACEMENTS.items():
            data = data.replace(latin, cyrillic)

        # Write data in new file
        new_file = file.with_stem(f"{file.stem}_cyrillic")
        new_file.write_text(data, 'utf-8', 'replace')
        print(new_file.absolute())
