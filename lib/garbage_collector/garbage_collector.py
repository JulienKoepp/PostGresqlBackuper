#!/usr/bin/python3

from lib.file_manager import force_write_string, read_all_lines, file_exists
from lib.config import Config
from os import system as run
from lib.colored_messages import print_error_message

class GarbageCollector:


    def __init__(self):
        self.config = Config()
        self.BACKUP_ENTRIES_FILE_PATH = self.config.BACKUP_FOLDER + '/backup_entries.txt'
        self._load_self_from_persistence()

    def register_backup(self, backup_filepath):
        self.backup_entries.append(backup_filepath)
        self._collect_garbage()

    def _collect_garbage(self):
        if len(self.backup_entries) > self.config.MAX_NB_BACKUPS_TO_KEEP:
            if run('rm ' + self.backup_entries[0]) == 0:
                self.backup_entries.pop(0)
            else:
                print_error_message('unable to delete oldest backup')
                exit(-6)
        self._save_self_to_persistance()


    def _load_self_from_persistence(self):
        self.backup_entries = []

        if file_exists(self.BACKUP_ENTRIES_FILE_PATH):
            lines = read_all_lines(self.BACKUP_ENTRIES_FILE_PATH)
            for line in lines:
                if line.find('/') != -1: #line should be a path and not blank
                    self.backup_entries.append(line.rstrip())#rstrip removes \n at the end of line

    def too_many_backups(self):
        return len(self.backup_entries) >= self.config.MAX_NB_BACKUPS_TO_KEEP

    def get_latest_backup_path(self):
        return self.backup_entries[-1]


    def _save_self_to_persistance(self):
        text_to_save = ''
        for entry in self.backup_entries:
            text_to_save += entry
            text_to_save += "\n"
        force_write_string(text_to_save, self.BACKUP_ENTRIES_FILE_PATH)
