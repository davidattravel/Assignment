def strip_punctuation(x):
    x = x.replace("'","")
    x = x.replace('"',"")
    x = x.replace(",","")
    x = x.replace(".","")
    x = x.replace(".","")
    x = x.replace("!","")
    x = x.replace(":","")
    x = x.replace(";","")
    x = x.replace('#',"")
    x = x.replace('@',"")
    x = x.replace(".","")
    return x

def get_pos(x):
    y = strip_punctuation(x)
    y = y.split()
    count = 0
    for i in range(len(y)):
        if y[i].lower() in positive_words:
            count = count + 1
    return count

def get_neg(x):
    y = strip_punctuation(x)
    y = y.split()
    count = 0
    for i in range(len(y)):
        if y[i].lower() in negative_words:
            count = count + 1
    return count

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

file = open("project_twitter_data.csv")
lines = file.readlines()
txtlst = []
retlst = []
replst = []
for line in lines:
    line = line.strip()
    lst = line.split(",")
    txtlst.append(lst[0])
    retlst.append((lst[1]))
    replst.append(lst[2])
txtlst = txtlst[1:]
retlst = retlst[1:]
replst = replst[1:]
tlst = []
for t in txtlst:
    tlst.append(strip_punctuation(t))
pscore = []
for p in tlst:
    pscore.append(get_pos(p))
nscore = []
for n in tlst:
    nscore.append(get_neg(n))
nets = []
for s in tlst:
    net_score = get_pos(s) - get_neg(s)
    nets.append(net_score)
pscore = [str(np) for np in pscore]
nscore = [str(nn) for nn in nscore]
nets = [str(ns) for ns in nets]
title = ['Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score']
retlst.insert(0, title[0])
replst.insert(0, title[1])
pscore.insert(0, title[2])
nscore.insert(0, title[3])
nets.insert(0, title[4])

newf = open("resulting_data.csv", "w")
for i in range(len(retlst)):
    newf.write(retlst[i] + ', ' + replst[i] + ', ' + pscore[i] + ', ' + nscore[i] + ', ' + nets[i] + '\n')
newf.close()


