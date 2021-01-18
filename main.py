from fastapi import FastAPI
from random import randint, choice

app = FastAPI()
colors = ['FF0000', 'FF7F00', 'FFFF00', '00FF00', '0000FF', '2E2B5F', '8B00FF']
shapes = [3, 4, 5, 6, 7, 8]
max_num = 99


@app.get('/numCount/{num_count}/radius/{radius}/maxX/{max_x}/maxY/{max_y}')
async def num_game(num_count: int, radius: int, max_x: int, max_y: int):
    result = []
    if num_count < 3 or num_count > 30:
        return {
            "error_code": -1,
            "error_msg": "num_count must be greater than 3 and less than 31",
            "data": [],
        }
    else:
        for i in range(num_count):
            ratio_x = int((max_x-2*radius)/radius)
            ratio_y = int((max_y-2*radius)/radius)
            item = {
                "num": randint(0, max_num),
                "color": choice(colors),
                "shape": choice(shapes),
                "x": randint(1, ratio_x)*radius,
                "y": randint(1, ratio_y)*radius,
                "radius": radius,
            }
            result.append(item)
        return {
            "error_code": 0,
            "error_msg": "Successful.",
            "data": result,
        }
