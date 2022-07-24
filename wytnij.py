# Importy
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Zmienne 


# Zmienna funkcji MCPI - Minecraft.Create() przypisana do zmiennej zwn. "mc"
mc = minecraft.Minecraft.create()


# Zmienna a - to wielkośc boku kwadratu do wyczyszczenia
a = 35

# Zmienna kordynatów (x,y,z) do przesunięcia początku kordynatów programu od WordSpawn'a (/setwordspawn - by zmienić początek kordynatów)
x = 0
y = 0
z = 0

# Zmienna prędkości usuwania bloków (a dokładniej funkcja czasu dla programu w PY) 
sleep = 0.0021

# Zmienna bloku z funcji MCPI - block.'*' bloki dostępne w dokumentacji MCPI
air = block.AIR




# Mój działający kod właściwy
# Pętla lini A 
while a >= 0:
 a = a - 1 # Zmiejszam A o 1 z każdą pętlą (A = A + 1)
 y = a + 1 # Przyrównuje Y do A zwiększając go o 1 punkt z każdą pętlą (Y = A + 1)
 for ia in range(0, 60): # W zasięgu 0, 60 wartości X 
  for iaa in range(1, 60): # W zasięgu 0, 60 wartości Z 
   mc.setBlock({ia},{y},{iaa},{air}) # Usuwam blok zamieniając obecny na powietrze
 while y == a: # jeżeli Y spotka się z twoim A 
  exit() # Opuszczam program
