
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

def print_object_attributes(data, attributes, level):
    for a in attributes:
        print("%s : %d" %(a, level))

def object_level_traversing(data, level):
    # let's get the attributes dynamically
    # if not a.startswith('__') - this will filter out the special methods
    # not callable(getattr(data, a)) - this will filter out the methods, as we only care about the object properties
    attributes = [a for a in dir(data) if not a.startswith('__') and not callable(getattr(data, a))]
    
    print_object_attributes(data, attributes, level)

    for attribute in attributes:
        val = getattr(data, attribute)
        key = attribute

        if isinstance(val, dict): # in case object attribute has dictionary as value
          print("%s : %d" %(key, level))
          dictionary_level_traversing(val, level + 1)

        elif isinstance(val, Person): # if val is another object
            object_level_traversing(val, level + 1)
        

def dictionary_level_traversing(data, level):
    for key, val in data.items():
        if isinstance(val, dict):
            print("%s : %d" %(key, level))
            dictionary_level_traversing(val, level + 1)
        elif isinstance(val, Person):
            print("%s : %d" %(key, level))
            object_level_traversing(val, level + 1)
        else:
            print("%s : %d" %(key, level))
    return

def print_depth(data):
    dictionary_level_traversing(data, 1)
    
if __name__ == '__main__':
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)

    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
                "user": person_b
            }
        }
    }
    print_depth(a)


