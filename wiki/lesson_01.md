# Practice Goals
* Learn how to get around the command line
* Using curl/wget to grab files online
* python basics (int, float, str, list, tuple)
* Piping data into python


## Practice: Unix
pwd: Find where we are in the Volume.
ls: List all the files and folders in our current location

ls accepts a lot of arguments:

* sudo: superuser permissions let's us see dotfiles
* -l, -n (-ln): view extended information about the files, like permissions, file size, etc. These are generally the most useful
* cat: puts a file through standard in/out. Generally not as useful as...
* less: a simple file viewer in bash. Here we can use
    * the arrows to move around
    * / to run a regex match
    * q to go back to the command line

Making a class folder: We'll store all of our work in here.

    cd # get back into your user folder.
    mkdir GA_Data_Science
    cd GA_Data_Science
    
Making files: occasionally we could make files this way. It's rarely needed, but a good skill. Here we'll make a file, move it, and copy it.

    touch file.txt
    ls # Lists our file!
    mv file.txt file_new.txt
    ls # Our file changed names!
    cp file_new.txt file_copied.txt
    ls # File was copied!
    echo 'Files can be written this way as well' > text_file.txt
    less text_file.txt


Downloading a file using curl:

    curl http://stat.columbia.edu/~rachel/datasets/nyt1.csv > nytimes.csv 

With longer files, we can use head or tail to read the first few or last few lines.

    head nytimes.csv
    tail nytimes.csv
    
## Practice: Python
Get into python using:

    python
    
(If Anaconda was installed correctly, we should see this referenced as python opens up)

    1 # Integers
    2
    1.0 # Floats
    2.0
    0 # Ints, but can also mean True or False
    1
    0 == True
    1 == True
    'string' # strings
    'A whole sentence'
    [1, 2, 3] # list, mutable (can change)
    (1, 2, 3) # tuple, immutable (can't be edited)
    
We're going to write our first class Python script that sums up a whole column of text from a comma seperated file.

    #!/usr/bin/python
    # Import required libraries
    import sys

    # Start a counter and store the textfile in memory
    count = 0
    lines = sys.stdin.readlines()
    lines.pop(0)

    # For each line, find the sum of index 2 in the list.
    for line in lines:
      count = count + int(line.strip().split(',')[2])

    print count
    
Let's make this file executable, and run it!

    chmod +X counter.py
    cat nytimes.csv | python counter.py

We can print a more robust line in bash, so let's change the last line to this instead:

    print 'Impressions Sum:', count

## Classwork

1. Right now the python script finds a sum of the impressions column. Update it to also return:
    1. The average age in the file
    2. Click through rate (avg clicks per impression)
    3. The oldest person in the file
2. This should all be write out to the standard out using a few lines with "print"
3. When you have a python script that works, upload it to Schoology under classwork day 1.

## Extra Credit!
How can you change the Python script a bit to:

* Cleanly ignore all string values?
* Output the results into a new text file?