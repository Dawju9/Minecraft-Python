#---------------------------[Używane  biblioteki]---------------------------------#
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
#---------------------------[Początek zmiennych]---------------------------------#
# Zmienna funkcji MCPI - Minecraft.Create() przypisana do zmiennej zwn. "mc"
mc = minecraft.Minecraft.create()

# Zmienna a - to wielkośc boku kwadratu do wyczyszczenia
a = 1

# Zmienna prędkości stawiania i usuwania bloków (a dokładniej funkcja czasu dla programu w PY) 
sleep = 0.3021
sleepbr = 0.621

# Zmienna kordynatów (x,y,z) do przesunięcia początku kordynatów programu od WordSpawn'a (/setwordspawn - by zmienić początek kordynatów)
x = 0
y = 0
z = 0

# Zmienna bloku z funcji MCPI - block.'*' bloki dostępne w dokumentacji MCPI
grass = block.GRASS # blok trawy
dirt = block.DIRT # blok ziemi
glasspn = block.GLASS_PANE # szklany panel
glass = block.GLASS # Blok szkła
stone = block.STONE # Blok kamienia
wood = block.WOOD # Blok drewna
woodpl = block.WOOD_PLANKS # Blok desek
air = block.AIR # Powietrze

# Zmienna pętli (ustowaniona na True - program działa w pętli)
loop = True

# Zmienna podwójnego bloku (Dodatkowa zmienna do testowania czy obecnie dwie płyty bloków 3x3 są postawione)
dwie = False 

# Zmienna dodatkowa yustawiona podstawowo na 2 (y') 
yd = 2

#---------------------------[Koniec  zmiennych]---------------------------------#
# Mój działający kod właściwy

mc.setBlock({x},{y},{z},{glass}) # Stawiam blok szkła

time.sleep(sleep) # Usypiam program na określony czas

mc.setBlock({x},{y},{z},{air}) # Zamieniam na powietrze

time.sleep(3) # Usypiam program na czas 3 sekund

while loop == True: # Gdy pętla True 
 for j in range(0, 7): # dla j korzynatu x jako 0-7
  mc.setBlock({j},{y},{z},{glass}) # Stawiam blok szkła
 mc.postToChat("punkt") # Debug punktu w chat
 mc.postToChat({a}) # Debug punktu w chat
 x = x + 4 # Inkrementuje x o 4 punkty z każdą pętlą
 a = a + 1 # Inkrementuje a punkt z każdą pętlą
 if(a == 40): # Jeśli a = 40 (Jeśli program jest na 40 punkcie)
  mc.postToChat("Wygrałeś zaczynamy od początku") # Debug punktu w chat
  loop = False # Ustawiam pętlę na False
  mc.postToChat("Zaczynamy za 20 sekund") # Debug punktu w chat
  time.sleep(20) # Usypiam program na czas 20 sekund
  # Zeruje program
  loop = True # Ustawiam pętlę na True
  # Zeruje zmienne kordynatów jak i droge programu "a"
  a = 0
  x = 0
  y = 0
  z = 0
  yd = 2
 if(dwie == False): # Jeśli brak drugiej płyty bloków
  mc.setBlock({x},{y},{z},{glass}) # Ustaw bloki
  x = x + 4 # Inkrementuje x o 4 punkty w pętli
  mc.setBlock({x},{y},{z},{glass}) # Ustaw bloki
  time.sleep(sleep) # Usypiam program na określony czas
  dwie = True # Ustawiam zmienną dwóch płyt na True
  continue # Kontynujue działanie programu
 if(dwie == True): # Jeśli są dwie płyty bloków
  time.sleep(sleepbr) # Usypiam program na określony czas
  x = x - 8 # Dekrementuje x o 8 punkty w pętli
  mc.setBlock({x},{y},{z},{air}) # Zamieniam bloki na powietrze
  x = x - 4 # Dekrementuje x o 4 punkty w pętli
  mc.setBlock({x},{y},{z},{air}) # Zamieniam bloki na powietrze
  time.sleep(sleep) # Usypiam program na określony czas
  dwie = False # Ustawiam zmienną dwóch płyt na False
  x = x + 4 # Inkrementuje x o 4 punkty w pętli
  continue # Kontynujue działanie programu
 continue # Kontynujue działanie programu
#---------------------------[Zasobnik]---------------------------------#
#mc.player.setPos({x},{yd},{z}, 0)
#z = z + 1
#mc.setBlock({x},{y},{z},{glass})
 #x = x - 1
 #z = z - 1
 #mc.setBlock({x},{y},{z},{air})
 #x = x + 3
 #z = z + 3
