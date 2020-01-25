
def dictionary_level_traversing(data, level):
    for key, val in data.items():
        if isinstance(val, dict):
            print("%s : %d" %(key, level))
            dictionary_level_traversing(val, level + 1)
        else:
            print("%s : %d" %(key, level))
    return

def print_depth(data):
    dictionary_level_traversing(data, 1)
    
if __name__ == '__main__':
    a = {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4
            }
        }
    }

    print_depth(a)


