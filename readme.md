Moodle Scripting
==========================

This is a program to convert Latex files to Moodle-compatible XML files.

The 'clean.py' is to import a Latex file, delete unnecessary formatting lines, and divide the whole text into 2 new files, namely description file, multiple-choice file.

Other types of files are yet to be implemented.

The 'xml_generator.py' is to convert the aforementioned files to xml format.


<h4>How to use it</h4>

1. change the file name in the second last 2 lines of 'clean.py' to your Latex file.

2. run 'clean.py'.

3. run 'xml_generator.py'

4. 2 xml files should have been created. Simply go to Moodle -> question bank -> import, then drag one file at a time to the file pool. The questions will automatically be generated.

