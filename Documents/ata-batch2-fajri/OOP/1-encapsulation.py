class Cat():

    def __init__ (self, fur_color, num_of_leg):
        self.fur_color = fur_color
        self.num_of_leg = num_of_leg

    def show_identity (self):
        print ('saya Kucing dengan detail, Warna Bulu: {} dengan jumlah kaki: {}'.format(self.fur_color, self.num_of_leg)) 

cat_1 = Cat('Hitam', '4')
cat_2 = Cat('Putih', '3')
cat_3 = Cat('Hitam Putih','4')
cat_4 = Cat('Poleng poleng', '3')
cat_5 = Cat('bintik bintik', '4')

cat_1.show_identity()
cat_2.show_identity()
cat_3.show_identity()
cat_4.show_identity()
cat_5.show_identity()

class Fish():

    def __init__ (self, type, feed):
        self.type = type
        self.feed = feed

    def show_identity (self):
        print ('saya Ikan dengan detail, Jenis: {}, makanan: {}'.format(self.type, self.feed)) 

fish_1 = Fish('paus', 'plankton')
fish_2 = Fish('cupang', 'cacing')
fish_3 = Fish('arwana','jangkrik')
fish_4 = Fish('sapu-sapu', 'pelet')

fish_1.show_identity()
fish_2.show_identity()
fish_3.show_identity()
fish_4.show_identity()

class Flower():

    def __init__ (self, nama, color, num_of_petal):
        self.nama = nama
        self.color = color
        self.num_of_petal = num_of_petal

    def show_identity (self):
        print ('saya Bunga dengan detail, Jenis: {}, color: {}, num of petal: {}'.format(self.nama, self.color, self.num_of_petal)) 

bunga_1 = Flower('bangkai', 'merah', '12')
bunga_2 = Flower('anggrek', 'putih', '8')
bunga_3 = Flower('mawar', 'merah', '3')
bunga_4 = Flower('melati', 'kuning', '5')

bunga_1.show_identity()
bunga_2.show_identity()
bunga_3.show_identity()
bunga_4.show_identity()

class Car():

    def __init__ (self, type, color, num_of_tire):
        self.type = type
        self.color = color
        self.num_of_tire = num_of_tire

    def show_identity (self):
        print ('saya mobil dengan detail, Type: {}, color: {}, num of tire: {}'.format(self.type, self.color, self.num_of_tire)) 

mobil_1 = Car('sedan', 'merah', '4')
mobil_2 = Car('truk', 'hijau', '6')
mobil_3 = Car('tronton', 'coklat', '12')
mobil_4 = Car('angkot', 'kuning', '4')

mobil_1.show_identity()
mobil_2.show_identity()
mobil_3.show_identity()
mobil_4.show_identity()