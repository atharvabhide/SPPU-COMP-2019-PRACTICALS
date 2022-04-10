# chaining method

SIZE = 100

class Node:
    def __init__(this, data, next):
        this.data = data
        this.next = None
        
def insert(head, data):
    node = Node(data, None)
    if (head == None):
        return node
    temp = head
    while (temp.next != None):
        temp = temp.next
    temp.next = node
    return head
        
class HashTableC:
    ht = []
    def __init__(this):
        for i in range(SIZE):
            node = Node(-1, None)
            this.ht.append(node)
    def hashFunction(this, data):
        return (data % SIZE)
    def insert(this, data):
        index = this.hashFunction(data)
        if (this.ht[index].data == -1):
            print("No collision occurred while inserting")
            this.ht[index].data = data
        else:
            print("Collision occurred while inserting!")
            node = this.ht[index]
            node = insert(node, data)
    def printHashTable(this):
        for i in range(SIZE):
            if (this.ht[i].data != -1):
                temp = this.ht[i]
                while (temp.next != None):
                    print(temp.data, end = "->")
                    temp = temp.next
                print(temp.data)
    def search(this, data):
        index = this.hashFunction(data)
        temp = this.ht[index]
        while (temp != None):
            if (temp.data == -1):
                print("Phone Number not present in the directory!")
                return
            elif (temp.data == data):
                print("Phone Number found in the directory!")
                return
            temp = temp.next
        print("Phone Number not present in the directory!")
        
# linear probing
        
class HashTableLP:
    ht = []
    def __init__(this):
        for i in range(SIZE):
            this.ht.append(-1)
    def hashFunction(this, data):
        return (data % SIZE)
    def insert(this, data):
        index = this.hashFunction(data)
        if (this.ht[index] == -1):
            print("No collision occurred while inserting")
            this.ht[index] = data
        else:
            print("Collision occurred while inserting")
            flag = False
            while (1):
                if (index == SIZE):
                    index = 0
                if (this.ht[index] == -1):
                    this.ht[index] = data
                    flag = True
                    return
                index += 1
            if (flag == False):
                print("The directory is full!")
    def printHashTable(this):
        for i in range(SIZE):
            if (this.ht[i] != -1):
                print(this.ht[i])
    def search(this, data):
        index = this.hashFunction(data)
        if (this.ht[index] == data):
            print("Phone Number found in the directory!")
            return
        temp = index
        index += 1
        while (1):
            if (index == SIZE):
                index = 0
            if (index == temp):
                print("Phone Number not found in the directory!")
                break
            if (this.ht[index] == data):
                print("Phone Number found in the directory!")
                flag = True
                break
            index += 1
        
method = int(input("Enter 1 for chaining method \nEnter 2 for linear probing method\n"))
if (method == 1):
    ht = HashTableC()
elif (method == 2):
    ht = HashTableLP()
else:
    print("Please enter a valid method!")
        
while (1):
    choice = int(input("Enter 1 to insert a Phone Number in the directory \nEnter 2 to search a Phone Number in the directory \nEnter 3 to Print the directory \nEnter 4 to quit \n"))
    if (choice == 1):
        n = int(input("Enter the count of Phone Numbers to be inserted-\n"))
        for i in range(n):
            x = int(input("Enter the Phone Number to be inserted-\n"))
            if (len(str(x)) != 10):
                print("Please enter a valid number!")
            else:
                ht.insert(x)
    elif (choice == 2):
        x = int(input("Enter the Phone Number to be searched in the directory-\n"))
        ht.search(x)
    elif (choice == 3):
        ht.printHashTable()
    elif (choice == 4):
        print("Thanks for trying out my code :) ")
        break
    else:
        print("Please Enter a valid choice!")
