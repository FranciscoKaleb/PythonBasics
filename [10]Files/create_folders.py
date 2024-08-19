import os

script_path = os.path.realpath(__file__) 
script_dir = os.path.dirname(script_path) 

# its good if theres a text file with a list of title and we make a folder for each title/topic
# then we count each topic and put that length in the range
try:
    for num in range(0, 9):
        os.mkdir(f'{script_dir}/[{num}]')

except OSError as error:
    print("folder already exist")

