# User Class to store all the information about a specific user and their music
class User:
    # init to initialize the user with a name and music collection
    def __init__(self, name):
        self.name = name
        self.collection = {}  

    # function to add a song to the user's collection
    def add_song(self, title, artist):
        self.collection[title] = artist

    # function to retrieve a song by title
    def retrieve_song(self, title):
        return self.collection.get(title, None)

    # function to change the artist by title
    def update_song(self, title, new_artist):
        if title in self.collection:
            self.collection[title] = new_artist
            return True
        return False

    # function to delete a song by title
    def delete_song(self, title):
        if title in self.collection:
            del self.collection[title]
            return True
        return False

    # function to display all songs in the user's collection
    def display_songs(self):
        if not self.collection:
            print("\033[33mNo songs in the collection.\033[0m")
        else:
            for title, artist in self.collection.items():
                print(f"\033[34m{title}\033[0m by \033[36m{artist}\033[0m")

# variables to store all users as well as the current user. 
users = {}
current_user = None

while True:
    # main loop for the menu (checks if there is a current user and changes the menu accordingly)
    print("\n\033[1m=== Menu ===\033[0m")
    if current_user:
        print(f"\033[1;35m== User {current_user.name} ==\033[0m")
    print("1) \033[32mAdd user\033[0m")
    if current_user:
        print("2) \033[32mChange User\033[0m")
        print("3) \033[32mAdd a song\033[0m")
        print("4) \033[32mRetrieve song details\033[0m")
        print("5) \033[32mUpdate song details\033[0m")
        print("6) \033[32mDelete a song\033[0m")
        print("7) \033[32mDisplay all songs\033[0m")
    print("0) \033[31mExit\033[0m")
    choice = input("\033[1mEnter input here:\033[0m ")

    # choice 1 - adding a new user and checking if the user already exists
    if choice == "1":
        username = input("\033[1mEnter Username:\033[0m ")
        if username in users:
            print("\033[33mUser already exists.\033[0m")
        else:
            users[username] = User(username)
            print(f"\033[32mUser {username} added.\033[0m")
            if not current_user:
                current_user = users[username]
    
    # choice 2 - changing the current user from the list of users
    elif choice == "2" and current_user:
        if not users:
            print("\033[33mNo users available.\033[0m")
            continue
        print("\033[1mSelect user:\033[0m")
        usernames = list(users.keys())
        for i, name in enumerate(usernames, 1):
            print(f"{i}) \033[34m{name}\033[0m")

        try:
            index = int(input("\033[1mEnter input here:\033[0m ")) - 1
            current_user = users[usernames[index]]
            print(f"\033[32mSwitched to user {usernames[index]}.\033[0m")
        except (ValueError, IndexError):
            print("\033[31mInvalid selection.\033[0m")

    # choice 3 - add a song and the artist to a collection
    elif choice == "3" and current_user:
        title = input("\033[1mEnter song title:\033[0m ")
        artist = input("\033[1mEnter song artist:\033[0m ")
        current_user.add_song(title, artist)
        print("\033[32mSong added.\033[0m")

    # choice 4 - locate a song by title and provide the artist
    elif choice == "4" and current_user:
        title = input("\033[1mEnter song title:\033[0m ")
        artist = current_user.retrieve_song(title)
        if artist:
            print(f"\033[34m{title}\033[0m by \033[36m{artist}\033[0m")
        else:
            print("\033[33mSong not found.\033[0m")

    # choice 5 - change the artist of a song, searching by title
    elif choice == "5" and current_user:
        title = input("\033[1mEnter song title:\033[0m ")
        if title in current_user.collection:
            new_artist = input("\033[1mEnter new artist:\033[0m ")
            current_user.update_song(title, new_artist)
            print("\033[32mSong updated.\033[0m")
        else:
            print("\033[33mSong not found.\033[0m")

    # choice 6 - delete a song by title
    elif choice == "6" and current_user:
        title = input("\033[1mEnter song title:\033[0m ")
        if current_user.delete_song(title):
            print("\033[32mSong deleted.\033[0m")
        else:
            print("\033[33mSong not found.\033[0m")

    # choice 7 - display all songs for the current user
    elif choice == "7" and current_user:
        print("\033[1mSongs in your collection:\033[0m")
        current_user.display_songs()

    # choice 0 - exit the program
    elif choice == "0":
        print("\033[31mExiting program. Goodbye!\033[0m")
        break

    else:
        print("\033[31mInvalid selection. Please try again.\033[0m")
