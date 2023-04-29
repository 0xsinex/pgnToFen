#!/bin/bash
#SBATCH -J extract_keres
#SBATCH --partition=main
#SBATCH --time=02:00:00
#SBATCH --cpus-per-task=1
#SBATCH --mem=64gb

# your code goes below
module load python
srun python ./convert.py



