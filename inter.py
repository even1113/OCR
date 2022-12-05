import torch
from torchvision import transforms
from PIL import Image
from torchvision.utils import save_image

img = Image.open('img_little.png', mode='r')
print('img_little')
print(img)
print('---' * 5)
img_to_tensor = transforms.ToTensor()(img)
print(img_to_tensor.shape)

nearest_neighbor_interpolation = transforms.Resize(size=(1024, 1024),
                                                   interpolation=transforms.InterpolationMode.NEAREST)
nearest_resize_img = nearest_neighbor_interpolation(img_to_tensor)
print(nearest_resize_img.shape)

bilinear_interpolation = transforms.Resize(size=(1024, 1024),
                                           interpolation=transforms.InterpolationMode.BILINEAR)
bilinear_resize_img = bilinear_interpolation(img_to_tensor)
print(bilinear_resize_img.shape)

bicubic_interpolation = transforms.Resize(size=(1024, 1024),
                                          interpolation=transforms.InterpolationMode.BICUBIC)
bicubic_resize_img = bicubic_interpolation(img_to_tensor)
print(bilinear_resize_img.shape)


save_image(nearest_resize_img, './nearest.png')
save_image(bilinear_resize_img, './bilinear.png')
save_image(bicubic_resize_img, './bicubic.png')
