import itertools
import subprocess

# Automated grid search experiments
lr_values = [0.5, 0.05, 0.025, 0.003]
momentum_values = [0.3, 0.1, 0.05, 0.03]

# Iterate over all combinations of hyperparameter values
for lr, momentum in itertools.product(lr_values, momentum_values):
    # Exe "dvc exp run --queue --set-param lr=<lr> --set-param momentum=<momentum>"
    subprocess.run(["dvc", "exp", "run", "--queue", 
                    "--set-param", f"lr={lr}",
                    "--set-param", f"momentum={momentum}"])