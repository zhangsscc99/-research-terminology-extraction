lst=[]
with open("/Users/mac/Desktop/ngram/brandeisinput/wordsFood.txt",'r') as f:
    it_lst=f.readlines()
    
    
f.close()




def change_form(lst):
    new_lst=[]
    
    for i in range(len(lst)):
        each=lst[i].split('\t')[0][:-1]
        each+='\n'
        new_lst.append(each)

    return new_lst

        
withoutnum=change_form(it_lst)

with open('/Users/mac/Desktop/ngram/brandeisinput/wordsFoodwithoutnum.txt','w') as f2:
    f2.writelines(withoutnum)
f2.close()
