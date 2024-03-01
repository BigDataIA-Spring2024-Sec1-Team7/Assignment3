# Assignment 3

## Problem Statement
Design 2 Python classes -
1. URLClass to represent the schema for the Assignment 2(Part 1) CFA webpages (224 pages). Each webpage needs to adhere to guidelines you define as a part of the URLClass
2. Two PDFClasses to represent the schema for the Grobid output.
MetaDataPDFClass : Stores metadata for the three PDF files
ContentPDFClass: Stores the extracted content from each PDF file

Do data and schema validation using these objects using Pydantic 2 and create “clean” csv files.
Build test cases using Pytest for each of the three classes.
Run transformation workflows using DBT to generate a summary table

## Codelab Link


## Project Goals

1. Build data models and field validators for URLClass, ContentClass and MetadataClass using Pydantic
2. Add test cases using pytest to test all validation clauses with pytest
3. Add a xml parser to extract and build content and meta data
4. Write all pydantic object data into respective csv files as clean data
5. Upload data from the clean csv into snowflake databases using sqlalchemy 
6. Run dbt data transformation workflows on these databases to generate summary table

## Data Sources

- 224 Refresher readings listed on the https://www.cfainstitute.org/en/membership/professional-development/refresher-readings#sort=%40refreadingcurriculumyear%20descending
- The topic outlines (3 pdf's)

## Technologies used
Scrapy, Selenium, SQLAlchemy, GROBID, Snowflake, Pydantic, Pytest, etree, dbt

## Architecture Diagram
<img width="1261" alt="image" src="https://github.com/BigDataIA-Spring2024-Sec1-Team7/Assignment3/assets/25281293/846c7dc7-2ea0-4260-9f77-7a04d0b80608">

## Pre-requisites

Before running this project, ensure you have the following prerequisites installed:

- [Python 3](https://www.python.org/downloads/): This project requires Python 3 to be installed. You can download and install Python 3 from the official Python website.

- [Docker](https://www.docker.com/get-started): Docker is used to containerize and manage dependencies for this project. Make sure Docker is installed on your system. You can download and install Docker from the official Docker website.


## How to run application locally

#### Creating Virtual Environment
1. Create a virtual environment using the command `python -m venv <name of virtual env>`. 
2. Install dependencies required to run the project using `pip install -r path/to/requirements.txt`
3. Activate created virtual env by running `source <name of virtual env>/bin/activate`

#### Webscraping
Webscraping uses selenium with scrapy to get the data from website. It opens the base url and fetches the links listed in the readings page using selenium driver and pagination. Multiple spiders are then spawned to open each link and scrape data from them.

##### How to run
1. Selenium chrome driver compatible with your current chrome version can be downloaded from [here](https://chromedriver.chromium.org/downloads). Put the downloaded executable file into `webscraping` folder.
2. Create a virtual environment using the instructions above and activate it
3. Run `cd scripts/webscraping` to switch directory into webscraping folder
4. Run `python -m scrapy crawl cfaspider` to begin scraping data
5. Results are stored in `scripts/webscraping/data` folder as a csv

#### Test Pydantic validation clauses
1. Change directory into `scripts/datavalidation` directory
2. Run `python -m pytest` to check validation clauses

#### Parse and validate data
1. Create virtual environment and activate it
2. Change directory into `scripts/datavalidation` directory
3. Run `python contentparser.py`, `python metadataparser.py` and `python urlclass_cleancsv.py`
4. Clean csv files are created in `scripts/clean_csv` folder

#### Scraped data upload to Snowflake
Scraped data is uploaded to snowflake using sqlalchemy. First the database, warehouse and tables required are created. The csv files are loaded into the table stage on snowflake and then copied into the table.

##### How to run
1. Create virtual environment and activate it
2. Change directory into `scripts/dataupload` directory and create a .env file to add the credentials required to connect with snowflake. The required fields are the following
a. `SNOWFLAKE_USER`, snowflake username
b. `SNOWFLAKE_PASS`, snowflake password
c. `SNOWFLAKE_ACC_ID`, snowflake account id
More details on how to obtain the above parameters can be found [here](https://docs.snowflake.com/en/user-guide/admin-account-identifier). Please refer to [snowflake documentation](https://docs.snowflake.com/en/developer-guide/python-connector/sqlalchemy) for further reference on setup.
3. Run the code using the command `python snowflake_upload_dev.py` or `python snowflake_upload_prod.py`. The data is uploaded from `scripts/webscraping/data/cfascraping_data.csv`.

#### Docker

GROBID is very easy to install and deploy in a Docker container. GROBID is a machine learning library for extracting, parsing and re-structuring raw documents such as PDF into structured XML/TEI encoded documents with a particular focus on technical and scientific publications

##### How to run
1. Pull the image from docker HUB

```sh
docker pull grobid/grobid:0.8.0
```

2. This will create the grobid image and pull in the necessary dependencies.
Here, we are using 0.8.0 version of Grobid.

3. Once done, run the Docker image and map the port to whatever you wish on
your host. We simply map port 8070 of the host to
port 8070 of the Docker :

```sh
docker run --rm --init --ulimit core=0 -p 8070:8070 lfoppiano/grobid:0.8.0
```

4. Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8070
```

## References

[PyPdf](https://pypdf2.readthedocs.io/en/3.0.0/): PyPDF2 is a free and open source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. PyPDF2 can retrieve text and metadata from PDFs as well.

[Grobid](https://grobid.readthedocs.io/en/latest/Run-Grobid/): GROBID is a machine learning library for extracting, parsing and re-structuring raw documents such as PDF into structured XML/TEI encoded documents with a particular focus on technical and scientific publications.

## Learning Outcomes
- Data structuring: Organizing extracted data into a CSV file with specific schema.
- Python programming: Developing Python notebooks to automate processes.
- Pydantic: Building models and writing validation using pydantic
- Pytest: Writing test cases to validate pydantic models
- Snowflake integration: Uploading data to a Snowflake database using SQLAlchemy
- dbt - Building transformations on uploaded data

