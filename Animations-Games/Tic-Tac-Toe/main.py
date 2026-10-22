import pygame 

pygame.init()

HEIGHT = 900
WIDTH = 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

#####X And O dims#####
def dimentions():
	dims = []

	for i in range(1, 3+1):
		row_dims = []
		for j in range(1, 3+1):
			if j == 1:
				x = ((WIDTH/3) / 2) * j
			elif j == 2:
				x = ((HEIGHT/3) / 2) * (j + 1)
			elif j == 3:
				x = ((HEIGHT/3) / 2) * (j + 2)

			if i == 1:
				y = ((HEIGHT/3) / 2) * i
			elif i == 2:
				y = ((HEIGHT/3) / 2) * (i + 1)
			elif i == 3:
				y = ((HEIGHT/3) / 2) * (i + 2)

			row_dims.append([x, y, ""])
		dims.append(row_dims)
	return dims
#######Draw Grid######
def Grid():
	def Horizontal():
		for i in range(1, 2+1):
			start_pos = ((HEIGHT/3)*i , 0)
			End_pos = ((HEIGHT/3)*i , HEIGHT)

			pygame.draw.line(window, (0, 0, 0), start_pos, End_pos, 3)

	def Vertical():
		for i in range(1, 2+1):
			start_pos = (0, (WIDTH/3)*i)
			End_pos = (WIDTH ,(WIDTH/3)*i)

			pygame.draw.line(window, (0, 0, 0), start_pos, End_pos, 3)

	Horizontal()
	Vertical()

	pygame.display.update()

#######Draw Board#####
font = pygame.font.SysFont("comicsans", 500)
board = [
	["", "", ""],
	["", "", ""],
	["", "", ""]]

def Draw_board():
	for i, li in enumerate(board):
		for j, ch in enumerate(li):
			if ch == "X":
				color = (255,0,0)
			else: 
				color = (0,0,255)
			dims = dimentions()

			font_text = font.render(ch, 1, color)
			x, y, ins =  dims[i][j]

			x = x - int(font_text.get_width()/2)
			y = y - int(font_text.get_height()/2)

			window.blit(font_text, (x, y+20))
			pygame.display.update()

######Colillion#######
def Collition(mx ,my, sign):
	global board

	if (mx in range(300)) and (my in range(300) and board[0][0] == ""):
		board[0][0] = sign 
		return True

	if (mx in range(300, 600)) and (my in range(300) and board[0][1] == ""):
		board[0][1] = sign 
		return True

	if (mx in range(600, 900)) and (my in range(300) and board[0][2] == ""):
		board[0][2] = sign 
		return True

	if (mx in range(300)) and (my in range(300, 600) and board[1][0] == ""):
		board[1][0] = sign 
		return True

	if (mx in range(300, 600)) and (my in range(300, 600) and board[1][1] == ""):
		board[1][1] = sign 
		return True

	if (mx in range(600, 900)) and (my in range(300, 600) and board[1][2] == ""):
		board[1][2] = sign 
		return True

	if (mx in range(300)) and (my in range(600, 900) and board[2][0] == ""):
		board[2][0] = sign 
		return True

	if (mx in range(300, 600)) and (my in range(600, 900) and board[2][1] == ""):
		board[2][1] = sign 
		return True

	if (mx in range(600, 900)) and (my in range(600, 900) and (board[2][2] == "")):
		board[2][2] = sign 
		return True
	return False

#####check-win########
def check_win():
	if board[0][0]  == "X" and board[0][1]  == "X" and board[0][2] == "X":
		draw_win(1)
		return True

	if board[1][0]  == "X" and board[1][1]  == "X" and board[1][2] == "X":
		draw_win(1)
		return True

	if board[2][0]  == "X" and board[2][1] == "X" and board[2][2] == "X":
		draw_win(1)
		return True

	if board[0][0]  == "X" and board[1][1]  == "X" and board[2][2] == "X":
		draw_win(1)
		return True

	if board[0][2]  == "X" and board[1][1]  == "X" and board[2][0] == "X":
		draw_win(1)
		return True

	if board[0][0]  == "X" and board[1][0]  == "X" and board[2][0] == "X":
		draw_win(1)
		return True

	if board[0][1]  == "X" and board[1][1]  == "X" and board[2][1] == "X":
		draw_win(1)
		return True

	if board[0][2]  == "X" and board[1][2] == "X" and board[2][2] == "X":
		draw_win(1)
		return True



	if board[0][0]  == "O" and board[0][1]  == "O" and board[0][2] == "O":
		draw_win(2)
		return True

	if board[1][0]  == "O" and board[1][1]  == "O" and board[1][2] == "O":
		draw_win(2)
		return True

	if board[2][0]  == "O" and board[2][1] == "O" and board[2][2] == "O":
		draw_win(2)
		return True

	if board[0][0]  == "O" and board[0][1]  == "O" and board[0][2] == "O":
		draw_win(2)
		return True

	if board[1][0]  == "O" and board[1][1]  == "O" and board[1][2] == "O":
		draw_win(2)
		return True

	if board[2][0]  == "O" and board[2][1] == "O" and board[2][2] == "O":
		draw_win(2)
		return True

	if board[0][0]  == "O" and board[1][1]  == "O" and board[2][2] == "O":
		draw_win(2)
		return True

	if board[0][2]  == "O" and board[1][1]  == "O" and board[2][0] == "O":
		draw_win(2)
		return True

	if board[0][0]  == "O" and board[1][0]  == "O" and board[2][0] == "O":
		draw_win(2)
		return True

	if board[0][1]  == "O" and board[1][1]  == "O" and board[2][1] == "O":
		draw_win(2)
		return True

	if board[0][2]  == "O" and board[1][2] == "O" and board[2][2] == "À":
		draw_win(2)
		return True

	if board[0][0]  == "O" and board[0][1]  == "O" and board[0][2] == "O":
		draw_win(2)
		return True

	if board[1][0]  == "O" and board[1][1]  == "O" and board[1][2] == "O":
		draw_win(2)
		return True

	if board[2][0]  == "O" and board[2][1] == "O" and board[2][2] == "O":
		draw_win(2)
		return True	
	return False

#####Draw win#########
winner_font = pygame.font.SysFont("comicsansms", 100)
def draw_win(winner):
	Draw_board()
	pygame.time.delay(1000)

	window.fill((255,255,255))

	text = winner_font.render(f"player {winner} win!", True, (0, 0, 0), True		)
	x = (WIDTH/2) - (text.get_width()//2)
	y = (HEIGHT/2) - (text.get_height()//2)

	window.blit(text, (x, y))
	pygame.display.update()
	
#####check Draw#######
def check_draw():
	n = 0
	for i in board:
		if "" not in i:
			n += 1
	if n == 3:
		return True

####Draw Draw#########
def Draw():
	window.fill((255,255,255))

	text = winner_font.render("Draw", True, (0, 0, 0))
	x = (WIDTH/2) - (text.get_width()//2)
	y = (HEIGHT/2) - (text.get_height()//2)

	window.blit(text, (x, y))
	pygame.display.update()

#######Main Loop######
def main():
	fps = 30
	clock = pygame.time.Clock()
	sign = []
	run = True

	while run:
		clock.tick(fps)

		Grid()
		Draw_board()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				mx, my = pygame.mouse.get_pos()

				try:
					if sign[-1] == "X":
						if Collition(mx, my, "O"):
							sign.append("O")

					elif sign[-1] == "O":
						if Collition(mx, my, "X"):
							sign.append("X")
				except:
					Collition(mx, my, "O")
					sign.append("O")

		if check_win():
			run = False

		if check_draw():
			Draw()
			run = False

	pygame.time.delay(2000)


window.fill((255, 255, 255))
pygame.display.update()

main()
pygame.quit()