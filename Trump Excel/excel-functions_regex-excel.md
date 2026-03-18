# REGEX Functions in Excel (10 Examples)

**Source:** https://trumpexcel.com/excel-functions/regex-excel

---

[Skip to content](https://trumpexcel.com/excel-functions/regex-excel/#content "Skip to content")

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2036%2036'%3E%3C/svg%3E)

Written by

[Sumit Bansal](javascript:void(0))

![Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2056%2056'%3E%3C/svg%3E)

Sumit Bansal

[LinkedIn](https://www.linkedin.com/in/sumitbansal23/)
 [YouTube](https://www.youtube.com/@trumpexcel)

Sumit Bansal is the founder of TrumpExcel.com and a Microsoft Excel MVP. He started this site in 2013 to share his passion for Excel through easy tutorials, tips, and training videos, helping you master Excel, boost productivity, and maybe even enjoy spreadsheets!

[📋 FREE EXCEL TIPS EBOOK - Click here to get your copy](https://trumpexcel.com/excel-functions/regex-excel/#below-title)

Excel now has three new REGEX functions, which allow us to work with text data a lot more efficiently.

*   _REGEXEXTRACT_
*   _REGEXREPLACE_
*   _REGEXTEST_

While Excel already has many text functions and functionalities to deal with text manipulation, REGEX functions can be quite helpful in some situations.

REGEX is not a new concept and has been around for more than 50 years, it’s only now that we have got it in Excel.

In this article, I will show you some practical examples of how you can use these new regex functions in Excel.

So let’s get started!

[**_Click here to download the example file and follow along_**](https://www.dropbox.com/scl/fi/c77zjwsckl8qwrvdtlot6/REGEX-Functions-in-Excel-Examples.xlsx?rlkey=rcg7y0cl106zznagokj7imo5o&dl=1)

This Tutorial Covers:

[Toggle](https://trumpexcel.com/excel-functions/regex-excel/#)

Regex Metacharacters (Tokens) Table with Examples
-------------------------------------------------

Below is a table where I have listed all the Regex meta characters along with their explanation and an example.

You’re not expected to remember all of these, but you can bookmark this page so that you can come back and refer to it whenever needed.

The usage of these tokens becomes a lot clearer when you start looking at the example covered later in this article.

| Metacharacter | Name | What it does | Examples |
| --- | --- | --- | --- |
| **.** | Dot | Matches any single character except newline (unless configured otherwise) | `a.c` matches “abc”, “a1c”, “a@c”, but not “a\\nc” |
| **\|** | Pipe | Acts as an OR operator, allowing either the expression before or after it to match | `cat\|dog` matches “cat” or “dog” |
| **\*** | Asterisk | Matches the preceding character or group zero or more times (greedy) | `ab*c` matches “ac”, “abc”, “abbc”, “abbbc”, etc. |
| **^** | Caret | Anchors the match to the beginning of the string or line | `^Hello` matches “Hello World” but not “World Hello” |
| **$** | Dollar | Anchors the match to the end of the string or line | `World$` matches “Hello World” but not “World Hello” |
| **+** | Plus | Matches the preceding character or group one or more times (greedy) | `ab+c` matches “abc”, “abbc”, “abbbc”, but not “ac” |
| **\\** | Backslash | Escapes the following character, treating metacharacters as literals or giving special meaning to ordinary characters | `\.` matches a literal dot, `\d` matches any digit |
| **?** | Question mark | Makes the preceding character or group optional, matching it zero or one time | `colou?r` matches both “color” and “colour” |
| **\[\]** | Brackets | Defines a character set, matching any single character within the brackets | `[aeiou]` matches any single vowel |
| **{}** | Braces | Specifies an exact number or range of occurrences for the preceding character or group | `a{2,4}` matches “aa”, “aaa”, and “aaaa” |
| **()** | Parentheses | Groups characters together and creates a capturing group | `(ab)+` matches “ab”, “abab”, “ababab”, etc. |
| **(?:)** | Non-capturing group | Groups characters without creating a capturing group | `(?:ab)+` same as above, but doesn’t create a capture |
| **\\d** | Digit | Matches any digit (equivalent to \[0-9\]) | `\d{3}` matches “123”, “456”, etc. |
| **\\w** | Word character | Matches any word character (equivalent to \[a-zA-Z0-9\_\]) | `\w+` matches “hello\_world123” |
| **\\s** | Whitespace | Matches any whitespace character (spaces, tabs, newlines) | `a\sb` matches “a b”, “a\\tb”, “a\\nb” |
| **\\b** | Word boundary | Matches a position where a word starts or ends | `\bcat\b` matches “cat” in “The cat sat” but not in “category” |
| **\[^\]** | Negated set | Matches any character that is not in the set | `[^aeiou]` matches any character that’s not a vowel |
| **(?=)** | Positive lookahead | Asserts that what follows the current position matches the given pattern, without consuming characters | `\w+(?=\d)` matches “abc” in “abc123” but not “123” |
| **(?!)** | Negative lookahead | Asserts that what follows the current position does not match the given pattern, without consuming characters | `\w+(?!\d)` matches “abc” in “abcdef” but not in “abc123” |
| **(?<=)** | Positive look behind | Asserts that what precedes the current position matches the given pattern, without consuming characters | `(?<=\d)\w+` matches “abc” in “123abc” but not in “defabc” |
| **(?<!)** | Negative look behind | Asserts that what precedes the current position does not match the given pattern, without consuming characters | `(?<!\d)\w+` matches “abc” in “\_abc” but not in “123abc” |
| **\\1, \\2, etc.** | Backreferences | Refers to a previously captured group | `(\w+)\s+\1` matches repeated words like “hello hello” |

Let me first tell you about the three REGEX functions in Excel.

REGEXTEST Function in Excel
---------------------------

The REGEXTEST function can be used to check if a text string matches the given regular expression pattern.

It returns TRUE if it finds a match and FALSE if it doesn’t.

Below is the syntax of the REGEXTEST function in Excel:

\=REGEXTEST(text, pattern, \[case\_sensitivity\])

Where:

*   _text_ – this is the text or the [cell reference](https://trumpexcel.com/absolute-relative-mixed-cell-references/)
     containing the text in which you want to look for the pattern
*   _pattern_ – this is the regex pattern that you want to look into the _text_ argument
*   _\[case\_sensitivity\]_ – this argument can be used to specify whether you want the match to be case-sensitive or not (use 0 for case-sensitive and 1 for case-insensitive). If omitted, this would be case-sensitive by default.

Here are a couple of simple examples to give you an idea of how the REGEXTEST function works:

*   _\=REGEXTEST(“cat”, “a”)_ – This would return TRUE because the letter “a” is found in the word “cat”.
*   _\=REGEXMATCH(“dog”, “^d”)_ – This would return TRUE because “d” is at the beginning of the word “dog”. The “^” in the regular expression means “start of the string”.
*   _\=REGEXMATCH(“apple”, “le$”)_ – This would return TRUE because “le” is at the end of “apple”. The “$” means “end of the string”.

REGEXEXTRACT Function in Excel
------------------------------

REGEXEXTRACT function can be used to extract the matching substring within the given string.

It would always return a text value as the output.

Below is the syntax of the REGEXEXTRACT function in Excel:

\=REGEXEXTRACT(text, pattern, \[return\_mode\], \[case\_sensitivity\])

Where:

*   _text_ – this is the text or the cell reference containing the text in which you want to look for the pattern
*   _pattern_ – this is the regex pattern that you want to look into the _text_ argument
*   _\[return\_mode\]_ – here you specify what part of the matching group you want to return.
    *   0 – Returns only the first match
    *   1 – Return all the matches as an array
    *   2 – Returns only the capture groups from the first match. Capture groups are patterns that are within parentheses (….)
*   \[case\_sensitivity\] – here you can specify whether you want the pattern matching to be case-sensitive or not. By default, it resorts to case-sensitive match.

REGEXREPLACE Function in Excel
------------------------------

REGEXEXTRACT function can be used to replace the matching substring within the given string with the specified string.

For example, if you want to replace the name of one company with another, you can use REGEXREPLACE.

Below is the syntax of the REGEXREPLACE function in Excel:

\=REGEXREPLACE(text, pattern, replacement, \[occurrence\], \[case\_sensitivity\])

Where:

*   text – this is the text or the cell reference containing the text in which you want to look for the pattern
*   pattern – this is the regex pattern that you want to look into the _text_ argument
*   replacement – this is the text you want as the replacement for the matching pattern
*   \[occurrence\] – here you can specify what instance of the occurrence you want to replace. By default, it replaces all instances.
*   \[case\_sensitivity\] – here you can specify whether you want the pattern matching to be case-sensitive or not. By default, it resorts to a case-sensitive match.

Now, let me start with some examples that would give you a flavor of how regex works in Excel and how it can be useful.

[**_Click here to download the example file and follow along_**](https://www.dropbox.com/scl/fi/c77zjwsckl8qwrvdtlot6/REGEX-Functions-in-Excel-Examples.xlsx?rlkey=rcg7y0cl106zznagokj7imo5o&dl=1)

Example 1 – Extract First or Last Name
--------------------------------------

Let’s start with a simple example.

Below is a dataset where I have some names in column A, and I want to extract the first and last names in two separate columns.

![Data set to split first and last name using regex functions in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20490%20336'%3E%3C/svg%3E)

Here is the formula to get the first name:

\=REGEXEXTRACT(A2:A11, "^\\S+")

![Regex formula to get the first name from full name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20610%20384'%3E%3C/svg%3E)

Let me explain how this formula works:

*   ^ – This caret symbol means “start of the string”. It tells the regex to look at the very beginning of the text.
*   \\S – This means “any character that is not a whitespace”. It includes letters, numbers, and symbols.
*   \+ – This means “one or more of the previous thing”. In this case, it’s looking for one or more non-whitespace characters.

Putting it all together, the formula says, _starting_ _from the beginning of the string in cell A2, find one or more characters that are not spaces and extract that_.

In simpler words, it grabs all the characters from the start of the name until it finds a space character. This effectively extracts the first name from each cell.

And, to get the last name, you can use the formula below:

\=REGEXEXTRACT(A2, "\\S+$")

![Regex formula to get last name from full name](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20600%20383'%3E%3C/svg%3E)

In the above formula:

*   \\S+: Matches one or more non-space characters
*   $: Anchors the match to the end of the text. This tells the formula to give the search result from the end.

So, it finds a group of non-space characters that occurs right at the end of the text, which is typically the last name in a full name string.

Example 2 – Extract First or Last Name (no space)
-------------------------------------------------

If you’re thinking that [extracting the first or last name](https://trumpexcel.com/extract-last-name-excel/)
 from full names is possible with text formulas in Excel (along with other features such as Find and Replace or Flash Fill or Power Query), you’re right.

So let me show you something that’s not so easy with Excel text formulas, but super easy with REGEX functions.

Below, I have a dataset of names, and I want to extract the first and last names. But the catch is that there is no space between the first and the last name.

![Data set to get first and last name without any space in between](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20432%20288'%3E%3C/svg%3E)

So, let me show you some Regex function magic now.

Here is the formula to get the first name:

\=REGEXEXTRACT(A2:A11, "(^\[A-Z\]\[a-z\]+)",1,0)

![Formula to extract first name with regex without space](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20524%20362'%3E%3C/svg%3E)

Let me explain the regex pattern here:

*   ^ – This anchor asserts the start of the string.
*   \[A-Z\] – This matches exactly one uppercase letter from A to Z.
*   \[a-z\]+ – This matches one or more lowercase letters from a to z.

So, this pattern matches a string that starts with an uppercase letter followed by one or more lowercase letters. And it stops as soon as it encounters anything other than a lowercase letter.

Similarly, if you want to extract the last name only, you can use the below formula:

\=REGEXEXTRACT(A2:A11, "(\[A-Z\]\[a-z\]+)$")

![Formula to extract last name with regex without space](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20520%20358'%3E%3C/svg%3E)

In this formula, I have replaced ^ from the beginning with a $ at the end, which means that it will give us the matching pattern from the end (which gives us the last name).

But wait, there is more.

What if I can extract the first and the last name using a single formula?

You can do that using the below formula:

\=REGEXEXTRACT(A2, "(\[A-Z\]\[a-z\]+)",1,0)

Enter this formula in cell A2 and then copy it for all the other cells in the column.

The above formula looks for the pattern (\[A-Z\]\[a-z\]+), which means that it looks for all the matching strings that start with an uppercase letter followed by all the lowercase letters.

In our example, it finds two pattern matches, the first and the last name, and it then gives us the result in two separate cells.

So, I can just enter this one formula in the cell and drag it down, and it will give me the first as well as the last name in two separate cells.

Also read: [How to Switch First and Last Name in Excel with Comma?](https://trumpexcel.com/switch-first-and-last-name-with-comma-excel/)

Example 3 – Extract Username/Domain from Email
----------------------------------------------

Below, I have a dataset where I have email addresses in column A, and I want to get the username and the domain name in separate columns.

![Email dataset to use with REGEX functions in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20286'%3E%3C/svg%3E)

Again, while there are other ways to do this in Excel, let me show you how to do this using REGEX.

Here is the formula to get the username from email using the REGEXEXTRACT function:

\=REGEXEXTRACT(A2:A11, "^(\[^@\]+)")

![REGEXEXTRACT formula to extract username from email](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20333'%3E%3C/svg%3E)

In this regex pattern:

*   ^ – Matches the start of the string
*   ( – Starts a capturing group
*   \[^@\]+ – Matches one or more characters that are not ‘@’
*   ) – Ends the capturing group

This pattern will capture everything from the start of the string up to (but not including) the ‘@’ symbol, which is typically the username in an email address.

And if you want to get the domain name, you can use the below formula:

\=REGEXEXTRACT(A2:A11, "\[^@\]+$")

![REGEXEXTRACT formula to extract domain from email](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20640%20335'%3E%3C/svg%3E)

In this regex pattern:

*   \[^@\] – This is a negated character set and matches any character that is not an @ symbol.
*   \+ – This quantifier means “one or more of the preceding element”. So \[^@\]+ means “one or more characters that are not @”.
*   $ – This gives us the matching string from the end of the text in the cell.

_If you’re thinking this can easily be done with regular text formulas in Excel, have a look at the next example._

Example 4 – Extract Email from Text
-----------------------------------

Now, let’s dial up the complexity a little bit.

Below, I have a dataset where I have some text in column A, and I want to extract the email addresses from each cell.

![Data set to get emails from text using regex](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20814%20286'%3E%3C/svg%3E)

Now, this is a bit complicated as the email can be anywhere in the text.

Here is the regex formula in Excel to tackle this:

\=REGEXEXTRACT(A2:A11, "\[A-Za-z0-9.\_%+-\]+@\[A-Za-z0-9.-\]+\\.\[A-Z|a-z\]{2,}")

![REGEX formula in Excel to extract emails from text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20815%20360'%3E%3C/svg%3E)

In this regex pattern:

*   \[A-Za-z0-9.\_%+-\]+ – This matches one or more characters that can be:
    *   Uppercase letters (A-Z)
    *   Lowercase letters (a-z)
    *   Numbers (0-9)
    *   Special characters: . \_ % + –

*   @ – This matches the @ symbol, which is required in email addresses
*   \[A-Za-z0-9.-\]+ – This matches one or more characters that can be:
    *   Uppercase letters (A-Z)
    *   Lowercase letters (a-z)
    *   Numbers (0-9)
    *   dot or hyphen
*   \\. – This matches a literal dot (.)
*   \[A-Z|a-z\]{2,} – This matches two or more characters that can be:
    *   Uppercase letters (A-Z)
    *   Lowercase letters (a-z)

While this works well if you only have one email address in the text, what if you have two or more?

Below, I have a dataset where I want to extract all the emails in the text in column A in column B (separated by a comma)

![Data set to get multiple emails from text using regex](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20700%20358'%3E%3C/svg%3E)

In this case, we can use a slightly modified regex pattern along with the TEXTJOIN function.

Here is the formula to do this:

\=TEXTJOIN(", ", TRUE, REGEXEXTRACT(A2,"\[A-Za-z0-9.\_%+-\]+@\[A-Za-z0-9.-\]+\\.\[A-Z|a-z\]{2,}", 1))

![REGEX formula in Excel to extract multiple emails from text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20701%20405'%3E%3C/svg%3E)

Enter this formula in cell B2 and then copy it for all the other cells in the column.

In the above formula, I have used 1 as the \[return\_mode\] argument in the REGEXEXTRACT function. This gives me all the matching strings (which are all the email addresses).

And since I wrapped this REGEXEXTRACT formula in TEXTJOIN, it gives me all the email addresses in single cells separated by a comma.

Example 5 – Extract Text in Parentheses
---------------------------------------

Below, I have a data set where I have some text in column A, and I want to extract all the text that is there in parenthesis in column B.

![Data set to extract text in parentheses using regex in Excel formulas](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20872%20288'%3E%3C/svg%3E)

Here is the formula to do that:

\=REGEXEXTRACT(A2:A11, "\\((.+)\\)")

![Excel REGEX formula to extract text in parenthesis](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20873%20331'%3E%3C/svg%3E)

In the above formula’s regex pattern:

*   \\( – This matches an opening parenthesis. The backslash is used to escape the parenthesis because parentheses have special meaning in regex.
*   ( – This opens a capturing group. It allows you to extract the content matched by the part of the pattern inside the parentheses.
*   (.+) – This is a capturing group that matches one or more (+) of any character except newline (.)
*   ) – This closes the capturing group.
*   \\) – This matches a closing parenthesis. Again, the backslash is used to escape it (here, escape means treating it as any other character and not considering it a special character in regex).

If you want to get the result without the parenthesis, you can use the below formula:

\=MID(REGEXEXTRACT(A2:A11, "\\((.+)\\)"),2,LEN(REGEXEXTRACT(A2:A11, "\\((.+)\\)"))-2)

Example 6 – Extract Numbers from String
---------------------------------------

Extracting numbers from an alphanumeric string in Excel can be a complicated regular (non-regex) Excel formula.

But with regex, this is really simple.

Below, I have a data set where I have some data in column A, and I want to extract the numbers in the text in each cell into the adjacent cell in column B.

![Data set to extract numbers from string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20430%20197'%3E%3C/svg%3E)

Here is the regex formula that does that:

\=REGEXEXTRACT(A2:A6, "\\d+")

![Excel regex formula to extract numbers from string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20573%20240'%3E%3C/svg%3E)

This is so simple and one of my favorite examples to show the utility of regex.

In this regex pattern:

*   \\d – this represents any digit from 0 to 9
*   \+ – this is a quantifier that means “one or more” of the preceding element (which is a digit).

So what this means is that this regex pattern is going to identify where a number starts in the text string, and it is going to keep going till it finds a non-digit character.

And since I am using REGEXEXTRACT, it will extract and give me all the numbers in one go.

And what if you have multiple numbers in the same cell (as shown below) and you want to extract all numbers in one cell?

You can use the following formula:

\=TEXTJOIN(", ",TRUE,REGEXEXTRACT(A2, "\\d+",1))

![TEXTJOIN and REGEXEXTRACT formula to get all numbers from string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20767%20247'%3E%3C/svg%3E)

In the above formula, I have used _REGEXEXTRACT(A2, “\\d+”,1)_, where I have used 1 as the second argument, which extracts all the numbers and gives it in separate cells.

The TEXTJOIN function then combines all the numbers and gives them in one cell (separated by a comma).

Example 7 – Extract URLs from Text String
-----------------------------------------

Below, I have some data in column A, and I want to extract only the URLs from this data in column B.

![Dataset with urls to extract using regex formulas in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20765%20168'%3E%3C/svg%3E)

Here is the formula to do this:

\=REGEXEXTRACT(A2, "\\b(https?://\[^\\s\]+|www.\[^\\s\]+)\\b")

![Formula to extract urls from string in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20833%20240'%3E%3C/svg%3E)

In the above regex pattern:

*   \\b – This represents a word boundary. It ensures the pattern matches whole words, not parts of words.
*   (…): Parentheses group parts of the regex together.
*   https?://: – this would match http:// as well as https://
*   \[^\\s\]+ – this would look for any character that is not whitespace and will continue to look till it finds a whitespace
*   | – this is an OR operator, separating two alternatives
*   www. -this matches “www.” literally
*   \[^\\s\]+ – this would look for any character that is not whitespace and will continue to look till it finds a whitespace
*   \\b – another word boundary to end the match

Example 8 – Get Phone Number in Specific Format
-----------------------------------------------

You can use the REGEXREPLACE function in Excel to find a pattern and replace it with something else.

This replacement could be a completely different string or a different format of the pattern REGEXREPLACE has found.

Below I have a data set where I have some [phone numbers](https://trumpexcel.com/format-phone-numbers-excel/)
 in different formats in column A, and I want them all in the standard (XXX) XXX-XXXX format.

![Phone numbers data set in Excel to format](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20372%20281'%3E%3C/svg%3E)

Here is the formula to do this:

\=REGEXREPLACE(REGEXREPLACE(A2, "\[^\\d+\]", ""),"^(\\+?\\d{0,3})?(\\d{3})(\\d{3})(\\d{4})$","($2) $3-$4")

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20718%20425'%3E%3C/svg%3E)

Let me explain how this works:

*   REGEXREPLACE(A2, “\[^\\d+\]”, “”) – This part of the formula removes everything that is not a digit and gives us only the numbers as one continuous string
*   ^(\\+?\\d{0,3})? – This is an optional group that can match a plus sign along with 0-3 digits. But since there is a question mark before the plus sign as well as the entire group, it means that it will match an empty string, a plus sign with up to three numbers, or just up to three numbers.
*   (\\d{3})(\\d{3})(\\d{4})$ – this part of the pattern will create three groups of three digits, three digits, and four digits. The $ means that these need to be at the end, so the last ten digits are taken by this.
*   ($2) $3-$4 – this is the part where we are replacing the identified three groups (in the above [bullet point](https://trumpexcel.com/bullet-points/)
    ) and making them show up in the (XXX) XXX-XXXX format.

Example 9 – Check Text Starting/Ending with a Specific Word
-----------------------------------------------------------

One common use case of REGEX is to check whether a string contains a specific word or not.

While this can be easily done in Excel with functions such as FIND or XLOOKUP, with the REGEXTEST function, you can take it up a notch.

Below, I have a dataset where I have some questions and comments in column A, and I want to extract all the questions from this data.

![Questions and comments data set for Regex](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20998%20312'%3E%3C/svg%3E)

Here is the formula that will do this:

\=FILTER(A2:A12,REGEXTEST(A2:A12, "^(what|how|when|where)|\\?$"))

![Formula to extract only questions using regex in Excel](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201001%20361'%3E%3C/svg%3E)

In the above formula, I have used a REGEXTEST function with the following pattern:

_^(what|how|when|where)|\\?$_

The above pattern looks for any sentence that starts with the words what, how, when, and where and ends with a question mark. Whenever this pattern matches, it returns a TRUE. Otherwise, it returns a FALSE.

This formula is then wrapped inside the [FILTER function](https://trumpexcel.com/filter-function/)
 that extracts and only gives the result where there is a question in column A.

In case you want to get all the cells where there is no question, you can use the below formula:

\=FILTER(A2:A11,IF(REGEXTEST(A2:A11, "^\[^(What|How|When)\].\*\[^?\]$"), TRUE, FALSE))

![Formula in Excel using regex to extract everything that is not a question](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20998%20385'%3E%3C/svg%3E)

Example 10 – Check if the String Contains Dates
-----------------------------------------------

Below, I have a data set where I have some cells that contain dates, and I want to use a regex pattern to check whether the cell contains a date or not.

![Dataset with Date in Excel Regex](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20421%20196'%3E%3C/svg%3E)

Here is the formula to do this:

\=REGEXTEST(A2, "\\d{2}\[/.-\]\\d{2}\[/.-\]\\d{4}")

![Formula to extract date using regex](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20733%20243'%3E%3C/svg%3E)

The above formula checks whether there is a date in the cell or not, and if there is a date, then it returns a TRUE; else, it returns FALSE.

In the regex pattern, I have hard-coded the date formats as DD/MM/YYYY or DD.MM.YYYY or DD-MM-YYYY.

You can modify the formula if there is any other date pattern you would like to include.

If you want to extract the date from each cell, you can use the below formula:

\=IFERROR(REGEXEXTRACT(A2:A6, "\\d{2}\[/.-\]\\d{2}\[/.-\]\\d{4}"), "No date found")

Example 11 – Check If String Contains Specific Words
----------------------------------------------------

Below, I have a data set, and I want to check whether the cells contain the words Excel, Python, or both.

![Dataset to extract specific words from text](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20445%20168'%3E%3C/svg%3E)

Here is the formula to do this:

\=REGEXTEST(A2, "Python|Excel")

![REGEXTEST formula to check whether specific words exist or not](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20690%20212'%3E%3C/svg%3E)

In the above formula, I have used the pattern _Python|JavaScript_, which is an OR operator that checks whether the words Python or Javascript appear anywhere in the cell or not.

Here are some variations of the patterns you can use:

*   ^(Python|JavaScript) – Starting with Python or JavaScript
*   (Python|JavaScript)$ – Ending with Python or JavaScript
*   ^(?!.(?:Python|JavaScript)).$ – Not including Python or JavaScript
*   ^(?:(?=._Python)(?!._JavaScript)|(?=._JavaScript)(?!.Python)).$ – Including either Python or JavaScript, but not both .(?:Python|JavaScript). – Including at least one of Python or JavaScript, possibly both ^(?!._Python)(?!.JavaScript).$ – Including neither Python nor JavaScript
*   (?i)Python|JavaScript – Case-insensitive match for Python or JavaScript

In this article, I showed you a couple of examples of using the new REGEX functions in Excel. To be honest, I’ve barely scratched the surface, and there are many more amazing things you can do with creating your own regex patterns.

If you have come across a useful example, I would love to hear about it in the comments section.

**Other Excel articles you may also like:**

*   [Excel Functions](https://trumpexcel.com/excel-functions/)
    
*   [VLOOKUP vs XLOOKUP Function – What’s the Difference?](https://trumpexcel.com/excel-functions/vlookup-vs-xlookup/)
    
*   [Formula vs Function in Excel](https://trumpexcel.com/formula-vs-function-excel/)
    
*   [Advanced Excel Functions and Formulas](https://trumpexcel.com/advanced-excel-functions-formulas/)
    
*   [How to Extract a Substring in Excel (Using TEXT Formulas)](https://trumpexcel.com/extract-a-substring-in-excel/)
    
*   [Extract Numbers from a String in Excel](https://trumpexcel.com/extract-numbers-from-string-excel/)
    
*   [How To Remove Text Before Or After a Specific Character](https://trumpexcel.com/remove-text-before-after-character-excel/)
    
*   [Excel Wildcard Characters](https://trumpexcel.com/excel-wildcard-characters/)
    

Sumit Bansal

Hey! I'm Sumit Bansal, founder of trumpexcel.com and a Microsoft Excel MVP. I started this site in 2013 because I genuinely love Microsoft Excel (yes, really!) and wanted to share that passion through easy Excel tutorials, tips, and [Excel training videos](https://www.youtube.com/@trumpexcel/)
. My goal is straightforward: help you master Excel skills so you can work smarter, boost productivity, and maybe even enjoy spreadsheets along the way!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free-Excel-Tips-EBook-Sumit-Bansal-1.png](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK

![Free Excel Tips EBook Sumit Bansal](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20800'%3E%3C/svg%3E)

**FREE EXCEL E-BOOK**

Get 51 Excel Tips Ebook to skyrocket your productivity and get work done faster

   

Name 

Email 

SEND ME THE EBOOK