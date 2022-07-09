import mcpi.minecraft as minecraft
import mcpi.block as block
import time
hiroszima = "nad bedrock"
mc = minecraft.Minecraft.create()
a = 1
x = 0
y = 0
z = 0
sleep = 0.3021
sleepbr = 0.621
grass = block.GRASS
dirt = block.DIRT
glasspn = block.GLASS_PANE
glass = block.GLASS
stone = block.STONE
wood = block.WOOD
woodpl = block.WOOD_PLANKS
air = block.AIR
loop = True
dwie = False
yd = 2
mc.setBlock({x},{y},{z},{glass})
#mc.player.setPos({x},{yd},{z}, 0)
mc.setBlock({x},{y},{z},{glass})
time.sleep(sleep)
mc.setBlock({x},{y},{z},{air})
time.sleep(3)
while loop == True:
 for j in range(0, 7):
  mc.setBlock({j},{y},{z},{glass})
 mc.postToChat("punkt")
 mc.postToChat({a})
 x = x + 4
 a = a + 1
 if(a == 40):
  mc.postToChat("Wygrałeś zaczynamy od początku")
  loop = False
  mc.postToChat("Zaczynamy za 20 sekund")
  time.sleep(20)
  loop = True
  a = 0
  x = 0
  y = 0
  z = 0
  yd = 2
  #mc.player.setPos({x},{yd},{z}, 0)
 if(dwie == False):
  mc.setBlock({x},{y},{z},{glass})
  x = x + 4
  mc.setBlock({x},{y},{z},{glass})
  time.sleep(sleep)
  dwie = True
  continue
 if(dwie == True):
  time.sleep(sleepbr)
  x = x - 8 
  mc.setBlock({x},{y},{z},{air})
  x = x - 4 
  mc.setBlock({x},{y},{z},{air})
  time.sleep(sleep)
  dwie = False
  x = x + 4
  continue
 #z = z + 1
#mc.setBlock({x},{y},{z},{glass})
 #x = x - 1
 #z = z - 1
 #mc.setBlock({x},{y},{z},{air})
 #x = x + 3
 #z = z + 3
 continue
