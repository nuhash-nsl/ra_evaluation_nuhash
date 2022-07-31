class Layer:
    def __init__(self, name):
        self.name = name
    def __call__(self,val):
        self.name = val
        return self.name


if __name__ == "__main__":
    layer = Layer("custom layer name")
    image = "parameter"
    print(layer(image))