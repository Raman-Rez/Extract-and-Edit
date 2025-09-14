import os

doc_path=input("YOUR DOCUMENT PATH: ")
folder_path=input("YOUR FOLDER PATH: ")
def main():
    Path(doc_path,folder_path)
    edit=Edit(doc_path,folder_path)
    edit.replace()
    edit.organize()
    edit.number()
    extract=Extract(doc_path,folder_path)
    extract.extrat()
    extract.frequent()
    print(extract)
    
class Path:
    def __init__(self,doc_path,folder_path):
        if (not (doc_path and folder_path)) or ('\\' not in (doc_path and folder_path)) or (".txt" not in doc_path):
            raise ValueError("Enter The Pathes Currectly")
        self.doc_path=doc_path
        self.folder_path=folder_path
class Edit(Path):
    def __init__(self,doc_path,folder_path):
        super().__init__(doc_path,folder_path)
    def replace(self):
        with open(self.doc_path) as file:
            file = file.readlines()
            for i in range(len(file)):
                file[i] = file[i].strip()
            list=[]
            res=''.join(file)
            list.append(res)
            list1=[]
            list2=[]
            list3=[]
            for j in list:
                for k in j:
                    if k == '.':
                        j = j.replace(k,'.\n')
                        break
                list1.append(j)
            for j in list1:
                for k in j:
                    if k == '?':
                        j = j.replace(k,'?\n')
                        break
                list2.append(j)
            for j in list2:
                for k in j:
                    if k == '!':
                        j = j.replace(k,'!\n')
                        break
                list3.append(j)
        with open(f'{self.folder_path}\\txt2.txt','w') as file2:
            file2.write(list3[0])
    
    def organize(self):
        with open(f'{self.folder_path}\\txt2.txt') as file3:
            file = file3.readlines()
            list=[]
            list1=[]
            for j in file:
                list.append(j.split(' '))
            for i in list:
                for j in i:
                    list1.append(j.capitalize())
            res1=' '.join(list1)
            list2=[] 
            list2.append(res1)

        with open(f'{self.folder_path}\\txt3.txt','w') as file:
            file.write(list2[0])

    def number(self):
        with open(f'{self.folder_path}\\txt3.txt') as file:
            file = file.readlines()
            list=[]
            list.append(f"{1}. {file[0]}")
            try:
                for i in range(len(file)):
                    list.append(f"{i+2}.{file[i+1]}")
            except:
                pass
        os.remove(f'{self.folder_path}\\txt3.txt')

        with open(f'{self.folder_path}\\Final Edit.txt','w') as file:
            for i in list:
                file.write(i)

class Extract(Path):
    def __init__(self,doc_path,folder_path):
        super().__init__(doc_path,folder_path)
        self.list_save=[]
    def extrat(self):
        with open(f'{self.folder_path}\\txt2.txt') as file:
            file=file.readlines()
            self.list_save.append(f"Number Of Sentance: {len(file)}")
            list=[]
            c=0
            x=0
            for i in file:
                list.append(i.rstrip().split(' '))
            for j in list:
                for k in j:
                    c+=1
                    for l in k:
                        x+=1
            self.list_save.append(f"Number Of Phrase: {c}")
            self.list_save.append(f"Number Of Character: {x}")
            list1=[]
            list2=[]
            for i in file:
                list1.append(i.rstrip())
                list2.append(len(i))
            for i in list1:
                if len(i) == max(list2)-1 :
                    self.list_save.append(f"The Biggest Sentance: {i}")
                if len(i) == min(list2)-1 :
                    self.list_save.append(f"The Smallest Sentance: {i}")
        os.remove(f'{self.folder_path}\\txt2.txt')
    def frequent(self):
        with open(self.doc_path,'r') as file:
            c = dict()
            for i in file.read().split():
                c[i] = c.get(i,0)+ 1
                s1= sorted(c.items(),key=lambda x: x[1])
                s2= sorted(c.items(),key=lambda x: x[1], reverse=True )
            self.list_save.append(f'The Most Frequent Word : {s2[0]}')
            self.list_save.append(f'The least Frequent Word : {s1[0]}')
    def __str__(self):
        return str(self.list_save)


if __name__=='__main__':
    main()