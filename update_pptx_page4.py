from pptx import Presentation
from pptx.util import Inches
import os

pptx_path = 'Naresh & Co Profile - Copy.pptx'
prs = Presentation(pptx_path)

# Remove last slide if it is the standalone Thailand slide
if len(prs.slides) > 8:
    last = prs.slides[-1]
    if any(getattr(shape, 'has_text_frame', False) and shape.has_text_frame and 'Thailand Project Photos' in shape.text for shape in last.shapes):
        prs.slides._sldIdLst.remove(prs.slides._sldIdLst[-1])

# Update page 2 wording
slide2 = prs.slides[1]
for shape in slide2.shapes:
    if getattr(shape, 'has_text_frame', False) and shape.has_text_frame:
        if shape.text.strip().startswith('Naresh & Co is a leading provider'):
            shape.text = 'Naresh & Co is a leading provider of telecom infrastructure fabricating and end-to-end engineering solutions for the telecommunication sector. We specialize in construction, installation and commissioning of wireless and wireline telecom equipment and networks across India and internationally.'
        elif shape.text.strip().startswith('Our portfolio spans supply and fabrication'):
            shape.text = 'Our portfolio spans supply and fabrication of telecommunications and EB mast, poles and towers; IBS Poles; Micro Towers (up to 16 m); Macro Towers (up to 55 m - GPT and RTT); lattice tower fabrication for 12 to 100 meters; and full deployment of 2G, 3G, 4G, 5G, MW, and Microwave hops.'

# Add Thailand images on page 4 using the picture 28 area
slide4 = prs.slides[3]
image_paths = [
    r'C:\Users\babuk\Downloads\IMG-20260525-WA0009.jpg',
    r'C:\Users\babuk\Downloads\IMG-20260525-WA0010.jpg',
    r'C:\Users\babuk\Downloads\IMG-20260525-WA0006.jpg',
    r'C:\Users\babuk\Downloads\IMG-20260525-WA0007.jpg',
    r'C:\Users\babuk\Downloads\IMG-20260525-WA0008.jpg',
]
existing_images = [p for p in image_paths if os.path.exists(p)]
if not existing_images:
    raise FileNotFoundError('Thailand image files not found.')

# Remove the existing large image block if present
for shape in list(slide4.shapes):
    if shape.shape_type == 13 and shape.name == 'Picture 28':
        sp = shape._element
        sp.getparent().remove(sp)
        break

# Find the original picture 28 placement area
area_left = Inches(0.4)
area_top = Inches(4.55)
img_width = Inches(1.6)
img_height = Inches(1.1)
for idx, img_path in enumerate(existing_images[:4]):
    col = idx % 2
    row = idx // 2
    left = area_left + Inches(col * 1.75)
    top = area_top + Inches(row * 1.25)
    slide4.shapes.add_picture(img_path, left, top, width=img_width, height=img_height)

prs.save(pptx_path)
print('Updated', pptx_path)
