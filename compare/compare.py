# import json

# def loadFont(keys):
#     a = ''
#     f = open("v1.json", encoding='utf-8')
#     content = json.load(f)

#     for key in keys:

#         a = content[key]
#         print(a)


#     # family = content['mscratch-i18n/msg']['blocks']['modify']
#     # return family

# t = loadFont(['mscratch-i18n/msg', 'blocks', 'modify'])

# print(t)



a = ['mscratch-i18n/msg', 'blocks', 'modify']
c = ''
b = iter(a)
while (d = next(b, -1) != -1):
    c = d

print(c)