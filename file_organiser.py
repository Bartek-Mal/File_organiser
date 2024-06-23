import os
import shutil
from enum import IntEnum

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

while running:
    print("1.Organise files\n2.Display files\n3.Delete file\n4.Move file\n5.Show presaved actions\n6.QUIT")
    choice = int(input("What would you like to do with your directory?: "))
    
    if choice == choices.Organise:
        path = str(input("Path: "))
        dir_manager.Set_Dir(path)
        dir_manager.path(dir_manager.directory)
    elif choice == choices.Display:
        path = str(input("Path: "))
        os.chdir(path)
        for files in os.listdir(os.getcwd()):
            print('--------------\n',files)
    elif choice == choices.Delete:
        print("""
                            !!WARNING!!
        Be aware that this action deletes the file permanently
        """)
        path = str(input("Path: "))
        os.chdir(path)
        file_to_delete = str(input("Which file would you like to delete?: "))
        os.remove(file_to_delete)
    elif choice == choices.Quit:
        running = False
