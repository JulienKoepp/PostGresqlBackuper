#!/usr/bin/python3

import configparser

class Config:
    _CONFIG_FILE_PATH='/media/cloudshell/main_data/applications/postgres_backuper/config_backup.ini'

    _BACKUP_SECTION_KEY = 'Backup'
    _BACKUP_FOLDER_KEY = 'backup_folder'
    _BACKUP_FILENAME_KEY = 'backup_filename'
    _DATABASE_NAME_KEY = 'database_name'

    _COMPRESSION_SECTION_KEY = 'Compression'
    _NB_CORES_FOR_COMPRESSING_KEY = 'nb_cores_for_compressing'

    _GARBAGE_COLLECTOR_SECTION_KEY = 'Garbage Collector'
    _MAX_NB_BACKUPS_TO_KEEP_KEY = 'max_nb_backups_to_keep'


    def __init__(self):
        parser = configparser.ConfigParser()
        parser.read(self._CONFIG_FILE_PATH)

        self.BACKUP_FOLDER = parser.get(self._BACKUP_SECTION_KEY, self._BACKUP_FOLDER_KEY)
        self.BACKUP_FILENAME = parser.get(self._BACKUP_SECTION_KEY, self._BACKUP_FILENAME_KEY)
        self.DATABASE_NAME = parser.get(self._BACKUP_SECTION_KEY, self._DATABASE_NAME_KEY)

        self.NB_CORES_FOR_COMPRESSING = int(parser.get(self._COMPRESSION_SECTION_KEY, self._NB_CORES_FOR_COMPRESSING_KEY))

        self.MAX_NB_BACKUPS_TO_KEEP = int(parser.get(self._GARBAGE_COLLECTOR_SECTION_KEY, self._MAX_NB_BACKUPS_TO_KEEP_KEY))
