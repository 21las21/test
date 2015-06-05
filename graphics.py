import pygame

def render():

  # pygame.draw.line - нарисовать отрезок
  #
  # pygame.draw.line(screen, <цвет>, <один конец отрезка>, <второй конец отрезка>)
  #
  # цвет (<красный>, <зеленый>, <синий>)
  # красный зеленый и синий - числа от 0 до 255
  #
  # цвет: (255, 255, 255) - белый, (0, 0, 0) - черный
  #
  # screen.fill - заполнить весь экран одним цветом
  # screen.fill(<цвет>)

  screen.fill((0, 0, 0))


  ## Попробуй порисовать разные отрезки, разными цветами

  pygame.draw.line(screen, (255, 255, 255), (0, 0), (640, 480))

screen = pygame.display.set_mode((640, 480))

loop = True
while loop:
  for e in pygame.event.get():
    if e.type == pygame.QUIT:
      loop = False
    elif e.type == pygame.KEYDOWN:
      if e.key == pygame.K_ESCAPE:
        loop = False

  render()

  pygame.display.flip()
