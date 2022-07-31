# super class
class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
# child class
class FlowerImage(Image):
    def __init__(self, width, height, flower_name):
        self.flower_name = flower_name
        super().__init__(width, height)

if __name__ == "__main__":
    img = Image(100,100)
    print(img.__dict__)
    img_derived = FlowerImage(122,122,"rose")
    print(img_derived.__dict__)