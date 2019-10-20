'''
Написать программу, которая
#1. принимает на вход в качестве именованного аргумента —input (-i) путь до считываемого файла
в формате <filename>.csv, в качестве второго аргумента  - —output (-o) - путь до целевого файла <filename>_odd.csv,
Нужно ли различать ввели ли .csv?
#2. сама программа считывает .csv,
#3. оставляет только нечетные строки,
#4. записывает их в целевой файл.
#5. Если в файле ноль нечетных строк, целевой файл не создается, программа предупреждает об ошибке.
#6. Если недостаточно аргументов / не хватает файлов по указанному пути - программа сообщает об ошибке.
'''
import argparse, csv, os

def main():
    #Получаем список необходимых переданных аргументовю Сохраняем в args
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, help='Path for file to import. Should be <filename>.csv')
    parser.add_argument('-o', '--output', type=str, help='path for output file. Should be <filename>_odd.csv')
    args = parser.parse_args()

    #Проверяем передали ли нам все необходимые аргументы (input & output)
    if args.input == None or args.output == None:
        print('Не хватает входящих аргументов')
        os._exit(0)

    # Проверка передали ли путь к файлу с расширением или без, верно ли указан output_odd.csv
    try:
        if args.input.rsplit('.')[1] != 'csv':    #попытка получить расширение файла
            (print("Расширение файла импорта должно быть CSV"))
            os._exit(0)
    except IndexError: #если расширение не указано - присвоим
        args.input = args.input + '.csv'
    try:
        if args.output.rsplit('.')[1] != 'csv':
            print("Расширение файла экспорта должно быть CSV")
            os._exit(0)
    except IndexError: #Если расширение не указано - присваиваем.
        args.output = args.output.rsplit('.')[0] + '.csv'
    #Если указано окончание файла не '_odd.csv' - добавим.
    if args.output[-8:] != '_odd.csv':
        args.output = args.output[0:-4] + '_odd.csv'

    #Проверка наличия существования сходного файла. Выходной проверять не будем. Он создается при необходимости
    if os.path.exists(args.input) == False:
        print(('Указанный входящий файл для импорта не сушествует'))
        os._exit(0)

    if os.path.dirname(args.output[0:-4]) != True:
        try:
            os.makedirs(os.path.dirname(args.output[0:-4]))
        except FileExistsError:
            pass
    return args.input, args.output


def sort_save(input_path, output_path):
    #Считываем четные строки входного файла, сохраняем в data_to_save
    try:
        with open (input_path, newline='', encoding='utf-8') as imported_file:
            counter=1
            data_to_save=[]
            reader = csv.reader(imported_file, quotechar='|', delimiter=',')
            for row in reader:
                if counter%2 != 0:
                    data_to_save.append(row)
                counter+=1
    except:
        (print('Ошибка при чтении файла'))
        os._exit(0)

    #Проверяем не равно ли количество четных строк нулю
    if len(data_to_save)==0:
         print('Нечетных строк ноль!') #Если равно нулю = следующий блок с созданием файла не сработает
         os._exit(0)
    #Если не равно нулю - записываем в выходной файл
    else:
        try:
            with open (output_path, 'w', newline='', encoding='utf-8') as out_file:
                writer = csv.writer(out_file)
                writer.writerows(data_to_save)
        except:
            print('Ошибка при записи файла')
            os._exit(0)
    return output_path

if __name__ == "__main__":
    input_path , output_path = main()
    sort_save(input_path,output_path)

print('Выполнено.  Можно открыть файл ' , output_path)