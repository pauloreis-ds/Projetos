import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bedroom, bathroom):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    data = np.zeros(len(__data_columns))
    data[0] = bedroom
    data[1] = bathroom
    data[2] = sqft
    if loc_index >= 0:
        data[loc_index] = 1

    return round(__model.predict([data])[0], 2)


def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/Recife_Imóveis_Model_columns.json", 'r') as file:
        __data_columns = json.load(file)['data_columns']
        __locations = __data_columns[3:]

    with open('./artifacts/Recife_Imóveis_Model.pkl', 'rb') as file:
        __model = pickle.load(file)


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == "__main__":
    load_saved_artifacts()
