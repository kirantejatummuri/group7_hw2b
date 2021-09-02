##README for testing workflow

###We use Github actions to automate the testing workflow. 

When there are any `push` or `pull request` events on the `main` branch the job named `build` is triggered.

The job runs on a Github-hosted runner which has the `latest ubuntu` image.

The job comprises of fours steps:

1. Checkout the code repository
```
uses:actions/checkout@v2
```

2. Install python version 
```
actions/setup-python@v1
```

3. Install dependencies

```
Upgrade pip and install the dependencies from requirements.txt file if available.
```

4. Run unit test cases
```
Use PyTest to run the sample unit test defined in test_sample.py
```

### test_sample.py

This file contains a sample test case. It checks if `2 == 2`. Since this is a valid equation, our test always passes.



