import sys
sys.path.insert(1, '../LocalBoulders')
from GB_Book import book
from GB_Data import *
#from GB_Images import *
# from GB_Images_test import *

if __name__ == '__main__':
    book.file_name = 'The_Crops_Guide'
    book.update()
    book.gen()