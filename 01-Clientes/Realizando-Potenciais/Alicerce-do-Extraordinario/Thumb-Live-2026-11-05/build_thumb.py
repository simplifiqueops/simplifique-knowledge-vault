from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = Path('/home/simplifique/vault/01-Clientes/Realizando-Potenciais/Alicerce-do-Extraordinario')
HERO = ROOT / 'Pagina-de-Vendas/assets/figma-hero'
OUT = ROOT / 'Thumb-Live-2026-11-05'
W, H = 1920, 1080

BG = HERO / 'hero-background.png'
VANESSA = HERO / 'hero-vanessa.png'
LOGO = OUT / 'logo-alicerce.png'
BOLD = '/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf'
REG = '/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf'


def cover(im, size, anchor=(0.5, 0.5)):
    tw, th = size
    scale = max(tw / im.width, th / im.height)
    nw, nh = round(im.width * scale), round(im.height * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left = round((nw - tw) * anchor[0])
    top = round((nh - th) * anchor[1])
    return im.crop((left, top, left + tw, top + th))

# Full-bleed hero background.
background = cover(Image.open(BG).convert('RGB'), (W, H), anchor=(0.46, 0.5)).convert('RGBA')
background = ImageEnhance.Contrast(background).enhance(1.07)
canvas = background

# Brand-dark overlay and left-to-right readability gradient.
overlay = Image.new('RGBA', (W, H), (8, 29, 31, 72))
canvas = Image.alpha_composite(canvas, overlay)
grad = Image.new('RGBA', (W, H), (0, 0, 0, 0))
gp = grad.load()
for x in range(W):
    t = x / (W - 1)
    a = int(224 * max(0.0, 1.0 - t / 0.78) ** 1.6 + 28)
    for y in range(H):
        gp[x, y] = (7, 26, 28, min(235, a))
canvas = Image.alpha_composite(canvas, grad)

# Soft halo behind Vanessa, echoing the page hero.
halo = Image.new('RGBA', (700, 700), (0, 0, 0, 0))
hd = ImageDraw.Draw(halo)
hd.ellipse((90, 90, 610, 610), outline=(240, 219, 185, 185), width=8)
hd.ellipse((130, 130, 570, 570), outline=(240, 219, 185, 95), width=5)
halo = halo.filter(ImageFilter.GaussianBlur(3))
canvas.alpha_composite(halo, (1130, 185))

# Official Vanessa cutout from the page hero.
vanessa = Image.open(VANESSA).convert('RGBA')
scale = 1020 / vanessa.height
vanessa = vanessa.resize((round(vanessa.width * scale), 1020), Image.Resampling.LANCZOS)
# Slightly increase clarity while preserving the original asset.
rgb = ImageEnhance.Contrast(vanessa.convert('RGB')).enhance(1.04)
rgb.putalpha(vanessa.getchannel('A'))
vanessa = rgb
canvas.alpha_composite(vanessa, (1120, 60))

# Prepare the official logo as a clean transparent white mark.
logo_src = Image.open(LOGO).convert('RGBA')
px = logo_src.load()
for y in range(logo_src.height):
    for x in range(logo_src.width):
        r, g, b, _ = px[x, y]
        lum = max(r, g, b)
        alpha = max(0, min(255, round((lum - 95) * 255 / 150)))
        px[x, y] = (255, 255, 255, alpha)
bbox = logo_src.getchannel('A').getbbox()
logo_src = logo_src.crop(bbox)
logo_w = 650
logo_h = round(logo_src.height * logo_w / logo_src.width)
logo_src = logo_src.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
canvas.alpha_composite(logo_src, (105, 82))

d = ImageDraw.Draw(canvas)
cream = (247, 241, 227, 255)
yellow = (255, 209, 13, 255)
dark = (8, 34, 37, 255)
gold = (241, 222, 192, 255)

# Live badge.
badge = (108, 335, 438, 413)
d.rounded_rectangle(badge, radius=18, fill=(140, 75, 68, 255))
d.ellipse((137, 360, 159, 382), fill=(255, 209, 13, 255))
d.text((180, 349), 'LIVE HOJE', font=ImageFont.truetype(BOLD, 43), fill=(255, 255, 255, 255))

# Main service information.
d.text((102, 455), '05/11', font=ImageFont.truetype(BOLD, 150), fill=cream, stroke_width=2, stroke_fill=(8, 34, 37, 120))
d.text((105, 620), 'ÀS 20H', font=ImageFont.truetype(BOLD, 112), fill=yellow)
d.text((111, 757), 'HORÁRIO DE BRASÍLIA', font=ImageFont.truetype(BOLD, 36), fill=gold)

# Presenter identification.
d.rounded_rectangle((105, 858, 955, 958), radius=22, fill=(8, 34, 37, 205), outline=(241, 222, 192, 155), width=2)
d.text((142, 885), 'COM DRA. VANESSA CESNIK', font=ImageFont.truetype(BOLD, 41), fill=cream)

# Controlled bottom accent.
d.rounded_rectangle((105, 1000, 760, 1009), radius=5, fill=yellow)

out = OUT / 'thumb-youtube-alicerce-live-2026-11-05.png'
canvas.convert('RGB').save(out, quality=95, optimize=True)
print(out)
print(Image.open(out).size)
