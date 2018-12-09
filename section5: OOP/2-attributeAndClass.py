class Badminton():
    game='indoor'
    def __init__(self,racket,shuttle,power):
        self.racket=racket
        self.shuttle=shuttle
        self.power=power

my_bad=Badminton(racket='yonex',shuttle='yonex',power=True)
print(type(my_bad))
print(my_bad.racket)
print(my_bad.shuttle)
print(my_bad.power)
print*my_bad.game)
