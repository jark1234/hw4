class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

class Circle(Base):
    def __init__(self, x, y, size):
        super().__init__(x, y, size)

    def draw(self):
        return f"""
           , - ~ ~ ~ - ,
       , '               ' ,
     ,                       ,
    ,                         ,
   ,                           ,
   ,                           ,
   ,                           ,
    ,                         ,
     ,                       ,
       ,                  , '
         ' - , _ _ _ ,  '
                """
    
    def shape(self):
        return f"({self.x}, {self.y})\n{self.size}"

def main():
    c = Circle(1, 2, 3)
    print(c.shape())
    print(c.draw())

main()

