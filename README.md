
# Automate Language Learning Taking Notes


Translate any language to a target language using DeepL's translation service. The program reads German phrases from a file, translates them using Selenium automation, and saves the translations along with the original phrases in a Markdown file. You can import this Markdown file into any software to make a better looking table like Notion.
## Installation

Selenium is a powerful tool for web automation testing. You can install it via pip by running:

```bash
  pip install selenium
```

WebDriver is a crucial component of Selenium that allows interaction with web browsers. For this project, we'll use Chrome WebDriver. Install the Chrome WebDriver using:

```bash
  pip install webdriver-manager
```


    
## Usage
Write the phrases you want to translate in a text file, then run the program. You will be asked to enter two inputs `Translate From` and `Translate Into`. Make sure to use for example: `de` for German `ar` for Arabic.
Here is a list of supported languages on DeepL website.
