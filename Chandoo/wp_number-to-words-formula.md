# Number to Words Excel Formula » Chandoo.org

**Source:** https://chandoo.org/wp/number-to-words-formula

---

*   [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

Number to Words – Excel Formula
===============================

*   Last updated on February 28, 2024

![Picture of Chandoo](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=300&d=mm&r=g)

#### Chandoo

Share

Facebook

Twitter

LinkedIn

**Convert a number to words in Excel using this amazing function.** For example, 123,456 to One hundred twenty-three thousand four hundred fifty-six. You can use this elegant Excel formula to convert number to words.

![convert number to words with this excel formula](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-excel-formula.jpg)

Excel Number to Words Formula
-----------------------------

Below I have provided number to words Excel formula. It assumes you have input number in cell A1.

_Note: This function can convert numbers up to 999,999 into words._

This works only in Office 365 with LET() & LAMBDA() functions If you have an older version of Excel, [click here for VBA UDF](https://chandoo.org/wp/number-to-words-formula/#vb-Number-to-words)
. ×

**The function:**

				
					`=LAMBDA(number,     LET(         th, INT(number / 1000),         th_h, MOD(th / 100, 10),         th_t, MOD(th, 100),         th_tens1, INT(th.t / 10),         th_tens2, MOD(th.t, 10),         h, MOD(D2 / 100, 10),         t, MOD(D2, 100),         tens1, INT(t / 10),         tens2, MOD(t, 10),         tens, {"twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"},         upto19, {"one", "two", "three", "four","five", "six", "seven", "eight", "nine", "ten"," eleven", "twelve","thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen","nineteen"},         CONCAT(             IF(                 th < 1,                 "",                 IF(th_h >= 1, INDEX(upto19, th_h) & " hundred ", "") &                     IF(                         th_t < 1,                         "",                         IF(                             th_tens1 < 2,                             INDEX(upto19, th_t),                             INDEX(tens, th_tens1 - 1) &                                 IF(th_tens2 >= 1, "-" & INDEX(upto19, th_tens2), "")                         )                     ) & " thousand "             ),             IF(h >= 1, INDEX(upto19, h) & " hundred ", ""),             IF(                 t < 1,                 "",                 IF(                     tens1 < 2,                     INDEX(upto19, t),                     INDEX(tens, tens1 - 1) & IF(tens2 >= 1, "-" & INDEX(upto19, tens2), "")                 )             )         )     ) )`
				
			

How this formula works?
-----------------------

[](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-formula.xlsm)

### [Formula & UDF to get Words from Number](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-formula.xlsm)

[Click here to download the sample file](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-formula.xlsm)
 for this page. You can see number to words formula in column C. Play with the values or examine the formula to learn more.

In order to understand the number to words formula, you must first understand the newly introduced LAMBDA() & LET() functions.

### **LAMBDA Excel Function:**

We can use LAMBDA() function to create custom functions in Excel easily. For example, we can take the logic of converting number to words and wrap it a LAMBDA with below syntax and call it number2words() as a custom function.

LAMBDA Syntax:

\=LAMBDA(value, _logic\_to\_convert\_the\_value\_to\_result_)

Learn more about [LAMBDA function in Excel here](https://chandoo.org/wp/what-is-lambda-function/)
.

### LET Excel Function:

LET function let’s us define variables to use with in the context of a formula. You can use LET function to shrink long formulas. Here is a quick example to explain the LET function.

**Original formula:**

				
					`=IF(SUM(A1:A10)>100, “Too high”,  IF(SUM(A1:A10)>20, “Medium”,  IF(SUM(A1:A10)>0, “Positive”,  “Could be zero or negative”)))`
				
			

**Same formula with LET():**

				
					`=LET(s, SUM(A1:A10),  IF(s>100, “Too high”,  IF(s>20, “Medium”,  IF(s>0, “Positive”,  "Could be zero or negative”))))`
				
			

We are using the SUM(A1:A10) several times in the original formula. In the LET() formula version, we start by defining a variable **s** that is equal to SUM(A1:A10) and then we use s in rest of the formula. This simplifies the formula and _supposedly_ makes it faster too (as Excel would calculate SUM(A1:A10) once.

[](https://support.office.com/en-us/article/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999)

### [Learn more about LET function](https://support.office.com/en-us/article/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999)

LET function is introduced newly and available only in Excel 365. Click here to read the documentation on LET function.

### Understanding Number to Words Excel formula

The process for turning number to words is not complicated. If you know how to convert words for numbers up to 999, then same logic is applied to _thousands, millions and billions_ too.

**So let’s understand the process for numbers up to 999.**

1.  Define two arrays _**upto19**_ and **_tys_** to hold {one,two…,nineteen} and {twenty, thirty…,ninety} respectively.
2.  From the input number (say in A1), calculate these 4 numbers and store them in variables.
    1.  h = MOD(A1/100,10)
    2.  t =  MOD(A1,100)
    3.  tens1 = INT(t/10)
    4.  tens2 = MOD(t,10)
3.  One way to look at these four variables is,
    1.  h has hundreds digit
    2.  t tells the last two digits
    3.  tens1 tells the tens digit
    4.  tens2 tells the ones digit
4.  So for an input number like 987, the 4 values would be h=9,  t=87, tens1=8 and tens2=7
5.  Now, construct the words version of number by simply concatenating below:
    1.  INDEX(upto19, h)
    2.  ” hundred “
    3.  if tens1<2 then INDEX(upto19, t)
    4.  else INDEX(tys, tens1-1)&”-“&INDEX(upto19, tens2)

_The actual formula needs a few more if conditions to stop the flow when you hit a round number (like 500 should five hundred_ with no other words after).

**The process for numbers up to 999,999:**

We just need to follow the same idea as above, but twice. Once for thousands and once for balance.

### Known limitations of this formula:

*   This formula works up to numbers 999,999 only.  You can scale it up to work with numbers up to a billion easily, but the formula gets longer.
*   It ignores any portion after decimal point. So **1003.20** becomes _one thousand three_.
*   It doesn’t show “zero” for 0 input value. The output would be blank instead.

Related: [Learn more about the AWESOME Index function](https://chandoo.org/wp/index-formula-usage-and-tips/)
.

Excel Number to Words Formula - Video Explanation
-------------------------------------------------

Just in case your head hurts after all that explanation above, watch this video to understand how the formula works (plus a quick demo of LET function). 

Excel Number to Words - **VBA** User Defined Formula
----------------------------------------------------

  

If you are not able to use the formula version then consider using below **VBA UDF to convert number to words.** This works up to a billion. 

				
					`Public Function number2words(thisNum As Double) As String     Dim bn As Integer, mn As Integer, th As Integer, h As Integer, retval As String          On Error GoTo msg          bn = Int(thisNum / 1000000000)     mn = Int(thisNum / 1000000) Mod 1000     th = Int(thisNum / 1000) Mod 1000     h = thisNum Mod 1000          If bn >= 1 Then         retval = num2words999(bn) & " billion "     End If     If mn >= 1 Then         retval = retval & num2words999(mn) & " million "     End If     If th >= 1 Then         retval = retval & num2words999(th) & " thousand "     End If     retval = retval & num2words999(h)          number2words = retval     Exit Function      msg:     number2words = "error"      End Function   Private Function num2words999(thisNum As Integer) As String     'convert any number up to 999 to words          Dim tys As Variant, upto19 As Variant          tys = Array("twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety")     upto19 = Array("one", "two", "three", "four", "five", "six", "seven", "eight",  "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",  "sixteen", "seventeen", "eighteen", "nineteen")          Dim h As Integer, t As Integer, tens1 As Integer, tens2 As Integer, retval As String          h = Int(thisNum / 100) Mod 10     t = thisNum Mod 100     tens1 = Int(t / 10)     tens2 = t Mod 10          If h >= 1 Then         retval = upto19(h - 1) & " hundred "     End If     If t >= 1 Then         If tens1 < 2 Then             retval = retval & upto19(t - 1)         Else             retval = retval & tys(tens1 - 2)             If tens2 >= 1 Then                 retval = retval & "-" & upto19(tens2 - 1)             End If         End If     End If     num2words999 = retval End Function`
				
			

How to use the Number2Words UDF?
--------------------------------

You do not need prior VBA knowledge to use this function. It works like any other Excel function once you install it.

### To install Number2Words function:

*   _You must have Personal Macros enabled. If not, [click here to read on how to do that](https://chandoo.org/wp/using-personal-macro-workbook/)
    ._
*   Go to your Personal Macros workbook. Add a module or open an existing module.
*   Paste the above code there.

### How to use the Number2Words function:

To use this function on value in A1, simply write =Number2Words(A1)

### Known limitations:

*   This function ignores any portion after decimal point
*   It doesn’t say “Zero” if input is 0 or blank. It would simply return blank.
*   The results are not capitalized. Use Excel functions like PROPER() to do that.
*   This function works up to 2 billion. 
*   If you email the result workbook to a colleague or client, then they cannot refresh the formula (unless they too have installed Number2Words UDF)

[](https://chandoo.org/wp/introduction-to-vba-macros/)

### [FREE VBA Crash Course](https://chandoo.org/wp/introduction-to-vba-macros/)

If you are curious about VBA, [click here](https://chandoo.org/wp/introduction-to-vba-macros/ "FREE VBA crash course")
 for my free 5 part crash course.

Download File - Number to Words Formula & UDF
---------------------------------------------

[](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-formula.xlsm)

### [Formula & UDF to get Words from Number](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-formula.xlsm)

[Click here to download the sample file](https://chandoo.org/wp/wp-content/uploads/2020/03/number-to-words-formula.xlsm)
 for this page. You can see number to words formula in column C. Column E has VBA version output. Play with the formulas or examine the code to learn more.

Comments or suggestions please....
----------------------------------

I hope you are finding the number to words formulas useful. Let me know if you are facing any issues or have suggestions for changing the outputs.

Facebook

Twitter

LinkedIn

**Share this tip** with your colleagues

![Excel and Power BI tips - Chandoo.org Newsletter](https://chandoo.org/wp/wp-content/uploads/2019/08/free-Excel-PBI-tips.png)

### Get FREE Excel + Power BI Tips

Simple, fun and useful emails, once per week.  
  
**Learn & be awesome.**

*   [5 Comments](https://chandoo.org/wp/number-to-words-formula/#comments)
    
*   [Ask a question or say something...](https://chandoo.org/wp/number-to-words-formula/#respond)
    
*   Tagged under [downloads](https://chandoo.org/wp/tag/downloads/)
    , [INDEX()](https://chandoo.org/wp/tag/index/)
    , [let function](https://chandoo.org/wp/tag/let-function/)
    , [new excel functions](https://chandoo.org/wp/tag/new-excel-functions/)
    , [udf](https://chandoo.org/wp/tag/udf/)
    , [VBA](https://chandoo.org/wp/tag/vba/)
    , [videos](https://chandoo.org/wp/tag/videos/)
    
*   Category: [Excel Howtos](https://chandoo.org/wp/category/excel-howtos/)
    , [VBA Macros](https://chandoo.org/wp/category/vba-macros/)
    

[PrevPreviousA quick personal update](https://chandoo.org/wp/a-quick-personal-update/)

[NextIs there a secret code in this data? \[Excel Homework\]Next](https://chandoo.org/wp/secret-code-problem/)

![](https://chandoo.org/wp/wp-content/uploads/2018/07/chandoo-instructor.png)

### Welcome to Chandoo.org

Thank you so much for visiting. My aim is to make **you awesome in Excel & Power BI.** I do this by sharing videos, tips, examples and downloads on this website. There are more than 1,000 pages with all things Excel, Power BI, Dashboards & VBA here. Go ahead and spend few minutes to be AWESOME.  
  
[Read my story](https://chandoo.org/wp/about/)
 • [FREE Excel tips book](https://chandoo.org/wp/subscribe/)

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/fast-track-excel-book-signup-v3-med.png)](https://chandoo.org/wp/subscribe/)

[Want an AWESOME  \
Excel Class?](https://chandoo.org/wp/excel-school-program/)

[![advanced-excel-dashboards-course-chandoo](https://chandoo.org/wp/wp-content/uploads/2019/08/advanced-excel-dashboards-course-chandoo.jpg)](https://chandoo.org/wp/excel-school-program/)

Overall I learned a lot and I thought you did a great job of explaining how to do things. This will definitely elevate my reporting in the future.

![](https://chandoo.org/wp/wp-content/uploads/2023/10/rebekah-spouser-1631059707542.jpeg)

Rebekah S

Reporting Analyst

[FREE Goodies for you...](https://chandoo.org/wp/excel-school-program/)

[![Excel formula list - 100+ examples and howto guide for you](https://chandoo.org/wp/wp-content/uploads/2018/06/100-formulas-excel-list.png)](https://chandoo.org/wp/excel-formula-list/)

[100 Excel Formulas List](https://chandoo.org/wp/excel-formula-list/)

From simple to complex, there is a formula for every occasion. Check out the list now.

[![](https://chandoo.org/wp/wp-content/uploads/2018/07/free-excel-templates-v1.png)](https://chandoo.org/wp/free-excel-templates-download/)

[20 Excel Templates](https://chandoo.org/wp/free-excel-templates-download/)

Calendars, invoices, trackers and much more. All free, fun and fantastic.

[![Advanced Pivot Table tricks](https://chandoo.org/wp/wp-content/uploads/2020/02/advanced-pivot-table-tricks.png)](https://chandoo.org/wp/advanced-pivot-tables)

[13 Advanced Pivot Table Skills](https://chandoo.org/wp/advanced-pivot-tables)

Power Query, Data model, DAX, Filters, Slicers, Conditional formats and beautiful charts. It's all here.

[![](https://chandoo.org/wp/wp-content/uploads/2019/08/introduction-to-powerbi-chandoo-thumb.jpg)](https://chandoo.org/wp/powerbi-introduction/)

[Get started with Power BI](https://chandoo.org/wp/powerbi-introduction/)

Still on fence about Power BI? In this getting started guide, learn what is Power BI, how to get it and how to create your first report from scratch.

Recent Articles on Chandoo.org

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Here is a fabulous New Year gift to you. A free 2025 Calendar Excel Template with built-in Activity planner. This is a fully dynamic and 100% customizable Excel calendar for 2025.

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![NZ GST Calculation - Excel Formula](https://chandoo.org/wp/wp-content/uploads/2025/07/nz-gst-calculation-excel-formula.png)](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

### [New Zealand GST Calculation with Excel \[Free Template\]](https://chandoo.org/wp/new-zealand-gst-calculation-with-excel-template/)

[![How to make a pivot from another pivot in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0157.png)](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

### [Make a Pivot from Another Pivot Table in Excel](https://chandoo.org/wp/make-a-pivot-from-another-pivot-table-in-excel/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

Best of the lot

*   [Excel for beginners](https://chandoo.org/wp/excel-basics/)
    
*   [Advanced Excel Skills](https://chandoo.org/wp/advanced-excel-skills/)
    
*   [Excel Dashboards](https://chandoo.org/wp/excel-dashboards/)
    
*   [Complete guide to Pivot Tables](https://chandoo.org/wp/excel-pivot-tables/)
    
*   [Top 10 Excel Formulas](https://chandoo.org/wp/top-10-formulas-for-aspiring-analysts/)
    
*   [Excel Shortcuts](https://chandoo.org/wp/complete-list-of-excel-shortcuts/)
    
*   [#Awesome Budget vs. Actual Chart](https://chandoo.org/wp/budget-vs-actual-chart-free-template/)
    
*   [40+ VBA Examples](https://chandoo.org/wp/excel-vba/examples/)
    

Related Tips
------------

[![2026 calendar and planner Excel template - how to use](https://chandoo.org/wp/wp-content/uploads/2025/12/screenshot-0282.png)](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

Learn Excel

### [FREE Calendar & Planner Excel Template for 2026](https://chandoo.org/wp/free-calendar-planner-excel-template-for-2026/)

[![Who is my boss's boss?](https://chandoo.org/wp/wp-content/uploads/2025/08/image.png)](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

Excel Challenges

### [Who is my boss’s boss? \[Data Analytics Challenge – 001\]](https://chandoo.org/wp/who-is-my-boss-boss-data-challenge-001/)

[![How to use XLOOKUP with two sheets in Excel?](https://chandoo.org/wp/wp-content/uploads/2025/06/SNAG-0152.png)](https://chandoo.org/wp/xlookup-with-two-sheets/)

Excel Howtos

### [How to use XLOOKUP with two sheets?](https://chandoo.org/wp/xlookup-with-two-sheets/)

[![Excel IF Statement Two Conditions - Perfect Examples](https://chandoo.org/wp/wp-content/uploads/2025/05/screenshot-0121.png)](https://chandoo.org/wp/excel-if-statement-two-conditions/)

Excel Howtos

### [Excel IF Statement Two Conditions](https://chandoo.org/wp/excel-if-statement-two-conditions/)

[![How to insert dates automatically in Excel](https://chandoo.org/wp/wp-content/uploads/2025/05/2025-05-07_10-35-53.gif)](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

Excel Howtos

### [How to insert dates in Excel automatically](https://chandoo.org/wp/how-to-insert-dates-in-excel-automatically/)

[![Lookup in any column - Excel formula trick](https://chandoo.org/wp/wp-content/uploads/2025/02/SNAG-0092.png)](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

Excel Howtos

### [How to lookup in any column – Excel Formula Trick](https://chandoo.org/wp/how-to-lookup-in-any-column-excel/)

### 3 Responses to “Filter one table if the value is in another table (Formula Trick)”

1.  ![](https://secure.gravatar.com/avatar/009649ad2a9f58f64a563b208b196d4e78b4e506bf2eeb2ab4c84a820fd0aa0e?s=64&d=mm&r=g) Montu says:
    
    [November 18, 2022 at 5:19 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107616)
    
    What about the opposite? I want a list of products without sales or customers with no orders. So I would exclude the ones that are on the other table.
    
    [Reply](https://chandoo.org/wp/number-to-words-formula/#comment-2107616)
    
    *   ![](https://secure.gravatar.com/avatar/534f3043f65d0d27072d17a5dc64da8425eaf628f6915bb23d453d3f6cd3e5df?s=64&d=mm&r=g) [Chandoo](http://chandoo.org/wp)
         says:
        
        [November 18, 2022 at 9:24 pm](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2107623)
        
        Good question. You can check for the =0 as countifs result. for example,  
        \=FILTER(orders, COUNTIFS(products, orders\[Product\])=0)  
        should work in this case.
        
        PS: I have added this example to the article now.
        
        [Reply](https://chandoo.org/wp/number-to-words-formula/#comment-2107623)
        
2.  ![](https://secure.gravatar.com/avatar/b466b5dcbff92562675873cda426fd5244289b247a4fa8c9018f1ab2867b509d?s=64&d=mm&r=g) [Raphael](http://nil/)
     says:
    
    [March 9, 2023 at 6:12 am](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#comment-2122498)
    
    Hi there!
    
    Could i check if there was a way to return certain fields of the table only?
    
    so based off your example above, i would like to continue to use the 'Products" table as a way to filter out items from my "Orders" table, but only want to show maybe only the "Product" and "Order Value" fields, rather than all 5 fields (sales person, customer, product, date, order value).
    
    [Reply](https://chandoo.org/wp/number-to-words-formula/#comment-2122498)
    

### Leave a Reply

[Click here to cancel reply.](https://chandoo.org/wp/filter-one-table-if-the-value-is-in-another-table-formula-trick/#respond)

 Name (required)

 Mail (will not be published) (required)

 Website

  

 Notify me of when new comments are posted via e-mail

Δ