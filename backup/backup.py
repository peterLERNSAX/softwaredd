"""
Backup
"""
import sys
import sqlite3
import io
from datetime import date

def main()->None:
    """main"""
    if "lager" in sys.argv:
        backup_lagerdb()
    if "user" in sys.argv:
        backup_userdb()

# Open() function
def backup_lagerdb()->None:
    """Backup lagerdb""" 
    path = f"lagerdb/backup_lager-{date.today()}.sql"
    conn = sqlite3.connect('../api/lager.db')
    with io.open(path, 'w') as p:
        # iterdump() function
        for line in conn.iterdump():
            p.write('%s\n' % line)

    print(' Backup performed successfully!')
    print(f' Data Saved as {path}')

    conn.close()

def backup_userdb()->None:
    """Backup user""" 
    path = f"userdb/backup_user-{date.today()}.sql"
    conn = sqlite3.connect('../softwaredd/db.sqlite3')
    with io.open(path, 'w') as p:
        # iterdump() function
        for line in conn.iterdump():
            p.write('%s\n' % line)

    print(' Backup performed successfully!')
    print(f' Data Saved as {path}')

    conn.close()

if __name__ == "__main__":
    main()
