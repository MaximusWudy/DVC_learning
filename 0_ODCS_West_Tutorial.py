conda activate iterative_ai

#### This tutorial will be focusing on the model experiment part of a data science project. 
#### This will not include any part in the development or staging of the model.
## DVC = data version control
    """
    Args:
    - name of the action
    - multiple dependencies
    - params to track
    - outputs to track
    -- results stored in a JSON file
    Py command you will need to execute
    """
dvc stage add --name training --deps hymenoptera_data/ --deps pretrained_model_tuner.py --params lr,momentum,model_name,num_classes,batch_size,num_epochs --outs model.pt --metrics-no-cache results.json python pretrained_model_tuner.py

    """Example Results
    Adding stage 'training' in 'dvc.yaml'                                 

To track the changes with git, run:

        git add dvc.yaml .dvc/.gitignore

To enable auto staging, run:

        dvc config core.autostage true
    """
    
#### Then we update using Git
git remote add origin https://github.com/MaximusWudy/DVC_learning.git
git remote set-url origin https://github.com/MaximusWudy/DVC_learning.git

git add . # staged changes
git status # check status
git commit -m "added dvc.yaml"

 git push -u origin main
 
 # run all together 
 # git add .; git commit -m "ran an exp"; git push

    """
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"

        to set your account's default identity.
        Omit --global to set the identity only in this repository.
    """
    
#### DVS is helpful in tracking changes in your data, to facilitate cross-platform collaboration
dvc import https://github.com/iterative/dataset-registry dvc-course/hymenoptera_data

#### Run an experiment!!
dvc exp run # run the experiment using commands and configs in the dvc.yaml file
dvc exp run --set-param lr=0.01

dvc exp show # show experiment table

    """
    ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────>
  Experiment                 Created        acc      loss   training_time   lr      momentum   model_name   num_classes   batch_size  >
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────>
  workspace                  -          0.87295   0.29441          2.2393   0.005   0.01       alexnet      2             10          >
  main                       03:17 PM   0.84426   0.34882          2.1446   0.001   0.01       alexnet      2             10          >
  ├── a8b3a72 [after-zigs]   03:21 PM   0.87295   0.29441          2.2393   0.005   0.01       alexnet      2             10          >
  └── 07f90c3 [undue-plug]   03:20 PM   0.84426   0.34882          2.1446   0.001   0.01       alexnet      2             10          >
 ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────>

    """
    
#### Pairwise exp comparison
dvc plots diff hilly-hoot undue-plug

#### Grid Search in Queue
python 0_grid_search.py # not run yet
dvc exp run --run-all --jobs 2 # now we run it, 2 jobs at the same time

    """
    Ran experiment(s): 
    To apply the results of an experiment to your workspace run:
        dvc exp apply <exp>

    To promote an experiment to a Git branch run:
        dvc exp branch <exp> <branch>
    """
    
#### Once we find the best model, we apply the best model
# it goes through the DVC tracking and this is the one you want to apply to all meta files (and upload to repo)
dvc exp apply hilly-hoot
# apply the changes to github repo
git add .; git commit -m "best exp so far"; git push

#### BONUS Section
# Use CML to automate 