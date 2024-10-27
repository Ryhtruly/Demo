from src.player import Player
from src.block import Block, Block2
from src.fire import Fire
from src.confige import HEIGHT
from src.fan import Fan, Fan_N, Fan_M
from src.saw import Saw_Row, Saw_Collum, Saw, Saw_Collum2, Saw_Row_N2, Saw_Row_N, Saw_Collum3

from src.food import Banana, Apple, Strawberry, Melon


def reset_game(selected_character):
    block_size = 96

    player = Player(100, 100, 50, 50, selected_character)

    floor = []
    saws = []
    saw_rows = []
    saw_collums = []
    fans = []
    fan_rows = []
    fires = []
    foods = []
    ciels = []
    arrows = []
    foods = []

    for i in range(100):
        x = i * block_size
        y = HEIGHT - block_size * 9
        ciels.append(Block(x, y, block_size))

    for i in range(3):
        block_x = i * block_size
        block_y = HEIGHT - block_size
        floor.append(Block(block_x, block_y, block_size))

    for i in range(9, 16):
        x = i * block_size
        y = HEIGHT - block_size
        floor.append(Block(x, y, block_size))

    for i in range(73, 90):
        x = i * block_size
        y = HEIGHT - block_size
        floor.append(Block(x, y, block_size))

    for i in range(44, 60):
        x = i * block_size
        y = HEIGHT - block_size
        floor.append(Block(x, y, block_size))

    for i in range(3, 9):
        x = (i + 0.2) * block_size
        y = HEIGHT - block_size
        saws.append(Saw(x, y, 38, 38))

    for i in range(29, 33):
        x = (i + 0.2) * block_size
        y = HEIGHT - block_size * 0.5
        fires.append(Fire(x, y, 16, 32))
        fires.append(Fire(x + 0.35, y - 0.2, 16, 32))

    for i in range(60, 73):
        x = (i + 0.2) * block_size
        y = HEIGHT - block_size * 0.5
        fires.append(Fire(x, y, 16, 32))
        fires.append(Fire(x + 0.35, y - 0.2, 16, 32))

    for i in range(34, 44):
        x = (i + 0.2) * block_size
        y = HEIGHT - block_size
        saws.append(Saw(x, y, 38, 38))

    for i in range(23, 29):
        x = i * block_size
        y = HEIGHT - block_size
        floor.append(Block(x, y, block_size))

    collums = [2, 3, 4, 5]
    start_pos = 56

    for i in range(len(collums)):
        height = collums[i]
        for j in range(2, height + 1):
            block_x = block_size * (start_pos + i + 0.2)
            block_y = HEIGHT - block_size * (j - 0.2)
            saws.append(Saw(block_x, block_y, 38, 38))

    for i in range(61, 70, 4):
        x = block_size * (i + 0)
        y = HEIGHT - block_size * 5
        saws.append(Saw_Collum2(x, y, 38, 38, 200))

    for i in range(63, 72, 4):
        x = block_size * (i + 0.2)
        y = HEIGHT - block_size * 3
        saws.append(Saw_Collum3(x, y, 38, 38, 200))

    for i in range(61, 70, 4):
        x = block_size * (i + 0.2)
        y = HEIGHT - block_size * 2
        saws.append(Saw_Row_N(x, y, 38, 38, 200))

    for i in range(63, 72, 4):
        x = block_size * (i + 0.2)
        y = HEIGHT - block_size * 6
        saws.append(Saw_Row_N2(x, y, 38, 38, 200))

    for i in range(16, 23):
        x = block_size * (i + 0.3)
        y = HEIGHT - block_size * 0.5
        fires.append(Fire(x, y, 16, 32))
        fires.append(Fire(x + 0.35, y - 0.2, 16, 32))

    for i in range(64, 69, 4):
        x = block_size * (i + 0.3)
        y = HEIGHT - block_size * 2.5
        fans.append(Fan_M(x, y, 24, 8, 220))

    saw_rows.append(Saw_Row(block_size * 11, HEIGHT - block_size * 6.5, 38, 38))
    saw_rows.append(Saw_Row_N(block_size * 23, HEIGHT - block_size * 1.5, 38, 38, 400))
    saw_collums.append(Saw_Collum(block_size * 10.2, HEIGHT - block_size * 1.8, 38, 38))
    saw_collums.append(Saw_Collum2(block_size * 15, HEIGHT - block_size * 5, 38, 38, 300))
    saw_collums.append(Saw_Collum2(block_size * 23.2, HEIGHT - block_size * 6, 38, 38, 270))
    saw_collums.append(Saw_Collum2(block_size * 26.2, HEIGHT - block_size * 7.5, 38, 38, 400))
    saw_collums.append(Saw_Collum2(block_size * 29.2, HEIGHT - block_size * 8, 38, 38, 600))
    saw_collums.append(Saw_Collum2(block_size * 32.2, HEIGHT - block_size * 8, 38, 38, 600))
    saw_collums.append(Saw_Collum2(block_size * 36.2, HEIGHT - block_size * 8, 38, 38, 200))
    saw_collums.append(Saw_Collum2(block_size * 52.2, HEIGHT - block_size * 6, 38, 38, 400))
    saw_collums.append(Saw_Collum3(block_size * 53.2, HEIGHT - block_size * 2, 38, 38, 400))
    fans.append(Fan(8.3 * block_size, HEIGHT - block_size * 3, 24, 8))
    fans.append(Fan(19.3 * block_size, HEIGHT - block_size * 3, 24, 8))
    fans.append(Fan(34.3 * block_size, HEIGHT - block_size * 2.5, 24, 8))
    fans.append(Fan_N(35.25 * block_size, HEIGHT - block_size * 2.5, 24, 8, 300))
    fans.append(Fan_N(35 * block_size, HEIGHT - block_size * 2.5, 24, 8, 300))
    fans.append(Fan_N(35.5 * block_size, HEIGHT - block_size * 2.5, 24, 8, 300))
    fans.append(Fan_N(35.75 * block_size, HEIGHT - block_size * 2.5, 24, 8, 300))
    fans.append(Fan_N(18.25 * block_size, HEIGHT - block_size * 2.5, 24, 8, 200))
    fans.append(Fan_N(18 * block_size, HEIGHT - block_size * 2.5, 24, 8, 200))
    fans.append(Fan_N(18.5 * block_size, HEIGHT - block_size * 2.5, 24, 8, 200))
    fans.append(Fan_N(18.75 * block_size, HEIGHT - block_size * 2.5, 24, 8, 200))
    fans.append(Fan_M(44.3 * block_size, HEIGHT - block_size * 1.8, 24, 8, 330))
    fans.append(Fan_M(block_size * 56.3, HEIGHT - block_size * 2.5, 24, 8, 180))
    fans.append(Fan_M(block_size * 58.3, HEIGHT - block_size * 4.5, 24, 8, 180))
    fans.append(Fan_M(block_size * 24.7, HEIGHT - block_size * 4, 24, 8, 180))

    for i in range(74, 79, 2):
        x = block_size * (i + 0.2)
        y = HEIGHT - block_size * 8
        saws.append(Saw_Collum2(x, y, 38, 38, 600))

    for i in range(75, 78, 2):
        x = block_size * (i + 0.2)
        y = HEIGHT - block_size * 4
        saws.append(Saw_Collum3(x, y, 38, 38, 380))

    import random

    food_types = [Banana, Apple, Strawberry, Melon]

    food_positions = [
        (4.2, 3.7), (6.2, 3.7), (9.2, 1.7), (11.2, 1.7), (14.2, 1.7),
        (12.2, 3.7), (13.2, 3.7), (4.2, 6.7), (6.2, 6.7), (10.2, 6.7),
        (15.2, 6.7), (17.2, 5.7), (21.2, 7.7), (21.7, 3.2), (27.7, 5.3),
        (24.7, 6.3), (30.7, 6.3), (28.2, 2.7), (37.2, 5.7), (38.2, 6.7), (40.2, 3.3), (44.2, 6.7), (39.2, 4.7),
        (56.2, 6.7), (59.2, 6.7), (62.3, 4.7), (66.2, 4.7),
        (70.2, 4.7), (64.2, 6.7), (68.2, 6.7), (75.2, 2.7), (77.2, 2.7)
    ]

    foods = [
        random.choice(food_types)(block_size * x, HEIGHT - block_size * y)
        for x, y in food_positions
    ]

    for saw_row in saw_rows:
        saw_row.on()

    for fire in fires:
        fire.on()

    for saw_collum in saw_collums:
        saw_collum.on()

    for fan in fans:
        fan.on()

    for saw in saws:
        saw.on()

    for arrow in arrows:
        arrow.on()

    objects = [*floor, *ciels, *saws, *saw_collums, *saw_rows, *fans, *fan_rows, *fires, *foods, *arrows, *foods]

    for i in range(1, 9):
        x = 0
        y = HEIGHT - i * block_size
        objects.append(Block(x, y, block_size))

    # Giả sử block_size và HEIGHT đã được định nghĩa ở phần đầu của chương trình
    def create_block(x, y, block_type, block_size, HEIGHT):
        return eval(f"{block_type}(block_size * {x}, HEIGHT - block_size * {y}, block_size)")

    # Định nghĩa thông tin blocks
    block_data = [
        # Format: (x, y, type)
        (33, 1, "Block"),
        (55, 2, "Block2"),
        (59, 6, "Block2"),
        (28, 2, "Block2"),
        (38, 6, "Block2"),
        (56, 8, "Block2"),
        (64, 8, "Block2"),
        (68, 8, "Block2"),
        (75, 2, "Block2"),
        (77, 2, "Block2")
    ]

    # Tạo blocks và thêm vào objects
    blocks = [create_block(x, y, block_type, block_size, HEIGHT) for x, y, block_type in block_data]
    objects.extend(blocks)

    objects.extend(blocks)

    for i in range(2, 5):
        x = block_size
        y = HEIGHT - i * block_size
        objects.append(Block2(x, y, block_size))

    for i in range(62, 71, 4):
        x = block_size * i
        y = HEIGHT - block_size * 4
        objects.append(Block2(x, y, block_size))

    for i in range(12, 14):
        x = i * block_size
        y = HEIGHT - block_size * 3
        objects.append(Block2(x, y, block_size))

    for i in range(4, 7, 2):
        x = i * block_size
        y = HEIGHT - 3 * block_size
        objects.append(Block2(x, y, block_size))

    for i in range(10, 16):
        x = i * block_size
        y = HEIGHT - block_size * 6
        objects.append(Block2(x, y, block_size))

    for i in range(3, 7):
        x = i * block_size
        y = HEIGHT - block_size * 6
        objects.append(Block2(x, y, block_size))

    for i in range(3, 6):
        x = block_size * 17
        y = HEIGHT - block_size * i
        objects.append(Block2(x, y, block_size))

    for i in range(21, 24):
        x = block_size * i
        y = HEIGHT - block_size * 7
        objects.append(Block2(x, y, block_size))
    objects.append(Block2(block_size * 23, HEIGHT - block_size * 8, block_size))

    for i in range(21, 23):
        x = block_size * i
        y = HEIGHT - block_size * 2.5
        objects.append((Block2(x, y, block_size)))
    for i in range(24, 26):
        x = block_size * i
        y = HEIGHT - block_size * 3.5
        objects.append(Block2(x, y, block_size))

    for i in range(27, 29):
        x = block_size * i
        y = HEIGHT - block_size * 4.5
        objects.append(Block2(x, y, block_size))

    for i in range(30, 32):
        x = block_size * i
        y = HEIGHT - block_size * 5.5
        objects.append(Block2(x, y, block_size))

    for i in range(2, 8):
        x = block_size * 33
        y = HEIGHT - block_size * i
        objects.append(Block2(x, y, block_size))

    for i in range(40, 44):
        x = block_size * i
        y = HEIGHT - block_size * 2.5
        objects.append(Block2(x, y, block_size))

    for i in range(36, 39):
        x = block_size * i
        y = HEIGHT - block_size * 5
        objects.append(Block2(x, y, block_size))

    for i in range(6, 9):
        x = block_size * 39
        y = HEIGHT - block_size * i
        objects.append(Block2(x, y, block_size))

    for i in range(7, 9):
        x = block_size * 52
        y = HEIGHT - block_size * i
        objects.append(Block2(x, y, block_size))

    for i in range(7, 9):
        x = block_size * 53
        y = HEIGHT - block_size * i
        objects.append(Block2(x, y, block_size))

    for i in range(5, 9):
        for j in range(41, 44):
            block_x = j * block_size
            block_y = HEIGHT - block_size * i
            objects.append(Block2(block_x, block_y, block_size))

    for i in range(3, 9):
        for j in range(45, 52):
            block_x = j * block_size
            block_y = HEIGHT - block_size * i
            objects.append(Block2(block_x, block_y, block_size))

    start = 80
    for i in range(len(collums)):
        height = collums[i]
        for j in range(2, height + 1):
            block_x = block_size * (start + i)
            block_y = HEIGHT - block_size * (j)
            objects.append(Block2(block_x, block_y, block_size))

    for i in range(2, 7):
        for j in range(84, 87):
            x = block_size * j
            y = HEIGHT - block_size * i
            objects.append(Block2(x, y, block_size))

    for i in range(2, 9):
        for j in range(87, 91):
            x = block_size * j
            y = HEIGHT - block_size * i
            objects.append(Block(x, y, block_size))

    for obj in objects:
        if isinstance(obj, (Saw, Saw_Collum, Saw_Row, Fire, Fan_N, Fan_M, Fan, Saw_Collum2, Saw_Row_N2, Saw_Row_N, Saw_Collum3)):
            obj.on()

    offset_x = 0
    return player, objects, offset_x

def reset_objects(objects):
    for obj in objects:
        if hasattr(obj, 'reset'):
            obj.reset()
