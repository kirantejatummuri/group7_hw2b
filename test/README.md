##README for testing workflow

We use `Github actions` and `Travis` to automate the testing workflow. 

###Automation through Github Actions
When there are any `push` or `pull request` events on the `main` branch the job named `build` is triggered. The job runs on a Github-hosted runner which has the `latest ubuntu` image.

The job comprises of fours steps:

```
1. Checkout the code repository
2. Install python version
3. Upgrade pip and install the dependencies from requirements.txt file if available
4. Use PyTest to run the sample unit test defined in test_sample.py
```

###Automation through Travis
On a new commit, the travis job is triggered.
It uses the latest ubuntu version.

The following steps are run through the job:
```
1. Upgrade pip
2. Install pytest
3. Runs the sample test case - test_sample.py
```

### test_sample.py

This file contains sample test cases. 
Functions preceeding with `test_` are run by pytest.
We have two sample functions, `test_addition` and `test_substraction` which perform simple arithmetic operations of addition and subtraction.




