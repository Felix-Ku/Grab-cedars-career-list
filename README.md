# Project Title

Application name: Cedars career grabber(Temp.)
Current version: 1.0

To extract daily career list from HKU Cedars 
Target link: http://www.cedars.hku.hk/careers/latest-announcement

## Inspiration

Although the HKU Cedars latest announcement list website is already well-designed and user-friendly, I found it quite troublesome to browse the website every day and download each and every interested documents (mainly PDF) manually.

Therefore, I would like to see if this application can help download the documents and extract information automatically. In the future versions, hopefully functions like remembering seen career information and generating automatic reminders for the registrations deadline can be added.

To make the application more useful, more functions need to be added.

First try of web scraping with python.

### Getting Started - Prerequisites

- Modules
- Administrative rights

### Installing

Change
```
url="http://www.cedars.hku.hk/careers/latest-announcement" 
```
to the latest link of HKU Cedars latest announcement (If there's any update of the url)

```
url="[TARGET_URL]" 
```

And change the output location of the CSV file to drive other than C:\ (If you havn't granted python the enough rights to write in C:\)

```
df.to_csv('d:\output.csv',encoding='utf_8_sig')
```
to
```
df.to_csv('[TARGET_LOCATION]',encoding='utf_8_sig')
```

## Testing

1. Start the application
2. HTTP request code received and confirm successful connection (200) (404=failed)
3. Check the CSV file generated

## Deployment

[Additional notes about how to deploy this on a live system]

## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - The web framework used
* [Panda](https://pandas.pydata.org/) - The dataframe and CSV output function
* [Requests](http://docs.python-requests.org/en/master/) - For http requests 

## Authors

* **Felix Ku** - *Initial work* - [Felix-Ku](https://felix-ku.github.io/Index/)

## Acknowledgments

* Do not input your HKU id inside 

## To-Do
(Functions to be added in future versions)

- Select the range of dates to be exported (Date compare)
- Download documents (Requires login of HKU accounts*) 
- Remember seen career (Check the current csv file to prevent importing information of previous carrer)
- Filtering company names or fields (Filtering the names and check automatically on search engines)
- Marking down the requirements of different companies for career references.

- Further simplify the codes

- Detailed future version:
  1. Input the range of dates to be selected
  2. Show options (To download all pdf goto 4. / To choose manully goto 3.)
  3. Show brief information of every latest career one by one and show options to choose whether to store or not
  ```
  Career/event name:
  Company/organiser name:
  Related field:
  Updated date:
  Registeration deadline:
  Brief description:
  
  Interested? (Yes/No)
  [User input]
  
  ``` 
  4. Generate CSV report and grab the pdf files
  5. Showing a brief report of the fields and companies extracted
  

