## Alternative `ImageFolder`s 

`IndexedImageFolder` is an alternative version of `ImageFolder` that returns the image index instead of the class index. This is useful in instance-based problems where the images need to have individual indices as opposed to a single class index.

`MultirootImageFolder` is an alternative version of `ImageFolder` that takes in multiple data directories as input (provided as a list).

See [`test_iif.py`]() and [`test_mif.py`]() for usage examples.

Both of these classes are drop-in replacements for `torchvision.datasets.ImageFolder`, hence can be used in the same way. The code in this repo is a simple modification of an [earlier version](https://github.com/pytorch/vision/blob/d6c7900d06c3388bf814cecbe90f91a9afecbefb/torchvision/datasets/folder.py) of `ImageFolder`.
