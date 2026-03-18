# How to Extract a Substring in Excel (Using TEXT Formulas)

**Source:** https://trumpexcel.com/extract-a-substring-in-excel

---

[Skip to content](https://trumpexcel.com/extract-a-substring-in-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/extract-a-substring-in-excel/#below-title)

Excel has a set of TEXT Functions that can do wonders. You can do all kinds of text slice and dice operations using these functions.

One of the common tasks for people working with text data is to extract a substring in Excel (i.e., get psrt of the text from a cell).

Unfortunately, there is no substring function in Excel that can do this easily. However, this could still be done using text formulas as well as some other in-built Excel features.

This Tutorial Covers:

[Toggle](https://trumpexcel.com/extract-a-substring-in-excel/#)

Let’s first have a look at some of the text functions we will be using in this tutorial.

Excel TEXT Functions
--------------------

Excel has a range of [text functions](https://trumpexcel.com/excel-functions/)
 that would make it really easy to extract a substring from the original text in Excel. Here are the Excel Text functions that we will use in this tutorial:

*   [RIGHT function](https://trumpexcel.com/excel-right-function/)
    : Extracts the specified numbers of characters from the right of the text string.
*   [LEFT function](https://trumpexcel.com/excel-left-function/)
    : Extracts the specified numbers of characters from the left of the text string.
*   [MID function](https://trumpexcel.com/excel-mid-function/)
    : Extracts the specified numbers of characters from the specified starting position in a text string.
*   [FIND function](https://trumpexcel.com/excel-find-function/)
    : Finds the starting position of the specified text in the text string.
*   [LEN function](https://trumpexcel.com/excel-len-function/)
    : Returns the number of characters in the text string.

Extract a Substring in Excel Using Functions
--------------------------------------------

Suppose you have a dataset as shown below:

![Extract Substring in Excel Using Formulas Email Data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20354%20187'%3E%3C/svg%3E)

These are some random (but superhero-ish) email ids (except mine), and in the examples below, I’ll show you how to extract the username and domain name using the Text functions in Excel.

### **Example 1 – Extracting Usernames from Email Ids**

While using Text functions, it is important to identify a pattern (if any). That makes it really easy to construct a formula. In the above case, the pattern is the @ sign between the username and the domain name, and we will use it as a reference to get the usernames.

Here is the formula to get the username:

\=LEFT(A2,FIND("@",A2)-1)

The above formula uses the LEFT function to extract the username by identifying the position of the @ sign in the id. This is done using the FIND function, which returns the position of the @.

For example, in the case of brucewayne@batman.com, FIND(“@”,A2) would return 11, which is its position in the text string.

Now we use the LEFT function to extract 10 characters from the left of the string (one less than the value returned by the LEFT function).

Also read: [TAKE Function in Excel](https://trumpexcel.com/excel-functions/take-function/)

### **Example 2 – Extracting the Domain Name from Email Ids**

The same logic used in the above example can be used to get the domain name. A minor difference here is that we need to extract the characters from the right of the text string.

Here is the formula that will do this:

\=RIGHT(A2,LEN(A2)-FIND("@",A2))

![Extract Substring in Excel Using Formulas domain name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20216'%3E%3C/svg%3E)

In the above formula, we use the same logic, but adjust it to make sure we are getting the correct string.

Let’s again take the example of brucewayne@batman.com. The FIND function returns the position of the @ sign, which is 11 in this case. Now, we need to extract all the characters after the @. So we identify the total length of the string and subtract the number of characters till the @. It gives us the number of characters that cover the domain name on the right.

Now we can simply use the RIGHT function to get the domain name.

Also read: [Check IF Cell Contains Partial Text in Excel](https://trumpexcel.com/check-if-cell-contains-partial-text-excel/)

### **Example 3 – Extracting the Domain Name from Email Ids (without .com)**

To extract a substring from the middle of a text string, you need to identify the position of the marker right before and after the substring.

For example, in the example below, to get the domain name without the .com part, the marker would be @ (which is right before the domain name) and . (which is right after it).

Here is the formula that will extract the domain name only:

\=MID(A2,FIND("@",A2)+1,FIND(".",A2)-FIND("@",A2)-1) 

![Extract Substring in Excel Using Formulas domian without com](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20740%20205'%3E%3C/svg%3E)

Excel MID function extracts the specified number of characters from the specified starting position. In this example above, FIND(“@”,A2)+1 specifies the starting position (which is right after the @), and FIND(“.”,A2)-FIND(“@”,A2)-1 identifies the number of characters between the ‘**@**‘ and the ‘**.**‘

_Update:_ One of the readers [William19](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2532881480)
 mentioned that the above formula wouldn’t work in case there is a dot(.) in the email id (for example, bruce.wayne@batman.com). So here is the formula to deal with such cases:

\=MID(A1,FIND("@",A1)+1,FIND(".",A1,FIND("@",A1))-FIND("@",A1)-1)

Using Text to Columns to Extract a Substring in Excel
-----------------------------------------------------

Using functions to extract a substring in Excel has the advantage of being dynamic. If you change the original text, the formula would automatically update the results.

If this is something you may not need, then using the [Text to Columns feature](https://trumpexcel.com/excel-text-to-columns-examples/)
 could be a quick and easy way to split the text into substrings based on specified markers.

Here is how to do this:

*   Select the cells where you have the text.![Extract Substring in Excel Using Formulas select data](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20347%20176'%3E%3C/svg%3E)
*   Go to Data –> Data Tools –> Text to Columns.![Extract Substring in Excel Using Formulas text to columns](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20350%20130'%3E%3C/svg%3E)
*   In the Text to Column Wizard Step 1, select Delimited and press Next.![Extract Substring in Excel Using Formulas Text to Columns1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20422'%3E%3C/svg%3E)
*   In Step 2, check the Other option and enter @ in the box right to it. This will be our delimiter that Excel would use to split the text into substrings. You can see the Data preview below. Click on Next.![Extract Substring in Excel Using Formulas Text to Columns2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20516%20424'%3E%3C/svg%3E)
*   In Step 3, General setting works fine in this case. You can however, choose a different format if you are splitting numbers/dates. By default, the destination cell is where you have the original data. If you want to keep the original data intact, change this to some other cell.![Extract Substring in Excel Using Formulas Text to Columns3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20518%20420'%3E%3C/svg%3E)
*   Click on Finish.

This will instantly give you two sets of substrings for each email id used in this example.![Extract Substring in Excel Using Formulas Text to Columns result](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20170'%3E%3C/svg%3E)

If you want to further split the text (for example, split batman.com to batman and com), repeat the same process with it.

Using FIND and REPLACE to Extract Text from a Cell in Excel
-----------------------------------------------------------

[FIND and REPLACE](https://trumpexcel.com/find-and-replace-in-excel/)
 can be a powerful technique when you are working with text in Excel. In the examples below, you’ll learn how to use FIND and REPLACE with wildcard characters to do amazing things in Excel.

_**See Also:**_ [Learn All about Wildcard Characters in Excel](https://trumpexcel.com/excel-wildcard-characters/)
.

Let’s take the same Email ids examples.

### **Example 1 – Extracting Usernames from Email Ids**

Here are the steps to extract usernames from Email Ids using the Find and Replace functionality:

*   Copy and paste the original data. Since Find and Replace works and alters the data on which it is applied, it is best to have a backup of the original data.![Extract Substring in Excel Using Formulas Find and Replace 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%20169'%3E%3C/svg%3E)
*   Select the data and go to Home –> Editing –> Find & Select –> Replace (or use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Ctrl + H).![Extract Substring in Excel Using Formulas Find and Replace 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20245'%3E%3C/svg%3E)
*    In the Find and Replace dialogue box, enter the following:
    *   Find what: @\*
    *   Replace with: (leave this blank)![Extract Substring in Excel Using Formulas Find and Replace 3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20450%20203'%3E%3C/svg%3E)
*   Click on Replace All.![Extract Substring in Excel Using Formulas Find and Replace 4](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20204'%3E%3C/svg%3E)

This will instantly [remove all the text](https://trumpexcel.com/remove-text-before-after-character-excel/)
 before the @ in the email ids. You’ll have the result as shown below:

![Extract Substring in Excel Using Formulas Find and Replace 8](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20166'%3E%3C/svg%3E)

_**How this works??**_ – In the above example, we have used a combination of @ and \*. An asterisk (\*) is a wildcard character that represents any number of characters. Hence, @\* would mean, a text string that starts with @ and can have any number of characters after it. For example in brucewayne@batman.com, @\* would be @batman.com. When we replace @\* with blank, it removes all the characters after @ (including @).

Also read: [REGEX Functions in Excel](https://trumpexcel.com/excel-functions/regex-excel/)

### **Example 2 – Extracting the Domain Name from Email Ids**

Using the same logic, you can modify the ‘Find what’ criteria to get the domain name.

Here are the steps:

*   Select the data.  
    ![Extract Substring in Excel Using Formulas Find and Replace 1](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20605%20169'%3E%3C/svg%3E)
*   Go to Home –> Editing –> Find & Select –> Replace (or use the [keyboard shortcut](https://trumpexcel.com/excel-keyboard-shortcuts/)
     Ctrl + H).![Extract Substring in Excel Using Formulas Find and Replace 2](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20274%20245'%3E%3C/svg%3E)
*    In the Find and Replace dialogue box, enter the following:
    *   Find what: \*@
    *   Replace with: (leave this blank)![Extract Substring in Excel Using Formulas Find and Replace 5](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20451%20202'%3E%3C/svg%3E)
*   Click on Replace All.![Extract Substring in Excel Using Formulas Find and Replace 6](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20456%20206'%3E%3C/svg%3E)

This will instantly [remove all the text](https://trumpexcel.com/remove-text-before-after-character-excel/)
 before the @ in the email ids. You’ll have the result as shown below:

![Extract Substring in Excel Using Formulas Find and Replace 7](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20487%20166'%3E%3C/svg%3E)

**You May Also Like the Following Excel Tutorials:**

*   [How to Count Cells that Contain Text Strings](https://trumpexcel.com/count-cells-that-contain-text/)
    .
*   [Extract Usernames from Email Ids in Excel \[2 Methods\]](https://trumpexcel.com/extract-usernames-from-email-ids/)
    .
*   [Excel Functions (Examples + Videos)](https://trumpexcel.com/excel-functions/)
    .
*   [Get More Out of Find and Replace in Excel](https://trumpexcel.com/find-and-replace-in-excel/)
    .
*   [How to Capitalize First Letter of a Text String in Excel](https://trumpexcel.com/capitalize-first-letter-excel/)
    
*   [How to Extract the First Word from a Text String in Excel](https://trumpexcel.com/extract-first-word-excel/)
    
*   [Separate Text and Numbers in Excel](https://trumpexcel.com/separate-text-and-numbers-in-excel/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

14 thoughts on “How to Extract a Substring in Excel (Using TEXT Formulas)”
--------------------------------------------------------------------------

1.  Bajlahlah/ljahlkja/12345/jakj;akj/abc  
    any formula to extract 12345 from string
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-13879)
    
2.  Column A Column B Column C
    
    Inv No. PC How Can I get the answer on column B  
    by using Excel Formula in Column C  
    18JH42A330EN00710076 A330 = What will be the formula??  
    18CH2S011S0047 S011  
    18JK2T007G0111 T007  
    18TN2O004G0280 O004  
    18PM080154WB0648 PM08
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-12997)
    
3.  How do you check for a specific text in a cell; for example I want to check for ALCON, my search should give me false for any text with a word SALCON or ALCONEX but only ALCON. Thanks.
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-12736)
    
4.  Thanks for this to help my team in doing text search to data.
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-11123)
    
5.  I am using Text to column menu for this, But I don’t know using the formula, it is very tricky,Thanks Sumit, Its very useful.
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2985)
    
    *   Thanks Thiyagarajan.. Glad you found this useful 🙂
        
        [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-3004)
        
6.  Nice Trick………………
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2975)
    
    *   Thanks for commenting Anand.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2979)
        
7.  Sumit,  
    I use these tricks almost everyday. Glad that you share with the world.
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2973)
    
    *   Thanks for commenting Rudra 🙂
        
        [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2978)
        
8.  Excellent. Add a note that “Example 3 – Extracting the Domain Name from Email Ids (without .com)” will not work if the email address has a dot (.) in it.
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2950)
    
    *   Thanks for pointing this out William.. I have updated the article with a note and the relevant formula.
        
        [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2955)
        
9.  Excellent………….thanks a million
    
    [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2948)
    
    *   Thanks Hemang.. Glad you liked it 🙂
        
        [Reply](https://trumpexcel.com/extract-a-substring-in-excel/#comment-2954)
        

### Leave a Comment [Cancel reply](https://trumpexcel.com/extract-a-substring-in-excel/#respond)

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