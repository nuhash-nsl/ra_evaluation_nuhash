import operator
def sort_multivalue_list(listo):
    """Sort multivalue list of dictionary according to attribute priority age>name>country
    Args:
        listo (List): Input List
    Returns:
        List: Sorted List
    """
    new_list = sorted(listo, key=lambda x: (x['age'], x['name'], x['country']))
    return new_list


if __name__ == "__main__":

    #our list of dictionary
    persons = [
    {
    "name": "Zohn",
    "age": 37,
    "country": "Zorway"
    },
    {"name": "Zohn",
    "age": 37,
    "country": "Dorway"
    },
    {"name": "Dan",
    "age": 39,
    "country": "Aorway"
    },
    {"name": "Dan",
    "age": 50,
    "country": "Borway"
    }
    ]
    
    print(sort_multivalue_list(persons))