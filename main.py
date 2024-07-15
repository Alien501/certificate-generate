from PIL import Image, ImageDraw, ImageFont

def generate_certificate(name, output_path):
    cert_image = Image.open('sample.png')
    image = ImageDraw.Draw(cert_image)
    font = ImageFont.truetype('pangolin.ttf', 190)
    image.text((800, 1200), name, font=font, fill=(255, 255, 255))
    cert_image.save(output_path)
    
part_list = [
    'Name 7',
    'Name 6',
    'Name 5',
    'Name 4',
    'Name 3',
    'Name 2',
    'Name 1',
]

for i in part_list:
    generate_certificate(i, output_path=f'./output/{i}.png')