import os, shutil, sys
from pathlib import Path


# Make a directory, ignoring if it already exists
def mk_dir(path):
    """Friendly wrapper to create paths without pre-existence errors"""
    try: os.mkdir(path)
    except FileExistsError: pass
    else: print(f"{path} successfully created")

# Alternative make a directory including parents that's probably easier and may not get errors
# I haven't tested this, just pulled from stackoverflow, not sure what errors it may or may not make
Path(path).mkdir(parents=True, exist_ok=True)

# Remove a directory and children entirely, ignoring if it doesn't exist
def rm_dir(path):
    """Friendly wrapper to remove paths without non-existence errors"""
    # NOTE - Path.rmdir() requires the folder to be empty, so shutil is a little easier for this
    try: shutil.rmtree(path)
    except FileNotFoundError: pass
    except PermissionError as e:
        print(repr(e))
        print(f"PermissionError exception trying to rm_dir {path}.  "
                     'Do you have one of the files open somewhere?  This seems to '
                     'clear it anyways so we won\'t exit here.')
    else: print(f"{path} successfully removed")


# Search for file patterns in a folder
for f in Path('./testdata').glob('*.csv'):
    print(f)

# Move/Rename files
# Note I believe this can accept Path objects as well as strings interchangeably
for f in Path('./testdata').iterdir(): f
print('renaming test1.csv to testmoved.csv')
shutil.move('./testdata/test1.csv', './testdata/testmoved.csv')
for f in Path('./testdata').iterdir(): f
print('renaming testmoved.csv to test1.csv')
shutil.move('./testdata/testmoved.csv', './testdata/test1.csv')
for f in Path('./testdata').iterdir(): f


