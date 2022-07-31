import os

def file_traverse(root_dir):
    """ Traverse in directory and prints file path.

    Args:
        root_dir (string): file path that is to be traversed
    """
    file_list = os.listdir(root_dir)
    for i in file_list:
        if not i.endswith('.txt'):
            file_path = root_dir + "/" +str(i)
            print(file_path)
            file_traverse(file_path)
        else:
            print(root_dir + "/" + str(i))

FILE_PATH = "./test"

if __name__ == "__main__":
    file_traverse(FILE_PATH)