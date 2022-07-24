import pathlib
import time
import pickle

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
PATH_EAST = MODEL_DIR / 'rf_east.pkl'
PATH_WEST = MODEL_DIR / 'rf_west.pkl'

sensors_paths = {'P39355': PATH_EAST,
                 'P39285': PATH_EAST,
                 'P93745': PATH_EAST,
                 'P39497': PATH_WEST,
                 'P93927': PATH_WEST,
                 'P96317': PATH_WEST}


def correct_rf(raw_purple_data, sensor_id, date_time=None):

    purple_data = format_purple_data(raw_purple_data)

    if sensor_id in sensors_paths.keys():
        model_path = sensors_paths[sensor_id]
    else:
        raise


    init = time.time()
    loaded_rf = pickle.load(open(model_path, 'rb') )
    load_time = init - time.time()
    pred_init = time.time()
    correction = loaded_rf.predict(purple_data)
    pred_time = pred_init - time.time()
    return list(correction), load_time, pred_time


def format_purple_data(raw_data):
    pm25_a = raw_data['PM25_A']
    pm25_b = raw_data['PM25_B']
    humedad = raw_data['Humedad']
    presion = raw_data['Presion']
    temperatura = raw_data['Temperatura']

    return [[pm25_a, pm25_b, humedad, presion, temperatura]]