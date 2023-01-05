class point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        print(class_name, "destroyed")
        
