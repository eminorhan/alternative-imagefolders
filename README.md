## Indexed ImageFolder 

An alternative `ImageFolder` that returns the image index instead of the class index. This could be useful in problems where the images in a given class need to have individual indices as opposed to a single class index. `IndexedImageFolder` can be used in the same way as `torchvision.datasets.ImageFolder`. This repo is a simple modification of an [earlier version](https://github.com/pytorch/vision/blob/d6c7900d06c3388bf814cecbe90f91a9afecbefb/torchvision/datasets/folder.py) of `ImageFolder`.
