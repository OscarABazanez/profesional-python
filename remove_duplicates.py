def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def run():
    random_list = [1,1,2,2,3,4]
    print('Usando un Ciclo for')
    print(remove_duplicates(random_list))

    print('-'*50)
    
    print('Usando el Set')
    print(set(random_list))

if __name__ == "__main__":
    run()