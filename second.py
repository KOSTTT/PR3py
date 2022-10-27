import os,sys

def check(file_name):
    with open("result_file/"+str(file_name), "r") as file:
        list_text = []
        while True:
            line = file.readline()
            if not line:
                break
            list_text.append(line.strip())
            
    all_simvols = 0
    max = 0
    min = 10
    kolv = 0
    kolvgl = 0
    kolvsogl = 0
    one = 0
    two = 0
    three = 0
    four = 0 
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    for i in range(len(list_text)):
        all_simvols += len(list_text[i])
        kolv+=1
        if(len(list_text[i]) > max):
            max = len(list_text[i])
        if(len(list_text[i])<min):
            min = len(list_text[i])
        for char in list_text[i]:
            if char in "aeiouy":
                kolvgl+=1
            else:
                kolvsogl+=1
        match len(list_text[i]):
            case 1:
                one+=1
            case 2:
                two+=1
            case 3:
                three+=1
            case 4:
                four+=1
            case 5:
                five+=1
            case 6: 
                six+=1
            case 7:
                seven+=1
            case 8: 
                eight +=1
            case 9: 
                nine+=1
            case 10:
                ten+=1
        
    print("*****************************************************************")
    print("Аналитика для файла ./result_files/"+str(file_name))
    print("*****************************************************************")
    print("1. Всего символов --> "+ str(all_simvols))
    print("2. Максимальная длина слова --> "+ str(max))
    print("3. Минимальная длина слова -->" + str(min))
    print("4. Средняя длина слова --> " + str(all_simvols//kolv))
    print("5. Количество гласных --> " +str(kolvgl))
    print("6. Количество согласных --> "+str(kolvsogl))
    print("7. Количество повтроений слов с одинаковой длиной: ")
    print("   * 1 сим. >> " + str(one) + " повтор.")
    print("   * 2 сим. >> " + str(two) + " повтор.")
    print("   * 3 сим. >> " + str(three) + " повтор.")
    print("   * 4 сим. >> " + str(four) + " повтор.")
    print("   * 5 сим. >> " + str(five) + " повтор.")
    print("   * 6 сим. >> " + str(six) + " повтор.")
    print("   * 7 сим. >> " + str(seven) + " повтор.")
    print("   * 8 сим. >> " + str(eight) + " повтор.")
    print("   * 9 сим. >> " + str(nine) + " повтор.")
    print("   * 10 сим. >> " + str(ten) + " повтор.")
    
    for i in range(1,11):
        print("* "+str(i)+" сим. >> "+str(array[i-1])+" повтор.")
    f.close()
    



