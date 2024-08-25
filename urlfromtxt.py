import os

# Read URLs from a text file
with open('urls.txt', 'r') as file:
    urls = file.readlines()

# Iterate over each URL and run the command
for url in urls:
    url = url.strip()  # Remove any leading/trailing whitespace or newline characters
    if url:  # Ensure the line isn't empty
        command = f"python ipa_archive.py add {url}"
        os.system(command)
