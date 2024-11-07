#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Yin Yin Kyaw
# DATE CREATED: 03,11,2024                                
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """  

    dognames_dic = {}
    with open(dogfile, "r") as f:
        for line in f:
            dog_name = line.strip().lower()
            if dog_name:
                for name in dog_name.split(", "):
                    dognames_dic[name.strip()] = 1
    """
    # results_dic with indicators for whether labels are dogs
    for key in results_dic:
        # Check if the pet label is in dognames_dic
        pet_label = results_dic[key][0].lower().strip()
        pet_is_dog = 1 if pet_label in dognames_dic else 0

        # Check if any phrase in the classifier label matches a dog name
        classifier_label = results_dic[key][1].lower()
        classifier_is_dog = 0
        classifier_phrases = classifier_label.split(", ")

        # Determine if classifier label matches any dog name
        for phrase in classifier_phrases:
            if phrase.strip() in dognames_dic:
                classifier_is_dog = 1
                break

        # Extend results_dic with the correct pet_is_dog and classifier_is_dog values (0 or 1)
        results_dic[key].extend([pet_is_dog, classifier_is_dog])

        # Debug print to verify
        print(f"File: {key}")
        print(f"  Pet Label: '{pet_label}' - Is Dog: {pet_is_dog}")
        print(f"  Classifier Label: '{classifier_label}' - Is Dog: {classifier_is_dog}")
        print("  Updated Entry:", results_dic[key])
        """
    for key in results_dic:
    # Retrieve and clean the pet label from results_dic
        pet_label = results_dic[key][0].lower().strip()
        
    # Check if the pet label is in dognames_dic to determine if it's a dog
        pet_is_dog = 1 if pet_label in dognames_dic else 0

    # Retrieve and clean the classifier label from results_dic
        classifier_label = results_dic[key][1].lower()
    
    # Initialize classifier_is_dog as 0 (not a dog) by default
        classifier_is_dog = 0

    # Split the classifier label into phrases to check each one individually
        classifier_phrases = classifier_label.split(", ")
    
    # Determine if any phrase in classifier label matches a dog name in dognames_dic
        for phrase in classifier_phrases:
            if phrase.strip() in dognames_dic:
                classifier_is_dog = 1
                break  # Stop checking once we confirm it's a dog

        # Update the match value
        # Update the match calculation to check if either label is a substring of the other
        match = 1 if (pet_label in classifier_label or classifier_label in pet_label) else 0


    # Ensure  adding pet_is_dog and classifier_is_dog as integers
        results_dic[key] = [results_dic[key][0], results_dic[key][1], match, pet_is_dog, classifier_is_dog]
        # Print statement to display results for each image
        print(f"File: {key}")
        print(f"  Pet Label: '{pet_label}' - Classified as {'Dog' if pet_is_dog else 'Not Dog'}")
        print(f"  Classifier Label: '{classifier_label}' - Classified as {'Dog' if classifier_is_dog else 'Not Dog'}")
        print(f"  Match: {'Matches' if match == 1 else 'No Matches'}")
        


        print("-" * 40)  # Divider for clarity

    # Example of output to verify the format    
    print("\nFinal Results Dictionary:")
    for key in results_dic:
        print(f"{key}: {results_dic[key]}")
