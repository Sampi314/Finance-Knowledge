# Excel TRANSLATE function | Exceljet

**Source:** https://exceljet.net/functions/translate-function

---

[Skip to main content](https://exceljet.net/functions/translate-function#main-content)

[](https://exceljet.net/functions/translate-function#)

*   [Previous](https://exceljet.net/functions/torow-function)
    
*   [Next](https://exceljet.net/functions/trimrange-function)
    

Excel 365

[Dynamic array](https://exceljet.net/functions#Dynamic-array)

TRANSLATE Function
==================

by Dave Bruns · Updated 24 Jan 2025

Related functions 
------------------

[DETECTLANGUAGE](https://exceljet.net/functions/detectlanguage-function)

 ![File](https://exceljet.net/core/modules/file/icons/x-office-spreadsheet.png "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet") [Download Worksheet](https://exceljet.net/file/8941/download?token=lpV3nig-)
 (26.77 KB)

![Excel TRANSLATE function](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/main/exceljet_translate_function.png "Excel TRANSLATE function")

Summary
-------

The Excel TRANSLATE function is designed to translate text from one language to another in Excel. The source and target languages are provided as special codes. For example, "en" for English, "fr" for French, "it" for Italian, and so on. 

> TRANSLATE is only available in Excel 365 and requires an internet connection.

Purpose 
--------

Translate text from one language to another

Return value 
-------------

Translated text

Syntax
------

    =TRANSLATE(text,[source_language],[target_language])

*   _text_ - The text to translate as a string or cell reference.
*   _source\_language_ - \[optional\] The source language code. Default = auto-detected..
*   _target\_language_ - \[optional\] The target language code. Default = system.

Using the TRANSLATE function 
-----------------------------

The TRANSLATE function translates text from one language to another in Excel. To perform a translation, TRANSLATE requires the text to translate and language codes to indicate the source and target language. The syntax for TRANSLATE looks like this:

    =TRANSLATE(text,[source_language],[target_language])

Typically, the _text_ is supplied as a cell reference like A1, but it can also be hardcoded as a string like "apple". While TRANSLATE takes three arguments, only the first argument is required. The other two arguments have the following default behaviors:

*   _source\_language_ - if not provided, the source language will be detected automatically by inspecting the _text_. Essentially, this is the same result you see with the DETECTLANGUAGE function, but you will not see what language TRANSLATE has selected. It is recommended to specify the source language when possible.
*   target _\_language_ - if not provided, the target language will default to the system setting of the user's computer. This might be convenient in some cases, but remember that you will not know this setting if you share a file with others.

> The TRANSLATE function uses Microsoft Translation Services and requires an internet connection.

### Table of Contents

*   [Basic Example](https://exceljet.net/functions/translate-function#basic-example)
    
*   [Example: Translate text into several languages](https://exceljet.net/functions/translate-function#example-translate-text)
    
*   [Example: Translate instructions dynamically](https://exceljet.net/functions/translate-function#example-dynamic-translation)
    
*   [Codes for common languages](https://exceljet.net/functions/translate-function#codes-common-languages)
    
*   [Notes](https://exceljet.net/functions/translate-function#notes)
    

### Basic Example

To use the TRANSLATE function, provide the text to translate, the source language language as a language code, and the desired target language as a language code. For example, to translate the word "apple" into French ("fr"), Italian ("it"), German ("de"), and Spanish ("es"), you can use the TRANSLATE function like this:

    =TRANSLATE("apple","en","fr")  //  returns "pomme"
    =TRANSLATE("apple","en","it")  //  returns "mela"
    =TRANSLATE("apple","en","de")  //  returns "Apfel"
    =TRANSLATE("apple","en","es")  //  returns "manzana"

> Note the source and target languages are specified with codes: English is "en", Italian is "it", German is "de", and Spanish is "es". The TRANSLATE function supports over 100 languages. See [below](https://exceljet.net/functions/translate-function#codes-common-languages)
>  for a list of codes for some common languages. 

### Example: Translate text into several languages

In this example, the goal is to translate the text entered in cell C5 into the 9 languages in the table below, using the codes in the range B8:B16 to determine the target languages. The formula in cell C8, copied down, looks like this:

    =TRANSLATE($C$5,$B$5,B8)

For this problem, the TRANSLATE function is configured as follows:

*   _text_ - provided as $C$5, locked to prevent changes when copying
*   _source\_language_ - provided as $B$5, locked to prevent changes when copying
*   _target\_language_ - provided as B8, relative to allow the reference to update when copying

As the formula is copied down column B, TRANSLATE returns a translation for the text in cell C5 using the language codes in column B to determine a target language.

![Excel TRANSLATE function worksheet example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/exceljet_translate_function_worksheet_example.png "Excel TRANSLATE function worksheet example")

Note that the TRANSLATE function is dynamic. If the text in cell B5 is changed, TRANSLATE will generate new translations. When a target language code in the range B8:B16 is changed, TRANSLATE will return a translation for the new target language.

### Example: Translate instructions dynamically

In this example, the goal is to translate instructions dynamically based on the language selected in a dropdown list, as shown in the workbook below. Here, the instructions are located in the range B4:B11, and the translation appears in E4:F11. The dropdown list appears in cell F2. The formula in cell E4 looks like this:

    =TRANSLATE(B4,"en",target)

Where "target" is a named range on another sheet, as explained below. Note that we are translating the table headers in addition to the instructions, so we start with cell B4. As the formula is copied down and across the table, it returns a translation for each cell using the language in cell F2 as the "target" language:

![TRANSLATE function example - dynamically translate instructions](https://exceljet.net/sites/default/files/images/functions/inline/translate_function_example_translate_instructions_dynamically.png "TRANSLATE function example - dynamically translate instructions")

Although we now have a target language in F2, the TRANSLATE function requires a language code. To convert the language name into the correct code, we have set up an [Excel Table](https://exceljet.net/articles/excel-tables)
 on a separate worksheet, as shown below. The table is named "languages" and performs two important functions:

1.  The first column in the table supplies values to the dropdown menu in cell F2 with [Data Validation](https://exceljet.net/articles/excel-data-validation-guide)
    .
2.  The XLOOKUP formula in F2 uses the table to find the correct language code for the selected language.

The dropdown menu is created using a Data Validation list that points to the first column of the "languages" table in the range B5:B24 on Sheet3. For mysterious reasons, Excel will not display the table name in this case, _but it will update the Source range_ if the table changes:

![The language dropdown menu is created with a Data Validation list](https://exceljet.net/sites/default/files/images/functions/inline/translate_function_language_dropdown_menu_with_data_validation.png "The language dropdown menu is created with a Data Validation list")

Below is the XLOOKUP formula in F5:

    =XLOOKUP(D5,languages[Language],languages[Code])

The inputs to XLOOKUP are as follows:

*   _lookup\_value_ - the named range "lang" (=Sheet2!F2)
*   _lookup\_array_ - languages\[Language\]
*   _return\_array_ - languages\[Code\]

![TRANSLATE function -  language code lookup example](https://exceljet.net/sites/default/files/styles/original_with_watermark/public/images/functions/inline/translate_function_language_code_lookup_example.png "TRANSLATE function -  language code lookup example")

Note that F5 is the named range "target", which provides a value for _target\_language_ in the TRANSLATE function. To recap, here is how this example works:

*   There are two named ranges: "lang" is cell F2 on Sheet2, which holds the result of the dropdown selection, and "target" is cell F5 on Sheet3 which holds the language code returned by XLOOKUP.
*   The Excel Table named "languages" is on Sheet3. This table contains the languages available to select in the dropdown in the first column (Language) and the corresponding language code in the second column (Code).
*   When a user selects a language from the dropdown menu, the value for "lang" (F2) is set, and the XLOOKUP formula in F5 returns the corresponding language code, which sets the value for "target."
*   The TRANSLATE formulas in the main worksheet use the target language code to perform a translation.
*   When the user selects a different language, the process repeats, and a new translation is automatically retrieved. 

> Excel Tables have a nice feature that we use in this example: If you add more languages to the table, the dropdown menu will automatically update. For more information about tables, see our [Excel Table guide](https://exceljet.net/articles/excel-tables)
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

> The TRANSLATE function supports over 130 languages. You can find the full list of supported languages [here](https://learn.microsoft.com/en-us/azure/ai-services/Translator/language-support)
> .   

### Notes

*   TRANSLATE always returns text, even if the _text_ is numeric.
*   If the _text_ is an empty string (""), TRANSLATE returns an empty string.
*   If a language code is not valid, TRANSLATE returns a #VALUE! error.
*   If the internet is not available, you may see a #CONNECT! error.

Related functions
-----------------

[![Excel DETECTLANGUAGE function](https://exceljet.net/sites/default/files/styles/card/public/images/functions/main/exceljet_detectlanguage_function.png "Excel DETECTLANGUAGE function")](https://exceljet.net/functions/detectlanguage-function)

### [DETECTLANGUAGE Function](https://exceljet.net/functions/detectlanguage-function)

The Excel DETECTLANGUAGE function detects the language of a given text string. The result is a language code. For example, if the language is English, the result is "en"; if the language is French, the result is "fr"; if the language is German, the result is "de", and so on. ...

Was this page helpful? Yes No Report a problem

Cancel Submit

![Dave Bruns Profile Picture](https://exceljet.net/sites/default/files/images/blocks/dave-round.webp)

Author![Microsoft Most Valuable Professional Award](https://exceljet.net/sites/default/files/images/blocks/microsoft-mvp-logo.webp)

### Dave Bruns

Hi - I'm Dave Bruns, and I run Exceljet with my wife, Lisa. Our goal is to help you work faster in Excel. We create short videos, and clear examples of formulas, functions, pivot tables, conditional formatting, and charts.

Related Information
-------------------

### Functions

*   [DETECTLANGUAGE Function](https://exceljet.net/functions/detectlanguage-function)
    

### Links

*   [Microsoft TRANSLATE function documentation](https://support.microsoft.com/en-us/office/translate-function-d34f71c7-2ffe-409a-9a63-5eb5e91aa3dd)
    

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