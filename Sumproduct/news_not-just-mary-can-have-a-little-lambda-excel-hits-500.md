# Not Just Mary Can Have a Little LAMBDA / Excel Hits 500

**Source:** https://sumproduct.com/news/not-just-mary-can-have-a-little-lambda-excel-hits-500/

---

[Home](https://sumproduct.com/)

\> Not Just Mary Can Have a Little LAMBDA / Excel Hits 500

*   July 27, 2021

Not Just Mary Can Have a Little LAMBDA / Excel Hits 500
=======================================================

Not Just Mary Can Have a Little LAMBDA / Excel Hits 500
=======================================================

27 July 2021

_By Liam Bastick (SumProduct) and Chris Gross (Microsoft Program Manager)_

It’s busy times in the land of Excel 365 – if you want to live on the cutting edge. Microsoft has just announced the release of no less than seven new **LAMBDA**\-associated functions (including a landmark 500th one – someone please bake Excel a cake) for the Beta variant, whilst also moving the recently released **LAMBDA** function a step closer to becoming Generally Available.

It’s a lot to take in. Where do we start? Perhaps let’s begin with revisiting **LAMBDA** itself.

**_LAMBDA Moves to Excel 365 Current Channel Preview_**

For those who have been hiding under a rock, let me start by saying **LAMBDA** rocks _(if this continues, this will be a very short article – Ed.)_. Simply put, **LAMBDA** allows you to define your own custom functions using Excel’s formula language. It’s User Defined Functions without a PhD in VBA or JavaScript. Now moved to the Office 365 Current Channel Preview from Beta, **LAMBDA** allows you to define a custom function in Excel’s very own formula language. Moreover, one function can call another (including itself), so there is no limit to the power you can deploy with a single function call.

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-19.jpg)

As a reminder, the syntax of **LAMBDA** perhaps remains not the most informative:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-15.jpg)

That’s, er, great. Perhaps a run-through might be best.

There are three key pieces of **\=LAMBDA** to understand:

1\. **LAMBDA** function components

2\. Naming a lambda

3\. Calling a lambda function.

**_1\. LAMBDA function components_**

Let’s take a simple example. Consider the following formula:

**\=LAMBDA(x, x+1)**

This is a very exciting formula, where we have **x** as the argument, which you may pass in when calling the **LAMBDA**, and **x+1** is the logic / operation to be performed.

For example, if you were to call this lambda function and define **x** as equal to five (5), then Excel would calculate

5 + 1 = 6

Except it wouldn’t. If you tried this you would get _#CALC!_ Oops. That’s because it’s not _quite_ as simple as that. You need to name your little **LAMBDA**.

**_2\. Naming a LAMBDA_**

To give your **LAMBDA** a name so it can be re-used, you have to use the Name Manager (**CTRL + F3** / go to the Ribbon and then go to **Formulas -> Name Manager**):

![](<Base64-Image-Removed>)

Once you open the ‘Name Manager’ you will see the following dialog:

![](<Base64-Image-Removed>)

You then click on ‘New’ and fill out the related fields, _viz._

![](<Base64-Image-Removed>)

To be clear:

*   **Name:** the name of your function (this is where you name it!)
*   **Comment:** a description and associated ToolTip, which will be shown when calling your function
*   **Refers to:** your lambda function definition (this is where you put your formula – **_NOT_** in the Excel worksheet!).

Once completed, you may press ‘OK’ to store your lambda and you should see the definition returned in the resultant window.

![](<Base64-Image-Removed>)

**_3\. Calling LAMBDA_**

Now that you have done this, your first new lambda function may be called in just the same way as every other Excel function is cited, _e.g._

**\=MYLAMBDA(5)**

which would equal six (6) and not _#CALC!_ as before.

You DON’T have to do it this way though if you don’t want to. You may call a lambda without naming it. If we hadn’t named this marvellous calculation, and simply authored it in the grid as we had first attempted, we could call it by simply typing:

**\=LAMBDA(x, x+1)(5)**

![](<Base64-Image-Removed>)

The sky’s the limit. You are not restricted to just numbers and text. You can also use:

*   **Dynamic arrays:** rather than passing a single value into a function, you can pass an array of values, and functions can also return arrays of values
*   **Data Types:** the value stored in a cell is no longer just a string or a number. A single cell can contain a rich Data Type, with a large set of properties, as discussed previously.

Functions can take data types and arrays as arguments, and they can also return results as data types and arrays. The same is now true with the lambdas you build.

Indeed, formulaic recursion is possible too, such as creating a Triangle number

![](<Base64-Image-Removed>)

using the lambda formula

**\=LAMBDA(x, IF(x<2, 1, x + Triangle(x – 1)))**

Now, yes, I know you can use the calculation

**\= x \* (x + 1) / 2**

but nobody likes a smart alec! You get the point.

To celebrate **LAMBDA** moving to Current Channel Preview, Microsoft has also added support for optional parameters. To make use of these new take-them-or-leave-them arguments, all you need to do is wrap the optional name in square brackets, “**\[\]**”, _e.g._

**\=LAMBDA(arg1, \[arg2\], IF(ISOMITTED(arg2), arg1, arg2))**

(In case you have no idea what **ISOMITTED** does (I am sure you can guess!), don’t worry, it’s one of the new functions divulged below…)

Simply put, this lambda will return the value of **arg1** if **arg2** is omitted; otherwise, it will return the value of **arg2**. I’d like to have called this lambda function **Jason** as it sort of checks if his **arg**s are naught, but sadly it’s not Friday 13th…

The lambda function is available to members of the Current Channel Preview program running Windows and Mac builds of Excel, but is only available to a random 50% of users as at the time of writing. Microsoft has stated that they will increase this “flight”, pending no bugs or other issues.

**_Introducing the New LAMBDA Helper Functions_**

**LAMBDA** now enhances Excel’s formula language, with its ability to be treated as an accepted value type with the introduction of these new functions. This is an important concept, which has existed across many programming languages, and is tantamount to the concept of lambda functions in general, never mind just in Excel.

Recently, Excel has introduced new types of values. This has included Data Types (Wolfram, Geography, Stocks, Power BI and Power Query can create Data Types) and dynamic arrays. Lambdas continue these enhancements by allowing Excel to understand functions as a value. This was enabled by the introduction of **LAMBDA**, but it requires support, which is what these seven new functions bring.

This means that previous Excel tasks which previously seemed practically impossible, may now be achieved by writing a **LAMBDA** and passing it as a _value_ into another function.

Bring on the newbies…

**_BYCOL_**

**BYCOL** is not a region of the Philippines, but rather a function that takes an array or range and calls a lambda, with all the data grouped by each row or column and then returns an array of single values.

Its syntax is as follows:

**BYCOL(array, \[lambda\])**

It has the following arguments:

*   **array:** this is required, and represents an array to be separated by column
*   **lambda:** an optional argument, this is a **LAMBDA** that takes a column as a single parameter and calculates just one result.

As an example, my co-author Chris and I have decided to make small talk and discuss the _weather_ – in particular, _whether_ we use Celsius or Fahrenheit as our temperature scale. Chris uses Fahrenheit because he is based in the United States (more on this fact later) and I use Celsius because I am _right_.

I have made up some average monthly temperatures for Melbourne (Australia), not that it matters given we are all in Lockdown:

![](<Base64-Image-Removed>)

I have called this Excel Table **Temps**, but it is a permanent name…

For the years 2011 to 2020 inclusive, I want to provide a detailed monthly breakdown of temperatures where the average temperature for the year was above 15 degrees Celsius. At this point, you would normally calculate the average temperature for each column using a formula such as

**\=AVERAGE(Temps\[2011\])**

for column **C** of this example spreadsheet.

This would be a “helper row”, _e.g._

![](<Base64-Image-Removed>)

But I am not going to do it that way. Instead, let’s use **BYCOL**. First of all, let’s see how it works. Consider the calculation

**\=BYCOL(Temps, LAMBDA(column, SUM(column)))**

Note I have used **Temps** as my array, which is cells **B4:L15**, _i.e._ it omits the header row of the table (cells **B3:L3**). I have to ignore the headers because the years would be included in the column totals being numbers – a classic _gotcha_!

This would produce the following result:

![](<Base64-Image-Removed>)

**BYCOL** produces a row vector, summing up each column of the table **Temps**, excluding the header row. The formula spills, using dynamic array logic and matches the width of the underlying array (_i.e._ the Table **Temps**). It only produces one row of data, as we have created a summation (just one value to report for each column).

Now, let’s consider the following formula:

**\=FILTER(Temps, BYCOL(Temps, LAMBDA(year, AVERAGE(year) > 15)))**

Here, **BYCOL** produces a row of TRUE or FALSE values, depending upon whether the average for each column exceeds 15 degrees Celsius. The dynamic array function **FILTER**, one of the recently introduced dynamic array functions then filters each column in **Temps** based upon whether the corresponding **LAMBDA** equates to TRUE or FALSE, _viz._

![](<Base64-Image-Removed>)

This returns the columnar data for the years 2013, 2014, 2016, 2017 and 2020 respectively – not that you would know from the above numerical dataset. I really wanted the headings, but having numerical values in the Table header did not help my cause (it would have caused my averages to calculate incorrectly). It is usually not a good idea to have numerical values in Table headers, and perhaps now you can understand why.

If I modify the Table’s headers as follows, I can now use the _entire_ Table:

![](<Base64-Image-Removed>)

The formula may be modified to

**\=FILTER(Temps\[#All\], BYCOL(Temps\[#All\], LAMBDA(year, AVERAGE(year) > 15)))**

which will produce a more informative spilled array:

![](<Base64-Image-Removed>)

**_BYROW_**

**BYROW** works very similarly to **BYCOL** (it is analogous to the relationship between **HLOOKUP** and **VLOOKUP**). This function applies a **LAMBDA** to each row and returns an array of the results. Its syntax is as follows:

**BYROW(array, \[lambda\])**

It has the following arguments:

*   **array:** this is required, and represents an array to be separated by row
*   **lambda:** an optional argument, this is a **LAMBDA** that takes a column as a single parameter and calculates just one result.

Let’s return to my above example:

![](<Base64-Image-Removed>)

**BYROW** effectively produces a column vector, summing up each row of the table **Temps**.

If I want the year-on-year comparisons for each month where the average temperature is above 15 degrees Celsius, I can again avoid using a “helper column” and instead use the formula

**\=FILTER(Temps, BYROW(Temps, LAMBDA(year, AVERAGE(year) > 15)))**

This time, I can ignore the header row. This will return the array

![](<Base64-Image-Removed>)

Once you get the hang of these **LAMBDA** helper functions, you will begin to wonder how you ever managed without them.

**_ISOMITTED_**

This new function checks whether the value is missing, and returns either TRUE (value is missing) or FALSE (value is not missing) accordingly. The syntax is simple:

**ISOMITTED(argument)**

where:

*   **argument** is a required parameter, and is the value you want to test, which may be based upon a **LAMBDA**.

The example

**\=LAMBDA(arg1, \[arg2\], IF(ISOMITTED(arg2), arg1, arg2))**

was provided earlier, where this lambda will return the value of **arg1** if **arg2** is omitted; otherwise, it will return the value of **arg2**.

**_MAKEARRAY_**

**MAKEARRAY** returns a calculated array of a specified row and column size, by applying a **LAMBDA** function. This function is useful for situations where you wish to combine or transform arrays, as well as being useful for generating data. The syntax is as follows:

**MAKEARRAY(rows, columns, lambda)**

It has the following arguments:

*   **rows:** this argument is required and represents the number of rows in the array (which must be greater than zero)
*   **columns:** this argument is also required and represents the number of columns in the array (which again must be greater than zero)
*   **lambda:** also necessary, this is the **LAMBDA** that is called to create the array. In particular, this lambda function must take two parameters, namely:
    *   **row\_index:** the index of the row (row number)
    *   **column\_index:** the index of the column (column number).

As an example, consider the following:

![](<Base64-Image-Removed>)

Imagine, for reasons best known to myself, I wanted to generate an array of colours of the rainbow (albeit with the final colour, ahem, slightly amended). In the image above, I have specified the number of rows (cell **D2**) and the number of columns (cell **D3**) in my array, and listed the colours in cells **B6:B12** inclusive.

The formula in cell **E6** is given by

**\=MAKEARRAY(D2, D3, LAMBDA(row, column, INDEX(B6:B12, RANDBETWEEN(1, 7))))**

The first two arguments in this formula are **D2** and **D3**, which refer to the number of rows and columns for the array to be generated respectively. The final argument of **MAKEARRAY** is the **LAMBDA**, which must take two parameters, corresponding to the value generated by LAMBDA, namely:

*   **row:** the index of the row
*   **column:** the index of the column.

The calculation thus uses the non-dynamic array function RANDBETWEEN to generate an integer between one \[1\] and seven \[7\] to select from the list of colours of the rainbow, stipulated in cells B6:B12. For example, if Excel generates the number 5, the value “Blue” will be chosen, _etc_.

Now it is true that existing functions could be used to achieve the same result, _e.g._

**\=INDEX(B6:B12, RANDARRAY(D2, D3, 1, 7, TRUE))**

This formula seems shorter and simpler, and indeed, may be the better option for this above illustration. But that is exactly what this is – a simple example. As more complex arrays need to be created, existing function counterparts may prove difficult, convoluted or impossible to construct – and this is precisely where **MAKEARRAY** and **LAMBDA** come in.

**_MAP_**

Ladies and gentlemen, may I welcome to the fore, **Excel’s 500th function** – as agreed by fellow Excel Most Valuable Professional (MVP) Bill Jelen and yours truly.

If you are giddy from this amazing fact, do be aware that the **MAP** function does not actually return a map!

Instead, it returns an array formed by mapping each value in the array(s) to a new value and applying a **LAMBDA** to create a new value accordingly. It has the following syntax:

**MAP(array1, lambda** _or_ **array2, \[lambda** _or_ **array2, …\])**

where:

*   **array1:** this is a required argument and represents the (first) array to be mapped
*   **array2 and subsequent arrays:** these are optional arguments and represent additional arrays to be mapped
*   **lambda:** this is a required argument which represents a **LAMBDA** which must be the final argument and must have a parameter for each array passed or another array to be mapped.

In short, **MAP** transforms values. Let’s return to my Melbourne temperatures data:

![](<Base64-Image-Removed>)

The formula

**\=FILTER(Temps, BYROW(Temps, LAMBDA(year, AVERAGE(year) > 15)))**

which returned the array

![](<Base64-Image-Removed>)

The problem is, these temperatures have all been provided in Celsius, which my co-author Chris doesn’t really understand. If he sees a temperature of 25 degrees, he will be breaking out the gloves, bobble hat and duffle coat, whereas us Aussies will be heading for the beach.

We need to convert – **_transform_** – this data to Fahrenheit, so our US colleagues may better understand. All I need to do is wrap the above formula in a **MAP** function:

**\=MAP(FILTER(Temps, BYROW(Temps, LAMBDA(year, AVERAGE(year) > 15))),  
LAMBDA(temperature, IF(ISNUMBER(temperature),  
CONVERT(temperature, “C”, “F”), temperature)))**

![](<Base64-Image-Removed>)

**CONVERT(temperature, “C”, “F”)** simply converts the variable **temperature** from degrees Celsius to degrees Fahrenheit. This is wrapped in an **IF(ISNUMBER())** check to ensure that we don’t try to convert text values (as this would cause an error): the **IF** statement leaves the value of **temperature** “as is” in this instance, and **LAMBDA** just wraps around all of this in order to declare the variable **temperature** “work”, so that **MAP** may do its work.

It’s true you could generate this result in stages, but the whole idea of these **LAMBDA** helper functions is to be able to create dynamic arrays in one fell swoop.

**_REDUCE_**

This penultimate function reduces an array to an accumulated value by applying a **LAMBDA** function to each value and returning the total value in what is known as the **accumulator**. Its syntax is as follows:

**REDUCE(\[initial\_value\], array, lambda)**

where:

*   **initial\_value:** this is an optional argument and represents the starting value for the **accumulator**, _i.e_. the “running total” prompted by the **lambda** expression
*   **array:** this is a required value and represents the array to be reduced
*   **lambda:** this is also a required value and represents a **LAMBDA** function called to reduce the **array**, that consists of two parameters:
    *   **accumulator:** the returned (aggregated) value from **LAMBDA**
    *   **value:** a value from **array**.

Returning to our temperature example given by the Excel Table **Temps**:

![](<Base64-Image-Removed>)

we could count how many months in the 10-year period had an average temperature between 15 and 20 degrees Celsius as follows:

**\=REDUCE(0, Temps, LAMBDA(accumulator, value,  
IF(AND(value >= 15, value <= 20), 1 + accumulator, accumulator)))**

For each element of the **Temps** Table, defined by the **LAMBDA** function as **value**, the **IF** statement tests whether the temperature is between 15 and 20 degrees Celsius:

**AND(value >= 15, value <= 20)**

If this is true, one gets added to the running total (**accumulator**), so that a count is maintained. The first argument of **REDUCE** – zero \[0\], the optional argument – simply specifies the starting value (**initial\_value**) for the **accumulator**, which must be zero in order for the count to make sense.

Again, we could create a second **array** which performs a corresponding check for each cell and count the TRUE values, but this formula _reduces_ the workload (_i.e._ it reduces the **array** of values to just one value by making use of the specified **LAMBDA**), allowing the computation to be performed once again without any helper stages.

**_SCAN_**

This final function scans an array by applying a **LAMBDA** to each value and returns an array that has each intermediate value. The syntax is as follows:

**SCAN(\[initial\_value\], array, lambda)**

where:

*   **initial\_value:** this is an optional argument and represents the starting value for the **accumulator**, _i.e_. the “running total” prompted by the **lambda** expression
*   **array:** this is a required value and represents the array to be scanned
*   **lambda:** this is also a required value and represents a **LAMBDA** function called to scan the **array**, that consists of two parameters:
    *   **accumulator:** the returned (aggregated) value from **LAMBDA**
    *   **value:** a value from **array**.

As a simple example, let’s consider a common problem when working with structured references, _i.e._ Excel Tables. Imagine I have the following sales for the first six months of the year:

![](<Base64-Image-Removed>)

I might wish to create a running total of these sales. One way I have seen people do this is as follows:

![](<Base64-Image-Removed>)

This is a horrible “hotch potch” of a formula:

**\=N(C1) + \[@Sales\]**

It mixes Excel cell referencing (cell **C1**, because you cannot refer to a value for a different record simply in an Excel Table), structured referencing (**\[@Sales\]**) and the **N** function, in order to treat the numerical value of text as zero \[0\] and therefore avoid _#VALUE!_ errors when adding amounts together.

It seems to work if values are added:

![](<Base64-Image-Removed>)

However, it all goes pear shaped when values are inserted:

![](<Base64-Image-Removed>)

This is where **SCAN** comes to the rescue. Assuming the Table is also called **Sales** (not just the field in column **B**), we can create the formula

**\=SCAN(0, Sales\[Sales\], LAMBDA(accumulator, value, accumulator + value))**

**SCAN** “scans” the array (_i.e._ the Excel Table **Sales**) by applying a **LAMBDA** to each value. It then returns an array of results corresponding to the accumulator value returned by the **LAMBDA**. As stated above, **SCAN** takes two parameters:

*   **accumulator:** the initial value returned by **SCAN** and each **LAMBDA** call
*   **value:** a **value** from the supplied **array**.

As above, the **initial\_value** is zero \[0\] so that the running total calculates correctly.

![](<Base64-Image-Removed>)

**_Word to the Wise_**

These functions will not be for everyone, in more ways than one. There are two key points:

1.  The concepts discussed here revolve around the notion of lambda functions, which may not be relevant to all users, especially for those that use Excel for “simple” tasks. But don’t let it scare or deter you from experimenting with these functions
2.  These new functions are only available presently to _c._ 50% of Office Insiders users running Beta Channel Version 2108 (Build 14312.20008) or later on Windows, or Version 16.52 (Build 21072100) or later on Mac. The **LAMBDA** function is now available to Office Insiders running Current Channel Preview Version 2107 (Build 14228.20154) or later on Windows, or Version 16.51 (Build 21071101) or later on Mac.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/not-just-mary-can-have-a-little-lambda-excel-hits-500/#0)
    
*   [Register](https://sumproduct.com/news/not-just-mary-can-have-a-little-lambda-excel-hits-500/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/not-just-mary-can-have-a-little-lambda-excel-hits-500/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/not-just-mary-can-have-a-little-lambda-excel-hits-500/#0)

[](https://sumproduct.com/news/not-just-mary-can-have-a-little-lambda-excel-hits-500/#0 "close")

top