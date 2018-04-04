#!/usr/bin/python3

import datetime
from lib.config import Config

class BackupNameFormatter:

    def __init__(self):
        self._config = Config()

    def _get_current_formatted_time(self):
        return datetime.datetime.now().strftime("_%d_%m_%Y__%Hh%M")

    def get_current_backup_filename(self):
        return self._config.BACKUP_FILENAME + self._get_current_formatted_time() + '.sql'
