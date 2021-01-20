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
    elif max_x < 100 or max_y < 100:
        return {
            "error_code": -2,
            "error_msg": "max_x and max_y must be greater than 99",
            "data": [],
        }
    elif (max_x-2*radius)*(max_y-2*radius)<=(num_count*radius*radius*4):
        return {
            "error_code": -3,
            "error_msg": "screen too small",
            "data": [],
        }
    else:
        all_points = []
        for x in range (radius, max_x-radius+1):
            for y in range(radius, max_y-radius+1):
                all_points.append((x,y))
        
        chosen_points = []
        for _ in range(num_count):
            px, py = choice(all_points)
            # remove all the points in the square centered by p
            for x in range (px-2*radius, px+2*radius+1):
                for y in range (py-2*radius, py+2*radius+1):
                    try:
                        all_points.remove((px, py))
                    except ValueError:
                        pass
            chosen_points.append((px,py))

        for px, py in chosen_points:
            item = {
                "num": randint(0, max_num),
                "color": choice(colors),
                "shape": choice(shapes),
                "x": px,
                "y": py,
                "radius": radius,
            }
            result.append(item)
        return {
            "error_code": 0,
            "error_msg": "Successful.",
            "data": result,
        }
