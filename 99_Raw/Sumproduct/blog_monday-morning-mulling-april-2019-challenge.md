# Monday Morning Mulling: April 2019 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-april-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: April 2019 Challenge

*   April 28, 2019

Monday Morning Mulling: April 2019 Challenge
============================================

Monday Morning Mulling: April 2019 Challenge
============================================

29 April 2019

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

Here we have a column called “Code” which has text and numbers. We want to get rid of the numbers and replace them with the section headings. Let’s pull it into Power Query. I will use this as an example:

![](<Base64-Image-Removed>)

First, I replicate the column “Code”:

![](<Base64-Image-Removed>)

I move the duplicate column to the left:

![](<Base64-Image-Removed>)

I now convert the data type of the duplicate column to data type “Whole Number” (say):

![](<Base64-Image-Removed>)

All text appears as “Error”. I can’t replace errors yet as the data type is a number not text. So I change the data type back to text first:

![](<Base64-Image-Removed>)

Now I can replace errors without an issue:

![](<Base64-Image-Removed>)

I use something that I know won’t be in the column:

![](<Base64-Image-Removed>)

It doesn’t have to be “Liam007”!! Now we have to replace “Liam007” with the corresponding value in the Code column. Because this varies, we CANNOT use ‘Replace Values…’. Instead, we have to go to the ‘Add Column’ tab and click on ‘Conditional Column’:

![](<Base64-Image-Removed>)

I then do the following:

![](<Base64-Image-Removed>)

Ensure the icon under ‘Output’ is ‘Select a column’ not ‘Enter a value’ otherwise you will get the same value throughout. This gives you:

![](<Base64-Image-Removed>)

I delete the first column (Code-Copy), rename ‘Custom’ as ‘Classification’ and move it to the left, _viz_.

![](<Base64-Image-Removed>)

I then Fill Down on the first column:

![](<Base64-Image-Removed>)

Voila!

![](<Base64-Image-Removed>)

You can then filter as you see fit. For example:

![](<Base64-Image-Removed>)

This may now be loaded into Excel:

![](<Base64-Image-Removed>)

Yay! Did you find a more elegant solution?

_The Final Friday Fix will return on Friday 31__May with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-april-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-april-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-april-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-april-2019-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-april-2019-challenge/#0 "close")

top