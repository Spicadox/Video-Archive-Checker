import datetime
import os
import sys
import re
from datetime import date
from send2trash import send2trash


# Function that checks for arguments and get user specified directories
def checkArguments():
    directory_list = ["H:\DownloadArchive"]
    if len(sys.argv) < 2 or len(directory_list) < 1:
        directory_list = input("Directory: ").split()
    else:
        for directory in sys.argv:
            if directory is not sys.argv[0]:
                directory_list.append(directory)
    return directory_list


def get_remove_directories(directories, ignore_directories):
    file_pattern = "([0-9]{8})(\s-\s.*)"
    dirs_to_remove = []
    current_date = str(datetime.date.today()).replace('-', '')
    print(f"Current Date: {current_date}")
    with open("remove_dirs.txt", 'w', encoding='utf-8') as txt_writer:
        txt_writer.write(current_date)
        for directory in directories:
            for folder, subfolders, files in os.walk(directory):

                # Remove ignore directories after the first walk
                for ignore_dir in ignore_directories:
                    if ignore_dir in subfolders:
                        subfolders.remove(ignore_dir)
                        continue


                # print("Roots: " + str(roots))
                # print("Directories: " + str(dirs))
                # print("Files: " + str(files))
                txt_writer.write("\n\nRoots: " + str(folder))
                if len(subfolders) != 0:
                    txt_writer.write("\nDirectories: " + str(subfolders))
                if len(files) != 0:
                    txt_writer.write("\nFiles: " + str(files))

                for dir in subfolders:
                    try:
                        date = re.match(pattern=file_pattern, string=dir).group(1)
                        if int(current_date)-int(date) > 7:
                            dirs_to_remove.append(rf"{folder}\{dir}")
                    except AttributeError:
                        continue
            txt_writer.write(f"Directories to remove: {str(dirs_to_remove)}")
        return dirs_to_remove


if __name__ == '__main__':
    ignore_directories = ["【Twitcasting Archive】", "【Member Stream】", "【Twitch】", "【Mildom】", "中岡TV。", "佐藤希Sato Nozomi"]
    # Number of days after which the directory should be remove(i.e.remove after 7 days)
    max_day = 7
    arguments = checkArguments()
    dirs_to_remove = get_remove_directories(arguments, ignore_directories)
    print(dirs_to_remove)
    print(f"Removing {len(dirs_to_remove)} directories...")
    try:
        send2trash(dirs_to_remove)
    except Exception as e:
        print(e)
    input("Press Enter To Exit...")