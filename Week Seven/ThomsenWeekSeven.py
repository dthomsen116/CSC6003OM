class CreatureNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class CreatureTree:
    def __init__(self):
        self.root = None

    def addRoot(self, name):
        if self.root is None:
            self.root = CreatureNode(name)
            print(f"\033[36mRoot '{name}' added.\033[0m")
        else:
            print("\033[33mRoot already exists.\033[0m")

    def getAllNodes(self):
        nodes = []
        self._collectNodes(self.root, nodes)
        return nodes

    def _collectNodes(self, node, nodes):
        if node is not None:
            nodes.append(node)
            self._collectNodes(node.left, nodes)
            self._collectNodes(node.right, nodes)

    def addChild(self, parentNode, childName, direction):
        if direction.upper() == "L":
            if parentNode.left is None:
                parentNode.left = CreatureNode(childName)
                print(f"\033[32m'{childName}' added to the LEFT of '{parentNode.name}'.\033[0m")
            else:
                print("\033[33mLeft child already exists.\033[0m")
        elif direction.upper() == "R":
            if parentNode.right is None:
                parentNode.right = CreatureNode(childName)
                print(f"\033[32m'{childName}' added to the RIGHT of '{parentNode.name}'.\033[0m")
            else:
                print("\033[33mRight child already exists.\033[0m")
        else:
            print("\033[31mInvalid direction. Use 'L' or 'R'.\033[0m")

    def printTree(self, node=None, indent="", isLeft=True):
        if node is None:
            node = self.root
            if not node:
                print("\033[33mTree is empty.\033[0m")
                return
            print("\n\033[35m=== Creature Tree ===\033[0m")

        if node.right:
            self.printTree(node.right, indent + ("│   " if isLeft else "    "), False)

        print(indent + ("└── " if isLeft else "┌── ") + f"\033[36m{node.name}\033[0m")

        if node.left:
            self.printTree(node.left, indent + ("    " if isLeft else "│   "), True)

        if indent == "":
            print("\033[35m======================\033[0m")

    def findAncestors(self, node, targetName, path):
        if node is None:
            return False
        if node.name == targetName:
            return True
        if (self.findAncestors(node.left, targetName, path) or
                self.findAncestors(node.right, targetName, path)):
            path.append(node.name)
            return True
        return False

    def printAncestors(self, name):
        path = []
        if self.findAncestors(self.root, name, path):
            lineage = " who is descended from the ".join(reversed(path))
            print(f"\033[34mThe {name} is descended from the {lineage}.\033[0m")
        else:
            print(f"\033[31m{name} not found in the tree.\033[0m")


def displayNodeSelectionMenu(nodes):
    print("\n\033[35m=== Select Parent Node ===\033[0m")
    for i, node in enumerate(nodes):
        print(f"{i}) {node.name}")
    print("=================================")
    while True:
        try:
            selection = int(input("\033[35mUser Input: Select node #: \033[0m"))
            if 0 <= selection < len(nodes):
                return nodes[selection]
            else:
                print("\033[31mInvalid selection. Please enter a number from the list.\033[0m")
        except ValueError:
            print("\033[31mInvalid input. Please enter a valid number.\033[0m")


def main():
    tree = CreatureTree()

    while True:
        print("\n\033[35m=== Menu ===\033[0m")
        if tree.root is None:
            print("0) Add Root Creature")
        else:
            print("1) Add Creature")
            print("2) Print All")
            print("3) Print Specific")
        print("=============")
        choice = input("\033[35mUser Input: \033[0m")

        if choice == "0" and tree.root is None:
            name = input("\033[35mName: \033[0m")
            tree.addRoot(name)

        elif choice == "1":
            nodes = tree.getAllNodes()
            if not nodes:
                print("\033[31mNo nodes available.\033[0m")
                continue

            parent = displayNodeSelectionMenu(nodes)

            direction = input("\033[35mUser Input (L/R): \033[0m").strip().upper()
            while direction not in ["L", "R"]:
                print("\033[31mInvalid direction. Enter 'L' or 'R'.\033[0m")
                direction = input("\033[35mUser Input (L/R): \033[0m").strip().upper()

            name = input("\033[35mCreature name: \033[0m")
            tree.addChild(parent, name, direction)

        elif choice == "2":
            tree.printTree()

        elif choice == "3":
            name = input("\033[35mNode name: \033[0m")
            tree.printAncestors(name)

        else:
            print("\033[31mInvalid selection or root already exists.\033[0m")


if __name__ == "__main__":
    main()
