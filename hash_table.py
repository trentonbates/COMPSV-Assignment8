class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return self.name + ': ' + self.number 

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''
    
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        if current is None:
            self.data[index] = Node(key, value)
            return
        
        while current:
            if current.key == key:
                current.value = value
                return
            
            if current.next is None:
                break

            current = current.next

        current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for i in range(len(self.data)):
            current = self.data[i]
            result = ''

            if current == None:
                print(f'Index {i}: Empty')
                continue

            while current:
                result += f' - {current.key}: {current.value}'
                current = current.next
            
            print(f'Index {i}: {result}')

'''
Why is a hash table the right structure for fast lookups?

    A hash table is ideal for fast lookups because it uses a hash function
    to convert a key (in this case, a contact's name) into an index within
    an array. This allows for direct access to stored data, typically providing
    average-case time complexity of O(1) for insertion, search, and update
    operations. Unlike lists, which require linear searches (O(n)), a hash table
    can locate a contact almost instantly, regardless of how many contacts exist.
    This makes it especially useful for applications like contact management, where
    quick retrieval of information by a unique key (such as a name) is essential.

How did you handle collisions?

    Collisions occur when two different keys hash to the same index. In this
    implementation, collisions are handled using separate chaining with linked
    lists. Each index in the hash table stores a linked list of Node objects.
    When a new contact hashes to an occupied index, it is added to the end of the
    linked list. During lookups or updates, the program traverses this list to find
    the matching key. This method is simple, efficient, and prevents data loss caused
    by overwriting existing entries.

When might an engineer choose a hash table over a list or tree?

    An engineer would choose a hash table when speed and simplicity are more important
    than maintaining order. Hash tables excel in applications that require frequent
    insertions, deletions, and lookups by key, such as dictionaries, caches, or contact
    books. In contrast, lists are better for maintaining sequential data, and trees are
    preferred when sorted order or range queries are required.
'''

contact_1 = Contact("Riley", "123-456-7890")
print(contact_1) # Riley: 123-456-7890

contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key) # Riley
print(node_1.value) # Riley: 123-456-7890
print(node_1.next) # None

table = HashTable(10)
table.print_table()

# Add some values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()

# Search for a value
contact = table.search("John") 
print("\nSearch result:", contact)  # Search result: John: 909-876-1234

# Edge Case #1 - Hash Collisons (assuming these hash to the same index) 
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()

# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()

# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris")) # None