# Text Messages

**Source:** https://sumproduct.com/thought/text-messages/

---

[Home](https://sumproduct.com/)

\> Text Messages

*   May 14, 2025

Text Messages
=============

You may not be a physicist but it’s time for some (text) string theory, even if it text all day to explain.

Text Messages
=============

You may not be a physicist but it’s time for some (text) string theory, even if it text all day to explain. By Liam Bastick, director with SumProduct Pty Ltd.

Query
-----

I have imported data from a third party database and negative numbers are being displayed as “123-” rather than (123). Worse, Excel is treating these numbers as text. How can I rectify the situation?

Advice
------

Numbers are regularly converted to text values when imported from one data source into another. This makes data manipulation difficult, if not seemingly impossible. Conversion may be awkward for the inexperienced.

Fortunately, Excel has several text string functions that can help ease the pain. In particular, two functions are required for the above problem.

### Determining text length with LEN()

**LEN(Text)** gives the length of **Text** in terms of number of text characters, Examples can be found in the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-text-string-functions-examples.xls)
:

![](<Base64-Image-Removed>)

LEN Examples

For example, blank cells have zero length, “” has length 2, but =”” has length zero. The **LEN()** function does not lie: in our example above cell **J18** (apparently “ok”) has 12 characters, which means there are 10 spaces following the final visible character (“k”).

### Obtaining the first n characters with LEFT()

**LEFT(Text,n)** returns the first **n** characters (reading from left to right of the text string referenced). For example:

![](<Base64-Image-Removed>)

LEFT Examples

e.g. For cell **J25** in the above example (which contains the characters “12345?), **LEFT(J25,3)** returns the text string “123?. It should be noted that:

*   If the original string were text in nature, the result would be text in nature also (i.e. truncated strings are not automatically converted to numbers)
*   If **n** is larger than the number of characters in Text, **LEFT(Text,n)** simply returns the entire text string, i.e. it does not return an error.

### Suggested solution

Hopefully, one solution to our above problem now become apparent.

![](<Base64-Image-Removed>)

Illustration of the Problem

Text strings always ending in a minus sign can be truncated to be one less than their original length (so only the numerical values are displayed) and then converted to a number. For example, if the value were in cell **J29** in accordance with the above illustration, then one solution would be

\=-LEFT(J29,LEN(J29)-1).

As a bonus, the minus sign converts the text into a number (this has been discussed previously in [SumProduct Squared..?](https://www.sumproduct.com/thought/sumproduct-squared)
).

### Word to the wise

These two functions are two of the more common text string functions but they are by no means the only ones. Other useful functions (with examples in the [attached Excel file](https://sumproduct.com/assets/user-upload/sp-text-string-functions-examples.xls)
) include:

*   **RIGHT(Text,n)** which returns the last **n** characters (reading from right to left of the text string referenced). Similar to **LEFT(Text,n)**, non-numerical values will remain non-numeric and values of **n** greater than the referenced text string itself will merely return the entire text string
*   **MID(Text,Start\_Number,n)** is like a halfway house between **LEFT()** and **RIGHT()**. This function returns **n** characters from the referenced text string starting with the character in position **Start\_Number**. Again, truncated text will not become numerical by default and if n exceeds the number of characters from **Start\_Number** to the final character, the remaining characters are displayed rather than an error value
*   **FIND(Find\_Text,Within\_Text,\[Start\_Number\])** is a search function which is case sensitive but does not allow wildcard characters. It seeks out the first instance of a character or characters (typed in inverted commas) in the **Within\_Text** text string. The **Start\_Number** argument is optional (hence the square brackets in the syntax) so that the first few characters in a text string may be ignored. If the **Find\_Text** cannot be located within **Within\_Text** the error #VALUE! is returned
*   **SEARCH(Find\_Text,Within\_Text,\[Start\_Number\])** is a search function which is not case sensitive but does allow for wildcard characters. It seeks out the first instance of a character or characters (typed in inverted commas) in the **Within\_Text** text string. The **Start\_Number** argument is optional (hence the square brackets in the syntax) so that the first few characters in a text string may be ignored. If the **Find\_Text** cannot be located within **Within\_Text** the error #VALUE! is returned
*   **TRIM(Text)** simply removes superfluous spaces within a text string, e.g. “John Smith ” would become “John Smith” instead.

![](<Base64-Image-Removed>)

Various Examples

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/text-messages/#0)
    
*   [Register](https://sumproduct.com/thought/text-messages/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/text-messages/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/text-messages/#0)

[](https://sumproduct.com/thought/text-messages/#0 "close")

top