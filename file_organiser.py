import os
import shutil
from enum import IntEnum
from colorama import Fore
from send2trash import send2trash



class Dir_management:
    def __init__(self):
        self.directory = None

    def Set_Dir(self, directory):
        self.directory = directory

        self.image_directory = os.path.join(directory, "IMAGE")
        self.pdf_directory = os.path.join(directory, "PDF")
        self.text_directory = os.path.join(directory, "TEXT")
        self.spreadsheet_directory = os.path.join(directory, "SPREADSHEETS")
        self.video_directory = os.path.join(directory, "VIDEOS")
        self.audio_directory = os.path.join(directory, "AUDIO")
        self.presentation_directory = os.path.join(directory, "PRESENTATIONS")
        self.cpp_directory = os.path.join(directory, "C++")
        self.zip_directory = os.path.join(directory, "ZIP")

        self.check_if_folder_exists()

    def path(self, directory):
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath):
                _, file_extension = os.path.splitext(filename)
                self.segregate(file_extension, filepath)

            elif os.path.isdir(filepath):
                inner_dir = filepath
                for inner_filename in os.listdir(inner_dir):
                    inner_filepath = os.path.join(inner_dir, inner_filename)

                    if os.path.isfile(inner_filepath):
                        _, inner_file_extension = os.path.splitext(inner_filename)
                        self.segregate(inner_file_extension, inner_dir)

    def check_if_folder_exists(self):
        directories = [self.image_directory, self.pdf_directory, self.text_directory, self.spreadsheet_directory,
                    self.video_directory, self.audio_directory, self.presentation_directory, self.cpp_directory, self.zip_directory]
        for dir in directories:
            if not os.path.exists(dir):
                os.mkdir(dir)

    def segregate(self, file_extension, filepath):
        if file_extension.lower() in ['.png', '.jpg']:
            shutil.move(filepath, self.image_directory)
        elif file_extension.lower() == '.pdf':
            shutil.move(filepath, self.pdf_directory)
        elif file_extension.lower() in ['.txt', '.doc', '.docx']:
            shutil.move(filepath, self.text_directory)
        elif file_extension.lower() in ['.xls', '.xlsx', '.csv']:
            shutil.move(filepath, self.spreadsheet_directory)
        elif file_extension.lower() in ['.mp4', '.avi', '.mov']:
            shutil.move(filepath, self.video_directory)
        elif file_extension.lower() in ['.mp3', '.wav']:
            shutil.move(filepath, self.audio_directory)
        elif file_extension.lower() in ['.ppt', '.pptx']:
            shutil.move(filepath, self.presentation_directory)
        elif file_extension.lower() in ['.cpp', '.h']:
            shutil.move(filepath, self.cpp_directory)


dir_manager = Dir_management()

running = True
choices = IntEnum('Choices', {'Organise':1 , 'Display':2 , 'Delete':3, 'Move':4, 'Show':5, 'Quit':6})


print(f"""{Fore.BLUE}
______ _     ___  ___
|  _  (_)    |  \/  |
| | | |_ _ __| .  . | __ _ _ __   __ _  __ _  ___ _ __
| | | | | '__| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |/ /| | |  | |  | | (_| | | | | (_| | (_| |  __/ |
|___/ |_|_|  \_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|
                                        __/ |
                                       |___/
     {Fore.GREEN}This is an app i made during a weekend to
       automate my directorymanagement tasks.
{Fore.RESET}""")


while running:
    print(f"{Fore.BLUE}1.Organise files\n2.Display files\n3.Delete file\n4.Move file\n5.Show presaved actions\n6.QUIT{Fore.RESET}")
    choice = int(input("What would you like to do with your directory?: "))

    if choice == choices.Organise:
        path = str(input("Directory path: "))
        dir_manager.Set_Dir(path)
        dir_manager.path(dir_manager.directory)
        print(f'''{Fore.CYAN} 
        ______ _ _           _____                       _              _ 
        |  ___(_) |         |  _  |                     (_)            | |
        | |_   _| | ___  ___| | | |_ __ __ _  __ _ _ __  _ ___  ___  __| |
        |  _| | | |/ _ \/ __| | | | '__/ _` |/ _` | '_ \| / __|/ _ \/ _` |
        | |   | | |  __/\__ \ \_/ / | | (_| | (_| | | | | \__ \  __/ (_| |
        \_|   |_|_|\___||___/\___/|_|  \__, |\__,_|_| |_|_|___/\___|\__,_|
                                        __/ |                             
                                        |___/                              
        {Fore.RESET}''')

    elif choice == choices.Display:
        path = str(input("Directory path: "))
        os.chdir(path)
        for files in os.listdir(os.getcwd()):
            print(f'{Fore.BLUE}--------------\n{Fore.RESET}',files)
    elif choice == choices.Delete:
        print(Fore.RED + """
                            !!WARNING!!
        Be aware that this action deletes the file permanently
        """ + Fore.RESET)
        path = str(input("Path: "))
        os.chdir(path)
        file_to_delete = str(input("Which file would you like to delete?: "))
        send2trash(file_to_delete)
        print(f'''{Fore.CYAN}
        ______ _ _     ______     _      _           _ 
        |  ___(_) |    |  _  \   | |    | |         | |
        | |_   _| | ___| | | |___| | ___| |_ ___  __| |
        |  _| | | |/ _ \ | | / _ \ |/ _ \ __/ _ \/ _` |
        | |   | | |  __/ |/ /  __/ |  __/ ||  __/ (_| |
        \_|   |_|_|\___|___/ \___|_|\___|\__\___|\__,_|
        {Fore.RESET}''')

    elif choice == choices.Move:
        print("First input a path you want to move files from, then choose a file,\nat last input a path you want to move it to")
        from_path = str(input("From path: "))
        file = str(input("Enter file name: "))
        file_path = os.path.join(from_path,file)
        to_path = str(input("To path: "))
        shutil.move(file_path,to_path)
        print(f''' {Fore.CYAN}
        ______ _ _     ___  ___                   _ 
        |  ___(_) |    |  \/  |                  | |
        | |_   _| | ___| .  . | _____   _____  __| |
        |  _| | | |/ _ \ |\/| |/ _ \ \ / / _ \/ _` |
        | |   | | |  __/ |  | | (_) \ V /  __/ (_| |
        \_|   |_|_|\___\_|  |_/\___/ \_/ \___|\__,_|
        {Fore.RESET}''')
    elif choice == choices.Show:
        action = int(input(("Choose 1 to make a presave or 2 to view presaved actions")))

        if action == 1:
            save = str(input("Make a presave (action path): "))
            with open("pre_save.txt","a",encoding="UTF-8") as pre_save:
                pre_save.write(save + "\n")
            print(f"Action {save} has been saved")
        elif action == 2:
            if os.path.exists("pre_save.txt"):
                with open("pre_save.txt","r", encoding="UTF-8") as pre_save:
                    content = pre_save.readlines()
                    if content:
                        print("Presaved actions:")
                        for line in content:
                            print(line.strip())
                    else:
                        print("No presaved actions found")
            else:
                print("No presaved actions found")
    elif choice == choices.Quit:
        running = False
