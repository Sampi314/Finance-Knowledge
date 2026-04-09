# Do You Choose to Use CHOOSE?

**Source:** https://sumproduct.com/thought/do-you-choose-to-use-choose/

---

[Home](https://sumproduct.com/)

\> Do You Choose to Use CHOOSE?

*   May 14, 2025

Do You Choose to Use CHOOSE?
============================

How to use the CHOOSE function in Excel.

Do You Choose to Use CHOOSE?
============================

Introduction
------------

_As a professional modeller, FCA and Excel MVP **Liam Bastick** highlights some of the more useful functions for financial modelling / Excel spreadsheeting. Here’s one you might **CHOOSE**…_

The Choice is Yours
-------------------

Do you choose to use **CHOOSE**? This function uses **index\_num** to return a value from the list of value arguments. **CHOOSE** may be used to select one of up to 254 values based on the index number (**index\_num**). For example, if **value1** through **value7** are the days of the week, **CHOOSE** returns one of the days when a number between 1 and 7 is used as **index\_num**.

The **CHOOSE** function employs the following syntax to operate:

**CHOOSE(index\_num, value1, \[value2\])**

The **CHOOSE** function has the following arguments:

*   **index\_num:** this is required and is used to specify which value argument is to be selected. **Index\_num** must be a number between 1 and 254, or a formula or reference to a cell containing a number between 1 and 254.
    *   if **index\_num** is 1, **CHOOSE** returns **value1**; if it is 2, **CHOOSE** returns **value2**; and so on
    *   if **index\_num** is less than 1 or greater than the number of the last value in the list, **CHOOSE** returns the _#VALUE!_ error value
    *   if **index\_num** is a fraction, it is truncated to the lowest integer before being used.
*   **value1**, **value2**, …: **value 1** is required, but subsequent values are optional. There may be between 1 and 254 value arguments from which **CHOOSE** selects a value or an action to perform based on **index\_num**. The arguments can be numbers, cell references, defined names, formulas, functions, or text.

It should be further noted that:

*   If **index\_num** is an array, every value is evaluated when **CHOOSE** is evaluated
*   The value arguments to **CHOOSE** can be range references as well as single values.

For example, the formula:

**\=SUM(CHOOSE(2,A1:A10,B1:B10,C1:C10))**

evaluates to:

**\=SUM(B1:B10)**

which then returns a value based on the values in the range **B1:B10**.

The **CHOOSE** function is evaluated first, returning the reference **B1:B10**. The **SUM** function is then evaluated using **B1:B10**, the result of the **CHOOSE** function, as its argument. A similar idea is also expressed by the formula

**\=SUM(A1:CHOOSE(2,A2,A3,A4))**

which will return the result of **\=SUM(A1:A3)**.

Certainly it is a function used in modelling, but perhaps it is not used as regularly as some others. This is useful for non-contiguous references:

![](<Base64-Image-Removed>)

Just so that we are clear on jargon: a **non-contiguous** range (with reference to Excel) means a range that cannot be highlighted with the mouse alone. In the image above, to highlight the cells coloured you would have to press down the **CTRL** key as well.

**INDEX**, **LOOKUP**, **VLOOKUP** and **HLOOKUP** all require contiguous references. They refer to lists, row vectors, column vectors and / or arrays. **CHOOSE** is different:

**\=CHOOSE(index\_num, value1, \[value2\]…)**

As explained above ,this function allows references to different calculations, workbook / worksheet references, _etc_. Try to use the function appropriately. For instance, a well-known Excel website proposes the following formula for calculating the US Thanksgiving date. Assuming cell **A1** has the year:

**\=DATE(A1,11,CHOOSE(WEEKDAY(DATE(A1,11,1)),26,25,24,23,22,28,27))**

To understand this formula, note that **DATE(Year,Month,Day)** returns a date and **WEEKDAY(Date)** returns a number 1 (Sunday) through 7 (Saturday). But doesn’t this formula look horrible? It is full of hard code and it contains an unnecessary number of arguments. The formula could exclude **CHOOSE** _viz_.

**\=DATE(A1,11,28-MOD(WEEKDAY(DATE(A1,11,1))+1,7))**

Now let me be clear here. I am not saying this is a simple, transparent formula. Test it. They both provide the same answer. **CHOOSE** – and plenty of additional hard code – has been used unnecessarily.

That’s not to say there isn’t a time and a place for **CHOOSE**. It is useful when you need to refer to cells on different worksheets or in other workbooks. Some argue that it is useful when a calculation needs to be computed using different methods, _e.g._

**\=CHOOSE(index\_num, calculation1, calculation2, calculation3, calculation4)**

I disagree. Let me explain. In the example below, I have created a lookup table in cells **E10:E13** which I have called **Data** (I will explain how to create range names later). The calculations are all visible on the worksheet, rather than hidden away in the formula bar. The **index\_num** selection, here referred to as **Selection\_Number**, is input in cell **E2**. The result?

![](<Base64-Image-Removed>)

It’s identical, but easier to follow

**\=INDEX(Data,Selection\_Number)**

I have taught financial modelling to many gifted analysts over the years and a common mistake made by many is that they build models that are easy to build rather than _models that are easy to understand_. The end user is the customer. It should be simple to use: taking shortcuts invariably only helps the modeller – and even then, more often than not, shortcuts will backfire.

**CHOOSE** can lead to opaque models that need to be rebuilt and are often less flexible to use. You have been warned!

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/do-you-choose-to-use-choose/#0)
    
*   [Register](https://sumproduct.com/thought/do-you-choose-to-use-choose/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/do-you-choose-to-use-choose/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/do-you-choose-to-use-choose/#0)

[](https://sumproduct.com/thought/do-you-choose-to-use-choose/#0 "close")

top