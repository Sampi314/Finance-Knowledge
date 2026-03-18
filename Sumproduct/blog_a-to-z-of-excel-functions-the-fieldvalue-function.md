# A to Z of Excel Functions: The FIELDVALUE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldvalue-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The FIELDVALUE Function

*   May 19, 2019

A to Z of Excel Functions: The FIELDVALUE Function
==================================================

A to Z of Excel Functions: The FIELDVALUE Function
==================================================

20 May 2019

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **FIELDVALUE** function._

**The FIELDVALUE function**

There’s some exciting news for those using Excel 2016 on an Office 365 basis (_i.e._ not the “perpetual licence”). You might not have this initially, but don’t fret. According to Microsoft, this feature is being made available to users on a “gradual basis” over several days or weeks. I t will first be available to Office Insider participants and later to Office 365 subscribers. If you are an Office 365 subscriber and you want it is as soon as it becomes available, do ensure you have the latest version of Office at all times (keep those updates updated!).

So what’s the big deal?

For a start, you can now get stock and geographic data in Excel. All you have to do is type text into a cell and convert it into the ‘Stocks’ data type or the ‘Geography’ data type. These two data types are new, and they are considered linked data types because they have a connection to an online data source. That connection allows you to bring back rich information that you can work with and refresh. You know – the things you have wanted to do for years!

Here’s a peek at the two new data types:

**_Data Type 1: Stocks_**

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-428.jpg)

In this graphic, the cells with company names in column **A** contain the ‘Stocks’ data type. You may tell this because they have this icon:

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-443.jpg)

The ‘Stocks’ data type is connected to an online source that contains more information. Columns **B** and **C** are extracting that information. Specifically, the values for price and change in price are getting extracted from the ‘Stocks’ data type in column **A**.

**_Data Type 2: Geography_**

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-416.jpg)

In this example, column **A** contains cells that have the ‘Geography’ data type. Indicated by the following icon:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-428.jpg)

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-385.jpg)

This data type is connected to an online source that contains more information. Columns **B** and **C** are again extracting that information. Specifically, the values for population and gasoline price are getting extracted from the ‘Geography’ data type in column **A**.

We are sure you can see how these data types might be useful. So how do you set it up? Assuming you have had your version of Excel 2016 updated, it’s as easy as, er, 1, 2, 3, 4, 5, 6…

**_Step 1: Type Some Text_**

![](<Base64-Image-Removed>)

That’s right: just type some text in cells. In this example, we wanted data based on geography, so we typed country names. However, you could also have typed province names, territories, states, cities, _etc._ If you want stock information, similarly type company names, fund names, ticker symbols, and so on.

**_Step 2: Create a Table_**

![](<Base64-Image-Removed>)

Although it’s not required, it is recommended you create an Excel Table. This is so ranges may be extended readily and easily later, should you wish. Select any cell in your data and go to **Insert > Table** or use the keyboard shortcut **CTRL + T**. This will make extracting online information easier later on.

**_Step 3: Select Some Cells_**

![](<Base64-Image-Removed>)

Next, select the cells that you want to convert to a data type.

**_Step 4: Pick a Data Type_**

![](<Base64-Image-Removed>)

On the ‘Data’ tab, click either ‘Stocks’ or ‘Geography’.

**_Step 5: Icons Appear_**

![](<Base64-Image-Removed>)

If Excel finds a match between the text in the cells and the online sources, it will convert your text to either the ‘Stocks’ data type or ‘Geography’ data type. You will know immediately if they have been converted since they will have the

![](<Base64-Image-Removed>)

icon for stocks and the

![](<Base64-Image-Removed>)

icon for geography.

**_Step 6: Add a Column_**

![](<Base64-Image-Removed>)

Click the ‘Add Column’ button:

![](<Base64-Image-Removed>)

, and then click a field name to extract more information, such as ‘Population’.

If you see the:

![](<Base64-Image-Removed>)

symbol instead of an icon, then Excel is having difficulty matching your text with data in Microsoft’s online sources. Go back and review your data. Correct any spelling mistakes and when you press **ENTER**, Excel will do its best to find matching information. If this does not work, click:

![](<Base64-Image-Removed>)

and a ‘Selector’ pane will appear. Search for data using a keyword or two, choose the data you want and then click ‘Select’. That’s it!

**_How to Write Formulae that Reference Data Types_**

You can use formulae that reference linked data types. This allows you to retrieve and expose more information about a specific linked data type. For example, consider the linked data type, Stocks, used in cells **A2:A11** below. In columns **B** and **C**, there are formulae that extract more information from the ‘Stocks’ data type in column **A**, _viz._

![](<Base64-Image-Removed>)

In this example, cell **B2** contains the formula **\=A2.Price**? and cell **C2** contains the formula =**A2.Change**. When the records are in a Table, you can use the column names in the formula instead. In this case, cell **B2** would contain the formula **\=\[@Company?\].Price** and cell **C2** would contain **\=\[@Company\].Change**. The additional benefit is that these formulae would automatically copy down too.

Some tips for when you start playing with these two new data types:

*   as soon as you type the dot operator (**.**) after a cell or column reference, Excel will present you with a formula AutoComplete list of fields that you can reference for that data type. Select the field you want from the list or type it if you know it

![](<Base64-Image-Removed>)

*   data type field references are not case sensitive, so you can enter =**A2.Price**, or **\=A2.price**
*   if you select a field that has spaces in the name, Excel will automatically add brackets (**\[ \]**) around the field name, _e.g._**\=A2.\[52 Week High\]**
*   the **FIELDVALUE** function can also be used, but it is recommended only for creating conditional calculations based on linked data types.

This last point is a nice lead into the other new item…

**_The FIELDVALUE Function_**

You can use the **FIELDVALUE** function to retrieve field data from linked data types like the ‘Stocks’ or ‘Geography’ data types. There are easier methods for writing formulae that reference data types _(see above)_, so the **FIELDVALUE** function should be used mainly for creating conditional calculations based on linked data types.

Similar to the new data types, this brand-new function is being made available to customers on a gradual basis over several days or weeks. It will first be available to Office Insider participants and later to Office 365 subscribers. If you are an Office 365 subscriber, make sure you have the latest version of Office or you may not get the update when it’s your turn.

**_Technical details_**

_Syntax_

**\=FIELDVALUE(value, field\_name)**

The **FIELDVALUE** function syntax has the following arguments:

*   **value**: this is the cell address, table column or named range that contains a linked data type
*   **field\_name**: this is the name or names of the fields you would like to extract from the linked data type.

_Description_

The **FIELDVALUE** function returns all matching fields(s) from the linked data type specified in the value argument. This function belongs to the **Lookup & Reference** family of functions.

**_Examples_**

In the following basic example, the formula, **\=FIELDVALUE(A2,”Price”)** extracts the **Price** field from the ‘Stock’ data type for the “internationally-renowned” JM Smucker Co.

![](<Base64-Image-Removed>)

The next example is a more typical example for the **FIELDVALUE** function. Here, we’ve used the **IFERROR** function to check for errors. If there isn’t a company name in cell **A2**, the **FIELDVALUE** formula returns an error, and in that case, displays nothing (**“”**). However, if there is a company name, then we want the formula to retrieve the **Price** from the data type in **A2** with **\=IFERROR(FIELDVALUE($A2,B$1),””)**.

![](<Base64-Image-Removed>)

Note that the **FIELDVALUE** function allows you to reference worksheet cells for the **field\_name** argument, so the above formula references cell **B1** for **Price** instead of manually entering “Price” in the formula.

If you try to retrieve data from a non-existent data type field, the **FIELDVALUE** function will return the new _#FIELD!_ error. For instance, you might have entered “Prices”, when the actual data type field is named “Price”. Double-check your formula to make sure you’ve used a valid field name. If you want to display a list of field names for a record, select the cell for the record and press **CTRL + SHIFT + F2**.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._

_A full page of the function articles can be found here._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldvalue-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldvalue-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldvalue-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldvalue-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-fieldvalue-function/#0 "close")

top