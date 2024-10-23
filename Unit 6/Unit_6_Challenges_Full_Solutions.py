import csv
import pandas as pd


with open('words_alpha.txt', 'r') as file:     # You must save .txt file to same folder as python file or provide full/relative path
    words = set(file.read().split())
        
dictionary_list = sorted(list(words))
print(len(dictionary_list))   # Confirm the list length is 370,104

####################################################
# Challenge 1

with open('j_words.txt', 'w') as file:
    for each_word in dictionary_list:
        if each_word[0].lower() == 'j':
            file.write(each_word+'\n')

####################################################
# Challenge 2

with open('palindromes.csv', 'w') as file:
    writer = csv.writer(file)
    for each_word in dictionary_list:
        if each_word == each_word[::-1]:
            writer.writerow([each_word])

####################################################
# Challenge 3

with open('long_words.txt', 'w') as file:
    for each_word in dictionary_list:
        if len(each_word.strip()) > 19:
            file.write(each_word+'\n')



df = pd.read_csv('titanic.csv')   # Read in the titanic data set into a dataframe for the remaining challenges

####################################################
# Challenge 4

num_survivors = df['Survived'].sum()           # Since survivor gets a 1 and non-survivor gets a 0, add up all the ones to get number of survivors
#num_survivors = len(df[df['Survived'] == 1]))    # Both of these methods will determine number of survivors

total_passengers = len(df)

percent_survived = round(num_survivors/total_passengers * 100, 2)

print(f'{percent_survived}%')


####################################################
# Challenge 5

men_survivors = len(df[(df['Survived']==1) & (df['Sex']=='male')])
women_survivors = len(df[(df['Survived']==1) & (df['Sex']=='female')])

men_passengers = len(df[df['Sex']=='male'])
women_passengers = len(df[df['Sex']=='female'])

percent_men_survived = round(men_survivors/men_passengers * 100, 2)
percent_women_survived = round(women_survivors/women_passengers * 100, 2)

print(f'Men survival rate = {percent_men_survived}%')
print(f'Women survival rate = {percent_women_survived}%')

####################################################
# Challenge 6

p1_class = round(len(df[(df['Survived']==1) & (df['Pclass']==1)])/len(df[df['Pclass']==1])*100, 2)
p2_class = round(len(df[(df['Survived']==1) & (df['Pclass']==2)])/len(df[df['Pclass']==2])*100, 2)
p3_class = round(len(df[(df['Survived']==1) & (df['Pclass']==3)])/len(df[df['Pclass']==3])*100, 2)

print(f'Class 1 survival rate = {p1_class}%')
print(f'Class 2 survival rate = {p2_class}%')
print(f'Class 3 survival rate = {p3_class}%')

####################################################
# Challenge 7

df.dropna(subset='Age', inplace=True)   # Drop any rows that don't have an age listed

under_18 = round(len(df[(df['Survived']==1) & (df['Age']<18)])/len(df[df['Age']<18])*100, 2)
over_18 = round(len(df[(df['Survived']==1) & (df['Age']>18)])/len(df[df['Age']>18])*100, 2)

print(f'Children survival rate = {under_18}%')
print(f'Adult survival rate = {over_18}%')

####################################################
# Save all results from challengs 4-7 to a csv file
data = {'percent_survived': percent_survived, 'percent_men_survived': percent_men_survived, 'percent_women_survived': percent_women_survived,
        'p1_class_survival': p1_class, 'p2_class_survival': p2_class, 'p3_class_survival': p3_class, 'children_survival': under_18,
        'adult_survival': over_18}

final_df = pd.DataFrame.from_dict(data, orient='index', columns=['Survival_Rate_%'])  #Convert dictionary to dataframe

final_df.to_csv('pandas_challenges_results.csv')   # Send dataframe to csv file

print(final_df)


















