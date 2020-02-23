# Test for populating the lists of positivve and negative words

def populateList():
    listOfNegatives = list() # Negatives
    with open ("negative.txt", "r") as myfile: # Opening
        for line in myfile: # Looping
            listOfNegatives.append(line.strip()) # Appending


    listOfPositives = list()
    with open ("positive.txt", "r") as myfile1:
        for line in myfile1:
            listOfPositives.append(line.strip())

