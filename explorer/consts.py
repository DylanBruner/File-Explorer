from PIL import Image

IMAGE_PATH = 'explorer/data/images/'
IMAGE_SIZE = (25, 25)
images = {'arrow_forward': None, 'arrow_back': None, 'file': None,
          'arrow_upward': None, 'refresh': None, 'search': None,
          'folder': None}

for name in images:
    images[name] = Image.open(IMAGE_PATH + name + '.png')
    images[name] = images[name].resize(IMAGE_SIZE)
    # images[name] = Image.eval(images[name], lambda x: 255 - x)


def toHex(rgb):
    return '#%02x%02x%02x' % rgb

BG_ONE       = toHex((50, 50, 50))
BORDER_COLOR = toHex((83, 83, 83))