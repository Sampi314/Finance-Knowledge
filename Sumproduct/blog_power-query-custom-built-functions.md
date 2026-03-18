# Power Query: Custom Built Functions

**Source:** https://sumproduct.com/blog/power-query-custom-built-functions/

---

[Home](https://sumproduct.com/)

\> Power Query: Custom Built Functions

*   September 12, 2017

Power Query: Custom Built Functions
===================================

Power Query: Custom Built Functions
===================================

13 September 2017

_Welcome to our Power Query blog. Today I create a simple function and show how to access it when building a query._

Last week, I looked at how to access and test the built-in Power Query functions. There are occasions, however, when I am repeatedly using the same logic, and I want to store it in a custom function of my own. Let’s take a look.

Back in [Uniting Different Types](https://sumproduct.com/blog/power-query-uniting-different-types/)
, I used some **M** code to combine two of my columns in the screenshot below:

![](<Base64-Image-Removed>)

If I often need to combine my columns in this way I can take my **M** code

**\= \[expense code\] & ” ” & Text.From(\[Expense Category\])**

and put it into a function of my own.

I begin by creating a blank query from my Excel worksheet:

![](<Base64-Image-Removed>)

Then, I need to access the Advanced Editor:

![](<Base64-Image-Removed>)

At the beginning of my function, I need to give it a name – I choose ‘**FormatExpenseType**‘. I need to define what parameters my function accepts (I’ve called them ‘**InText**‘ and ‘**InNumber**‘). Next, I apply my logic to combine the parameters and finish my function syntax by defining the output (‘**result**‘). I can specify a value for my function should I wish (I have chosen not to, but I still need the final line):

**let FormatExpenseType =(InText as text, InNumber as number)=>**

**let result =**  **InText & ” ” & Text.From(InNumber)**

**In result**

**In FormatExpenseType**

![](<Base64-Image-Removed>)

Once I have created my query, I can name it ‘**FormatExpenseType**‘, ready to use in other queries. I can test it first by clicking ‘Invoke’, or choose to ‘Close and Load’ from the ‘Home’ or ‘File’ tabs to store the function in my workbook.

![](<Base64-Image-Removed>)

Choosing to invoke creates a new query rather than adding an unnecessary step to my function:

![](<Base64-Image-Removed>)

My query is now shown as a function in my workbook, and hovering over it shows me the details behind it.

![](<Base64-Image-Removed>)

I can also choose to invoke from here, which would create a new query in exactly the same way as invoking from the Query Editor.

![](<Base64-Image-Removed>)

I am ready to call this function from my ‘**Table1**‘ query. First, I double click on ‘**Table1**‘. In the ‘Add Column’ tab in the Query Editor, I can ‘Invoke Custom Function’:

![](<Base64-Image-Removed>)

I am prompted to enter a new column name and select a function – in this case I can only see the one I have created.

![](<Base64-Image-Removed>)

This time, instead of values, I choose columns as my parameters:

![](<Base64-Image-Removed>)

I select the **_expense code_** and **_Expense Category_** columns.

![](<Base64-Image-Removed>)

I have deliberately used a query where I already have my original **_Expense Type_** column for comparison, so now I test my function:

![](<Base64-Image-Removed>)

The function works perfectly – and because it will work on any text and number column combination I could rename it to be more generic (_e.g._**FormatTextPlusNumber**) and use it for other columns.

Want to read more about Power Query? A complete list of all our Power Query blogs can be found [here](https://www.sumproduct.com/thought/power-query-blog-series)
. Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-custom-built-functions/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-custom-built-functions/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-custom-built-functions/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-custom-built-functions/#0)

[](https://sumproduct.com/blog/power-query-custom-built-functions/#0 "close")

top