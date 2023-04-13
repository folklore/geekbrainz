class Listik:
    def __init__(self, value = None):
        if(value != None):
            self.head = self.Nodka(value)
        else:
            self.head = None


    class Nodka:
        def __init__(self, value):
            self.value = value
            self.next = None


    def add(self, value):
        nodka = self.Nodka(value)

        if(self.head):
            nodka.next = self.head
        self.head = nodka


    def print(self):
        nodka = self.head
        print(nodka.value)

        while(nodka.next):
            nodka = nodka.next
            print(nodka.value)


    def reverse(self):
        prev_nodka = None
        crnt_nodka = self.head
        next_nodka = None

        while(crnt_nodka):
            next_nodka = crnt_nodka.next

            crnt_nodka.next = prev_nodka
            prev_nodka = crnt_nodka

            crnt_nodka = next_nodka

            if crnt_nodka:
                self.head = crnt_nodka



listik = Listik(1)

for i in range(2, 6):
    listik.add(i)

print('Original')
listik.print()

listik.reverse()

print('Reversed')
listik.print()


# sg@mbp ads % python3 3.py
# Original
# 5
# 4
# 3
# 2
# 1
# Reversed
# 1
# 2
# 3
# 4
# 5
# sg@mbp ads % 
