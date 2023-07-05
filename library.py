from PIL import Image, ImageDraw

def ellipse(x, y, offset):
    image = Image.new("RGB", (400, 400), "blue")
    draw = ImageDraw.Draw(image)
    draw.ellipse((x, y, x+offset, y+offset), fill="red")
    return image


def make_gif():
    frames = []
    x = 0
    y = 0
    offset = 50
    for number in range(20):
        frames.append(ellipse(x, y, offset))
        x += 35
        y += 35
        
    frame_one = frames[0]
    frame_one.save("circle.gif", format="GIF", append_images=frames,
                   save_all=True, duration=100, loop=0)
    

if __name__ == "__main__":
    make_gif()
