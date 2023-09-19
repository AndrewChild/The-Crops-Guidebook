from dataStructure import *


book = Book(
    name='The Crops',
    collaborators=['Andrew Child', 'Griffin Thoms', 'Silas Thoms', 'Jonah Kreitzberg', 'Cryus McDowell'],
    repo='https://github.com/AndrewChild/The-Crops-Guidebook',
    dl='https://github.com/AndrewChild/The-Crops-Guidebook/raw/main/The_Crops_Guide.pdf',
    paths={
        'LaTeXTemplates': '../LocalBoulders/templates/',
        'LaTeXOut': './sections/',
        'pdf': './',
        'ghost_script': r'C:\Program Files\gs\gs10.00.0\bin\gswin64.exe',
    }
)



if __name__ == '__main__':
    sys.exit()
