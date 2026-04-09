# A to Z of Excel Functions: The DETECTLANGUAGE Function

**Source:** https://sumproduct.com/blog/a-to-z-of-excel-functions-the-detectlanguage-function/

---

[Home](https://sumproduct.com/)

\> A to Z of Excel Functions: The DETECTLANGUAGE Function

*   August 4, 2024

A to Z of Excel Functions: The DETECTLANGUAGE Function
======================================================

A to Z of Excel Functions: The DETECTLANGUAGE Function
======================================================

5 August 2024

_Welcome back to our regular A to Z of Excel Functions blog. Today we look at the **DETECTLANGUAGE** function._

**The DETECTLANGUAGE function**

Currently in Preview, you should be careful using this function: its signature and results may change substantially before being broadly released, based upon feedback from those fortunate enough to be able to access them. Therefore, we strongly recommend you do not rely on this function in important workbooks until it is Generally Available.

**DETECTLANGUAGE** detects the language of text you provide using the Microsoft Translation Services and returns the language code. The full signature is:

**DETECTLANGUAGE(text)**

The function has the following arguments:

*   **text:** the **text** or reference to cells containing **text** to evaluate.

Currently, there are 133 languages supported – including two variations of Klingon!!

The supported languages and their respective language codes are as follows:

![](https://sumproduct.com/wp-content/uploads/2025/05/5daaf9320f0aaa46a119a898c4d698c5-1.jpg)![](https://sumproduct.com/wp-content/uploads/2025/05/30cc9476f3ce67d1934ca91bc192063f-1.jpg)![](https://sumproduct.com/wp-content/uploads/2025/05/5e135a4d4c2ef842df98fc88023b7f2f-1.jpg)![](https://sumproduct.com/wp-content/uploads/2025/05/2b0e02f86c97b8edbef1269ea3829aa5-1.jpg)![](https://sumproduct.com/wp-content/uploads/2025/05/7f783d061d4d6ae2bec2f111634f3661-1.jpg)![](https://sumproduct.com/wp-content/uploads/2025/05/c9f3764b72e7ee895454698829888e6e-1.jpg)

Suppose you have the following text in cell **A1**: “Hola mundo!” and you want to find out what the language of the text is. You can use the **DETECTLANGUAGE** function as follows:

**\=DETECTLANGUAGE(A1)**

This will return the detected language for the text in cell **A1**. The language code “es” for Spanish will be displayed in the cell where you entered the formula.

Alternatively, you may just type the text in, _viz._

![](<Base64-Image-Removed>)

![](<Base64-Image-Removed>)

Common errors include the following:

*   **Text Too Long:** you have too many characters in a cell. Reduce your cell size and try again
*   **Error in Value:** you have a non-text value in your cell. The function only accepts a text argument
*   **Invalid Language:** you have entered an invalid language code or one not presently supported (see above)
*   **Request Throttled:** you have exceeded your daily quota of the translation function.

These functions are currently available to Beta Channel users running:

*   Windows: Version 2407 (Build 16.0.17808.20000) or later
*   Mac: 16.87 (Build 24062430) or later.

_We’ll continue our A to Z of Excel Functions soon. Keep checking back – there’s a new blog post every business day._ _A full page of the function articles can be found [here](https://www.sumproduct.com/thought/a-to-z-of-excel-functions)
._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-detectlanguage-function/#0)
    
*   [Register](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-detectlanguage-function/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-detectlanguage-function/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-detectlanguage-function/#0)

[](https://sumproduct.com/blog/a-to-z-of-excel-functions-the-detectlanguage-function/#0 "close")

top