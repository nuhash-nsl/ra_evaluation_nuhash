class LaptopBrand(object):
     def __init__(self, floors=100):
         self._floors = [None]*floors

     def __setitem__(self, floor_number, data):
          self._floors[floor_number] = data

     def __getitem__(self, floor_number):
          return self._floors[floor_number]

if __name__ == "__main__":
    laptopBrand = LaptopBrand()

    laptopBrand[0] = 'LENOVO'
    laptopBrand[1] = 'Asus'
    laptopBrand[2] = 'DELL'
    
    print(laptopBrand[2])