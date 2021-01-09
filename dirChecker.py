import os
import sys
import csv

# Function that checks for arguments and get user specified directories
def checkArguments():
    directory_list = []
    if len(sys.argv) < 2:
        # directory_list = [directory for directory in input("Directory: ").split()]
        directory_list = [input("Directory: ")]
        # user_input = input("Directory: ")
        # directory_list = user_input
        # directory_list = user_input.split()

        # print(directory_list)
    else:
        for directory in sys.argv:
            if directory is not sys.argv[0]:
                directory_list.append(directory)
    return directory_list


def directoryChecker(directories):
    totalCount = 0
    videoCount = 0
    fileFound = False
    rootDir = False
    subDir = 0
    subdirectory_no_files = 0
    extension_list = [".mkv", ".mp4", ".webm"]
    with open("output.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for directory in directories:
            for roots, dirs, files in os.walk(directory):
                totalCount += len(dirs)
                # print(dirs)
                # print(roots,dirs,files)
                # If there are no files in subfolders and subfolder is not the user inputted folder path

                # if len(files) == 0 and roots not in directory and files is [] and dirs is not None:
                #if len(files) == 0 and roots not in directory and files is []:
                # print(roots)
                if len(files) == 0:
                    if len(dirs) != 0:
                        subdirectory_no_files += 1
                        print("Parent Directory: " + roots)
                    else:
                        # print(files)
                        subDir +=1
                        print("\t"+roots)
                        csv_writer.writerow([roots])

                # Loop through all files in the subfolders in reverse order
                for file in reversed(files):
                    # If any of the files is a video then increment videoCount and set fileFound to true
                    # and go to next folder
                    if extension_list[0] in file or extension_list[1] in file or extension_list[2] in file:
                        videoCount = videoCount + 1
                        break
                    # Else if there aren't any videos in the folder write it and all files have been seen
                    else:
                        #len(dirs) == 0 solved and prevented user input directory to be considered as empty
                        if file == files[0] and len(dirs) == 0:
                            print("\t"+roots)
                            csv_writer.writerow([roots])
                            break
                        # If there is no video in user inputted directory
                        if len(dirs) == 0:
                            # print(dirs)
                            rootDir = True
    if subdirectory_no_files:
        videoCount+=subdirectory_no_files+subDir
    # if subdirectory_no_files and subDir:
    #     videoCount -= subDir+1
    if rootDir and not subdirectory_no_files:
        videoCount+=1
    if subDir and not subdirectory_no_files:
        videoCount+=subDir
    print("Total Directories: " + str(totalCount))
    print("Missing Videos: " + str(totalCount - videoCount))
    # for files in iglob("I:\夏色まつり🏮ホロライブ1期生\*.mp4", recursive=True):
    #     print(files)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arguments = checkArguments()
    directoryChecker(arguments)


