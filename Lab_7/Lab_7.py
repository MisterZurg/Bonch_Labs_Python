class Tree:
   def __init__(self, kind, height):
       self.kind = kind
       self.age = 0
       self.height = height

   def info(self):
       print("{}, возраст:{} лет, высота: {} метров.".format(self.kind, self.age, self.height))

class TreeGrow(Tree):
   def __init__(self, kind, height):
       super().__init__(kind, height)  # super - инициализация родителя

   def grow(self):
       self.age += 1
       self.height += 0.5
       print("Дерево выросло")
Tree_1 = TreeGrow("Яблоня", 0.5)
Tree_1.info()
Tree_1.grow()
Tree_1.info()