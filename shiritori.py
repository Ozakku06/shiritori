#coding utf-8

import random

shiritori_len = 15

katakana_table={
    'ア':0,
    'ァ':0,
    'イ':1,
    'ィ':1,
    'ウ':2,
    'ゥ':2,
    'ヴ':2,
    'エ':3,
    'ェ':3,
    'オ':4,
    'ォ':4,
    'カ':5,
    'ガ':5,
    'キ':6,
    'ギ':6,
    'ク':7,
    'グ':7,
    'ケ':8,
    'ゲ':8,
    'コ':9,
    'ゴ':9,
    'サ':10,
    'ザ':10,
    'シ':11,
    'ジ':11,
    'ス':12,
    'ズ':12,
    'セ':13,
    'ゼ':13,
    'ソ':14,
    'ゾ':14,
    'タ':15,
    'ダ':15,
    'チ':16,
    'ヂ':16,
    'ツ':17,
    'ヅ':17,
    'ッ':17,
    'テ':18,
    'デ':19,
    'ト':19,
    'ド':19,
    'ナ':20,
    'ニ':21,
    'ヌ':22,
    'ネ':23,
    'ノ':24,
    'ハ':25,
    'バ':25,
    'パ':25,
    'ヒ':26,
    'ビ':26,
    'ピ':26,
    'フ':27,
    'ブ':27,
    'プ':27,
    'ヘ':28,
    'ベ':28,
    'ペ':28,
    'ホ':29,
    'ボ':29,
    'ポ':29,
    'マ':30,
    'ミ':31,
    'ム':32,
    'メ':33,
    'モ':34,
    'ヤ':35,
    'ャ':35,
    'ユ':36,
    'ュ':36,
    'ヨ':37,
    'ョ':37,
    'ラ':38,
    'リ':39,
    'ル':40,
    'レ':41,
    'ロ':42,
    'ワ':43,
    'ヲ':44,
    'ン':45
}

data = []
candidate = []
final = []
num_group = max(katakana_table.values())

for _ in range(num_group):
    data.append([])

f = open('name.txt')
names = f.readlines()
names = [x.replace('\n','') for x in names]
names = [x.replace('\r','') for x in names]
f.close()
for name in names:
    index = katakana_table[name[0]]
    data[index].append(name)
usefirstname = input('一人目決めます? y/n:')
if usefirstname == 'y':
    first_name = input('名前を入力してね:')
    if first_name in names:
        final.append(first_name)
    else:
        print('そのキャラおりゃん')
        exit(-1)
else:
    random_name = random.choice(names)
    final.append(random_name)

crt = 0
next_group = katakana_table[final[crt][-1]]
candidate.append(data[next_group][:])
for i in final:
    if i in candidate[crt]:
        candidate[crt].remove(i)
while(crt < shiritori_len-1):
    for i in final:
        if i in candidate[crt] and i != final[-1]:
            candidate[crt].remove(i)
    
    if candidate[crt]:
        rand = random.randint(0,len(candidate[crt])-1)
        final.append(candidate[crt][rand])
        del candidate[crt][rand]
        crt = crt + 1
        next_group = katakana_table[final[crt][-1]]
        candidate.append(data[next_group][:])
        for i in final:
            if i in candidate[crt]:
                candidate[crt].remove(i)
    else:
        del candidate[crt]
        del final[crt]
        crt = crt - 1
        if(crt < 0):
            print('みつかりゃん')
            exit(-1)

for name in final:
    print(name)
