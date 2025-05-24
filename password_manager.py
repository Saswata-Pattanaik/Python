from cryptography.fernet import Fernet as fer

master_pwd = input("what is the master password: ")

def return_key():
    with open("key.key", 'rb') as key:
        key = key.read()
        return key

key = return_key()
cipher = fer(key)

def view():
    try:
        with open("password.txt",'r') as file:
            lines_collection = file.readlines()
            if not lines_collection:
                print("no password found")
                return
            for lines in lines_collection:
                lines = lines.rstrip()
                name , pwd = lines.split("|")
                pwd = cipher.decrypt(pwd.encode()).decode()
                print("name: ", name, "password: ", pwd)
    except Exception as e:
        print(e)
        print("no passwords found or decryption failed")

def add(name, password):
    password = cipher.encrypt(password.encode()).decode()
    with open("password.txt",'a') as pwd:
        final_password = str(name + '|' + password + '\n')
        pwd.write(final_password)

if __name__ == "__main__":
    while True:
        user_input = input("do you want to see the password or add password to the list or quit: (view/add/q) ")
        if user_input == "q":
            print("thank you for using")
            break
        if user_input == "view":
            view()
        if user_input == "add":
            name = input("write the username: ")
            password = input("write the password: ")
            add(name,password)