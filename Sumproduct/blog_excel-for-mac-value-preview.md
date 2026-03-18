# Excel for Mac: Value Preview

**Source:** https://sumproduct.com/blog/excel-for-mac-value-preview/

---

[Home](https://sumproduct.com/)

\> Excel for Mac: Value Preview

*   January 18, 2024

Excel for Mac: Value Preview
============================

Excel for Mac: Value Preview
============================

19 January 2024

_This week in our series about Microsoft Excel for Mac, we show how to work around the missing feature, Evaluate Formula, by using a new feature and some old-school techniques._

This is a follow-up to our previous blog about writing and editing formulae, and how those tasks are a little different on Mac than on Windows. Some formulae are very simple. Debugging them is a simple matter of looking at the formula and knowing whether it’s right or wrong. For example, you may have a formula calculating the **SUM** of a few values. You can often just look at the values, calculate it in your head, and know whether you’ve got it right or wrong.

On the other hand, you may have much more complex formulae, where checking is not so easy to do in your head. In that case, there are a few tricks and tools you can use. However, there is one less tool on Mac than there is on Windows, because the ‘Evaluate Formula’ dialog isn’t available on a Mac (as of late 2023).

**_Value Preview_**

In early 2023, Microsoft added a handy feature called ‘Value Preview ToolTips’ to Excel on Windows, Mac and the web. These ToolTips are a great way for you to check the values being calculated by your formula and the parts making up the formula. It’s also very easy to use. Simply highlight part of your formula, and a ToolTip will appear showing you the current value of whatever you’ve selected. It works with references, functions, parameters within a function and the entire formula. In some cases, you might select something that doesn’t calculate and then Excel won’t show a value.

To make sure you select parts of the formula that can be calculated, you can use the function ToolTips to your advantage. As shown in the image below, you can click the function arguments to highlight the related part of the formula. In the **IF** formula, clicking on **logical\_test** highlights that part of the formula

![](https://sumproduct.com/wp-content/uploads/2025/05/image1-1703263849.gif)

There’s a shortcut key you can press to disable or enable the Value Preview ToolTips. Just press **CTRL + OPT + P**. On a Mac, this only works when you are not editing a cell (on Windows, it may be turned on / off anytime with **CTRL + ALT + P**).

**_F9 and ESC: The Old School Way_**

A handy trick for debugging formulae that is much less necessary now that we have the Value Preview ToolTips is to press **F9** when you’ve selected part of the formula that you want to evaluate. Excel will calculate the selection and replace what you selected with the current value. Just remember to press **ESC** after doing this, otherwise you might accidentally save a hard-coded value where you didn’t mean to.

As you can see in the image below, we highlight part of the formula, then press **F9** which changes the cell reference **G21** to its value (11). Then, we press **ESC** to avoid saving it as a hard-coded value.

![](https://sumproduct.com/wp-content/uploads/2025/05/image2-1703263884.gif)

**_Formula Builder_**

As we described in the [previous post](https://www.sumproduct.com/blog/article/excel-for-mac-writing-and-editing-formulae)
, you can use the ‘Formula Builder’ to help debug. When you’ve entered enough information for Excel to start calculating, it will show you the current values above each field in the pane.

_Please come back for future posts in this series, as we cover much more about Excel for Mac._

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/excel-for-mac-value-preview/#0)
    
*   [Register](https://sumproduct.com/blog/excel-for-mac-value-preview/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/excel-for-mac-value-preview/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/excel-for-mac-value-preview/#0)

[](https://sumproduct.com/blog/excel-for-mac-value-preview/#0 "close")

top