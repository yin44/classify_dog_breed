#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Yin Yin Kyaw
# DATE CREATED: 02,11,2024                               
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Create an empty dictionary to store the results
    results_dic = {}

    # Get a list of files in the  directory
    # Loop through each filename in the directory
    for filename in listdir(image_dir):
        # Skip hidden files
        if filename[0] != ".":
            # Convert the filename to lowercase
            low_pet_image = filename.lower()

            # Split the filename by underscores to separate words
            word_list_pet_image = low_pet_image.split("_")

            # Initialize an empty string for the pet label
            pet_name = ""

            # Only include alphabetic words to build the label
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_name += word + " "

            # Strip any extra whitespace from the pet name
            pet_name = pet_name.strip()

            # Add to results dictionary if the filename is not already there
            if filename not in results_dic:
                results_dic[filename] = [pet_name]
            else:
                print(f"Warning: Duplicate file {filename} found in directory.")

    return results_dic
    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key in results_dic:
        print("Filename=", key, "   Pet Label=", results_dic[key][0])



#image_dir = "/data/pet_images"
#results_dic = get_pet_labels(image_dir)