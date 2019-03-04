file1 = open('index.h', 'w')
file2 = open('index.cpp', 'w')
file1.write('#include<iostream>\nvoid TestFunc();')
file2.write('#include"index.h"\nvoid TestFunc() { \n')
file2.write('std::cout << "TestFunc from A directory works correctly" << std::endl; \n}')

