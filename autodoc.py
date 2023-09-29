import os 
import sys
import pathlib

""""
we want to use ai docs to create documents for the mess we have created
navigate through each files and create a document for each file
we'll save the document in a folder called docs, using the file name as the title of the document
"""

document_destination = "/Users/nolanpestano/Documents/GitHub/Jelly_ROS_22-23/Documentation"

# go to the catkin_ws/src directory, and all of the subdirectories. if there is a .py file, create a document for it
pathlist = pathlib.Path().glob('catkin_ws/src/**/*.py')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
     
    # we have the path to the file, now we need to create a document for it
    in_use = open(path_in_str, "w+")
    
    #copy all the contents into chatgpt
    # soon !!
  
    # to do, add the folder structure to the document destination
    # use the file name as the title of the document
    file_name = os.path.basename(path_in_str)
    file_name = file_name.replace(".py", ".txt")
    
    # create the document
    document = open(document_destination + "/" + file_name, "w+")
    document.write("This is the document for " + file_name)
    
    

    # close the document
    document.close()
    
    # test for now, add functionality later

    print(path_in_str)