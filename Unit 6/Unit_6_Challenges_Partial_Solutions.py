import csv
import pandas as pd

with open('words_alpha.txt', 'r') as file:     # You must save .txt file to same folder as python file or provide full/relative path
    words = set(file.read().split())
        
dictionary_list = sorted(list(words))
print(len(dictionary_list))   # Confirm the list length is 370,104

####################################################
# Challenge 1

with open(_________, ____) as file:     # Fill in arguments --> file name and read/write code
    for each_word in dictionary_list:
        if ________.______ == 'j':      # Look up how to pull the first letter of a word and convert it to lowercase
            file.write(________+'\n')   # What variable do you want to write to the file?  The \n is there to create a new line

####################################################
# Challenge 2

with ______('palindromes.csv', ____) as file:
    writer = ___._______(file)              # Look up how to write to csv file using csv module
    for each_word in dictionary_list:
        if each_word == _______________:    # Look up how to reverse a string (how to slice a string backwards)
            writer._________(__________)

####################################################
# Challenge 3

with open('long_words.txt', 'w') as file:
    for __________ in ___________:
        if len(___________.strip()) > _____:    # .strip() removes any space characters from a string
            file.write(_________+'\n')



df = pd.read_csv('titanic.csv')   # Read in the titanic data set into a dataframe for the remaining challenges

####################################################
# Challenge 4

num_survivors = df['__________'].______()           # Since survivor gets a 1 and non-survivor gets a 0, add up all the ones to get number of survivors
#num_survivors = len(df[df['_______'] == __]))    # Both of these methods will determine number of survivors

total_passengers = len(_____)

percent_survived = round(__________/________ * 100, 2)

print(f'{_____________}%')


####################################################
# Challenge 5

men_survivors = len(df[(df['__________']==1) & (df['_______']=='_______')])
women_survivors = len(df[(df['_________']==__) & (df['_____']=='________')])

men_passengers = len(___[___['_______']=='______'])
women_passengers = len(df[____['Sex']=='_______'])

percent_men_survived = round(___________/____________ * 100, 2)
percent_women_survived = round(___________/____________ * 100, 2)

print(f'Men survival rate = {_____________}%')
print(f'Women survival rate = {_____________}%')

####################################################
# Challenge 6

p1_class = round(len(df[(___['___________']==1) & (df['________']==___)])/len(df[df['________']==___])*100, 2)
p2_class = round(len(df[(df['Survived']==___) & (df['________']==2)])/len(df[df['________']==___])*100, 2)
p3_class = round(len(df[(df['__________']==___) & (df['Pclass']==___)])/len(df[df['Pclass']==3])*100, 2)

print(f'Class 1 survival rate = {p1_class}%')
print(f'Class 2 survival rate = {p2_class}%')
print(f'Class 3 survival rate = {p3_class}%')

####################################################
# Challenge 7

df.__________(subset='Age', inplace=True)   # Look up how to drop any rows that don't have an age listed (google --> pandas how to drop rows that don't have a value for a particular column)

under_18 = round(len(df[(df['_______']==1) & (df['____']<____)])/len(df[df['_____']<____])*100, 2)
over_18 = round(len(df[(df['________']==1) & (df['_____']>____)])/len(df[df['______']>____])*100, 2)

print(f'Children survival rate = {under_18}%')
print(f'Adult survival rate = {over_18}%')

####################################################
# Save all results from challengs 4-7 to a csv file
data = {'percent_survived': percent_survived, 'percent_men_survived': percent_men_survived, 'percent_women_survived': percent_women_survived,
        'p1_class_survival': p1_class, 'p2_class_survival': p2_class, 'p3_class_survival': p3_class, 'children_survival': under_18,
        'adult_survival': over_18}

final_df = pd._________._________(data, orient='index', columns=['Survival_Rate_%'])  #Convert dictionary to dataframe

final_df._______('pandas_challenges_results.csv')   # Send dataframe to csv file

print(final_df)
