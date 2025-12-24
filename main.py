from Merchant import Merchant
import json
from UsersDb import UsersDb

def main():
    db = UsersDb.read_file('data.json')
    print(db)

if __name__ == '__main__':
    main()