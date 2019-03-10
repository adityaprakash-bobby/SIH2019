# Dashboard for MSMEs

It is a project made on the fulfillment of Smart India Hackathon 2019. It helps the small companies under MSME to analyse and get a look over how their products are performing in the market. As well as it helps predict the future demands of the products.

## Setup:
```bash
# clone the repo and jump into the folder
git clone https://github.com/adityaprakash-bobby/SIH2019
cd SIH2019/

# setup the virtual environment
virtualenv -p python3 venv
source venv/bin/activate

# intall the dependencies
pip install -r requirements.txt
```

#### Setup to use plotly:

Create an account in Plotly. Get the access tokens and username.

Change the following lines in the files dashboard/analysis.py and dashboard/prediction.py

> plotly.tools.set_credentials_file(username='your-plotly-username-here', api_key='your-plotly-api-key-here')

### Access the application

```bash
# run the server
python manage.py runserver
```

Now navigate to https://localhost:8000/
