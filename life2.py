import pygame
import sys
from pygame.locals import *
import json
import time
import random
class Button:
    def create_button(self, surface, color, x, y, length, height, width, text, text_color):
        surface = self.draw_button(surface, color, length, height, x, y, width)
        surface = self.write_text(surface, text, text_color, length, height, x, y)
        self.rect = pygame.Rect(x,y, length, height)
        return surface

    def write_text(self, surface, text, text_color, length, height, x, y):
        font_size = int(length//len(text))+8
        myFont = pygame.font.SysFont("Calibri", font_size)
        myText = myFont.render(text, 1, text_color)
        surface.blit(myText, ((x+length/2) - myText.get_width()/2, (y+height/2) - myText.get_height()/2))
        return surface

    def draw_button(self, surface, color, length, height, x, y, width):           
        for i in range(1,10):
            s = pygame.Surface((length+(i*2),height+(i*2)))
            s.fill(color)
            alpha = (255/(i+2))
            if alpha <= 0:
                alpha = 1
            s.set_alpha(alpha)
            pygame.draw.rect(s, color, (x-i,y-i,length+i,height+i), width)
            surface.blit(s, (x-i,y-i))
        pygame.draw.rect(surface, color, (x,y,length,height), 0)
        pygame.draw.rect(surface, (190,190,190), (x,y,length,height), 1)  
        return surface

    def pressed(self, mouse):
        if mouse[0] > self.rect.topleft[0]:
            if mouse[1] > self.rect.topleft[1]:
                if mouse[0] < self.rect.bottomright[0]:
                    if mouse[1] < self.rect.bottomright[1]:
                        print("Some button was pressed!")
                        return True
                    else: return False
                else: return False
            else: return False
        else: return False

class GameOfLife:
    def __init__(self, width: int=640, height: int=480, cell_size: int=10, speed: int=100) -> None:
        self.width = width
        self.height = height
        self.delta = 60
        self.cell_size = cell_size
        self.flag = True
        # Устанавливаем размер окна
        self.screen_size = width, height+self.delta
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)
        self.Button1 = Button()
        self.Button2 = Button()
        self.Button3 = Button()
        self.Button4 = Button()
        self.Button5 = Button()
        self.Button6 = Button()
        self.Button7 = Button()
        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        # @see: http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))
        """
    Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
    """
    def draw_grid(self) -> None:
       # print(self.cells)
        for i in range(0 , len(self.cells)):
            for j in range(0 , len(self.cells[i])):
          #  print(cells[i][j],i,j)
         # p.draw.rect(root , RED , [i * 20 , j * 20 , 20 , 20])
              # print(i,j,self.cell[i][j])
             #  print('OOOKKK')
               if self.cells[i][j] == 1:
                #print('отрисовал')
                 r = 50
                 g = 200
                 b = 0
               #  r = random.randint(10,255)
               #  g = random.randint(10,255)
               #  b = random.randint(10,255)
                 pygame.draw.rect(self.screen ,pygame.Color('white') , [j *self.cell_size , i*self.cell_size  , self.cell_size ,self.cell_size ])
               else:
                 pygame.draw.rect(self.screen , pygame.Color('black') , [j *self.cell_size , i*self.cell_size  , self.cell_size ,self.cell_size ])  
       # pygame.draw.rect(self.screen, pygame.Color('black'), self.cell)
        

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        flag_up = False
        flag = True
        last = [0,0]
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            #if flag:
            self.draw_grid()        
            self.draw_lines()
        # () - цвет, отступ слева, отступ сверху, ширина, высота
            self.Button1.create_button(self.screen, (107,142,35), 20, self.height, 80,    self.delta,    0, "Сохранить", (255,255,255))
            self.Button2.create_button(self.screen, (107,142,35), 80+self.delta, self.height, 80,    self.delta,    0, "Загрузить", (255,255,255))
            self.Button3.create_button(self.screen, (107,142,35), 100*2+self.delta, self.height, 80,    self.delta,    0, "Остановить", (255,255,255))
            self.Button4.create_button(self.screen, (107,142,35), 105*3+self.delta, self.height, 80,    self.delta,    0, "Запустить", (255,255,255))
            self.Button5.create_button(self.screen, (107,142,35), 107*4+self.delta, self.height, 80,    self.delta,    0, "Очистить", (255,255,255))
            self.Button6.create_button(self.screen, (107,142,35), 110*5+self.delta, self.height, 80,    self.delta,    0, "Скорость+", (255,255,255))
            self.Button7.create_button(self.screen, (107,142,35), 110*6+self.delta, self.height, 80,    self.delta,    0, "Скорость-", (255,255,255))
            
            pygame.display.flip()
         #   time.sleep(100)
            clock.tick(self.speed)
            if flag:
               self.get_next_generation()
           # running = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   # print('ttyt')
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button1.pressed(pygame.mouse.get_pos()):
                        with open('file.txt', 'w') as fw:
                            json.dump(self.cells, fw)
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button2.pressed(pygame.mouse.get_pos()):
                        try:
                            with open('file.txt', 'r') as f:
                                 self.cells = json.load(f)
                            self.draw_grid()
                            flag = False
                        except Exception:
                              pygame.quit()
                              sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button3.pressed(pygame.mouse.get_pos()):
                        #print('3')
                        flag = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button4.pressed(pygame.mouse.get_pos()):
                       # print('4')
                        flag = True
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button5.pressed(pygame.mouse.get_pos()):
                        self.cells =[[0 for j in range(self.width // self.cell_size)] for i in range(self.height //self.cell_size)]
                        self.draw_grid()
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button6.pressed(pygame.mouse.get_pos()):
                        self.speed +=1
                if event.type == pygame.MOUSEBUTTONDOWN and self.Button7.pressed(pygame.mouse.get_pos()):
                         if self.speed>1:
                             self.speed-=1
                if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0]<self.width and event.pos[1]<self.height:
                  #  print(self.width//self.cell_size,self.height//self.cell_size)
                  #  print(len(self.cells),len(self.cells[0]))
                    flag_up = True
                    if self.cells[event.pos[1]//self.cell_size][event.pos[0]//self.cell_size] == 1:
                        self.cells[event.pos[1]//self.cell_size][event.pos[0]//self.cell_size] = 0
                    else:
                        self.cells[event.pos[1]//self.cell_size][event.pos[0]//self.cell_size] = 1
                if event.type == pygame.MOUSEMOTION and flag_up and event.pos[0]<self.width and event.pos[1]<self.height:
                    if last[0]==event.pos[1]//self.cell_size and last[1]==event.pos[0]//self.cell_size:
                        pass
                    else:
                        last[0] = event.pos[1]//self.cell_size
                        last[1] = event.pos[0]//self.cell_size
                        if self.cells[event.pos[1]//self.cell_size][event.pos[0]//self.cell_size] == 1:
                            self.cells[event.pos[1]//self.cell_size][event.pos[0]//self.cell_size] = 0
                        else:
                            self.cells[event.pos[1]//self.cell_size][event.pos[0]//self.cell_size] = 1
                if event.type == pygame.MOUSEBUTTONUP and flag_up:
                    flag_up = False
                  #  print('clickcckkckcc',event.pos)
            #if not(self.flag):
             #   running = False
        '''
        while True:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print('ttyt')
                        pygame.quit()
                        sys.exit()
           # running = False
        '''
     #   pygame.quit()
    """
        Создание списка клеток.

    Клетка считается живой, если ее значение равно 1, в противном случае клетка
    считается мертвой, то есть, ее значение равно 0.

    Parameters
    ----------
    randomize : bool
        Если значение истина, то создается матрица, где каждая клетка может
        быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

    Returns
    ----------
    out : Grid
        Матрица клеток размером `cell_height` х `cell_width`.
    """
    def create_grid(self, randomize: bool=False):
        if randomize:
            self.cells = [[random.choice([0 , 1]) for j in range(self.width // self.cell_size)] for i in range(self.height //self.cell_size)]
        return self.cells
    def get_neighbours(self, cell):
        system=[[-1 , -1] , [-1 , 0] , [-1 , 1] , [0 , -1] , [0 , 1] , [1 , -1] , [1 , 0] , [1 , 1]]
        count = 0
        for i in system:
            # все клетки вокруг заданной
            if self.cells[(cell[0] + i[0]) % len(self.cells)][(cell[1] + i[1]) % len(self.cells[0])]:
                count += 1
        return count
    """
    Вернуть список соседних клеток для клетки `cell`.

    Соседними считаются клетки по горизонтали, вертикали и диагоналям,
    то есть, во всех направлениях.

    Parameters
    ----------
    cell : Cell
        Клетка, для которой необходимо получить список соседей. Клетка
        представлена кортежем, содержащим ее координаты на игровом поле.

    Returns
    ----------
    out : Cells
        Список соседних клеток.
    """
    def get_next_generation(self):
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        cells2 = [[0 for j in range(len(self.cells[0]))] for i in range(len(self.cells))]
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j]:
                    if self.get_neighbours([i , j]) not in (2 , 3):
                        cells2[i][j] = 0
                        continue
                    cells2[i][j] = 1
                    continue
                if self.get_neighbours([i , j]) == 3:
                    cells2[i][j] = 1
                    continue
                cells2[i][j] = 0
        if self.cells == cells2:
            self.flag = False
        self.cells = cells2
       # cell = [0,1]
       # self.get_neighbours(cell)
       # print(-1%255)

if __name__ == '__main__':
    game = GameOfLife(1200, 700, 7)
    grid = game.create_grid(randomize=True)
   # pp(grid)
    game.run()
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   # print('ttyt')
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and game.Button1.pressed(pygame.mouse.get_pos()):
                        print('1')
                if event.type == pygame.MOUSEBUTTONDOWN and game.Button2.pressed(pygame.mouse.get_pos()):
                        print('2')
                if event.type == pygame.MOUSEBUTTONDOWN and game.Button3.pressed(pygame.mouse.get_pos()):
                        print('уже остановлено')
                if event.type == pygame.MOUSEBUTTONDOWN and game.Button4.pressed(pygame.mouse.get_pos()):
                        print('4')
                if event.type == pygame.MOUSEBUTTONDOWN and game.Button5.pressed(pygame.mouse.get_pos()):
                        self.cells =[[0 for j in range(self.width // self.cell_size)] for i in range(self.height //self.cell_size)] 
