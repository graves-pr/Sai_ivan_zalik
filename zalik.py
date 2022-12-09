f = open("file.txt",'r',encoding='utf8')
tegword = input("Введіть слово: ")
list = f.read().split('\n\n')
c = 0
for i in list:
    for a in i.split():

        if a == tegword:
            print("Потрібний абзац: "+ i +"\n")
            c += 1
            break #для того випадку коли у одному абзаці наявно декілько шукаємих слів, щоб не виводило повторно один тей самий абзац.
            
if c == 0:
    print("Слово не знайдено.")