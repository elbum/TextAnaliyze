from konlpy.tag import Mecab
import operator


mecab = Mecab(dicpath='/usr/local/lib/mecab/dic/mecab-ko-dic')
a = (mecab.pos(u'영등포구청역에 있는 맛집 좀 알려주세요'))
# print(mecab.pos(u'영등포구청역에 있는 맛집 좀 알려주세요'))
# print(a)


textfile = "/Users/alboom/PycharmProjects/Crawler/test.mlf"

f = open(textfile,'r+',encoding='utf-8')

text = f.read()

a=mecab.pos(text)

# print(a)

wordcount = {}
for word in a :
    if word not in wordcount :
        wordcount[word] = 1
    else :
        wordcount[word]+=1

wordcount_st = dict(sorted(wordcount.items(),key=operator.itemgetter(1),reverse=True))


for x in wordcount_st :
    print(x,wordcount_st[x])


f.close()

exit(1)
