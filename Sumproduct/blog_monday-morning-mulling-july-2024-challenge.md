# Monday Morning Mulling: July 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-july-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: July 2024 Challenge

*   July 28, 2024

Monday Morning Mulling: July 2024 Challenge
===========================================

Monday Morning Mulling: July 2024 Challenge
===========================================

29 July 2024

_On the final Friday of each month, we set an Excel problem (or something similar!) for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_The Challenge_**

This month’s challenge was to dynamically substitute text in a dataset. Specifically, you needed to replace certain keywords in a text string with their corresponding substitutes from another list.

![](<Base64-Image-Removed>)

You were given a text string with multiple occurrences of the placeholder ‘\[e\]’ and a replacement table that provides different replacement values for each ‘\[e\]’. The main goal was to create a dynamic solution that replaces each ‘\[e\]’ in the text string with the corresponding value from the replacement table. You could download the original question file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/July/sp-substitute-text---starter-file.xlsm)
.

As always, there were some requirements:

*   the formula needed to be within just one \[1\] column (no “helper” cells)
*   you needed to ensure the solution was dynamic so that it updated when new placeholders or replacement values were added
*   no VBA or Power Query was allowed; this was purely a formula challenge.

**_Suggested Solution 1_**

You can find our Excel file [here](https://sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/July/sp-substitute-text---suggested-solutions.xlsm)
, which shows our suggested solution. The steps are detailed below:

**_Splitting and Joining_**

The main idea is to split the text string by the delimiter ‘\[e\]’ into multiple parts. Then, add the replacement values at the end of those parts and join them together to create a new text string that satisfies the requirements.

In the Excel file, we have named **Text** as the text string value, **Parameter** as the placeholder value, and **tbl\_Replace** refers to the replacement table.

**1\. SPLITTING THE TEXT**

We use the **[TEXTSPLIT](https://www.sumproduct.com/news/article/recent-text-and-array-functions-an-update)
** function to split the text string into multiple parts:

**\=TEXTSPLIT(Text,Parameter)**

This formula creates a dynamic array that spills to the right.

![](<Base64-Image-Removed>)

For easier visualisation, we change the formula to make it spill down:

**\=TEXTSPLIT(Text,,Parameter)**

![](<Base64-Image-Removed>)

Placing this side by side with **tbl\_Replace**:

![](<Base64-Image-Removed>)

**2\. JOINING THE TEXT**

At this point, we use the **TEXTJOIN** function to join everything together:

**\=TEXTJOIN(tbl\_Replace\[Replace\],0,TEXTSPLIT(Text,Parameter))**

![](<Base64-Image-Removed>)

This will give us the desired solution.

**_Suggested Solution 2_**

We can achieve the same result using multiple iterative formulas with the **SUBTITUTE** function. To replicate the action above in one formula, we can use:

**\=REDUCE(Text,  
SEQUENCE(ROWS(tbl\_Replace\[Replace\])), LAMBDA(a,v, SUBSTITUTE(a, Parameter,  
INDEX(tbl\_Replace\[Replace\], v), 1)))**

![](<Base64-Image-Removed>)

This works as follows:

*   **SEQUENCE(ROWS(tbl\_Replace\[Replace\]))** creates an array from one \[1\] to the number of replacements we have
*   **INDEX(tbl\_Replace\[Replace\], v)** picks up the suitable replacement value
*   the **REDUCE** function acts as a _For Each_ loop, like VBA.

The picture below illustrates the process of **REDUCE** gettingthe result with each iteration:

![](<Base64-Image-Removed>)

**_Word to the Wise_**

There are some differences in the results of Solution 1 and Solution 2. If there are more placeholders than replacement values:

*   Solution 1 will loop back to the first replacement value
*   Solution 2 will keep ‘\[e\]’.

![](<Base64-Image-Removed>)

We appreciate there are many, many ways this could have been achieved. If you have produced an alternative, radically different approach, congratulations – that’s half the fun of Excel!

_The Final Friday Fix will return on Friday 30 August 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-july-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-july-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-july-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-july-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-july-2024-challenge/#0 "close")

top