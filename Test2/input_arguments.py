# import sys, getopt
# import csv
# import random
#
#
# def main(argv):
#     inputfile = ''
#     outputfile = ''
#     name_list = []
#     lname_list = []
#     address_list = []
#     try:
#         opts, args = getopt.getopt(argv,"hi:o:a:",["ifile=","ofile=","afile="])
#     except getopt.GetoptError:
#         print('test.py -i <inputfile> -o <outputfile>')
#         sys.exit(2)
#     for opt, arg in opts:
#         if opt == '-h':
#             print('test.py -i <inputfile> -o <outputfile>')
#             sys.exit()
#         elif opt in ("-i", "--ifile"):
#             inputfile = arg
#         elif opt in ("-o", "--ofile"):
#             outputfile = arg
#         elif opt in ("-a", "--afile"):\
#             addressfile = arg
#         print('Input file is "', inputfile)
#         print('Output file is "', outputfile)
#     with open(inputfile, 'r') as file:
#         csv_file = csv.reader(file)
#         my_list = list(csv_file)
#     for i in range(len(my_list)):
#         my_list[i][1] = int(my_list[i][1])
#     for i in range(len(my_list)):
#         for j in range(0, my_list[i][1]):
#             name_list.append(my_list[i][0])
#    with open(outputfile, 'r') as file1:
#        csv_file = csv.reader(file1)
#             my_list = list(csv_file)
#    for i in range(len(my_list)):
#        my_list[i][1] = int(my_list[i][1])
#    for i in range(len(my_list)):
#     for j in range(0, my_list[i][1]):
#         lname_list.append(my_list[i][0])
#    with open(addressfile, 'r') as file2:
#     csv_file = csv.reader(file2)
#         my_list = list(csv_file)
#    for i in range(len(my_list)):
#     my_list[i][1] = int(my_list[i][1])
#    for i in range(len(my_list)):
#     for j in range(0, my_list[i][1]):
#         address_list.append(my_list[i][0])
#
#    random.shuffle(name_list)
#    random.shuffle(lname_list)
#    random.shuffle(address_list)
#
#    from itertools import zip_longest
#    with open('finalData.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=',',
#                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     data = list(zip_longest(name_list, lname_list, address_list, fillvalue=' '))
#     for row in data:
#         row = list(row)
#         spamwriter.writerow(row)
#    print("Program completed")
#
#
# if __name__ == "__main__":
#    main(sys.argv[1:])