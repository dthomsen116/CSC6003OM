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
            print("No songs in the collection.")
        else:
            for title, artist in self.collection.items():
                print(f"{title} by {artist}")

# variables to store all users as well as the current user. 
users = {}
current_user = None

while True:
    # main loop for the menu (checks if there is a current user and changes the menu accordingly)
    print("\n===Menu===")
    if current_user:
        print(f"==User {current_user.name}==")
    print("1) Add user")
    if current_user:
        print("2) Change User")
        print("3) Add a song")
        print("4) Retrieve song details")
        print("5) Update song details")
        print("6) Delete a song")
        print("7) Display all songs")
    print("0) Exit")
    choice = input("Enter input here: ")

    # choice 1 - adding a new user and checking if the user already exists
    if choice == "1":
        username = input("Enter UserName: ")
        if username in users:
            print("User already exists.")
        else:
            users[username] = User(username)
            print(f"User {username} added.")
            if not current_user:
                current_user = users[username]
    
    # choice 2 - changing the current user from the list of users
    elif choice == "2" and current_user:
        if not users:
            print("No users available.")
            continue
        print("Select user:")
        usernames = list(users.keys())
        for i, name in enumerate(usernames, 1):
            print(f"{i}) {name}")

        try:
            index = int(input("Enter input here: ")) - 1
            current_user = users[usernames[index]]
            print(f"Switched to user {usernames[index]}.")
        except (ValueError, IndexError):
            print("Invalid selection.")

    # choice 3 - add a song and the artist to a collection
    elif choice == "3" and current_user:
        title = input("Enter song title: ")
        artist = input("Enter song artist: ")
        current_user.add_song(title, artist)
        print("Song added.")

    # choice 4 - locate a song by title and provide the artist
    elif choice == "4" and current_user:
        title = input("Enter song title: ")
        artist = current_user.retrieve_song(title)
        if artist:
            print(f"{title} by {artist}")
        else:
            print("Song not found.")

    # choice 5 - change the artist of a song, searching by title
    elif choice == "5" and current_user:
        title = input("Enter song title: ")
        if title in current_user.collection:
            new_artist = input("Enter new artist: ")
            current_user.update_song(title, new_artist)
            print("Song updated.")
        else:
            print("Song not found.")

    # choice 6 - delete a song by title
    elif choice == "6" and current_user:
        title = input("Enter song title: ")
        if current_user.delete_song(title):
            print("Song deleted.")
        else:
            print("Song not found.")

    # choice 7 - display all songs for the current user
    elif choice == "7" and current_user:
        print("Songs in your collection:")
        current_user.display_songs()

    # choice 0 - exit the program
    elif choice == "0":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid selection. Please try again.")
