from module2 import max_of_three
import pickle


def create_db_pickle(result):
    with open('max_of_three.pickle', 'wb') as file:
        my_dict = dict()
        my_dict['max_func_from_module2'] = result
        pickle.dump(my_dict, file, pickle.HIGHEST_PROTOCOL)


def load_db_pickle():
    create_db_pickle(max_of_three(7, 8, 9))
    with open('max_of_three.pickle', 'rb') as file:
        my_file = pickle.load(file)
        print(my_file)
