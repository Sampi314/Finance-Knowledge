# Excel REDUCE Function (Made Easy with Lots of Examples)

**Source:** https://trumpexcel.com/excel-functions/reduce-function

---

[Skip to content](https://trumpexcel.com/excel-functions/reduce-function/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/reduce-function/#below-title)

REDUCE function is one of the hardest [functions in Excel](https://trumpexcel.com/excel-functions/)
, and in this article, I will simplify it for you with lots of examples.

_Reduce function is available in Excel for Microsoft 365, Excel for Microsoft 365 for Mac, and Excel for the web_

[**_Click here to download the example file_**](https://www.dropbox.com/scl/fi/1xrcdqs2o0v7zwgj13hmh/REDUCE-Function.xlsx?rlkey=rbllhxyyrrvdx9f7smywfjp4h&dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/reduce-function/#)

What does the Reduce Function do?
---------------------------------

The REDUCE function is a lambda helper function that processes each value in an array or range, one at a time, and accumulates them into a single final result.

Here are the three most important things to remember about the REDUCE Function:

*   It goes through a array of values (that could be a range of cells).
*   You can specify what to do with each value using the [LAMBDA function](https://trumpexcel.com/excel-functions/lambda/)
     (specified within the reduce function).
*   **It always returns a single value** (hence the name, because it reduces the result to one single value).

Reduce Function Syntax
----------------------

\=REDUCE(\[initial\_value\], array, lambda(accumulator, value, body))

where:

*   _\[initial\_value\]_ – This is your starting point. Think of it as the value you want to begin with before processing any elements. If you skip this argument, Excel uses the first value in your array as the starting point and begins processing from the second value.
*   _array_ – This is the range or array you want to process. Simple as that. It could be A1:A10, or any array of values you want REDUCE to work through.
*   _lambda_ – This is where the magic happens. The LAMBDA function has three parts:
    *   _accumulator_ – This holds your running result as REDUCE moves through each element in your array. Whatever result comes out of each step gets carried forward to the next step and stored in this accumulator. It’s the container that keeps track of your function’s progress.
    *   _value_ – This is the current item REDUCE is looking at from your array. As REDUCE moves through each cell in your range, this argument represents the number being processed.
    *   _body_ – This is your instruction (the custom lambda) where you specifu what you want to do with the accumulator and the current value.

Decoding REDUCE Function (with a simple analogy)
------------------------------------------------

Let me make REDUCE crystal clear by connecting it to something you already know inside out: the [SUM function](https://trumpexcel.com/excel-sum-function/)
.

_Note: This example is just to show you how the REDUCE function works. If all you need to do is add numbers in a range, there is no need to use the REDUCE function and can as this can easily be done using the SUM function._

Below, I have a dataset where I have 10 numbers in A2:A11 and I want to add all of them.

![Dataset to show the reduce function with SUM](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20510%201032'%3E%3C/svg%3E)

Here is the SUM formula to do this:

\=SUM(A2:A11)

![Using the SUM function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201040%201354'%3E%3C/svg%3E)

When you use the SUM formula, you probably think Excel just magically adds everything up and gives you the answer.

But here’s what’s actually happening behind the scenes:

*   Step 1: Excel starts with 0
*   Step 2: It looks at A2 and adds the number in A2 to 0
*   Step 3: It takes that result and adds the value in A3 to it
*   Step 4: It takes that result and adds the value in A4 to it
*   …. and the steps continue till the last cell

Notice the pattern? Excel goes through each value, does something with it (adds it to the running total), carries that result forward, and repeats.

This is exactly how REDUCE function works in Excel.

The only difference is that instead of being stuck with the SUM function, REDUCE lets you decide what happens at each step.

Here’s SUM function recreated using the REDUCE function:

\=REDUCE(0, A2:A11, LAMBDA(a, v, a + v))

![Doing a simple sum using the reduce function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201520%201340'%3E%3C/svg%3E)

Let me break down what’s happening:

*   _0_ is your starting point (just like SUM starts with 0)
*   _A2:A11_ is your range (same as SUM)
*   _a_ is your running result that carries forward. It starts with 0 (or whatever value is specified as the first argument of the REDUCE function), and after every step, the result of the Lambda function is assigned to this variable.
*   v is the current cell being processed. So this would be A2 then A3 then A4 and so on.
*   _a + v_ is what happens within the lambda function

The formula goes:

*   Start: total = 0
*   Step 1: Look at A2 → Calculate 0 + 1 = 1 → Save 1 back into _a_
*   Step 2: Look at A3 (which has 2) → Calculate 2 + _a_ \= 3 → Save 3 back into _a_
*   Step 3: Look at A4 (which has 3) → Calculate 3 + _a_ = 6 → Save 6 back into _a_
*   …. continues till the last cell and the last calculation is then assigned to _a_
*   The reduce function returns the value stored in _a_

![Showing the step-by-step process of the reduce function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202013%201341'%3E%3C/svg%3E)

See what’s happening? At each step, REDUCE:

*   Takes the current value from the accumulator (_a_)
*   Performs your calculation with the current cell value (_v_)
*   Saves that result back into the accumulator (_a_)
*   Moves to the next cell and repeats

The _accumulator_ is constantly being updated and carrying the result forward. That’s why it’s called an “accumulator”, as it accumulates the results as it goes.

Now here’s where it gets interesting.

Since you control what happens in that LAMBDA function, you can change the rules. Instead of simply adding the numbers, you can rewrite the lambda function to only add numbers that are greater than 5 (or create any LAMBDA you want).

This is what makes the REDUCE function so powerful.

Now let’s look at some practical examples of using the REDUCE function in Excel.

Note: If you omit the first argument in the REDUCE function, it will automatically take the first value in the specified range in the second argument.

Example 1 – Conditional Sum using REDUCE
----------------------------------------

Below I have a dataset where I want to add all the numbers that are greater than 50.

![Dataset for conditional sum using reduce function](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20806%20922'%3E%3C/svg%3E)

Now of course, you can do this using the [SUMIF function](https://trumpexcel.com/excel-sumif-function/)
. But let me still show you how to use the REDUCE function so that we can then use the same concept in more advanced examples later.

Here is the reduce formula that will do the conditional sum:

\=REDUCE(0,B2:B11,LAMBDA(a,v,IF(v>50,a+v,a)))

![Reduce function calculate conditional sum in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201766%201213'%3E%3C/svg%3E)

Here’s what’s happening in the formula:

*   0 – this is the first argument, which tells the function that the starting value is going to be 0.
*   B2:B11 – this is the range on which the lambda function would be applied.
*   LAMBDA(a,v,IF(v>50,a+v,a)) – this is the lambda function that does the conditional sum.
    *   a – this is the accumulator value which starts with 0, and then holds the result after each cell is being processed by the lambda function.
    *   v – this is the current value being processed by the lambda function.
    *   IF(v>50,a+v,a) – this is the if condition that checks whether the value in the cell is more than 50 or not. If the value is more than 50, that value is added to the existing value in the accumulator variable (_a_), and if it is not more than 50, the previous accumulator value is returned as is.

Now that I have shown you two simple examples of using the REDUCE function, let’s move on to some advanced use cases.

[**_Click here to download the example file_**](https://www.dropbox.com/scl/fi/1xrcdqs2o0v7zwgj13hmh/REDUCE-Function.xlsx?rlkey=rbllhxyyrrvdx9f7smywfjp4h&dl=1)

Example 2: Conditional Count using REDUCE
-----------------------------------------

Below I have a dataset where I have customer names in Column A and their order details in Column B.

![Dataset to do Conditional Count using REDUCE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201494%20952'%3E%3C/svg%3E)

Note that the value of the order is preceded by a country code such as US-5500, which means that this order is from the US, and the value is 5500.

I want to fetch the total sales value by region and get the results in E2:E5.

Below is the formula that will do this.

\=REDUCE(0,B2:B13,LAMBDA(a,v,IF(TEXTBEFORE(v,"-")=D2:D5,a+TEXTAFTER(v,"-"),a)))

![Formula for Conditional Count using REDUCE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201626%201193'%3E%3C/svg%3E)

Here is what is happening in the above formula.

*   0 – this is the first argument, which tells the function that the starting value is going to be 0.
*   B2:B13 – this is the range where we want to process each cell one-by-one.
*   LAMBDA(a,v,IF(TEXTBEFORE(v,”-“)=D2:D5,a+TEXTAFTER(v,”-“),a)) – this is the lambda function that splits the country code and the numerical sales value and only adds the sales value for a given country.
    *   _a_ – this is the accumulator value which starts with 0, and then holds the result after each cell is being processed by the lambda function.
    *   _v_ – this is the current value being processed by the lambda function.
    *   _IF(TEXTBEFORE(v,”-“)=D2:D5,a+TEXTAFTER(v,”-“),a)_ – this is the IF formula that fetches the country code before the dash and checks if this is equal to the country code specified in column C. If the country code matches, it uses the text of the function to extract the numerical value and adds it to the accumulator. All cells are processed one by one, and conditional sum is done based on the contrary code in column.

Example 3: Conditional Concatenation
------------------------------------

Below I have a dataset where I have names in column A, and I want to concatenate and get all the names specific for each region in D2:D4

![Dataset for conditional concatenation in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201952%20952'%3E%3C/svg%3E)

Below is the formula that will do this.

\=SUBSTITUTE(REDUCE("",A2:A13,LAMBDA(a,v,IF(TEXTAFTER(v,", ")=C2:C4,a&", "&TEXTBEFORE(v,","),a))),", ","",1)

![Reduce formula for conditional concatenation in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201238'%3E%3C/svg%3E)

Here is what is happening within the REDUCE formula:

*   “” – This is the first argument in the Reduce function. Since the expected output of this function is a text string, I am starting with a null string that will act as the starting point. Then, all the names for each country will be concatenated to this blank string.
*   A2:A13 – this is the range where we want to process each cell one-by-one.
*   LAMBDA(a,v,IF(TEXTAFTER(v,”, “)=C2:C4,a&”, “&TEXTBEFORE(v,”,”),a)) – this is the lambda function that uses an [if condition](https://trumpexcel.com/excel-if-function/)
     to extract the country code after the name and based on that country code adds the name to the accumulator

The result of the REDUCE function always gives us a leading comma followed by a space character (“, “). So I’ve used the [SUBSTITUTE function](https://trumpexcel.com/excel-substitute-function/)
 to remove the first instance of it from the final result.

Example 4: Text to Column with REDUCE
-------------------------------------

Below I have the address dataset in a comma-separated format, and I want to get each element of the address in a separate cell.

![Dataset for Text to columns using REDUCE](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201028'%3E%3C/svg%3E)

While I can use the text split function to extract each element from a row, I cannot do it for the entire array in one go.

For example, I can use the below formula to get the first address split into separate columns.

\=TEXTSPLIT(A2,", ")

![TEXTSPLIT applied on one cell works](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201136'%3E%3C/svg%3E)

But it wouldn’t work if I use the below formula, where instead of A2, I use the entire range A2:A13.

\=TEXTSPLIT(A2:A13,", ")

![TEXTSPLIT doesn't spill in both direction](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201134'%3E%3C/svg%3E)

And the reason for this is that TEXTSPLIT (and many other dynamic array formulas) can only spill the result in one direction, either the row or the column.

But if I want one single formula that would give me the entire result where all the addresses are split into separate cells, I can do that by using the below Reduce formula.

\=DROP(REDUCE("",A2:A13,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,",")))),1)

![REDUCE Formula splits in both direction](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202560%201137'%3E%3C/svg%3E)

Here is what is happening in the above REDUCE formula.

*   “” – Since the expected output of the formula is a text string, I’m starting with a null string.
*   A2:A13 – this is the range where we want to process each cell one-by-one.
*   LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,”,”))))
    *   a – this is the accumulator value (starting with a “”).
    *   v – this is the current value being processed by the lambda function.
    *   VSTACK(a,TEXTSPLIT(v,”,”)) – The TEXTSPLIT function takes each cell one-by-one and splits the result using comma as the delimiter. And for each cell, the result of the TEXTSPLIT function is added as a new row to the accumulator value using the VSTACK function.

Since I started with a null string as the initial value, VSTACK gives the result that has an extra row in the beginning that needs to be removed. This is done by using the [DROP function](https://trumpexcel.com/excel-functions/drop-function/)
.

Example 5: Find Unique Words in a Range
---------------------------------------

Below I have a movie genre dataset in column A, and I want to split all the genres in all the cells and then get the total number of unique genres.

![Dataset to get unique values](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201404%201035'%3E%3C/svg%3E)

Below formula will do this

\=DROP(UNIQUE(REDUCE("",A2:A10,LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,," "))))),1)

![Reduce formula to get unique words in a range](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201765%201366'%3E%3C/svg%3E)

Here is what is happening in the above REDUCE formula.

*   “” – Since the expected output of the formula is a text string, I’m starting with a null string.
*   A2:A10 – this is the range where we want to process each cell one-by-one.
*   LAMBDA(a,v,VSTACK(a,TEXTSPLIT(v,,” “)))
    *   a – this is the accumulator value (starting with a “”).
    *   v – this is the current value being processed by the lambda function.
    *   VSTACK(a,TEXTSPLIT(v,,” “)) – This part of the lambda function uses the TEXTSPLIT function to split the content of each cell based on space character as the delimiter. This would split each movie genre and give the result as a column (as I have used space as the third argument in the TEXTSPLIT funciton which makes it a row delimiter, so the result is given in a column). VStack then combines all these genres into one single column.

So, in short, the above REDUCE function is going to split and give us all the words in the selected range in one column.

Now, there are two things that need to be done – remove the first cell as it holds the null character which was our starting point, and remove all the duplicates.

This is done using the DROP function (which removes the first item from the result) and the UNIQUE function (which removes duplicates and gives only unique movie genres).

[**_Click here to download the example file_**](https://www.dropbox.com/scl/fi/1xrcdqs2o0v7zwgj13hmh/REDUCE-Function.xlsx?rlkey=rbllhxyyrrvdx9f7smywfjp4h&dl=1)

Example 6: Bulk Find and Replace
--------------------------------

This is an advanced example that showcases the power of REDUCE function. It’s a use case where we’re able to achieve something using the reduce function that would not be possible (or very difficult) to do using other Excel functions.

Below I have a dataset where I have trainings done by people in column B, but these trainings use codes such as XL for Excel and PPT for PowerPoint.

![Dataset to do bulk find and replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202040%20814'%3E%3C/svg%3E)

I want to replace these codes with actual training names (using the table in E1:F4).

In this example, I want the function to go through each cell in the given range (B2:B11), then analyze each code in each cell, and finally replace that code with the full training name using the table in E1:F4.

Below is the formula that will do this:

\=REDUCE(B2:B11,E2:E5,LAMBDA(a,v,SUBSTITUTE(a,v,XLOOKUP(v,E2:E5,F2:F5))))

![Reduce formula to do bulk find and replace](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202040%20998'%3E%3C/svg%3E)

Let me explain what’s happening in this formula.

*   B2:B11 – this range acts as the initial value. Since this is a range, the formula is going to go through the entire reduce function multiple times, one for each cell in this range.
*   E2:E5 – this is the range that will act as the current value for each iteration.
*   LAMBDA(a,v,SUBSTITUTE(a,v,XLOOKUP(v,E2:E5,F2:F5)))
    *   a – this is the accumulator value which starts with the value in cell B2.
    *   v – this is the current value (where the formula would process each cell in E2:E5)
    *   SUBSTITUTE(a,v,XLOOKUP(v,E2:E5,F2:F5)) – this is where the magic happens. This formula goes through each cell in the range E2:E5 and makes the susbtitution in the accumulator value.

Since I’m using B2:B11 as the initial\_value argument, the entire formula is run for each cell in this range, and the result is returned as an array that spills across the column.

Note: If this formula confuses you, just replace B2:B11 with B2 and see what you get. It will give you the result in one single cell only for the cell B2. And if then replace B2 with B2:B11, it’ll give you the results for all the cells in this range

In this article, I’ve covered how to use the REDUCE function and covered some basic as well as advanced examples.

I hope you found this article helpful.

_Below are some other Excel articles you may find useful:_

*   [10 VLOOKUP Examples For Beginner & Advanced Users](https://trumpexcel.com/excel-vlookup-function/)
    
*   [20 Advanced Excel Functions and Formulas (for Excel Pros)](https://trumpexcel.com/advanced-excel-functions-formulas/)
    
*   [Split Text into Multiple Rows in Excel](https://trumpexcel.com/split-text-to-rows-excel/)
    
*   [MAP Function in Excel (6 Examples)](https://trumpexcel.com/excel-functions/map-function/)
    

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