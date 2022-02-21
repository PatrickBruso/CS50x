from keras.preprocessing.image import load_img
import warnings

img = load_img('static/palettes/ammo8.png')
print(type(img))
print(img.format)
print(img.mode)
print(img.size)