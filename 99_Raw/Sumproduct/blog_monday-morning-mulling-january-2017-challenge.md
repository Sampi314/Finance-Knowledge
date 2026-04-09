# Monday Morning Mulling: January 2017 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-january-2017-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: January 2017 Challenge

*   January 29, 2017

Monday Morning Mulling: January 2017 Challenge
==============================================

Monday Morning Mulling: January 2017 Challenge
==============================================

30 January 2017

Last week, we asked if you could find a way to extract and output just the **bold** characters from the cell. How did you go? We couldn’t find a function that would help us at all, so we created our own!

**The Solution**

If you’ve been following our VBA blog series and don’t have much experience with VBA at all, then this might go a bit over your head. However, I’ll try to explain as we go along:

![](<Base64-Image-Removed>)

Wow, that’s something! Well, let’s consider what it’s doing and break it into steps:

*   Firstly, it’s a function that we’re going to call “udfExtractNonBold”, and it takes a cell range as it’s input (e.g. =udfExtractNonBold(A1))
*   For the cell range input, firstly check if it’s actually a string. If it’s a number, check to see if the whole thing is bold (can you bold certain parts of a number? Maybe we can ask that next month!).
*   If it’s a string, then go through each character one at a time. Check if that character is bold, and if so, add it to a new string that we’re storing (the thing called ‘returnValue’).
*   Finally, output the returnValue – if there’s no bold, it will give us a blank result. If there was bold text, it will give us only the text that was bolded, and nothing else in the cell.

Erm, simple! How did you go? Did you do it differently? Let us know!

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-january-2017-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-january-2017-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-january-2017-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-january-2017-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-january-2017-challenge/#0 "close")

top