# Excel DETECTLANGUAGE function | Exceljet

**Source:** https://exceljet.net/functions/detectlanguage-function

---

[Skip to main content](https://exceljet.net/functions/detectlanguage-function#main-content)

[](https://exceljet.net/functions/detectlanguage-function#)

*   [Previous](https://exceljet.net/functions/chooserows-function)
    
*   [Next](https://exceljet.net/functions/drop-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

DETECTLANGUAGE Function
=======================

by Dave Bruns · Updated 18 Jun 2025

Related functions 
------------------

[TRANSLATE](https://exceljet.net/functions/translate-function)

![Excel DETECTLANGUAGE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_detectlanguage_function.png "Excel DETECTLANGUAGE function")

Summary
-------

The Excel DETECTLANGUAGE function detects the language of a given text string. The result is a language code. For example, if the language is English, the result is "en"; if the language is French, the result is "fr"; if the language is German, the result is "de", and so on. 

> DETECTLANGUAGE is only available in Excel 365 and requires an internet connection.

Purpose 
--------

Detect the language of a given text string

Return value 
-------------

A language code

Syntax
------

    =DETECTLANGUAGE(text)

*   _text_ - A sample of the language as a text string.

Using the DETECTLANGUAGE function 
----------------------------------

The DETECTLANGUAGE figures the language for a given text string. The result from DETECTLANGUAGE is a short language code indicating the language. For example, if the language is English, the result is "en"; if the language is French, the result is "fr"; if the language is Japanese, the result is "ja", and so on. Some of these codes are intuitive, but some aren't. See below for a list of common language codes. DETECTLANGUAGE only accepts one argument, text, so the syntax is very simple and looks like this:

    =DETECTLANGUAGE(text)

Typically, the _text_ is supplied as a cell reference like A1, but it can also be hardcoded as a string like "apple". 

> The DETECTLANGUAGE function uses Microsoft Translation Services, so it requires an internet connection.

### Basic Example

To use the DETECTLANGUAGE function, simply provide some text. For example, if we give DETECTLANGUAGE the word "apple", it "detects" English and returns "en":

    =DETECTLANGUAGE("apple")  //  returns "en"

Likewise, if we give DETECTLANGUAGE the word for "apple" in four languages (French, Italian, German, and Spanish), it returns the four corresponding language codes: "fr," "it," "de," and "es."

    =DETECTLANGUAGE("pomme")  //  returns "fr"
    =DETECTLANGUAGE("mela")  //  returns "it"
    =DETECTLANGUAGE("Apfel")  //  returns "de"
    =DETECTLANGUAGE("manzana")  //  returns "es"

> Note that DETECTLANGUAGE always returns a language code like "en", "it", "de", "es", etc. The TRANSLATE function supports over 100 languages, so there are _many_ potential codes. See below for a list of common languages and codes. 

### Example: Get language codes

In the worksheet below, we have text for "Is there a coffee shop around here?" in 12 languages. The goal is to determine the language codes based on the text in column B. The formula in D8, copied down, looks like this:

    =DETECTLANGUAGE(B5)

As the formula is copied down the column, DETECTLANGUAGE returns a language code for each text string, as seen in column D below:

![DETECTLANGUAGE example: Get language codes](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/detectlanguage_example_get_language_codes.png "DETECTLANGUAGE example: Get language codes")

Note that the DETECTLANGUAGE function is dynamic. If any of the text in column B is changed to a different language, TRANSLATE will return a new language code. 

### Example: Get language names

Getting language codes automatically is great, but you probably want to know how to get an actual language name. To do that, you will want to set up a lookup table in your worksheet with columns for the language code and the language name. In the worksheet below, we have defined an [Excel Table](https://exceljet.net/articles/excel-tables)
 called "languages" like this:

![A language lookup table for DETECTLANGUAGE](https://exceljet.net/sites/default/files/images/functions/inline/detectlanguage_language_lookup_table.png "A language lookup table for DETECTLANGUAGE")

Then we can use the [XLOOKUP function](https://exceljet.net/functions/xlookup-function)
 to get the correct language for a given code, as seen in column E of the worksheet below. The formula in cell E5 looks like this:

    =XLOOKUP(D5,languages[Code],languages[Language])

The inputs to XLOOKUP are as follows:

*   lookup\_value - D5
*   lookup\_array - languages\[Code\]
*   return\_array - languages\[Language\]

![Using XLOOKUP to get the language name using the code](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/detectlanguage_example_get_language_name_from_code.png "Using XLOOKUP to get the language name using the code")

If you want to look up the language name from the code in one step, you can combine the formulas above into one formula like this:

    =XLOOKUP(DETECTLANGUAGE(B5),languages[Code],languages[Language])

In this formula, DETECTLANGUAGE returns a language code to XLOOKUP as the lookup value, and XLOOKUP uses the code to get the language name in a single step.

> Excel Tables make it possible to use "structured references" in formulas, like languages\[Code\] and languages\[Language\]. One advantage to structured references is that we don't need to lock any references in a formula like this. To learn more see our [Excel Table guide](https://exceljet.net/articles/excel-tables)
> .

### Codes for common languages

The below shows language codes for some common languages that can be used with the TRANSLATE function. Note that some languages, like Portuguese, have more than one variant. For example, the code "pt" specifies Portuguese for Brazil, while "pt-pt" specifies Portuguese for Portugal.

| Language | Code | Notes |
| --- | --- | --- |
| Arabic | ar  |     |
| Chinese | zh-Hans | Simplified |
| Czech | cs  |     |
| Danish | da  |     |
| Dutch | nl  |     |
| English | en  |     |
| Finnish | fi  |     |
| French | fr  |     |
| German | de  |     |
| Hindi | hi  |     |
| Indonesian | id  |     |
| Italian | it  |     |
| Japanese | ja  |     |
| Korean | ko  |     |
| Norwegian | nb  | Bokmål |
| Polish | pl  |     |
| Portuguese | pt  | Brazilian |
| Spanish | es  |     |
| Swedish | sv  |     |
| Thai | th  |     |
| Vietnamese | vi  |     |

> The DETECTLANGUAGE function supports over 130 languages. You can find the full list of supported languages [here](https://learn.microsoft.com/en-us/azure/ai-services/Translator/language-support)
> .   

### Notes

*   DETECTLANGUAGE always returns a language code as text.
*   If the _text_ is an empty string (""), DETECTLANGUAGE also returns an empty string.
*   If the internet is not available, you may see a #CONNECT! error.
*   Use the [TRANSLATE function](https://exceljet.net/functions/translate-function)
     to translate text to another language.

Related functions
-----------------

[![Excel TRANSLATE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_translate_function.png "Excel TRANSLATE function")](https://exceljet.net/functions/translate-function)

### [TRANSLATE Function](https://exceljet.net/functions/translate-function)

The Excel TRANSLATE function is designed to translate text from one language to another in Excel. The source and target languages are provided as special codes. For example, "en" for English, "fr" for French, "it" for Italian, and so on. 

> ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [TRANSLATE Function](https://exceljet.net/functions/translate-function)
    

### Links

*   [Microsoft DETECTLANGUAGE function documentation](https://support.microsoft.com/en-us/office/detectlanguage-function-0748e285-1912-4d24-b735-57d18142fa3b)
    

Thank you for your very clear explanation on how to test for an existing tab name in a workbook using ISREF and INDIRECT. With your guidance, I am able to build a flexible template that can use variables to test...I really like your site layout and your concise directions. Thank you again!

Thierry

[More Testimonials](https://exceljet.net/feedback)

Get [Training](https://exceljet.net/training)

----------------------------------------------

### Quick, clean, and to the point training

Learn Excel with high quality video training. Our videos are quick, clean, and to the point, so you can learn Excel in less time, and easily review key topics when needed. Each video comes with its own practice worksheet.

[View Paid Training & Bundles](https://exceljet.net/training)

[![Excel foundational video course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_excel.png "Excel foundational video course")](https://exceljet.net/training)

[![Excel Pivot Table video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_pivot.png "Excel Pivot Table video training course")](https://exceljet.net/training)

[![Excel formulas and functions video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_formula_0.png "Excel formulas and functions video training course")](https://exceljet.net/training)

[![Excel Charts video training course](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_core_charts.png "Excel Charts video training course")](https://exceljet.net/training)

[![Video training for Excel Tables](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_excel_tables.png "Video training for Excel Tables")](https://exceljet.net/training)

[![Dynamic Array Formulas](https://exceljet.net/sites/default/files/styles/product_image/public/images/course/cover_dynamic_array_formulas_0.png "Dynamic Array Formulas")](https://exceljet.net/training)