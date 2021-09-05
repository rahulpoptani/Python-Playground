f = open('abc.txt', 'r')

print(f.name)
print(f.mode)

# required to close to avoid leaks
f.close()

# context manager - allows us to access the file within the close and close the file when we exit the block
with open('abc.txt', 'r') as file:
    # load the complete file data, ok for small files
    file_context = file.read()
    print(file_context)

    file_lines = file.readlines()
    print(file_lines)

    file_oneline = file.readline()
    print(file_oneline, end = '')
    file_oneline = file.readline()
    print(file_oneline, end = '')
    
    # If you read big file, you end up with memory exceptions
    # in order to read big files, do
    for line in file:
        print(line, end='')

    # If you want to specify the number of characters you want to read
    file_content = file.read(10) # 100 characters only
    print(file_content, end='')

    file_content = file.read(10) # Next 100 characters
    print(file_content, end='')

    # to loop 100 characters at a time
    size_to_read = 10
    file_content = file.read(size_to_read)
    while len(file_content) > 0:
        # print(file_content, end='')
        print(file_content, end='*') # can see where the file content is ending. Good Interview question. To add * after every 10 characters and save as file.
        file_content = file.read(size_to_read)

    # Point back to start of file after reading few characters
    size_to_read = 10
    file_content = file.read(size_to_read)
    print(file_content, end='')
    file.seek(0)
    file_content = file.read(size_to_read)
    print(file_content)



# You can access file object eve outside context manager, it just the file will be closed
print(file.closed)


# To read from one file and write to another file
with open('abc.txt', 'r') as rf:
    with open('abc_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# Read and Write file in chunk
with open('abc.txt', 'r') as rf:
    with open('abc_copy.txt', 'w') as wf:
        chunk_size = 10
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


