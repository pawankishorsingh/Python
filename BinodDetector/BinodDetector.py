import os

def detect_binod(filename):
    with open(filename) as f:
        contents = f.read()
        if "binod" in contents.lower():
            return True
        else:
            return False

if __name__ == "__main__":
    dir_content = os.listdir()
    count_binod=0
    for item in dir_content:
        if item.endswith('txt'):
            print (f"Detecting Binod inside {item}: ", end="")
            flag = detect_binod(item)
            if flag == True:
                print("Found")
                count_binod+=1
            else:
                print("Not Found")
    
    print("\nSummary:", end = "")
    print(f"Total {count_binod} Binods found.")