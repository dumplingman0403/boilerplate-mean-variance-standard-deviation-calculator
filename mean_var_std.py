import numpy as np

def calculate(in_list):
    if (len(in_list) != 9):
        raise ValueError('List must contain nine numbers.')
    print(in_list)
    np_list = np.reshape(in_list, (3, 3))
    

    mean = [np_list.mean(axis=0).tolist(), np_list.mean(axis=1).tolist(), np_list.mean()]
    variance = [np.var(np_list, axis=0).tolist(), np.var(np_list, axis=1).tolist(), np.var(np_list)]
    sd = [np.std(np_list, axis=0).tolist(), np.std(np_list, axis=1).tolist(), np.std(np_list)]
    l_max = [np.max(np_list, axis=0).tolist(), np.max(np_list, axis=1).tolist(), np.max(np_list)]
    l_min = [np.min(np_list, axis=0).tolist(), np.min(np_list, axis=1).tolist(), np.min(np_list)]
    l_sum = [np.sum(np_list, axis=0).tolist(), np.sum(np_list, axis=1).tolist(), np.sum(np_list)]

    calculations = {
        'mean': mean,
        'variance': variance,
        'standard deviation': sd,
        'max': l_max,
        'min': l_min,
        'sum': l_sum
    }

    return calculations

