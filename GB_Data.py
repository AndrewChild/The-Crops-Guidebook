from dataStructure import Area, Subarea, Formation, Route, Variation
from GB_Book import book

Area(name='The Crops',
     parent=book,
     gps=None,
     description='', )

Subarea(name='Lower Talus Field',
        parent=book.areas['The Crops'],
        description='')
Subarea(name='Middle Talus Field',
        parent=book.areas['The Crops'],
        description='')
Formation(name='MILF Den',
          parent=book.subareas['Lower Talus Field'],
          description='')
Formation(name='Mellon Helmet',
          parent=book.subareas['Lower Talus Field'],
          description='')
Formation(name='Sarlacc Pit',
          parent=book.subareas['Middle Talus Field'],
          description='')
Route(name='Griffin\'s Problem',
      parent=book.formations['MILF Den'],
      grade=7,
      rating=3,
      FA='Griffin Thoms',
      description='')
Route(name='Oakridge Hot China',
      parent=book.formations['MILF Den'],
      grade=0,
      rating=2,
      FA='Griffin Thoms',
      description='')
Route(name='Mellon Helmet',
      parent=book.formations['Mellon Helmet'],
      grade=5,
      rating=2,
      FA='Andrew Child',
      description='')
Route(name='Battle Cat',
      parent=book.formations['Mellon Helmet'],
      grade=3,
      rating=1,
      FA='Griffin Thoms',
      description='')
Route(name='Catacomb',
      parent=book.formations['Sarlacc Pit'],
      grade=13,
      rating=3,
      FA='Jonah Kreitzberg',
      description='')
Route(name='Riot',
      parent=book.formations['Sarlacc Pit'],
      grade=9,
      rating=2,
      FA='Jonah Kreitzberg',
      description='')
Variation(name='Do You Like Wendy\'s?',
          parent=book.routes['Griffin\'s Problem'],
          grade=1,
          rating=2,
          FA='Jonah Kreitzberg',
          description='')

if __name__ == '__main__':
    sys.exit()
