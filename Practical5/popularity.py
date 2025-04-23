# pseudocode:
# create a dictionary with given datas
# print the dictionary
# import matplotlib
# use the datas in the dictionary to define the x and y axis in the bar plot
# show the plot
# ask the user to input a language
# if the language is in the dictionary, print the popularity of the language
# elif the language is not in the dictionary, print that the language is not in the dictionary

Dictionary={"Javascript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}      #creating a dictionary
for key in Dictionary:
    print(key,":",Dictionary[key],"%")     #print the correct dictionary

import pandas as pd                            #import nessasary libraries
import matplotlib.pyplot as plt
df = pd.DataFrame(list(Dictionary.items()), columns=['Language', 'Users_Percentage'])    #Use Pandas to convert dictionary data into data boxes, making it easy to use its built-in drawing function
df.plot(kind='bar', x='Language', y='Users_Percentage', color='purple')     #Enter basic parameters to draw a bar chart
plt.title('Programming language popularity')    #add a title to the chart
plt.show()

#Dear professor, you might have to close the window first to continue running the code.
INPUT= input("Enter the language (Javascript, HTML, Python, SQL, TypeScrip) you want to know the popularity of: ")
if INPUT in Dictionary:
    print("The popularity of",INPUT,"is",Dictionary[INPUT],"%")    	#for a given programming language, print the popularity.
else:
    print("The language you entered is not in the dictionary")