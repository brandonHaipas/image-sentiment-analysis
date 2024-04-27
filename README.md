# image-sentiment-analysis

In this project the idea of using color to identify emotions is explored. Firstly models for binary classification (positive or negative emotion) and secondly models for multiclass classification. 

First, create an environment with anaconda or venv. For using ``venv``, install it first with pip:
```
pip install virtualenv
```

Then create an environment:
```
python -m venv name-of-environment
```

Lastly, activate it:

```
.\name-of-environment\Scripts\activate
```

With the environment activated, now install the dependencies:
- For venv:
```
pip install -r requirements.txt
```
- For conda:
```
conda install --file requirements.txt
```
Now that the requirements have successfully been installed, download the dataset [Image Sentiment Polarity](https://data.world/crowdflower/image-sentiment-polarity), save it in the root folder for this project and run this command:
```
python get-data.py
```
After a couple of hours all the images will be saved in the ``images`` folder, and the file ``color-dataset.csv`` should've been created.

After that, explore the notebook inside this project as you see fit.