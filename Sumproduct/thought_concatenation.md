# Concatenation

**Source:** https://sumproduct.com/thought/concatenation/

---

[Home](https://sumproduct.com/)

\> Concatenation

*   May 14, 2025

Concatenation
=============

Can you see the join?.

Concatenation
=============

Ever thought about making text dynamic? Consider concatenation. By Liam Bastick, Director with SumProduct Pty Ltd.

Query
-----

I have to construct monthly reports for presentation to the Board. I have automated many of the reports and charts, but I find myself repeating the same commentaries over and over again. Any tips please?

Advice
------

Having had to write a few monthly reports on a regular basis, I share this reader’s pain. However, if you are prepared to invest some time in reducing what can be a highly repetitive task, Excel can help.

Excel has a useful feature for this purpose called concatenation. This will link text with the values in cells and / or the results of various formulae. For example, consider the following:

![](<Base64-Image-Removed>)

Concatenation Example 1

This shows how simple concatenation is. Using the CONCATENATE function, the above example is no more difficult than:

\=CONCATENATE(“You have picked the colour “,G11)

Note that the text has to be in inverted commas and if you require spacing this needs to be built into the text component too.

This formula could be simplified using the ampersand (**&**) operator instead:

\=”You have picked the colour “&G11

This alternative formula would do exactly the same thing and does not require you to learn how to spell CONCATENATE. Seriously, the operator is preferred in any case since it is slightly more efficient and allows for more items to be joined together.

For the more pedantic amongst you, the text above does not form a sentence. Indeed, it also treats “Orange” as a proper noun as it capitalises the “O”. Also, there is no full stop. Therefore, we might wish to refine the above example as follows:

![](<Base64-Image-Removed>)

Concatenation Example 2

In this example, I have generated the more elaborate formula, viz.

\=”You have “&IF(G11=””,”not yet picked.”,”picked the colour “&LOWER(G11)&”.”)

Working our way through this formula, this version allows for what happens if cell G11 is unpopulated (i.e. the expression **G11=””** means G11 is blank / empty), inserts the full stop and turns “Orange” into “orange” using Excel’s LOWER function (this makes everything lower case).

Concatenation often means manipulating the appearance of text: as well as the **LOWER** function, **UPPER** (upper case) and **PROPER** (pseudo-title case: capitalises the first letter of each and every word) can be useful partners in crime.

Concatenation is often referred to as “mixed text”, in that it is a mixture of text and other arguments such as cell references and / or formulae results. Typically, mixed text will often contain numbers too, and these can be a little more awkward to format. You cannot simply Format Cells (CTRL + 1) as this formats cells containing numerical data only.

In this case, we have to fall back on the useful **TEXT** function which formats, er, numbers. The syntax of TEXT is as follows:

\=TEXT(Reference,”Mask”)

The reference is the cell or formula that needs to be formatted and the Mask is the syntax you would enter for Custom number formatting in the Format Cells (CTRL + 1) dialog box:

![](<Base64-Image-Removed>)

Format Cells, Custom Formats

This was discussed in detail in the [Number Formatting](https://www.sumproduct.com/thought/number-formatting)
 article.

To see how this works in practice, consider the following:

![](<Base64-Image-Removed>)

Concatenation Example 3

Again, the eagle-eyed will spot no full stop, but that is not the point here. The formula

\=”The number is “&TEXT(G25,”$#,##0.0,,m”)

takes the value in cell G25 and displays it to the nearest $0.1m.

Speaking from experience, with practice much mundane monthly reporting commenting on numbers can be automated using this technique; the key is to identify all the scenarios that may occur and allow for them. The formulae may get slightly complex, e.g.

![](<Base64-Image-Removed>)

Concatenation Example 4

This example commentary considers how revenue has changed from one month to the next:

**\=IF(Prior\_Period\_Revenue=0,”Revenue is “&TEXT(Current\_Period\_Revenue,”$#,##0?)&” this month.”,  
****IF(OR(Prior\_Period\_Revenue<0,Current\_Period\_Revenue<=0),”Revenue inputs need to be reviewed.”,  
****IF(Prior\_Period\_Revenue=Current\_Period\_Revenue,”Revenue remains constant at “&TEXT(Current\_Period\_Revenue,”$#,##0″)&” for the month.”,  
****“Revenue has “&  
****IF(Current\_Period\_Revenue>Prior\_Period\_Revenue,”increased”,”decreased”)&  
****” by “&TEXT(ABS(Current\_Period\_Revenue/Prior\_Period\_Revenue-1),  
****“#,##0.0%”)&” this month.”)))**

The examples cited above can all be found in the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-concatenation-examples.xls)
. Good luck working that final formula through!

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/concatenation/#0)
    
*   [Register](https://sumproduct.com/thought/concatenation/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/concatenation/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/concatenation/#0)

[](https://sumproduct.com/thought/concatenation/#0 "close")

top