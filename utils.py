import requests
from colorthief import ColorThief

# now let's define a function to save the images. this function is meant to be placed in a try except fashion afterwards
def save_img(pic_url, img_name):
    try:
        response = requests.get(pic_url, stream=True)
        if not response.ok:
            print("Failed to download image:", response.status_code)
            return response.status_code

        with open(img_name, 'wb') as handle:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)

        print("Image saved successfully as", img_name)
    except Exception as e:
        print(f"The error {str(e)} ocurred while saving the image")
        return 600
    return response.status_code

def create_dict (num):
  result = {}
  for i in range(0, num):
    result[f"red_{str(i)}"] = []
    result[f"green_{str(i)}"] = []
    result[f"blue_{str(i)}"] = []
  result["label"] = []
  return result

def imagen_colores(img):
    color_thief = ColorThief(img)
    palette = color_thief.get_palette(color_count= num, quality = 1)
    result = []
    for i in range(0, num):
        color = palette[i]
        result.append(color[0])
        result.append(color[1])
        result.append(color[2])
    return result