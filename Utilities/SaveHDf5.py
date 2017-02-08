

#saves savedata in dataSet at path file.
#path <- file path
#saveData <- data to be saved
#dataSet <- the dataset to be opened
#group <- the group to save the dataset in
def saveAt(path, savedata = None, dataSet = None, group = None):
    import h5py
    import numpy as np

    checkPath(path)

    if savedata is None and dataSet is None and group is None: #case with just filename
        data1 = np.random.random(size=(10, 10))
        with h5py.File(path + '.h5', 'a') as hf:
            hf.create_dataset('testData', data=data1)
    elif savedata is None and group is None:   #case with filename and data
        with h5py.File(path + '.h5', 'a') as hf:
            hf.create_dataset('testData', data=savedata)
    elif group is None:#case with filename, data, and dataset name to store it in
        with h5py.File(path + '.h5', 'a') as hf:
            hf.create_dataset(dataSet, data=savedata)
    else:
        with h5py.File(path + '.h5', 'a') as hf:#case with filename, data, dataset name, and group
            if group not in hf.keys():
                hf.create_group(group)
            g1 = hf.get(group)
            g1.create_dataset(dataSet, data = savedata)


def saveGroup(path, group):
    import h5py

    with h5py.File(path + '.h5', 'a') as hf:
         hf.create_group(group)

#lists the keys of a file
def listKeys(fileName, group = None):
    import h5py
    if group is None:
        with h5py.File(fileName + '.h5', 'a') as hf:
            print(list(hf.keys()))
    else:
        with h5py.File(fileName + '.h5', 'a') as hf:
            g1 = hf.get(group)
            print(list(g1.keys()))

def loadData(fileName, dataSet, group = None):
    import h5py
    if group is None:
        with h5py.File(fileName + '.h5', 'r') as hf:
            data = hf.get(dataSet)
    else:
        with h5py.File(fileName + '.h5', 'r') as hf:
            g1 = hf.get(group)
            data = g1.get(dataSet)
    return data

def checkPath(path):
    path = path[:path.rfind("/")]
    import os
    import errno

    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise



