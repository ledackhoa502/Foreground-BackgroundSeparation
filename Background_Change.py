from torchvision import models
from PIL import Image
import torch
import numpy as np
import cv2
# Apply the transformations needed
import torchvision.transforms as T


# Define the helper function
def decode_segmap(image, source, bgimg, nc=21):
    label_colors = np.array([(0, 0, 0),  # 0=background
                             # 1=aeroplane, 2=bicycle, 3=bird, 4=boat, 5=bottle
                             (46, 69, 58), (4, 68, 191), (107, 71, 45), (195, 210, 110), (244, 84, 24),
                             # 6=bus, 7=car, 8=cat, 9=chair, 10=cow
                             (219, 54, 207), (128, 128, 128), (202, 12, 248), (218, 251, 200), (157, 125, 126),
                             # 11=dining table, 12=dog, 13=horse, 14=motorbike, 15=person
                             (122, 245, 185), (62, 40, 170), (86, 128, 236), (64, 128, 128), (192, 128, 128),
                             # 16=potted plant, 17=sheep, 18=sofa, 19=train, 20=tv/monitor
                             (142, 113, 57), (252, 96, 6), (125, 43, 201), (231, 93, 180), (160, 244, 250)])

    r = np.zeros_like(image).astype(np.uint8)
    g = np.zeros_like(image).astype(np.uint8)
    b = np.zeros_like(image).astype(np.uint8)

    for l in range(0, nc):
        idx = image == l
        r[idx] = label_colors[l, 0]
        g[idx] = label_colors[l, 1]
        b[idx] = label_colors[l, 2]

    rgb = np.stack([r, g, b], axis=2)

    # Load the foreground input image
    foreground = cv2.imread(source)

    # Load the background input image
    background = cv2.imread(bgimg)

    # Change the color of foreground image to RGB
    # and resize images to match shape of R-band in RGB output map
    foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)
    background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
    foreground = cv2.resize(foreground, (r.shape[1], r.shape[0]))
    background = cv2.resize(background, (r.shape[1], r.shape[0]))

    # Convert uint8 to float
    foreground = foreground.astype(float)
    background = background.astype(float)

    # Create a binary mask of the RGB output map using the threshold value 0
    th, alpha = cv2.threshold(np.array(rgb), 0, 255, cv2.THRESH_BINARY)

    # Apply a slight blur to the mask to soften edges
    alpha = cv2.GaussianBlur(alpha, (7, 7), 0)

    # Normalize the alpha mask to keep intensity between 0 and 1
    alpha = alpha.astype(float) / 255

    # Multiply the foreground with the alpha matte
    foreground = cv2.multiply(alpha, foreground)

    # Multiply the background with ( 1 - alpha )
    background = cv2.multiply(1.0 - alpha, background)

    # Add the masked foreground and background
    outImage = cv2.add(foreground, background)

    # Return a normalized output image for display
    return outImage / 255


def segment(net, path, bgimagepath, dev='cuda'):
    img = Image.open(path)

    trf = T.Compose([T.ToTensor(),
                     T.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])])
    inp = trf(img).unsqueeze(0).to(dev)
    out = net.to(dev)(inp)['out']
    om = torch.argmax(out.squeeze(), dim=0).detach().cpu().numpy()

    rgb = decode_segmap(om, path, bgimagepath)
    return rgb


def bgChange(image1, image2):
    dlab = models.segmentation.deeplabv3_resnet101(pretrained=1).eval()
    return segment(dlab, image1, image2)
