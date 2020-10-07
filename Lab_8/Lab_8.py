class Shark():
   def swim(self):
       print("Акула плавает.")
   def swim_backwards(self):
       print("Акула не может плыть задом, но может плыть вниз.")
   def skeleton(self):
       print("Скелет акулы состоит из хрящей.")

class Clownfish():
   def swim(self):
       print("Рыба плавает.")
   def swim_backwards(self):
       print("Рыба не может плыть назад.")
   def skeleton(self):
       print("Скелет рыбы состоит из костей.")

sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton()

