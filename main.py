import argparse
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

parser = argparse.ArgumentParser(
                    prog="Caption",
                    description="A script for making outlined text for videos")

parser.add_argument("-t", "--TEXT", default="Hello world!", type=str)
parser.add_argument("-i", "--INNER_FILL", default="white", type=str)
parser.add_argument("-o", "--OUTER_FILL", default="black", type=str)
parser.add_argument("-fs", "--FONT_SIZE", default=128, type=int)
parser.add_argument("-os", "--OUTLINE_SIZE", default=128//16, type=int)
args = parser.parse_args()

# Use a GNU font
font = ImageFont.truetype("./FreeSans.ttf", args.FONT_SIZE)

# Create a temporary image for the text box
image = Image.new("RGBA", (1000, 1000), "white")
draw_obj = ImageDraw.Draw(image)

# Determine text box size
_, _, w, h = draw_obj.textbbox((0, 0), str(args.TEXT), stroke_width=args.OUTLINE_SIZE, font=font)
t = Image.new("RGBA", (w, h), (255, 0, 0, 0))
t_draw = ImageDraw.Draw(t)
t_draw.text((0, 0), text=str(args.TEXT), fill=args.INNER_FILL, stroke_fill=args.OUTER_FILL, stroke_width=args.OUTLINE_SIZE, font=font)

t.save("./output.png")
