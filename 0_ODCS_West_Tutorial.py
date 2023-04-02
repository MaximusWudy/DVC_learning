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

    """
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"

        to set your account's default identity.
        Omit --global to set the identity only in this repository.
    """
    
#### DVS is helpful in tracking changes in your data, to facilitate cross-platform collaboration
dvc import https://github.com/iterative/dataset-registry dvc-course/hymenoptera_data

#### Run an experiment!!
dvc exp show # show experiment table
dvc exp run # run the experiment using commands and configs in the dvc.yaml file