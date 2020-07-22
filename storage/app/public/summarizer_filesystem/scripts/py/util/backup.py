#backup files from previous run, clean the database tables

import os, time, subprocess

dir_path = os.path.dirname(__file__)

#timestamp used as directory name for backup
backuptime = time.strftime('%d_%m_%Y_%H_%M_%S', time.localtime())
#path to working directory
working_dir = os.path.join(dir_path, '../../../files/working/')
#path to backup directory
backup_dir = os.path.join(dir_path, '../../../files/backup/')

#directories to backup
system_paths = [
    'dataset',
    'clean_articles',
    'mapping',
    'summaries',
    ]

#for every directory
for i, path in enumerate(system_paths):

    #path to backup directory 
    backup = backup_dir + backuptime + '/' + path
    #create directory
    os.makedirs(backup, exist_ok = True)
    #list of files to move
    file_list = os.listdir(working_dir + path)

    #every file
    for file in file_list:
        #move it to backup directory
        os.replace(working_dir + path + '/' + file, backup + '/' + file)
    #re-create working directory
    os.makedirs(working_dir + path, exist_ok = True)


