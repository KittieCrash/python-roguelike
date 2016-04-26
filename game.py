import libtcodpy as libtcod

##########################################################
# Constants and Functions
##########################################################

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

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
			playery -= 1
		elif key.c == ord('s'):
			playery += 1
		elif key.c == ord('d'):
			playerx += 1
		elif key.c == ord('a'):
			playerx -= 1

###########################################################
# Intiailization and Game Loop
###########################################################

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/Roguelike-like', False)
con = libtcod.console_new(SCREEN_WIDTH, SCEREEN_HEIGHT)

playerx = SCREEN_WIDTH/2
playery = SCREEN_HEIGHT/2



while not libtcod.console_is_window_closed():
	libtcod.console_set_default_foreground(con, libtcod.white)
	libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)
	libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
	libtcod.console_flush()

	libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)

	#handle keys and exit game if needed
	exit = handle_keys()
	if exit:
		break