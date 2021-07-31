def main():
    #write your code below this line
    list_of_names = []

    while True:
        name = input()

        if name == '':
            break

        list_of_names.append(name)

    print(list_of_names[2])        

if __name__ == '__main__':
    main()
