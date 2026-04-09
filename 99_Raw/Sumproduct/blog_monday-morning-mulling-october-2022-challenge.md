# Monday Morning Mulling: October 2022 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-october-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: October 2022 Challenge

*   October 30, 2022

Monday Morning Mulling: October 2022 Challenge
==============================================

Monday Morning Mulling: October 2022 Challenge
==============================================

31 October 2022

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to find and replace multiple values at once in Excel.

**_The Challenge_**

How did you usually find and replace a character in a text string in Excel? Many people use the ‘Find & Replace’ functionality in Excel, which works fine for single replacements. However, if you have tens, hundreds or thousands of items to replace this method seems very tedious and inefficient. Luckily, there were several ways to do the mass replacement in Excel more elegantly and effectively. Therefore, in this month’s challenge we challenged you to do that; you could download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/oct/fff/sp-bulk-replace---challenge.xlsx)
.

This month’s challenge was to write a **formula** to replace multiple letters in some text strings. The replacement table (here, called Replace) might be as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/0c587a24eeae36ccc1c5ee13ebaa9e21.jpg)

The result should look similar to the picture _(below__)_:

![](https://sumproduct.com/wp-content/uploads/2025/05/1500a8e527158173ada1590b8c37eaec.jpg)

As always, there were some requirements:

*   the formula needed to be within just one column (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA
*   the formula should be dynamic enough to update when a similar text string is added
*   only Excel 2016 functions were accepted.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/oct/mmm/sp-bulk-replace---suggested-solution.xlsx)
 which demonstrates our suggested solution.

Before we discuss the solution, I would like to note there are several complicating factors here. Let’s go through them.

**_Problem 1: SUBSTITUTION – a Pragmatic Approach_**

For a standard approach, you might think of using multiple nested **SUBSTITUTE** functions here along with [**INDEX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)
 functions. For example, if we have a single character to replace here, we will use the following formula:

**\=SUBSTITUTE(Texts\[@Text\],**

**INDEX(Replace\[@Old  \
Character\], 1), INDEX(Replace\[@New Character\], 1))**

In the formula above, the **Texts**, **Replace** is the name of the table. Therefore, **Texts\[@Old Text\], \[@Old Character\]**, and **\[@New Character\]** specify one row of column **Text**, **Old Character**, and **New Character** respectively. If we want to replace two \[2\] characters, we can nest the function like this:

**\=SUBSTITUTE(SUBSTITUTE(Texts\[@Text\],**

**INDEX(Replace\[@Old  \
Character\], 1), INDEX(Replace\[@New Character\], 1)),**

**INDEX(Replace\[@Old  \
Character\], 2), INDEX(Replace\[@New Character\], 2))**

Therefore, with the same principle, if we want to replace n values, we will nest our function like this:

**\=SUBSTITUTE(SUBSTITUTE(…SUBSTITUTE(Texts\[@Old  \
Text\],**

**INDEX(Replace\[@Old  \
Character\], 1), INDEX(Replace\[@New Character\], 1)),**

**INDEX(Replace\[@Old  \
Character\], 2), INDEX(Replace\[@New Character\], 2)),**

**…**

**INDEX(Replace\[@Old  \
Character\], n), INDEX(Replace\[@New Character\], n))**

This pragmatic approach might work but it makes the function hard to inspect in case of any error occurs. Besides that, it is not dynamic, if we put more characters to replace, we will have to modify the formula to adapt to the new inputs. Therefore, this approach is rejected.

**_Problem 2: Sequencing in the non-SEQUENCE world_**

When [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 were introduced, they introduced many useful Excel functions that come along with them, especially the **SEQUENCE** function. This function helps us generate a list of sequential numbers in an array. Hence, we can combine the **SEQUENCE** function with other functions like [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 or [**LEN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-len-function)
 to transform the text string into individual cells in a spreadsheet with the following formula:

**\=MID(Texts\[@Old Text\],  
SEQUENCE(1, LEN(Texts\[@Old Text\])),1)**

**SEQUENCE(1, LEN(Texts\[@Old Text\]))** will help us create a horizontal list of the consecutive text string from one \[1\] to the last number which is equal to the length of the string. For example:

![](<Base64-Image-Removed>)

The [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 function will then extract each character of a string with the starting point one by one, equal to the number list created by **SEQUENCE** above.

![](<Base64-Image-Removed>)

However, the problem is **SEQUENCE** does not exist in Excel 2016. Hence, we must find a workaround to do sequencing in “legacy” Excel that does not have the **SEQUENCE** function. Rats.

**_Problem 3: Number or not Number?_**

One minor problem you might encounter is whether the value in the Replace table is in the number type or the text type. Therefore, you have to convert these numbers into the same type. If you do not convert them into the same type, it can cause a problem for you later on when you use any lookup or match function. The idea here is that you also have to include the conversion within the formula as well.

**_Problem 4: Legacy Excel World_**

Before [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 became a thing, we had previously written an array formula in what we now call a legacy **CTRL + SHIFT + ENTER** (**CSE**) array. Thus, what is the difference between those two? First, the “legacy” CSE array formulae require entering **CTRL + SHIFT + ENTER** after completing the formula. For some formulae, we have to select a range for the output and then press the combination **CTRL + SHIFT + ENTER** whereas the [Dynamic Array](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 functions do not require this method of entry. This is not an issue, but it requires us to visualise the outputs before they are generated so that we select the correct range for the outputs.

**_Brainstorming_**

To address the replacement for the **SEQUENCE** function, may we introduce you to the [**INDIRECT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-indirect-function)
 and **ROW** functions? Let’s employ the following trick. Consider the following formula:

**\=ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old  \
Text\]\])))**

With respect to **“A1:A”&LEN(Texts\[@\[Old Text\]\]** this part of the formula will create a text string which is the range of the cell **A1** to one of the cells in column **A**, depending upon the length of the text string. For example, the first text string has 12 characters, so this piece of formula will return **A1:A12**.

Then we need a formula that can capture a text string here, since **ROW** requires a reference input, so it will not be able to capture a text reference here. This is where the [**INDIRECT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-indirect-function)
 function comes in handy since it is used to capture the text reference. Therefore, we wrap the [**INDIRECT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-indirect-function)
 around the text string above, then we will have the value of the first column. However, it will return an _#VALUE!_ error in some versions of Excel, so what you can do here is select the cell containing your formula and a range that equal to the length of the old text string you have. Next, you press **CTRL + SHIFT + ENTER**, and voilà you generate the following:

![](<Base64-Image-Removed>)

After that, we wrap the **ROW** function around the [**INDIRECT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-indirect-function)
 function we have. Then, the formula we just create can mimic the **SEQUENCE** function which gives us the following sequence:

![](<Base64-Image-Removed>)

**_Backed to suggested solutions_**

Now return to the example of **SEQUENCE**, [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
, and [**LEN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-len-function)
functions we discuss in problem two \[2\], we can finally replace the **SEQUENCE** function with the formula we create earlier:

**\=MID(Texts\[@\[Old Text\]\],ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old  \
Text\]\]))),1)**

This formula will give us the following visual:

![](<Base64-Image-Removed>)

From here we can write a lookup function to match the character in the **Texts\[@\[Old Text\]\]** with the **Replace\[Old Character\]** and we return these matches with the accordance **Replace\[New Character\]**.

Here we suggested you use the [**INDEX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)
 and [**MATCH**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-match-function)
functions. We will have the following formula for the [**MATCH**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-match-function)
function:

**\=MATCH(MID(Texts\[@\[Old  \
Text\]\],ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old Text\]\]))),1), Replace\[Old  \
Character\],0)**

This will be able to match correctly for the first second and third text strings but the fourth text string which is a number will not match. This is the issue we discuss in problem three \[3\], so for it to work we must wrap our lookup array argument in the **TEXT** function to transform all the characters that have number type into text type.

**\=TEXT(Replace\[Old Character\],”0″)**

Therefore, our complete function will look like this:

**\=MATCH(MID(Texts\[@\[Old  \
Text\]\],ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old  \
Text\]\]))),1),TEXT(Replace\[Old Character\],”0”),0)**

After writing the formula we will have the following visual:

![](<Base64-Image-Removed>)

Then we wrap the [**INDEX**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-index-function)
 function around the [**MATCH**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-match-function)
 function to replace the old characters in the text string with new characters:

**\=INDEX(Replace\[New  \
Character\],MATCH(MID(Texts\[@\[Old Text\]\],ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old  \
Text\]\]))),1),TEXT(Replace\[Old Character\],”0”),0))**

So, we have the following array:

![](<Base64-Image-Removed>)

We need all the places where it shows _#N/A!_ to keep the original text, so we can use the [**IFERROR**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-iferror-function)
 function here:

**\=IFERROR(INDEX(Replace\[New  \
Character\],MATCH(MID(Texts\[@\[Old  \
Text\]\],ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old  \
Text\]\]))),1),TEXT(Replace\[Old Character\],”0”),0)),MID(Texts\[@\[Old  \
Text\]\],ROW(INDIRECT(“A1:A”&LEN(Texts\[@\[Old Text\]\]))),1))**

Which will give us the following visual:

![](<Base64-Image-Removed>)

At this step, we introduced the last function that will help you merge all the arrays which is the [**CONCAT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-concat-function)
 function. The [**CONCAT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-concat-function)
 function is the succeeding [**CONCATENATE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-concatenate-function)
 function and is used to merge text. Therefore, you wrap this function around all the formulas we have so far, and you will have the new text string here:

**\=CONCAT(IFERROR(INDEX(Replace\[New  \
Character\],MATCH(MID(\[@\[Old Text\]\],ROW(INDIRECT(“A1:A”&LEN(\[@\[Old  \
Text\]\]))),1),TEXT(Replace\[Old Character\],”0”),0)),MID(\[@\[Old  \
Text\]\],ROW(INDIRECT(“A1:A”&LEN(\[@\[Old Text\]\]))),1)))**

As we know [**CONCAT**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-concat-function)
 function will merge all our arrays into one \[1\] cell so, we can safely press **CTRL + SHIFT + ENTER** to get the results of multiple replacements. Which will give you the following result table:

![](<Base64-Image-Removed>)

How cool is that?

**_Word to the Wise_**

Although this solution works quite well when replacing a single **Replace\[Old Character\]** in the **Texts\[@Old Text\]** for a single or multiple **Replace\[New Character\]**, it cannot replace multiple characters of the **Texts\[@Old Text\]** with a single or multiple **Replace\[Old Character\]**. However, this could be a challenge for another Final Friday Fix…

_The Final Friday Fix will return on Friday 25 November 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-october-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-october-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-october-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-october-2022-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-october-2022-challenge/#0 "close")

top