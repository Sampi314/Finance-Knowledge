# TRANSLATE Function in Excel

**Source:** https://trumpexcel.com/excel-functions/translate

---

[Skip to content](https://trumpexcel.com/excel-functions/translate/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/translate/#below-title)

Have you ever needed to translate text from one language to another while working in Excel?

Maybe you’re creating reports for international clients or generating invoices in multiple languages.

Good news – Microsoft Excel now has a built-in TRANSLATE function that can help you do this quickly and easily.

Excel is typically used for [data analysis](https://trumpexcel.com/two-variable-data-table-in-excel/)
 and number crunching, so translation might seem like an odd feature to include. But it’s actually quite handy when you need quick translations without leaving your spreadsheet.

TRANSLATE is a new [Excel function](https://trumpexcel.com/excel-functions/)
, so you’ll need Excel with Microsoft 365 or Excel on the web to use it. If you’re using older versions, this function won’t be available.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/translate/#)

Syntax of TRANSLATE Function in Excel
-------------------------------------

The TRANSLATE function is straightforward and uses three arguments:

    =TRANSLATE(text, [source_language], [target_language])

Here’s what each part means:

*   **Text**: The text you want to translate. You can use a [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     or type text directly in quotes.
*   **Source Language** (optional): The original language of your text. While Excel can usually detect this automatically, I recommend specifying it for better accuracy.
*   **Target Language** (optional): The language you want to translate into. If you do not specify this argument, you would get the same text you used as the first argument.

All language codes must be two-letter codes in double quotes. For example, “en” for English, “es” for Spanish, or “fr” for French. [Here is the official documentation](https://learn.microsoft.com/en-us/azure/ai-services/Translator/language-support)
 from Microsoft that lists all the supported languages.

_Note that Google Sheets also has a similar function called GOOGLETRANSLATE that has the same syntax._

Now let’s look at some examples of using the Translate function in Excel.

Example 1: English to Spanish Translation in Excel
--------------------------------------------------

Let’s say you have English text in cell A1 that you want to translate to Spanish.

![Dataset to use translate function in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201325%20707'%3E%3C/svg%3E)

Your formula would look like this:

    =TRANSLATE(A2, "en", "es")

![Translate function in Excel for English to Spanish](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201388%20833'%3E%3C/svg%3E)

When you press Enter, Excel instantly translates your text into Spanish.

You can then copy this formula down to translate multiple cells at once.

Even though I don’t speak Spanish fluently, I checked with my Spanish-speaking friends, and they said the translation was as good as it gets.

Example 2: Automatically Detect Language and then Translate in Excel
--------------------------------------------------------------------

Let’s say you’re working with a dataset that has multiple different languages (e.g., English, Spanish, Portuguese, and Dutch) and you want to translate all of them with one formula to English.

This can be done using the new DETECTLANGUAGE function along with the TRANSLATE functoin.

Below I have a dataset where I have text in different languages in column A, and I want to translate everything into English and get the result in column B.

![Text in different languages that need to be translated into English](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201582%20824'%3E%3C/svg%3E)

Below is the formula that will do this.

    =TRANSLATE(A2,DETECTLANGUAGE(A2),"en")

![Translate function to first detect the language and then translate it into English.](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201620%20942'%3E%3C/svg%3E)

In the above formula, I have used the DETECTLANGUAGE function as the second argument that automatically detects the language and returns the two-letter code for that language. And since the third argument is “en”, whatever language is detected is converted into English.

**Important note**: While the translations are generally accurate, don’t rely on them completely for critical documents. Always review the results to ensure accuracy and proper context.

Limitations of the Excel TRANSLATE Function
-------------------------------------------

Before you start using TRANSLATE extensively, there are some important things to know.

### Internet Connection Required

The TRANSLATE function needs an active internet connection to work. The translation happens online, so you can’t use this feature offline.

### 3,000 Character Limit

Through testing, I discovered there’s a 3,000 character limit per translation. If your text is longer than this, you’ll get a #VALUE! error.

I tested this with dummy text and confirmed that anything under 3,000 characters works fine. But add even a few more characters, and the function fails (I have shown the test in the video above).

### Common Error Scenarios

You might encounter errors in these situations:

*   **Non-text values**: The function only works with text. Numbers or other data types will cause errors.
*   **Invalid language codes**: Using incorrect two-letter language codes will result in errors.
*   **Request throttling**: Microsoft doesn’t specify the exact limits, but there’s likely a daily quota on translations. You can’t run unlimited translations.

When to Use Excel’s TRANSLATE Function
--------------------------------------

Excel’s TRANSLATE function is perfect for quick translations within your existing workflows. It’s great for:

*   Translating column headers for international reports
*   Creating multilingual [invoices](https://trumpexcel.com/invoice-generator-pdf/)
     or forms
*   Quick translation checks while analyzing data

However, **Excel isn’t a dedicated translation tool**. For long documents or professional translations, you’re better off using specialized translation software.

I hope you found this Excel tutorial helpful. If you have any questions or suggestions, do let me know in the comments area.

**Other Excel articles you may also like:**

*   [Excel Skills (Basic, Intermediate, and Advanced)](https://trumpexcel.com/excel-skills/)
    
*   [Excel TEXT Function](https://trumpexcel.com/excel-text-function/)
    
*   [20 Advanced Excel Functions and Formulas](https://trumpexcel.com/advanced-excel-functions-formulas/)
    
*   [Find and Remove Duplicates in Excel](https://trumpexcel.com/find-and-remove-duplicates-in-excel/)
    
*   [Excel Custom Number Formatting Tricks](https://trumpexcel.com/excel-custom-number-formatting/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK