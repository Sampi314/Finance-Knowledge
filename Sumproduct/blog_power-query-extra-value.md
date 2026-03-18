# Power Query: Extra Value

**Source:** https://sumproduct.com/blog/power-query-extra-value/

---

[Home](https://sumproduct.com/)

\> Power Query: Extra Value

*   March 19, 2019

Power Query: Extra Value
========================

Power Query: Extra Value
========================

20 March 2019

_Welcome to our Power Query blog. This week, I look at some more Value M functionality._

Last week [Power Query: Value Added](https://www.sumproduct.com/blog/article/power-query-blogs/power-query-value-added)
, I looked at the **M** functions **Value.Is()** and **Value.FromText()**. This week, I will look at additional **M** functionalities that use **Value()**. To start, I begin with

Value.As(**value** as any, **type** as type) as any

where **value** is the data being analysed and **type** is the data type being tested for.

In the Microsoft help pages, **Value.As()** is described as follows:

**Value.As** is the function corresponding to the **as** operator in the formula language. The expression **value as type** asserts that the value of a **value** argument is compatible with **type** as per the **is** operator. If it is not compatible, an error is raised.

The difference between **Value.As()** and **Value.Is()** is that the latter returns a logical, or Boolean (TRUE / FALSE) result, whereas the former either returns the value, or issues an error. I can demonstrate the difference in the following example:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-467.jpg)

The **M** code I have used for **Value.As()** is:

\= Value.As(Value.FromText(\[Column1\]), type number))

I have taken a mixed data column and tested for whether the data is a number. **Value.As()** has issued an error when the data cannot be a number, and returned the number when it is a valid number. In contrast, **Value.Is()** has returned TRUE for a valid number and FALSE if the data cannot be a valid number. Therefore, **Value.As()** could be useful when I want to remove rows that do not contain a valid number (by choosing the ‘Remove Errors’ option from the ‘Remove Rows’ section of the ‘Home’ tab).

Let’s move on. I will now consider

Value.Add(**value1** as any, **value2** as any, optional **precision** as nullable number) as any

where **value1** and **value2** are the values to be added, and the **precision** the values are considered to can be specified.

There are of course many ways of adding and merging columns, an example of how to use **Value.Add()** is shown on the next screenshot:

![](<Base64-Image-Removed>)

A quirk of **Value.Add()** is that it doesn’t deal with nulls:

![](<Base64-Image-Removed>)

This can be solved by replacing nulls with zeros before applying the **Value.Add()** functionality. Although **Value.Add()** will work for two values of type **any**, a result will only be given for valid numbers, otherwise an error is issued.

Next up is

Value.Divide(**value1** as any,  **value2** as any, optional **precision** as nullable number) as any 

where **value1** and **value2** are the values to be added, and the **precision** the values are considered to can be specified.

This is another way to divide one value by a second value:

![](<Base64-Image-Removed>)

Finally, for this week:

Value.Equals(**value1** as any, **value2** as any, **equater** as record) as logical  

where **value1** and **value2** are the values to be compared. The optional **equater** means that the user can define the conditions where the values would be equal.

Comparing values is often useful in calculations, and **Value.Equals()** is a logical function, but in this case not a Boolean operator, since more information is returned. If the first value is greater than the second value (according to the rules supplied in the **equater**_(sic)_, if present), then 1 is returned. If the values are the same, zero (0) is returned, and if the first value is less than the second value, -1 is returned.

As the next example shows, text and nulls can also be compared:

![](<Base64-Image-Removed>)

The characters in text values are compared by their position in the alphabet.

Come back next time for more ways to use Power Query!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-extra-value/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-extra-value/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-extra-value/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-extra-value/#0)

[](https://sumproduct.com/blog/power-query-extra-value/#0 "close")

top