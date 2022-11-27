import os
big_filepath=os.listdir('/Users/mac/Downloads/wiki_zh')
filepaths=[]
for i in range(len(big_filepath)):
    #small_filepath=[]
    

    path='/Users/mac/Downloads/wiki_zh/'+big_filepath[i]
    small_filepath=os.listdir(path)
    for j in range(len(small_filepath)):
        path2=path+'/'+small_filepath[j]

        filepaths.append(path2)
len(filepaths)
#filepaths
import json
words=[]
def write_to_words(filepath):
    with open(filepath,'r') as json_file:
        big_lst=json_file.readlines()
        #print(len(big_lst))
        for i in range(len(big_lst)):

            data = json.loads(big_lst[i])
        
            words.append(data['title']+'\n')
for i in range(len(filepaths)):
    filepath=filepaths[i]
    write_to_words(filepath)

    # Print the type of data variable
    #print("Type:", type(data))

    # Print the data of dictionary
    #print("\nPeople1:", data['title'])
with open('/Users/mac/Desktop/ngram/brandeisinput/wiki_corpus.txt','w') as f2:
    f2.writelines(words)
f2.close()

