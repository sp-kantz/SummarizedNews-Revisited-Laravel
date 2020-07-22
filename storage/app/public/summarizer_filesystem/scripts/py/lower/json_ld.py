import json, os

dir_path = os.path.dirname(__file__)

clean = os.path.join(dir_path, '../../files/working/clean_articles/')

#paths to directories
paths = {
        #path to dataset (cleaned json format) directory  
        'clean' : os.path.join(dir_path, '../../../files/working/clean_articles/'),
        #path to summaries directory
        'summaries' : os.path.join(dir_path, '../../../files/working/summaries/'),
        #path to mapping directory
        'mapping' : os.path.join(dir_path, '../../../files/working/mapping/')
    }

#open json file, return data
def get_data(path, filename):

    #read the file
    with open(paths[path] + filename) as file_read:
        data = json.load(file_read)
    file_read.close()

    return data

#save data to json file
def store_data(path, filename, data):

    with open(paths[path] + filename + '.json', "w") as file_write:
        json.dump(data, file_write)
    file_write.close()
