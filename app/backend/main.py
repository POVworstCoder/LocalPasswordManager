import webview

from database.create.create_db import create_db
from database.find.user_db_find import find_all, find_by_id
from database.edit.user_db_edit import create_account, edit_account_id_column

#create_account("Leandro","leandro.mani@liip.ch","test.ch","password12345!")

find_all()


class Api:
    def createDatabase(self):
        create_db()

    def findAll(self):
        find_all()

    def findById(self,id):
        find_by_id(id)

    def createAccount(self,username,email,site_url,password):
        create_account(username,email,site_url,password)

    def editAccountByIdAndColumn(self,id,column,data):
        edit_account_id_column(id,column,data)

def main():
    webview.create_window(
        "Vue + Python Desktop App",
        "frontend/dist/index.html",
        js_api=Api()
    )
    webview.start()

if __name__ == "__main__":
    main()
