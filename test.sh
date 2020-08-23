#!/bin/bash

#SBATCH --nodes=1
#SBATCH --exclude=loopy8
#SBATCH --ntasks=1
#SBATCH --gres=gpu:2080ti:4
#SBATCH --mem=100GB
#SBATCH --time=48:00:00
#SBATCH --array=0
#SBATCH --job-name=test_iif
#SBATCH --output=test_iif_%A_%a.out

module purge
module load cuda-10.1

python -u /misc/vlgscratch4/LakeGroup/emin/indexed-image-folder/test.py '/misc/vlgscratch4/LakeGroup/emin/headcam/preprocessing/S_data_1fps_2000cls_pytorch/'

echo "Done"
