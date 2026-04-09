# Final Friday Fix: February 2019 Challenge

**Source:** https://sumproduct.com/blog/final-friday-fix-february-2019-challenge/

---

[Home](https://sumproduct.com/)

\> Final Friday Fix: February 2019 Challenge

*   February 21, 2019

Final Friday Fix: February 2019 Challenge
=========================================

Final Friday Fix: February 2019 Challenge
=========================================

22 February 2019

_On the final Friday of each month, we’re going to set an Excel challenge for you to puzzle over so that you can get your “Excel fix”. Challenge your office colleagues to see who can solve the puzzle quickest. There’s no prizes at this stage, you’re playing for bragging rights only!_

Welcome to this week’s Friday Fix. This week we are drawing the problem from our consulting work, this being a task that we’ve been asked to do as part of our consulting business.

The problem here relates to Data Validation. Normally, you can get use data validation to restrict inputs to only values that come from a list. However, what if you want values from your data validation to subsequently populate your list?

The request that we have is innocuous enough. We want to create a data validation input cell that will take values from a list and populate a dropdown. If a value is entered that does not exist in the list, we want a prompt to check whether this value is correct, or whether it was entered in error. This should work similar to the “Warning” option of data validation which will allow you to enter a value and keep it with a warning message, despite not meeting the data validation criteria.

Here’s the tricky thing though. As values are entered, any new values should be included into the data validation list for future reference.

![](<Base64-Image-Removed>)

This leaves us in a sticky situation, because a formula that adds a new value to the data validation list will no longer trigger the warning criteria in the data validation. That is, while the value might not exist in the data validation list when you are typing it in, a formula-driven list will pick up the value before the data validation check is applied, thus ignoring the data validation effectively and allowing the new value to be entered in without warning.

So, this is the challenge this week: can you find a solution that will allow you to enter a value using a drop down list, check if manually entered items are intended to be added to the list, and allow users to cancel their actions if entered in error?

_Sound easy? Have a go. We’ll publish a couple of solutions in Monday’s blog. Have a great weekend!_

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/final-friday-fix-february-2019-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/final-friday-fix-february-2019-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/final-friday-fix-february-2019-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/final-friday-fix-february-2019-challenge/#0)

[](https://sumproduct.com/blog/final-friday-fix-february-2019-challenge/#0 "close")

top