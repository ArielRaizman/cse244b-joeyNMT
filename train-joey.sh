#!/bin/bash
#SBATCH --job-name=joeynmt_train
#SBATCH --output=joey_%j.log
#SBATCH --error=joey_%j.err
#SBATCH --partition=96x24gpu4
#SBATCH --gres=gpu:1            # Request 1 GPU
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4       # Good for data loading
#SBATCH --mem=16G               # Adjust based on your dataset size
#SBATCH --time=10:00:00         # Max time limit

# Load necessary modules

module load cuda/12.8.1


# python3 -m venv joey_env
# pip install joeynmt

# Activate environment
source /home/araizman/cse244b-joeyNMT/joey_env/bin/activate

# Run JoeyNMT training
# Replace 'configs/transformer_toy.yaml' with your actual config file
python -m joeynmt train config.yaml