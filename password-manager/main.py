from cryptography.fernet import Fernet

""" def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() """


def load_key():
    file = open("key.key", "rb")
    key = file.read
    file.close()
    return key


# master_pwd = input("What is the master password? ")
key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        #'r' mode is read
        for line in f.readlines():
            # rstrip() gets rid of \n
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        #'a' mode is append
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to ass a new password or view existing ones? (view or add) Press Q to quit. "
    ).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
