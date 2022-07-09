import mcpi.minecraft as minecraft
import mcpi.block as block
import time
hiroszima = "nad bedrock"
mc = minecraft.Minecraft.create()
a = 35
#
#
# while ys <= -3: 
#  mc.setBlock({x},{ys},{z},{stone})
#  mc.setBlock({x},{ys},{z},{stone})
#  ys = ys + 1
# zmienne 
x = 0
y = 0
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
 y = a + 1
 for ia in range(0, 60):
  for iaa in range(1, 60):
   mc.setBlock({ia},{y},{iaa},{air})
 while y == a:
  exit()
   #time.sleep(0.0000002)