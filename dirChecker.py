import os
import sys
import csv

# Function that checks for arguments and get user specified directories
def checkArguments():
    directory_list = []
    if len(sys.argv) < 2:
        directory_list = input("Directory: ").split()
    else:
        for directory in sys.argv:
            if directory is not sys.argv[0]:
                directory_list.append(directory)
    return directory_list


def directoryChecker(directories):
    totalCount = 0
    videoCount = 0

    # extension_list = [".mkv", ".mp4", ".webm"]
    with open("output.csv", 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for directory in directories:
            for roots, dirs, files in os.walk(directory):
                totalCount += len(dirs)
                if len(files) == 0:
                    if len(dirs) != 0:
                        totalCount+=1
                        print("Parent Directory: " + roots)
                    else:
                        videoCount = videoCount + 1
                        print("\t"+roots)
                        csv_writer.writerow([roots])
                # Loop through all files in the subfolders in reverse order
                # for file in reversed(files):
                #     # If any of the files is a video then increment videoCount and set fileFound to true
                #     # and go to next folder
                #     if extension_list[0] in file or extension_list[1] in file or extension_list[2] in file:
                #         # videoCount = videoCount + 1
                #         break
                    # Else if there aren't any videos in the folder write it and all files have been seen
                    # else:
                    #     #len(dirs) == 0 solved and prevented user input directory to be considered as empty
                    #     #Doesnt do anything
                    #
                    #     if file == files[0] and len(dirs) == 0:
                    #         # testing += 1
                    #         print("\t"+roots)
                    #         csv_writer.writerow([roots])
                    #         break

    print("Total Directories: " + str(totalCount))
    print("Missing Videos: " + str(videoCount))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arguments = checkArguments()
    directoryChecker(arguments)


