def Main():
    print("Welcome To MadLibs Game!")
    print("Please Choose for The Languages!")
    print("1. Indonesia")
    print("2. English")
    languages = int(input("Choose 1 or 2: "))

    if languages == 1:
        MadLibIndoesia()
    else:
        MadLibEnglish()

def MadLibIndoesia():
    animals = input("Masukkan Kata Hewan: ")
    profession = input("Masukkan Kata Profesi: ")
    cloth = input("Masukkan Kata Pakaian: ")
    things = input("Masukkan Kata Benda: ")
    name = input("Masukkan Nama: ")
    place = input("Masukkan Nama Tempat: ")
    verb = input("Masukkan Kata Kerja: ")
    food = input("Masukkan Nama Makanan: ")
    print('Katakan ' + food + '!, Sang Fotografer berkata lalu kamera pun mengeluarkan flash ' + name + ' dan aku akan pergi ke ' + place +' untuk mengambil foto saat ulang tahunku. Foto pertama kita harus berdandan seperti ' + animals + ' yang berpura pura menjadi ' + profession + '. saat kita melihat foto kedua, itulah yang aku inginkan. Kami berdua terlihat seperti ' + things + ' memakai ' + cloth + ' dan ' + verb + ' --persis seperti yang ada dalam pikiranku')

def MadLibEnglish():
    animals = input("Enter a Animal: ")
    profession = input("Enter a Profession: ")
    cloth = input("Enter a Cloth: ")
    things = input("Enter a Things: ")
    name = input("Enter a Name: ")
    place = input("Enter a Place: ")
    verb = input("Enter a Verb: ")
    food = input("Enter a Food: ")
    print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animals + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

Main()
