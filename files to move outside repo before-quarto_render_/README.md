# MUSA_5500_Final

**Using Yelp and Zillow Data to find Commercial Corridors in Philadelphia**

### Current Status

*   This repository currently has a `data` folder that houses webscraped data scraped from Zillow and will hopefully house the yelp and final cleaned datasets

*   The Jupyter notebooks or .ipynb files currently reference these directories to write and read files
    -   these are located in `modified-webscraping`
    -   Zillow outputs (though empty) are currently in `webscraping-outputs-Z`

* Once working without issue, making the data retrieval a python script that adds to existing csvs would be nice 


#### Problems

*   Providence Adu (original code in `providence_adu_Code`) used a specific tag that had listing information and the description, but that is not currently working
    -   page 1 runs but returns None & later pages give a NoneType AttributeError
