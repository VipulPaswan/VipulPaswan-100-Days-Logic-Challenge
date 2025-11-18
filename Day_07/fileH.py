""" 
1) open a file
2) read/write
3) close a file


File opening modes:--
r,w,a
r+,w+,a+
"""

import os

def write_to_file(filename,name):
          f=open(filename,'w')
          f.write(name)
          f.close()
          
def append_to_file(filename,name):
          f=open(filename,'a')
          f.write('\n')
          f.write(name)
          f.close()

def read_to_file(filename):
          
          try:
                    f=open(filename,'r')
                    text=f.read()
                    print(text)
          
          except  FileNotFoundError:
                    print("File not found") 
         

def main():
          # name=input("Enter your name")
          # write_to_file('file1.txt',name)
          # append_to_file('file1.txt',name)
          # read_to_file('file1.txt')
          
          # os.rename('file1.txt','myfile.txt')
          os.rename('myfile.txt','file1.txt')
           
main()        







