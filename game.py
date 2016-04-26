import libtcodpy as libtcod

##########################################################
# Constants, Classes, Functions
##########################################################

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

class Object:
	#this is a generic object: a player, a monster, an item, stairs
	#they are all represented by a character on screen
	def __init__(self, x, y, char, color):
		self.x = x
		self.y = y
		self.char = char
		self.color = color

	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def draw(self):
		libtcod.console_set_default_foreground(con, self.color)
		libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

	def clear(self):
		libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)


def handle_keys():
	global playerx, playery

	key = libtcod.console_check_for_keypress(True)
	if key.vk == libtcod.KEY_ENTER and key.lalt:
		libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
	elif key.vk == libtcod.KEY_ESCAPE:
		return True;
	#movement keys
	elif key.vk == libtcod.KEY_CHAR:
		if key.c == ord('w'):
			player.move(0, -1)
		elif key.c == ord('s'):
			player.move(0, 1)
		elif key.c == ord('d'):
			player.move(1, 0)
		elif key.c == ord('a'):
			player.move(-1, 0)

###########################################################
# Intiailization and Game Loop
###########################################################

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/Roguelike-like', False)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)

#create object representing the player
player = Object(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white)

#create an NPC
npc = Object(SCREEN_WIDTH/2 - 5, SCREEN_HEIGHT/2, '@', libtcod.yellow)

objects = [npc, player]



while not libtcod.console_is_window_closed():
	
	for object in objects:
		object.draw()

	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	libtcod.console_flush()

	for object in objects:
		object.clear()

	#handle keys and exit game if needed
	exit = handle_keys()
	if exit:
		break