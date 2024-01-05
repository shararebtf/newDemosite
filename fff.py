Paragraph = ('GitHub is an AI-powered developer platform that allows developers to create,'
            ' store, and manage their code.'
            ' It uses Git software, providing the distributed version control of Git plus access control,'
            ' bug tracking, software feature requests, task management, continuous integration, and wikis for every project.'
            'Headquartered in California, it has been a subsidiary of Microsoft since 2018.').lower()

#Show total number of words
#To calculate the total number of words.you need remove all Contraction(\') and space
#split paragraph to words
Paragraph = Paragraph.replace('\'', ' ')
Paragraph = Paragraph.replace('\n', ' ').split(' ')
print("Total number of words: ", len(Paragraph))


#To calculate the total number of unique words.you need to convert the paragraph into a set and then count the len words
ListWords = set(Paragraph)
print("Unique number of words: ", len(ListWords))


#To calculate the total number of unique words.you need create a list of Tobe verbs
Count = 0
TobeListWords = {}
TobeList = {'am': 0, 'is': 0, 'are': 0, 'was': 0, 'were': 0, 'm': 0, 's': 0, 're': 0, 'be': 0}
for i in Paragraph:
    if i in TobeList:
        Count += 1
        TobeList.update({i: TobeList.get(i) + 1})
        TobeListWords.update({i: TobeList.get(i)})
print("Total number of To be occurrences: ", Count)
print("Number of each to be words: ", TobeListWords)

