# A quick guide to Excel file types.

**Source:** https://www.financialmodellinghandbook.org/a-quick-guide-to-excel-file-types

---

XLS files were phased out about 1,000 years ago and so we're not going to discuss these here. The three main files types you'll need to deal with when saving your model are:

### XLSX

This is the default file structure that replaced the old binary .xls format. This format does not support Excel macros. Underlying this format there is a folder of XML documents. This makes this file structure **extensible.** This means that external applications or programs can manipulate the contents of the underlying XML format, allowing programmers to create software that can edit Excel spreadsheets without ever opening Excel. The XLM file structure are also less susceptible to corruption than binary files.

### XLXM

This is the same file structure as XLSX but with macros enabled.

### XLXB

These are binary file. They open and save faster than XML based file and take up less space. However, they can have difficulties integrating with non-Excel applications such as Bloomberg or Capital IQ. They also have a higher risk of file corruption.

### Experiment.

In this chapter we introduced a macro into the workbook, and we saved the file in XLSB format.

The file was 609 KB in XLSB format.  

If we save the same file in XLSM format the file size becomes 732 KB.

💡

This is an 20% increase in file size moving from XLSB to XLSM

### Recommendation

If you have macros in your file and do not need to integrate with external apps that require an XML file structure - **use XLSB.**

### Excel file type quick summary

|     |     |     |     |
| --- | --- | --- | --- |
| **Excel file type** | **XLSX** | **XLSM** | **XLSB** |
| File format | XML | XML | Binary |
| Can store VBA? | No  | Yes | Yes |
| File size | Larger | Larger | Smaller |
| File opening | Slower | Slower | Faster |
| Risk of file corruption | Lower | Lower | Higher |

[![](https://www.financialmodellinghandbook.org/content/images/2023/09/FinancialModellingHandbookHero--3--164.png)](https://buyfinancialmodellinghandbook.org/?add-to-cart=380&quantity=1&ref=financialmodellinghandbook.org)

* * *

Comments
--------

Sign in or become a Financial Modelling Handbook member to join the conversation.  
Just enter your email below to get a log in link.

 Send a log in link Great! Please check your inbox (or spam folder) for a log in link. Something didn't work. Please try again.

Sorry, comments couldn't be loaded. It looks like this account is not currently active.

### Subscribe to Financial Modelling Handbook

Don’t miss out on the latest financial modelling guides. Sign up now to get access to the library of members-only guides.

[jamie@example.com\
\
Subscribe](https://www.financialmodellinghandbook.org/a-quick-guide-to-excel-file-types#/portal/signup)