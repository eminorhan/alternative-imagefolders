import argparse
import torch
import torchvision.transforms as transforms
from multiroot_image_folder import MultirootImageFolder


parser = argparse.ArgumentParser(description='Test multiroot image folder')
parser.add_argument('--data-dirs', nargs='+', help='dataset directories')
parser.add_argument('--workers', default=16, type=int, help='number of data loading workers')
parser.add_argument('--batch-size', default=1024, type=int, help='mini-batch size')
parser.add_argument('--gpu', default=None, type=int, help='GPU id to use.')


if __name__ == '__main__':

    args = parser.parse_args()

    print('List of data directories:', str(args.data_dirs))

    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                     std=[0.229, 0.224, 0.225])

    dataset = MultirootImageFolder(
        args.data_dirs,
        transforms.Compose([transforms.RandomApply([transforms.ColorJitter(0.8, 0.8, 0.8, 0.2)], p=0.8),
                            transforms.RandomGrayscale(p=0.2),
                            transforms.ToTensor(),
                            normalize])
    )

    data_loader = torch.utils.data.DataLoader(
        dataset, batch_size=args.batch_size, shuffle=False,
        num_workers=args.workers, pin_memory=True, sampler=None
    )

    print('Data loader size:', len(data_loader))
    print('Image folder size:', len(data_loader.dataset))

    mif_len = len(data_loader.dataset)

    for i, (images, target) in enumerate(data_loader):

        if args.gpu is not None:
            images = images.cuda(args.gpu, non_blocking=True)
            target = target.cuda(args.gpu, non_blocking=True)

        print('Iter:', i, 'Images shape:', images.shape, 'Targets shape:', target.shape)
        print('Targets:', target)  # targets should be ordered when data_loader.shuffle is False

