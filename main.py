import os
import hashlib

# specify the directory to search for duplicates
directory = '/path/to/directory'

# create a dictionary to store file hashes and paths
hashes = {}

# loop through all files in the directory
for filename in os.listdir(directory):
    filepath = os.path.join(directory, filename)
    
    # check if the file is an image
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
        
        # open the file and calculate its hash
        with open(filepath, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        
        # if the hash is already in the dictionary, we've found a duplicate
        if file_hash in hashes:
            print(f"Duplicate found: {filename}")
            
            # prompt the user to delete the duplicate
            delete = input("Do you want to delete this file? (y/n): ")
            if delete.lower() == 'y':
                os.remove(filepath)
                print(f"Deleted {filename}")
            else:
                print(f"Not deleting {filename}")
        else:
            hashes[file_hash] = filepath
