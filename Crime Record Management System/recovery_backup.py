import shutil   #shutil is used for file copying and file operations.
import os    #os is used to check files and interact with system folders

def create_backup():

    try:

        # Backup files list
        files = [
            "criminals.txt",
            "fir.txt",
            "cases.txt",
            "evidence.txt",
            "wanted.txt",
            "victims.txt"
        ]

        for file in files:

            # Copy file to backup version
            backup_file = file.replace(".txt", "_backup.txt")

            shutil.copy(file, backup_file)

        print("Backup Created Successfully!")

    except FileNotFoundError:

        print("Some files not found! Backup failed.")


def restore_backup():

    try:

        files = [
            "criminals.txt",
            "fir.txt",
            "cases.txt",
            "evidence.txt",
            "wanted.txt",
            "victims.txt"
        ]

        for file in files:

            backup_file = file.replace(".txt", "_backup.txt")

            if os.path.exists(backup_file):

                shutil.copy(backup_file, file)

        print("Data Restored Successfully!")

    except Exception as e:

        print("Restore Failed:", e)

