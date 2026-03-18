# Copy Values from Discontinuous Ranges to Specific Ranges

**Source:** https://sumproduct.com/thought/copy-values-from-discontinuous-ranges-to-specific-ranges/

---

[Home](https://sumproduct.com/)

\> Copy Values from Discontinuous Ranges to Specific Ranges

*   October 11, 2019

Copy Values from Discontinuous Ranges to Specific Ranges
========================================================

VBA Blogs: Copy Values from Discontinuous Ranges to Specific Ranges
===================================================================

11 October 2019

_Welcome back to the VBA blog. This week, we are going to introduce a method to copy values from discontinuous ranges to other specific regions._

Today, we are going to create VBA script to copy values from discontinuous ranges and paste them to other specific ranges. It is a useful method to automate updating values in certain instances.

For our example, let’s say we want to copy the values from the right sections to the left sections as shown below:

![](https://sumproduct.com/wp-content/uploads/2025/06/e774d10cbbb9450fc45efbe51abdf434-719.jpg)

The result would look like this:

![](https://sumproduct.com/wp-content/uploads/2025/06/f32e5a15e2cf9c3e4d2d058458ce054d-825.jpg)

If we copy the values from the right section directly, Excel will show that multiple selections are not allowed in this case, as shown by the prompt _(below)_:

![](https://sumproduct.com/wp-content/uploads/2025/06/f1140ff857fc3b6f5f97a6a24f4a6fc7-735.jpg)

However, we can circumvent this problem using VBA code.

The first step is to define named ranges for the copy and paste ranges. In this case, we define multiple ranges **$K$3:$O$8** and **$J$11:$N$16** as **copyrng**, as shown below. The ranges here are simply the raw data to be copied.

![](https://sumproduct.com/wp-content/uploads/2025/06/72aa864d2854c6fefb1083fba0ab5792-682.jpg)

Similarly, we define the ranges to be pasted as **pasterng** with the region **$C$3:$G$8** and **$B$11:$F$16**, as shown below:

![](https://sumproduct.com/wp-content/uploads/2025/06/36776d1da4d05b45bb5a5d09375f407c-580.jpg)

Then we define the relevant variables:

Dim i, j As Integer

Dim ncount As String

The next step is to allocate the address of the named range **pasterng** to variable **ncount**. The **Range.Address** property returns a string value that represents the range reference. In this case, the range reference of **$C$3:$G$8** and **$B$11:$F$16** is assigned to variable **ncount**.

ncount = Range(“pasterng”).Address

Then, we use the variable **ncount** to calculate the numbers of commas stored in the address reference. The number of commas represent the number of range references. We use the **Len** function to find the length of the string value, then we use the **Substitute** function to remove the comma in the string and assign the difference of the two lengths to variable **i**.

i = Len(ncount) – Len(Application.WorksheetFunction.Substitute(ncount, “:”, “”))

After this step, we use the ‘For loop’ to loop through each area property stored in ranges and set the value in **pasterng** same as **copyrng**. **Range.Areas** returns an **Areas** collection that represents all the ranges in a multiple-area selection.

For j = 1 To i

  Range(“pasterng”).Areas(j).Value = Range(“copyrng”).Areas(j).Value

Next

Combing all the lines of code together, we get this:

Sub CopyRange()

Dim i, j As Integer

Dim ncount As String

ncount = Range(“pasterng”).Address

i = Len(ncount) – Len(Application.WorksheetFunction.Substitute(ncount, “:”, “”))

For j = 1 To i

  Range(“pasterng”).Areas(j).Value = Range(“copyrng”).Areas(j).Value

Next

End Sub

By using this method, we can copy the value from discontinuous ranges to another specific region automatically.

See you next week for more VBA tips!

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/thought/copy-values-from-discontinuous-ranges-to-specific-ranges/#0)
    
*   [Register](https://sumproduct.com/thought/copy-values-from-discontinuous-ranges-to-specific-ranges/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/copy-values-from-discontinuous-ranges-to-specific-ranges/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/copy-values-from-discontinuous-ranges-to-specific-ranges/#0)

[](https://sumproduct.com/thought/copy-values-from-discontinuous-ranges-to-specific-ranges/#0 "close")

top