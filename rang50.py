import mcpi.minecraft as minecraft
import mcpi.block as block
import time
hiroszima = "nad bedrock"
mc = minecraft.Minecraft.create()
a = 15
#
#
# while ys <= -3: 
#  mc.setBlock({x},{ys},{z},{stone})
#  mc.setBlock({x},{ys},{z},{stone})
#  ys = ys + 1
# zmienne 
x = 0
y = 0
za = a
yok = 1
xok = 2
zok = 2
yd = -1
yds = -2
z = 0
#sleep = 0.0021
sleep = 0
grass = block.GRASS
dirt = block.DIRT
glass = block.GLASS_PANE
stone = block.STONE
wood = block.WOOD
woodpl = block.WOOD_PLANKS
air = block.AIR
#stst = block.STONE_STAIRS
#  print(f"B aktualnie jest = {b}")
#  mc.postToChat("   aktualny a    ")
#  mc.postToChat({b})
while a >= 0:
 a = a - 1
 x = x + 1
 
 
 mc.postToChat("")
 mc.postToChat("")
 mc.postToChat("")
 mc.setBlock({x},{y},{z},{grass})
 #mc.postToChat("stawiam dirt")
 #mc.player.setPos({xok},{yok},{zok}, 68)
 #mc.setBlock({x},{yd},{z},{dirt})
 #mc.setBlock({x},{yds},{z},{stone})
 time.sleep(sleep)
 while a == 0:
  x = 0
  z = z + 1
  a = za
  #yds = yds - 1
 while z == za:
  print(f" skonczyłem budowac")
  mc.postToChat("skonczyłem budowac podstawę")
  time.sleep(1)
  
   #dirt
  iaaa = 0
  azzz = a +1 
  while iaaa >= -1:
   iaaa = iaaa - 1
   for ia in range(0, a):
    for iaa in range(1, azzz):
     mc.setBlock({iaa},{iaaa},{ia},{dirt})
     #time.sleep(0.0000002)
    #stone
  iaaa = -2
  azzz = a +1 
  while iaaa >= -4:
   iaaa = iaaa - 1
   for ia in range(0, a):
    for iaa in range(1, azzz):
     mc.setBlock({iaa},{iaaa},{ia},{stone})
     #time.sleep(0.0000002)
  
  for i in range(1, 7):
   mc.setBlock(4,{i},3,{wood})
   time.sleep(sleep)
  for js in range(5, 9):
   mc.setBlock({js},1,3,{woodpl})
   time.sleep(sleep)
  for ij in range(1, 7):
    mc.setBlock(9,{ij},3,{wood})
    time.sleep(sleep)

  for ia in range(4, 9):
   mc.setBlock(4,1,{ia},{woodpl})
   time.sleep(sleep)
  for ia in range(4, 9):
   mc.setBlock(9,1,{ia},{woodpl})
   time.sleep(sleep)
    
  for i in range(1, 7):
   mc.setBlock(4,{i},9,{wood})
   time.sleep(sleep)
  for js in range(5, 9):
   mc.setBlock({js},1,9,{woodpl})
   time.sleep(sleep)
  for ij in range(1, 7):
    mc.setBlock(9,{ij},9,{wood})
    time.sleep(sleep)
    
    #podłoga
  for ia in range(4, 9):
   for iaa in range(5, 9):
    mc.setBlock({iaa},0,{ia},{woodpl})
    time.sleep(sleep)
    #dach
  for ia in range(4, 9):
   for iaa in range(5, 9):
    mc.setBlock({iaa},6,{ia},{woodpl})
    time.sleep(sleep)
    #szklo 1
  for iz in range(4, 9):
   for izz in range(2, 6):
    mc.setBlock(4,{izz},{iz},{glass})
    time.sleep(sleep)
    #szklo 2
  for iz in range(4, 9):
   for izz in range(2, 6):
    mc.setBlock(9,{izz},{iz},{glass})
    time.sleep(sleep)
    #szklo 3
  for iz in range(5, 9):
   for izz in range(2, 6):
    mc.setBlock({iz},{izz},3,{glass})
    time.sleep(sleep)
    #szklo 4
  for iz in range(5, 9):
   for izz in range(2, 6):
    mc.setBlock({iz},{izz},9,{glass})
    time.sleep(sleep)  
  #mc.setBlock(2,2,8,{stst})
  time.sleep(0)
  exit()
  
  
      #restart od zera
  #iaaa = 10
 # azzz = a + 1 
  #while iaaa >= -9:
   #iaaa = iaaa - 1
   #for ia in range(0, a):
    #for iaa in range(1, azzz):
     #mc.setBlock({iaa},{iaaa},{ia},{air})
     #time.sleep(0.0000002)