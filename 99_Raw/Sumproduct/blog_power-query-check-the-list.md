# Power Query: Check the List

**Source:** https://sumproduct.com/blog/power-query-check-the-list/

---

[Home](https://sumproduct.com/)

\> Power Query: Check the List

*   November 5, 2019

Power Query: Check the List
===========================

Power Query: Check the List
===========================

6 November 2019

_Welcome to our Power Query blog. This week, we look at ‘remove error’ for lists._

The next screen shows a very simple list with just one problem:

![](https://sumproduct.com/wp-content/uploads/2025/05/e774d10cbbb9450fc45efbe51abdf434-333.jpg)

There is an error. My ‘Manage Items’ section allows me to add and remove items (I have expanded the latter to show that errors are not an option), or remove duplicates – but there is no function for removing errors.

One way I can tackle this is to ‘Convert to Table’ and transform my data.

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-337.jpg)

I accept the defaults.

![](https://sumproduct.com/wp-content/uploads/2025/05/f1140ff857fc3b6f5f97a6a24f4a6fc7-322.jpg)

Now, when I look at the options to ‘Remove Rows’, I can see that I can ‘Remove Errors’ if I wish. I do this.

![](https://sumproduct.com/wp-content/uploads/2025/05/72aa864d2854c6fefb1083fba0ab5792-296.jpg)

On the ‘Transform’ tab, I have the option to ‘Convert to List’:

![](https://sumproduct.com/wp-content/uploads/2025/05/36776d1da4d05b45bb5a5d09375f407c-253.jpg)

I now have my list without the errors, but it has taken three steps to achieve this:

**#”Converted to Table” = Table.FromList(Column1, Splitter.SplitByNothing(), null, null, ExtraValues.Error),**

**#”Removed Errors” = Table.RemoveRowsWithErrors(#”Converted to Table”, {“Column1”}),**

**Column2 = #”Removed Errors”\[Column1\]**

I’d like to be able to do this in one step. In order to achieve this, I need to use three **List() M** code functions. The first one is:

List.Transform(**list** as list, **transformation** as function)  as list

This performs the transformation on each item in the **list** and returns the new **list**.

In this case, the transformation will use the next **M List()** function:

List.Positions(**list** as list) as list

This function returns a list of offsets for the input **list**. When using **List.Transform** to change a **list**, the **list** of positions can be used to give the transform access to the position.

Finally, I will use **List.RemoveNulls()** to tidy up my list.

List.RemoveNulls(**list** as list) as list

This removes all occurrences of null values in the **list**. If there are no null’ values in the list, the original **list** is returned. (Ideally there would be a **List.RemoveErrors()** that looks a lot like this, but not yet!)

I will combine these functions to give the following step:

**\= List.RemoveNulls(List.Transform(List.Positions(Column1),each try Column1{\_} otherwise null))**

(**Column1** is the previous step defining my list.)

![](<Base64-Image-Removed>)

This has removed the error in one step without needing to convert my list to a table.

_Come back next time for more ways to use Power Query!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/power-query-check-the-list/#0)
    
*   [Register](https://sumproduct.com/blog/power-query-check-the-list/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/power-query-check-the-list/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/power-query-check-the-list/#0)

[](https://sumproduct.com/blog/power-query-check-the-list/#0 "close")

top