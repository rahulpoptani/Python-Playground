
try:
    f = open('Notes.txt')
    if f.name == 'Notes.txt':
        raise Exception("User Defined Exception")
except FileNotFoundError as e:
    print('File Not Found')
except Exception as e:
    print('Error is: {}'.format(e))
else:
    # Runs ony when no exception
    print(f.read())
    f.close()
finally:
    # Runs in any condition. Ex: closing database
    print('finaly')