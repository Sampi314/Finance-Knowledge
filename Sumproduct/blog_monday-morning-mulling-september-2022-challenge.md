# Monday Morning Mulling: September 2022 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-september-2022-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: September 2022 Challenge

*   October 2, 2022

Monday Morning Mulling: September 2022 Challenge
================================================

Monday Morning Mulling: September 2022 Challenge
================================================

3 October 2022

_On the final Friday of each month, we set an Excel / Power Pivot / Power Query / Power BI problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

The challenge this month was to extract a name from a text string that contains special characters.

**_The Challenge_**

There may be a time when you are using Excel that you wish to extract a name of a person from a churn of endless text strings that has all sorts of characters that you have never seen or used before. We gave you a similar challenge here, you can download the question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/sep/fff/sp-extracting-name---challenge.xlsx)
.

This month’s challenge was to write a **formula** to extract the name of a person from a text string. The result should look like as picture _(below__)_:

![](<Base64-Image-Removed>)

As always, there were some requirements:

*   the formula needed to be within just one column (no “helper” cells)
*   this was a formula challenge; no Power Query / Get & Transform or VBA!
*   the formula should be dynamic enough when a similar text string was added.

**_Suggested Solution_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/sep/mmm/sp-extracting-name---suggested-solution.xlsx)
 which demonstrates our suggested solution.

Before we discuss the solution, I would like to note there are several complicating factors here. Let’s go through them.

**_Problem 1: The Unremovable White Space_**

When tackling this problem, we might rely on some functions like **TRIM** and [**CLEAN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-clean-function)
 to clear the text. The **TRIM** function helps us strip extra white space from the text leaving only a single space between words and no space characters at the start or end of the text. The [**CLEAN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-clean-function)
 function helps us remove all nonprintable characters from text. Thus, using the **TRIM** and [**CLEAN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-clean-function)
 functions might help us remove all unwanted white spaces and nonprintable characters:

**\=CLEAN(TRIM(Text\[@Text\]))**

In the formula above, **Text** is the name of the table. Therefore, **Text\[@Text\]** specifies one row of column **Text**, where the above formula is located. However, these two functions do not appear to work with these text strings no matter how many times these functions apply: the white space is still there. This is because there are some special invisible characters that the **TRIM** and [**CLEAN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-clean-function)
 function cannot remove. Hence, using **TRIM** and [**CLEAN**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-clean-function)
functions for this challenge will not solve our problem.

**_Problem 2: The Unfindable Apostrophe_**

The [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
 function is quite useful here to address the challenge. It may help us look for the position of a character within the text string. Moreover, the target text we need to extract is between the white space and the apostrophe, so [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
 can give us the location of those items which can, later on, be used to extract the target text.

However, you might run into the problem that the [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
 function results in the _#VALUE!_ error when you try to search for the apostrophe. This is because there is a “weird” apostrophe within the text string which is different from the normal apostrophe on the keyboard. Therefore, the [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
 function must be tweaked to be able to search for that apostrophe in the text string.

**_Brainstorming_**

To address the unremovable white space and unfindable apostrophe problems, we will need a quick inspection of the text string to fully understand it. Therefore, we will transform each letter of the text string into individual cells in the spreadsheet.

For Microsoft Excel 365 and online versions, we may use [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 with the following formula:

**\=MID(Text\[@Text\], SEQUENCE(1, LEN(Text\[@Text\])),1)**

**SEQUENCE(1, LEN(Text\[@Text\]))** will help us create a horizontal list of the consecutive text string from one \[1\] to the last number which is equal to the length of the string. For example:

![](<Base64-Image-Removed>)

The [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 function will then extract each character of a string with the starting point one by one, equal to the number list created by **SEQUENCE** above.

After you copy down the formula, the result should look like this:

![](<Base64-Image-Removed>)

We can see that there are many invisible characters and white space at the beginning of the strings.

Next, we will need to identify what those invisible characters are. We can use **UNICODE** and **UNICHAR** functions to our [Dynamic Arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
 above. **UNICODE** allows us to return numeric code for the first character in a text string. **UNICHAR** translates that code back into a character. (You can also use [**CODE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-code-function)
 and [**CHAR**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-char-function)
 functions here, but we suggest using **UNICODE** and **UNICHAR** as some special characters are not in the database of [**CODE**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-code-function)
 and [**CHAR**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-char-function)
). The formula to return numeric code is as follows:

**\=UNICODE(MID(Text\[@Text\], SEQUENCE(1, LEN(Text\[@Text\])),1))**

The result is as follows:

![](<Base64-Image-Removed>)

Upon inspection, we can see that the codes of these “invisible characters” are 160 and 32. Unicode 32 is our normal “Space” generated by pressing the spacebar on the keyboard, while 160 is the “No-Break Space”, generated by pressing **ALT + 0160**.

For the normal “Apostrophe” that we use on the keyboard, they have the Unicode of 39, while the apostrophe used in the text string is the “Right Single Quotation Mark” which has the Unicode 8217.

**_Back to the Suggested Solution_**

As we can see here, all 3-text strings have 32 in front of the target name and 8217 at the end of the target name. So, we can write a [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
 function to find their position of them.

This situation is perfect to extract the key data from the text string as [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
function will give out the position of the first appearance of the letter. So, if we use [**FIND**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-find-function)
 function on the “No-Break Space” character that has Unicode 160, it will result in three \[3\] which is not a desirable starting position.

Hence, the starting position of the target text should be:

**\=FIND(UNICHAR(32), Text\[@Text\])+1**

and the number of characters we extract is:

**\=FIND(UNICHAR(8217), Text\[@Text String\])-FIND(UNICHAR(32), Text\[@Text\])-1**

From here we can use the [**MID**](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-mid-function)
 function to extract the target text as follows:

**\=MID(Text\[@Text\], FIND(UNICHAR(32), Text\[@Text\]) +1, FIND(UNICHAR(8217), Text\[@Text\])-FIND(UNICHAR (32), Text\[@Text\])-1)**

See you next month!

_The Final Friday Fix will return on Friday 28 October 2022 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-september-2022-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-september-2022-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-september-2022-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-september-2022-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-september-2022-challenge/#0 "close")

top