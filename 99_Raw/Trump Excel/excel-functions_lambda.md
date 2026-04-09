# Excel LAMBDA Function - Easy Explanation with Examples

**Source:** https://trumpexcel.com/excel-functions/lambda

---

[Skip to content](https://trumpexcel.com/excel-functions/lambda/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/lambda/#below-title)

Since Excel released the LAMBDA function, it has been the talk of the town.

Lambda is different from [other Excel functions](https://trumpexcel.com/excel-functions/)
. While all the other Excel functions do some calculations and give you the result, **Lambda allows you to create your own functions.**

That’s right – you don’t need to resort to [VBA or any other programming language](https://trumpexcel.com/excel-vba/)
 to create your own functions. You can do that right within a cell using LAMBDA.

To put it in simple words, the Lambda function allows you to create your own custom functions in Excel, which helps you simplify and use complex formulas.

In this article, I will start with the basics of the Excel LAMBDA function and show you how it works.

While the first few examples may seem very basic (and may even make you feel that the Lambda function is worthless), as I progress through these examples, you will notice that the LAMBDA function can actually be quite powerful when it comes to simplifying your formulas.

Finally, when I discuss recursive Lambdas, you will realize that they do something that no other Excel function can.

Lambda function can recursively call itself and even call other Lambda functions you have created. Examples of how to use recursive lambdas are also covered in this article.

Enough of the talk.

Let’s dive in and see the magic of the Lamda function in Excel.

[_**Click here to download the example file and follow along**_](https://www.dropbox.com/scl/fi/6byi43wadhaorhy2ic53j/Excel-Lambda-Function-Examples.xlsx?rlkey=itppbtxpird0pv9ebw31u6s55&dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/lambda/#)

Excel LAMBDA Function Syntax
----------------------------

Before I get into the fun of creating Lambda functions, let me quickly tell you the syntax:

\=LAMBDA(\[parameter1, parameter2, …,\] calculation)

Here:

*   **\[parameter1, parameter2, …,\]** – These are the values that you want to use in the formula that you will create using LAMBDA. These could be cell references, numeric values, or text values. You can use up to 253 parameters in one single lambda formula. Also, this is an optional argument.
*   **calculation** – This is the formula that you want the Lambda function to use to calculate and give you the result. This is the required argument and should return a value.

Now, let me first show you how to create a very basic Lambda in Excel.

Creating a Basic Lambda Function
--------------------------------

Below, I have two numbers that I want to add.

![Two numbers to add in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20378%20156'%3E%3C/svg%3E)

Now, if you have to add these two numbers, you can use either of the two following formulas:

\=A2 + B2

or

\=SUM(A2,B2)

![Simple sum function to add two numbers in Excel3](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20571%20265'%3E%3C/svg%3E)

Now, let me show you how to create a Lambda function that takes two arguments (the cell references) and gives you the sum of these two numbers.

_At this point, I am fully aware that this is a useless Lambda, and I can easily use any of the above two formulas instead. But my aim here is not to show you a practical example of using the Lambda function but rather use a very simple use case to explain how the Lambda function works in Excel. More practical examples are covered later in this article._

So, let’s create that Lambda.

Enter the following formula in the cell:

\=LAMBDA(a,b,a+b)(A2,B2)

You’ll notice that it gives us the right result – 30.

![LAMBDA function to add two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20691%20308'%3E%3C/svg%3E)

Now, let me explain what’s going on.

_\=LAMBDA(a,b,a+b)_ – This part of the formula is the Lambda function we have created. It takes two arguments (a and b), and the last argument is the calculation, which tells the formula what to do with these arguments.

So, in our case, the calculation is to do a + b.

Now, if you just enter =LAMBDA(a,b,a+b) in a cell and hit enter, you will see the calculation error (#CALC!).

![LAMBDA Function showing CALC error when adding two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20654%20285'%3E%3C/svg%3E)

This is because while=LAMBDA(a,b,a+b) has created a formula for us, it does know what to add. We haven’t given it the values for _a_ and _b_.

So, we give these values just like we would give them in a [SUM function](https://trumpexcel.com/excel-sum-function/)
, within brackets.

So, our final formula becomes

\=LAMBDA(a,b,a+b)(A2,B2)  

![LAMBDA function to add two numbers](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20691%20308'%3E%3C/svg%3E)

So, think of it like this – we have created a lambda function that adds two values, and then we have given Lambda the two values that we want to add.

Now, while this works, this is not how Lambda is supposed to be used.

Excel allows you to put the LAMBDA function in a [named range](https://trumpexcel.com/named-ranges-in-excel/)
 and then use the name of that range as a formula.

For example, let me save this Lambda formula with the name AddTwoNos and then I will be able to use the function _AddTwoNos_ in the worksheet just like any other regular function.

Here are the steps to save a Lambda function as a named range:

1.  Copy the Lambda function =LAMBDA(a,b,a+b). Note that I’m not copying the arguments I passed to the function in the brackets. Just the Lamda formula
2.  Hold the Control key and then press the F3 key to open the Name Manager dialog box. Alternatively, you can also click on the _Formulas_ tab and then click on _Name Manager._

![Click on the name manager in the formulas tab](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20206'%3E%3C/svg%3E)

2.  Click on the New button. This will open the new name dialog box

![Click on the new button in the name manager dialog Box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20469'%3E%3C/svg%3E)

3.  Enter a name for the function. In this case, I will use _AddTwoNos_

4.  In the ‘Refers to’ field, copy and paste the Lambda formula

![Enter the name of the lambda and the formula it refers to](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

5.  Click Ok

Now that we have the named range in place, we can use the function AddTwoNos in any cell in Excel.

Below is the formula that uses our Lambda formula calculation to add two numbers.

\=AddTwoNos(A2,B2)

This will give us the result as 30.

![LAMBDA function to add two numbers created](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20631%20280'%3E%3C/svg%3E)

Note: When you create a custom function with LAMBDA and then use it in a cell in Excel, you will see the function show up in the intellisense as you type the first few characters of the function name.

If you are with me so far, here are two things to know:

*   You’re awesome!!
*   We’ve seen how to create a very basic lambda that enables us to create our own custom function, specify what arguments it should take and what calculation should happen in the back end, give a name to that function, and then use it in the worksheet just like any other regular function.

At this point, if you don’t share my enthusiasm, I don’t blame you.

But let me tell you this: what we have done forms the basis of some amazing things we can do with the Lambda function in Excel.

[_**Click here to download the example file and follow along**_](https://www.dropbox.com/scl/fi/6byi43wadhaorhy2ic53j/Excel-Lambda-Function-Examples.xlsx?rlkey=itppbtxpird0pv9ebw31u6s55&dl=1)

Examples of Using the LAMBDA Function in Excel
----------------------------------------------

Let me now take you through some practical examples where you can think of using lambda in your work.

### Calculate Commission Using LAMBDA Function (One Condition)

Let’s start with an easier one.

Below, I have a data set where I have names, regions, and sales values for some employees.

![Data set to calculate commission](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20405'%3E%3C/svg%3E)

In this data set, I want to calculate commissions in column D based on the following criteria:

*   Commission is 5% if the Sales value is more than 50,000
*   Commission is 3% if the Sales value is less than 50,000

I can do this using a simple if statement as shown below:

\=IF(C2>50000,C2\*5%,C2\*3%)

![IF function to calculate the commission](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20453'%3E%3C/svg%3E)

Now, let me show you how to create a Lambda function from this.

Again, I am aware that I can use the [IF function](https://trumpexcel.com/excel-if-function/)
 instead of creating the Lambda function. But the idea here is to showcase how the Lambda function can be created and used, and then I’ll show you more complex examples where creating a Lambda would actually be helpful.

Below is the Lambda function that I’ve created:

\=LAMBDA(sales,IF(sales>50000,sales\*5%,sales\*3%))

In this function, I have provided one parameter (sales), and then the if function calculation that uses the sales parameter to calculate the commission.

If I enter this formula in a cell and hit the Enter key, it will give me the calculation error (#CALC!)

![Lambda function shows a calculation error without the right input](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20790%20481'%3E%3C/svg%3E)

This is because while the lambda function is fine, it doesn’t know what value it should use for the sales parameter.

I can get it to work by using the below formula instead:

\=LAMBDA(sales,IF(sales>50000,sales\*5%,sales\*3%))(C2)

![Lambda function working within a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20830%20484'%3E%3C/svg%3E)

Here, I have added (C2) after the LAMBDA function, So it knows that it can take the value in cell C2 as the value of the sales parameter.

Now that I know that my Lambda function works, let me create a custom function with this so that I can use a simplified formula to calculate commission instead of the IF function.

Here are the steps to do this:

1.  Copy the Lambda function =LAMBDA(sales,IF(sales>50000,sales_\*5%,sales\*_3%)). Note that I’m not copying the arguments I passed to the function in the brackets. Just the Lamda formula
2.  Hold the Control key and then press the F3 key to open the Name Manager dialog box.
3.  Click on the New button. This will open the New Name dialog box
4.  Enter a name for the function. In this case, I will use _SalesCom_

![Enter the new name for the lambda function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

5.  In the ‘Refers to’ field, copy and paste the Lambda formula

![Add the lambda formula to the refers to field in name manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

6.  Click Ok

The above steps have converted my Lambda function into a Named Range, and now I can use _SalesCom_ as any other regular function in my worksheet.

So, I can now use the below function to get the commission:

\=SalesCom(C2) 

![Lambda function used to calculate the sales commission](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20585%20454'%3E%3C/svg%3E)

As you can see, this is simpler than using the longer IF function.

Also, in this case, I have hard coded the commission percentage values in the formula, but if you want, you can have those values in a cell reference and then use that cell reference instead.

Now, If you’re still thinking that the LAMBDA function hasn’t proved itself useful yet, as the IF function was already simple enough, let me show you a slightly complicated function that can be further simplified using the Lambda function in the next example.

### Calculate Commission Using LAMBDA Function (Two Conditions)

Below, I have the same data set with names, regions, sales, and commission columns, and I want to calculate the commission based on the following conditions:

*   If the region is the US, the commission would always be 5%, irrespective of the Sales value.
*   If the region is not the US, then the Commission would be 5% of the sales value is more than 50,000
*   Else, the commission would be 3%

![Data set to calculate commission](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20530%20405'%3E%3C/svg%3E)

Below is the nested IF function that can do this:

\=IF(B2="US",C2\*5%,IF(C2>50000,C2\*5%,C2\*3%))

![IF function to calculate commission based on two conditions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20360'%3E%3C/svg%3E)

Now, let’s convert this function into a Lambda function, so that I can create my own custom function, which is a lot more simple than the above nested IF function.

In the above function, since there are two different cell references I’m using (B2 and C2), I will have to create a Lambda function that uses two parameters before the calculation.

Here is the LAMBDA function that works:

\=LAMBDA(region,sales,IF(region="US",sales\*5%,IF(sales>50000,sales\*5%,sales\*3%)))

If you enter this formula in a cell in Excel and press Enter, it is going to give you the calculation error (#CALC!). This is because the function does not know what values it should take for _region_ and _sales_ parameter.

![Lambda function gives the calculation error](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20370'%3E%3C/svg%3E)

I can test whether my Lambda function is working or not by using the below formula in a cell in Excel.

\=LAMBDA(region,sales,IF(region="US",sales\*5%,IF(sales>50000,sales\*5%,sales\*3%)))(B2,C2)

![Lambda function that works to calculate commission based on two conditions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20368'%3E%3C/svg%3E)

Since the Lambda function is working fine, let me use this to create my own function.

Here are the steps to convert the Lambda function into a named range so that I can use that named range as a custom function in my worksheet:

1.  Copy the Lambda function _\=LAMBDA(region,sales,IF(region=”US”,sales\*5%,IF(sales>50000,sales\*5%,sales\*3%)))_. Note that I’m not copying the arguments I passed to the function in the brackets. Just the Lamda formula.
2.  Hold the Control key and then press the F3 key to open the Name Manager dialog box.
3.  Click on the New button. This will open the New Name dialog box
4.  Enter a name for the function. In this case, I will use _SalesCom_2

![Enter the name for the lambda function in the New Name dialog box](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

5.  In the ‘Refers to’ field, copy and paste the Lambda formula

![Enter the formula in the refers to field](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

6.  Click Ok

Now that I have saved my Lambda function as a named range, I can use that as a custom function on my worksheet.

Below is the formula I can use:

\=SalesCom2(B2,C2)

![LAMBDA custom function to calculate commissions](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20625%20453'%3E%3C/svg%3E)

As you can see, I am able to replace a nested If function with a much simpler Lambda function that takes just two arguments.

As you get comfortable in creating Lambda function in Excel, you will be able to convert long and complicated formulas into your own simpler custom functions.

By now, I hope you have a decent understanding of how the lambda function can be created and used in Excel.

Now, let me show you a couple more examples of creating Lambda functions in Excel.

Also read: [Creating a User Defined Function (UDF) in Excel VBA](https://trumpexcel.com/user-defined-function-vba/)

### Extract Numbers from a String using the LAMBDA Function

Below, I have a data set where I have some product IDs in column A, and I want to extract only the numerical value in these product IDs in column B.

I can do that using the Excel formula below:

\=TEXTJOIN("",TRUE,IFERROR(MID(A2,SEQUENCE(LEN(A2)),1)\*1,""))

![Formula to extract numbers from a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20287'%3E%3C/svg%3E)

The above formula separates each character in the cell and analyzes whether it’s a number or not. If it is a number, it is kept, and if it is not a number, it is replaced by a blank.

As you can see, this is not a very simple formula, and if I convert this into a Lambda function, I would be able to use a very simplified function that takes one single argument and gives me the numeric part from the cell.

So, let’s create the LAMBDA function for this.

Below is the lambda function where I’ve used the parameter pdid (for product ID):

\=LAMBDA(pdid,TEXTJOIN("",TRUE,IFERROR(MID(pdid,SEQUENCE(LEN(pdid)),1)\*1,"")))

If you enter this formula in a cell in Excel and hit enter, it is going to give you the calculation error (#CALC!) as it does not know what pdid is.

So, if you want to check the formula, you can use the below formula instead, where I give the value of _pdid_ in brackets after the formula.

\=LAMBDA(pdid,TEXTJOIN("",TRUE,IFERROR(MID(pdid,SEQUENCE(LEN(pdid)),1)\*1,"")))(A2)

![Lambda formula to extract numbers from a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20261'%3E%3C/svg%3E)

The above formula would return 231, which tells me that my Lambda function is working fine.

Now, let me create my own simplified version of this formula. I will call that formula GETNUM.

Below are the steps to create my own custom function using the above lambda function:

1.  Copy the Lambda function _\=LAMBDA(pdid,TEXTJOIN(“”,TRUE,IFERROR(MID(pdid,SEQUENCE(LEN(pdid)),1)\*1,””)))_
2.  Open the Name Manager dialog box (you can do this by using the [keyboard shortcut](https://trumpexcel.com/20-excel-keyboard-shortcuts/)
     Control + F3).
3.  Click on the New button. This will open the New Name dialog box
4.  Enter a name for the function. In this case, I will use _GETNUM_

![Give the Lambda Formula a name in the name manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20379%20289'%3E%3C/svg%3E)

5.  In the ‘Refers to’ field, copy and paste the Lambda formula we copied in step 1

![Enter the formula and refers to field in name manager](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20377%20289'%3E%3C/svg%3E)

6.  Click Ok

Now, I can use the below function to get only the numeric part from a cell:

\=GetNum(A2)

![Lambda custom function works to extract the numbers from a cell](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20567%20332'%3E%3C/svg%3E)

As you can see, I was able to convert a relatively complex formula into an extremely simple one that takes one single argument and gives me the expected result.

It can be quite a time saver if you need to use this formula in multiple places in your workbook. So you can create it once and reuse it as many times as you want in the same workbook.

Creating Recursive Lamba Function
---------------------------------

Recursive Lambda is an advanced concept that allows you to create a lambda function and then call the same function from within itself.

It’s a pretty well-known concept in the programming world, and with Lambda you can bring the same concept in your worksheets as well.

Below is the video in which I’ve explained recursive lambda in detail (starts at 19 minutes and 20 seconds mark):

Since this is an advanced concept, I would request you to get used to the basic usage of lambda function first and then try a couple of scenarios where recursive lambda can be used.

Some Questions You May have about the Excel Lambda function
-----------------------------------------------------------

Below are some of the questions I’ve got from Excel users about this new Excel Lambda function:

**Q. Can I create a Lambda function and use it in all my workbooks?**

A: As of writing this article, there is no way you can create a lambda function in one workbook and then use it in all the workbooks in your system.

If there is a lambda function that you need to reuse on another workbook, you will have to copy and create a name range for that lambda function in that workbook as well.

**Q. In what versions of Excel is the Lambda function available?**

A: It is only available in Excel with Microsoft 365 in Excel on the web. If you’re using prior versions of Excel, you won’t be able to use it.

**Q. What is the benefit of creating a custom function using Lambda as compared to VBA?**

**A:** The biggest benefit of using the lambda function to create a custom function is that you do not need to know any programming skills beforehand.

Also, unlike the VBA method, you do not need to save your files as macro-enabled files and enable any privacy or security settings to use these custom functions in the worksheet.

However, VBA, being a programming language, allows you to do a lot more than what can be achieved using a custom function created using Lambda.

I hope you found this article about the Excel Lambda function useful.

If you have any questions or suggestions for me, do let me know in the comments section.

**Other Excel articles you may also like:**

*   [Excel XLOOKUP Function](https://trumpexcel.com/xlookup-function/)
    
*   [20 Advanced Excel Functions and Formulas](https://trumpexcel.com/advanced-excel-functions-formulas/)
    
*   [Excel Filter Function](https://trumpexcel.com/filter-function/)
    
*   [INDEX & MATCH Functions Combo in Excel (10 Easy Examples)](https://trumpexcel.com/index-match/)
    
*   [LET Function in Excel](https://trumpexcel.com/excel-functions/let-function/)
    
*   [Excel REDUCE Function](https://trumpexcel.com/excel-functions/reduce-function/)
    
*   [Excel MAP Function](https://trumpexcel.com/excel-functions/map-function/)
    

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