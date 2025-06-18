# Class for the Folder structure
class Folder:

    # initialization of the Folder class
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subfolders = []

    # func to add a file to the folder
    def addFile(self, fileName):
        self.files.append(fileName)


    # func to add subfolder to the folder
    def addSubfolder(self, folder):
        if not any(f.name == folder.name for f in self.subfolders):
            self.subfolders.append(folder)
            print(f"\033[32mFolder '{folder.name}' added.\033[0m")
        else:
            print(f"\033[33mFolder '{folder.name}' already exists.\033[0m")

    # func to show all of the folders in the structure
    def getAllFolders(self, prefix=""):
        folders = [(prefix + self.name, self)]
        for sub in self.subfolders:
            folders.extend(sub.getAllFolders(prefix + self.name + " > "))
        return folders

    # func to count the number of files in the folder and its subfolders
    def __countFiles(self):
        count = len(self.files)
        for folder in self.subfolders:
            count += folder.__countFiles()
        return count

    # func to check if the folder is equal to another folder or string (data validation)
    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        return False

    # func to get the length of the folder (number of files)
    def __len__(self):
        return self.__countFiles()

    # func to get the string representation of the folder and its contents
    def __str__(self, indent=0):
        result = " " * indent + f"\033[1;34m--Folder: {self.name}\033[0m\n"
        for file in self.files:
            result += " " * (indent + 2) + f"\033[35m--File: {file}\033[0m\n"
        for folder in self.subfolders:
            result += folder.__str__(indent + 2)
        return result

# Main Menu
def showMenu(currentFolderName):
    print("\n\033[1m=== Menu ===\033[0m")
    print(f"\033[1;35m== Current Folder: {currentFolderName} ==\033[0m")
    print("1) \033[32mAdd File\033[0m")
    print("2) \033[32mAdd Folder\033[0m")
    print("3) \033[32mSelect Folder\033[0m")
    print("4) \033[32mPrint Folder\033[0m")
    print("0) \033[31mExit\033[0m")

# main loop
def main():
    root = Folder("Root")
    currentFolder = root

    while True:
        showMenu(currentFolder.name)
        choice = input("\033[1mUser Input:\033[0m ")

        # add a file to the current folder
        if choice == "1":
            fileName = input("\033[1mEnter file name:\033[0m ")
            currentFolder.addFile(fileName)
            print("\033[32mFile added.\033[0m")

        # add a subfolder to the current folder
        elif choice == "2":
            folderName = input("\033[1mEnter folder name:\033[0m ")
            newFolder = Folder(folderName)
            currentFolder.addSubfolder(newFolder)

        # select a subfolder from the current folder (by making a menu to select from instead of typing the name for user experience)
        elif choice == "3":
            allFolders = root.getAllFolders()
            print("\n\033[1mAvailable Folders:\033[0m")
            for i, (path, folderObj) in enumerate(allFolders):
                print(f"{i + 1}) \033[34m{path}\033[0m")

            try:
                selection = int(input("\033[1mSelect folder by number:\033[0m ")) - 1
                if 0 <= selection < len(allFolders):
                    currentFolder = allFolders[selection][1]
                    print(f"\033[32mSwitched to folder '{currentFolder.name}'.\033[0m")
                else:
                    print("\033[31mInvalid number selected.\033[0m")
            except ValueError:
                print("\033[31mPlease enter a valid number.\033[0m")

        # print the root folder and its contents
        elif choice == "4":
            print(currentFolder.__str__())

        # exit the loop/program
        elif choice == "0":
            print("\033[31mExiting. Goodbye!\033[0m")
            break

        # error handling for invalid input
        else:
            print("\033[31mInvalid selection. Please try again.\033[0m")

if __name__ == "__main__":
    main()


