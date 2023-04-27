"""
restore
"""

import sys
import os

def main()->None:
    """main"""
    if sys.argv[1] == "lager":
        restore_lagerdb(sys.argv[2])
    if sys.argv[1] == "user":
        restore_user(sys.argv[2])

def restore_lagerdb(path:str)->None:
    """restore lagerdb"""
    os.system(f"sqlite3 ../api/lager.db < {path}")

def restore_user(path:str)->None:
    """restore userdb"""
    os.system(f"sqlite3 ../softwaredd/db.sqlite3 < {path}")

if __name__ == "__main__":
    main()