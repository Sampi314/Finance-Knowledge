# Monday Morning Mulling: September 2024 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-september-2024-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: September 2024 Challenge

*   September 29, 2024

Monday Morning Mulling: September 2024 Challenge
================================================

Monday Morning Mulling: September 2024 Challenge
================================================

30 September 2024

_On the final Friday of each month, set an Excel for you to puzzle over for the weekend. On the Monday, we publish one suggested solution. No-one is stating this is the best approach, it’s just the one we selected. If you don’t like it, lump it – or contact us with your preferred solution._

**_The Challenge_**

On Friday, we gave you another bold challenge that sounds simple but requires some thought.

We asked you to consider the following:

![](https://sumproduct.com/wp-content/uploads/2025/05/e99287e639e41c464f05cb25d42feee6-1.jpg)

You can download the original question file [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Sept/sp-boldly-go.xlsx)
. We have a list of accounting data, where some of the **Account** data is shown in bold case. We need to filter the data so that only the rows with bold account codes are shown.

This month’s challenge was simple. You had to solve it as simply as possible, with no Preview features, VBA or Power Query. This is a deceptively simple Excel challenge!

**_Suggested Solution_**

The colourful key to solving this month’s challenge is not to apply some advanced filtering, but to consider how we can manipulate the bold text so we may use the simple filter functions to achieve our goal.

![](https://sumproduct.com/wp-content/uploads/2025/05/8fda6be25f6df0ae63aaa69142c6313a-1.jpg)

It may not be possible to ‘Filter by Bold’, but there is an option to ‘Filter by Color’. We can do this by using the Find functionality. Let’s begin by selecting the data in the **Account** column and using the shortcut **CTRL** + **F** to show the ‘Find and Replace’ dialog.

![](https://sumproduct.com/wp-content/uploads/2025/05/c221b3543b93c7b0c3478f84a1d43ab9-1.jpg)

Since we want to find a cell format and not a value, we need to use the Options button to see what other functionality is available:

![](<Base64-Image-Removed>)

Using the Format button, we may determine the format to be found from a cell:

![](<Base64-Image-Removed>)

If we select one of the cells with bold text, a Preview of the formatting is shown:

![](<Base64-Image-Removed>)

We may now ‘Find All’:

![](<Base64-Image-Removed>)

The next step is to replace the formatting with a colour. There are two \[2\] ways to do this.

**_Replace formatting with Replace tab_**

On the Replace tab, we may replace the formatting. This time we show the ‘Format…’ option. This is the option we would have chosen in the Find tab if it had been difficult to locate a bold cell to copy.

![](<Base64-Image-Removed>)

In the ‘Replace Format’ dialog, we may choose from any cell format:

![](<Base64-Image-Removed>)

For our example, we would like to change the font, therefore we access the Font tab and choose a colour. We also make the new font bold too:

![](<Base64-Image-Removed>)

We click OK, we are shown the Preview for the replacement:

![](<Base64-Image-Removed>)

We ‘Replace All’ and the bold font is now red:

![](<Base64-Image-Removed>)

**_Replace font using CTRL + A_**

There is a simpler method we could use for this example. Starting from the point where we found the rows that had bold text:

![](<Base64-Image-Removed>)

If we use **CTRL**\+ **A**, we select all the cells with bold formatting:

![](<Base64-Image-Removed>)

We may then change the colour on the selected cells from the Home tab:

![](<Base64-Image-Removed>)

Using either method, we now have the bold text in red:

![](<Base64-Image-Removed>)

Now, we may use the filter button on the **Account** heading to filter on the bold text:

![](<Base64-Image-Removed>)

The data has been filtered as required:

![](<Base64-Image-Removed>)

Problem solved. The solution file may be inspected [here](https://www.sumproduct.com/assets/blog-pictures/2022/fff-mmm/2024/Sept/sp-boldly-go-solution.xlsx)
.

_The Final Friday Fix will return on Friday 25 October 2024 with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business working day._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-september-2024-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-september-2024-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-september-2024-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-september-2024-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-september-2024-challenge/#0 "close")

top