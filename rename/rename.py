import  os



def rename(destination_address):
     # destination_address= "E:/family/Nainital/"
    i = 0
    for temp in os.listdir(destination_address):
        name = "Trip " + str(i) + ".jpg"
        my_source = destination_address + temp
        name = destination_address + name
        # try:

        os.rename(my_source,name)
        # except FileExistsError:
        #     print("sorry")
        i += 1

if __name__ == '__main__':
    rename(input("enter the path "))
    print("Ho Gya Bhai")