import os

# Global Variables
media_extensions = ['.bmp', '.mp3']
txt_extensions = ['.txt', '.doc', '.docx']

# Create our own safe makedirs function
def my_safe_makedirs(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

#This move function creates target directory if that does not exist
def my_move(dir, list_of_files):
    my_safe_makedirs(dir)
    for file in list_of_files:
        print(f"Moving {file} inside {dir}")
        os.replace(file, f"{dir}/{file}")

if __name__ == "__main__":
    dir_contents = os.listdir(".")
    media_files = [file for file in dir_contents if os.path.splitext(file)[1].lower() in media_extensions ]
    txt_files = [file for file in dir_contents if os.path.splitext(file)[1].lower() in txt_extensions ]

    print(f"Media files: {media_files}")
    print(f"Text files: {txt_files}")
    print("")

    #Move media Files inside "Media" directory
    my_move('Media', media_files)

    #Move text Files inside "Text" directory
    my_move('Text', txt_files)

    print("")
    print ("Done. Directory content organized successfully.")
