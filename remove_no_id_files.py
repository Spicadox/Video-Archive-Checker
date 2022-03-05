import os
import sys
import re
from send2trash import send2trash


# Function that checks for arguments and get user specified directories
def checkArguments():
    directory_list = ["M:\Hololive\Gen 3\Pekora Ch. 兎田ぺこら"]
    # if len(sys.argv) < 2:
    #     directory_list = input("Directory: ").split()
    # else:
    #     for directory in sys.argv:
    #         if directory is not sys.argv[0]:
    #             directory_list.append(directory)
    return directory_list


def remove_files(directories):
    totalCount = 0
    removeCount = 0
    videoRenameCount = 0
    files_to_remove = []
    pattern = "([0-9]{8} - .* \()(.{11})(\).*)"
    no_id_pattern = "([0-9]{8} - .*)(\..{3,4})"
    extension_list = [".mkv", ".mp4", ".webm"]
    with open("output.txt", 'w', newline='') as txt_writer:
        for directory in directories:
            for roots, dirs, files in os.walk(directory):
                # totalCount += len(dirs)
                # if len(files) == 0:
                #     if len(dirs) != 0:
                #         totalCount += 1
                #         print("Parent Directory: " + roots)
                #     else:
                #         print("\t"+roots)
                #         txt_writer.write([roots])
                # Loop through all files in the subfolders in reverse order

                print("\n" + roots)
                print(f"Number of files: {len(files)}")
                txt_writer.write("\n" + roots)
                video_id = None
                for file in files:
                    totalCount += 1
                    re_match = re.match(pattern, file)
                    if re_match is not None:
                        video_id = re_match.group(2)
                    # If any of the files is a video then increment removeCount and set fileFound to true
                    # and go to next folder
                    if extension_list[0] not in file and extension_list[1] not in file and extension_list[2] not in file:
                        if re_match is None:
                            # send2trash(file)
                            print(f"Files to Remove: {file}")
                            files_to_remove.append(rf"{roots}\{file}")
                            txt_writer.write("\n" + file)
                            removeCount += 1

                    for extension in extension_list:
                        if extension in file and video_id is not None and re.match(pattern, file) is None:
                            videoRenameCount += 1
                            re_match = re.match(no_id_pattern, file)
                            new_video_name = f"{re_match.group(1)} ({video_id}){re_match.group(2)}"
                            print(f"Renaming video to: {new_video_name}")
                            txt_writer.write(f"\nRenaming video to: {new_video_name}")
                            # os.rename(file, new_video_name)


    print("Total Directories: " + str(totalCount))
    print("Remove Count: " + str(removeCount))
    print("Video Rename Count: " + str(videoRenameCount))

    input("Press Enter to start the delete process...")
    print(files_to_remove)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arguments = checkArguments()
    remove_files(arguments)
    input("Press Enter To Exit...")