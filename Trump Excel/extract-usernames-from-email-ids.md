# Extract Usernames from Email Ids in Excel

**Source:** https://trumpexcel.com/extract-usernames-from-email-ids

---

[Skip to content](https://trumpexcel.com/extract-usernames-from-email-ids/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/extract-usernames-from-email-ids/#below-title)

A colleague asked me if she could quickly extract usernames from Email Ids. She had more than 1000 records and less than 2 minutes to do it.

![Extract Usernames from Email Ids - Sample Data](https://trumpexcel.com/wp-content/uploads/2014/10/Picture12.png)In this tutorial, I will show you 2 methods to do this. And none of it would take more than a minute.

#### Method 1 – Using Text to Column

This is the easiest way if the data has a pattern. For example, in email id, there would always be a username, followed by ‘@’, and ends with the domain name.

The trick is to extract the text before the @ sign. Here is how you can do this:

1.  Select all the email ids
2.  Go to Data –> Data Tools –> Text to Columns
3.  In the Text to Column Wizard
    *   Step 1: Ensure Delimited is checked as the data description and click Next  
        ![Extract Usernames from Email Ids - Step 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20271'%3E%3C/svg%3E)
    *   Step 2: In Delimiters options, select Other, and type @ in the text field adjacent to it. Click Next  
        ![Extract Usernames from Email Ids - Step 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20271'%3E%3C/svg%3E)
    *   Step 3: In the Data preview you can see the data has been separated by username and domain name. Select the second column in Data preview (the one which has the domain name) and select Do not import Column option in Column data format. Also, you can select a Destination cell where the Usernames to be extracted  
        ![Extract Usernames from Email Ids - Step 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20335%20271'%3E%3C/svg%3E)
4.  Click on Finish

This will give you the usernames from the email ids. Note that if you do not specify a destination cell in Step 3, the original data is overwritten with the extracted data (excel does warn you before overwriting).

This method is super fast and you can have the list in a couple of seconds. However, it is not dynamic. If you add a record or make any changes in existing email ids, you will have to do this again.

_**Related:** [7 Amazing Things Excel Text to Columns Can Do For You](https://trumpexcel.com/excel-text-to-columns-examples/)
_

#### Method 2 – Using Excel Formulas

[Excel Formulas](https://trumpexcel.com/excel-functions/)
 has the benefit of making the results dynamic. With formulas, if you change the email ids, the result would update automatically.

Here is the formula you can use to do this:

\=LEFT(A2,FIND("@",A2,1)-1)

There are 2 parts to it:

*   [FIND](https://trumpexcel.com/excel-find-function/)
    (“@”,A2,1) returns the position of @. In case of abc@gmail.com, it will return 4. Now we want to extract the text on the left of @, so we subtract 1 from this formula (which would return 3)
*   [LEFT](https://trumpexcel.com/excel-left-function/)
    (A2,FIND(“@”,A2,1)-1) extracts all the characters to the left of @

Whichever method you choose, it will not take you more than 2 minutes to do it.

Mission Accomplished 🙂

**You May Also Like the Following Excel Tutorials:**

*   [Analyze Each Character of a Text String](https://trumpexcel.com/analyze-each-character-in-excel-using-the-triad-of-indirect-row-mid/)
    .
*   [How to Extract a Substring in Excel (Using TEXT Formulas).](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [Extract Data from Drop Down List Selection in Excel](https://trumpexcel.com/extract-data-from-drop-down-list/)
    .
*   [Separate First and Last Name in Excel (Split Names Using Formulas)](https://trumpexcel.com/separate-first-and-last-name-excel/)
    
*   [How to Combine First and Last Name in Excel](https://trumpexcel.com/combine-first-and-last-name-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

13 thoughts on “Extract Usernames from Email Ids in Excel \[2 Methods\]”
------------------------------------------------------------------------

1.  PERFECT
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-12595)
    
2.  Don’t forget you can use Flash Fill for Excel 2013 and later versions.
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-9207)
    
3.  Hi Sumit,
    
    i have written this function the pop up is showing “You’ve entered too many arguments for this function”
    
    Please help me  
    My ID is [ktogra@gmail.com](mailto:ktogra@gmail.com)
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1762)
    
    *   Hi Khushhal.. Thanks for commenting. The formula seems to be working fine on my system. I checked it for various versions of excel. Can you share the file or data set (in drop box or onedrive)?
        
        [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1763)
        
4.  Excellent!!!!!!
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1600)
    
    *   Thanks for commenting Neeraj.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-2072)
        
5.  Great tips Sumit! One other I thought of was to do a Find and Replace.  
    Find: @\*  
    Replace:  
    Leave the replace field blank. This will find all the “@” symbols and the asterisk symbol “\*” is a wildcard that will include everything after the “@”. Replace it with nothing and you will be left with the username only.
    
    This will of course modify the original records, so you might want to make a copy of the data first. But I still think it can be accomplished in under 2 minutes. 🙂
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1583)
    
    *   Thanks for sharing this Jon.. Definitely a good way to do this quickly 🙂
        
        [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1584)
        
    *   I was just going to suggest this, only to see that Jon had already done that…My search for an original tip continues 🙂
        
        [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-2068)
        
6.  Great.
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1581)
    
    *   Thanks for commenting.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-2071)
        
7.  Nice
    
    [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-1573)
    
    *   Thanks for commenting Dhiraj.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/extract-usernames-from-email-ids/#comment-2070)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/extract-usernames-from-email-ids/#respond)

Comment

Name Email Website

  

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

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