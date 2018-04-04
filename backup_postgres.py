#!/usr/bin/python3

from lib.colored_messages import print_ok, print_error_message
from lib.backup_name_formatter import BackupNameFormatter
from lib.config import Config
from lib.file_manager import folder_exists, file_is_empty, file_exists
from os import system as run
from lib.advanced_printf import print_no_return as nor_print
from lib.garbage_collector.garbage_collector import GarbageCollector

# - - - - error codes - - - -
#
#  0 = success
# -1   backup folder does not exist or permission error
# -2   asking postgres to backup failed
# -3   compressing backup failed
# -4   deleting uncompressed backup failed
# -5   backing up twice within the same minute
# -6   can't delete oldest backup

config = Config()
name_formatter = BackupNameFormatter()
backup_filepath = config.BACKUP_FOLDER + '/' + name_formatter.get_current_backup_filename()
garbage_collector = GarbageCollector()


nor_print("\n" + 'preparing to backup database ' + config.DATABASE_NAME + ' to the following location: ' + config.BACKUP_FOLDER + ' ...')
if not folder_exists(config.BACKUP_FOLDER):
    print_error_message('backup folder does not exist')
    exit(-1)

if file_exists(backup_filepath + '.7z'):
    print_error_message('it is not possible to backup the same DB twice within a minute')
    exit(-5)

nor_print("\n\n" + 'backing database up...')
run('/usr/bin/pg_dump ' + config.DATABASE_NAME + ' > ' + backup_filepath)


if file_is_empty(backup_filepath): #error code always 0 so workaround
    print_error_message('asking postgres to backup failed')
    exit(-2)
print_ok()


nor_print("\n" + 'compressing backup file...')
if run('/usr/bin/7z a ' + backup_filepath + '.7z -mmt=' + str(config.NB_CORES_FOR_COMPRESSING) + ' ' + backup_filepath) >= 2:
    print_error_message('compressing backup failed')
    exit(-3)

nor_print("\n" + 'deleting uncompressed backup...')
if run('rm ' + backup_filepath) != 0:
    print_error_message('deleting uncompressed backup failed')
    exit(-4)
print_ok()

nor_print("\n" + 'deleting oldest backup if needed ...')
garbage_collector.register_backup(backup_filepath + '.7z')
print_ok()

print("\n")

exit(0)
