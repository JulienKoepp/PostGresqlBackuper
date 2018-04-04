#!/usr/bin/python3

from lib.garbage_collector.garbage_collector import GarbageCollector
from lib.config import Config
from lib.file_manager import file_exists
from os import system as run
from lib.colored_messages import print_ok, print_error_message
from lib.advanced_printf import print_no_return as nor_print
import getpass
import sys

# - - - - error codes - - - -
#
#  0 = success
# -1   backup file does not exist or there are no backups
# -2   unable to uncompress backup file
# -3   unable to fill DB with backup data
# -4   unable to delete uncompressed backup

config = Config()
backup_filepath = ''
garbage_collector = GarbageCollector()

if len(sys.argv) > 1: #a backup path was given
    backup_filepath = sys.argv[1]
else:#no backup path given, restore latest backup
    backup_filepath = garbage_collector.get_latest_backup_path()

backup_filepath = backup_filepath.rstrip()
uncompressed_filepath = backup_filepath.replace('.7z', '', 1)


nor_print("\n" + 'preparing to restore backup  ' + backup_filepath + ' for database ' + config.DATABASE_NAME + ' ...')
if not file_exists(backup_filepath):
    print_error_message('backup file does not exist or there are no backups')
    exit(-1)

nor_print("\n" + 'uncompressing backup file...')
if run('/usr/bin/7z x ' + backup_filepath + ' -o' + config.BACKUP_FOLDER) >= 2:
    print_error_message('uncompressing backup failed')
    exit(-2)
print_ok()

current_username = getpass.getuser()

nor_print("\n" + 'restoring data in DB...')
if run('psql -U ' + current_username + ' -d ' + config.DATABASE_NAME + ' -f ' + uncompressed_filepath)  != 0:
    print_error_message('unable to fill DB with backup data')
    exit(-3)
print_ok()



nor_print("\n" + 'deleting uncompressed backup...')
if run('rm ' + uncompressed_filepath)  != 0:
    print_error_message('unable to delete uncompressed backup')
    exit(-4)
print_ok()

print("\n")

exit(0)
