# Monday Morning Mulling: July 2020 Challenge

**Source:** https://sumproduct.com/blog/monday-morning-mulling-july-2020-challenge/

---

[Home](https://sumproduct.com/)

\> Monday Morning Mulling: July 2020 Challenge

*   August 2, 2020

Monday Morning Mulling: July 2020 Challenge
===========================================

Monday Morning Mulling: July 2020 Challenge
===========================================

3 August 2020

_On the final Friday of each month, we set an Excel problem for you to puzzle over for the weekend. On the Monday, we publish a solution. If you think there is an alternative answer, feel free to email us. We’ll feel free to ignore you._

Welcome to this month’s Monday Morning Mulling. Our solution to this month’s challenge uses a function most of you never even have considered, or perhaps didn’t even _know_ existed…

**_The Challenge_**

“All” I wanted to do was be able to take a text string and split it up so that each element of text was split into a separate column **_formulaically_**, _e.g._

![](<Base64-Image-Removed>)

Note I have used different separators (delimiters) in the two examples displayed. The fact I have used four elements each time is entirely coincidental.

As usual, please feel free to refer to the [associated Excel file](https://sumproduct.com/assets/blog-pictures/2020/fff-mmm/july/mmm/sp-splitting-text-example.xlsm)
 to see how our solution works.

**_Suggested Solution_**

It’s not impossible to come up with some monstrous calculation using a combination of [text functions](https://www.sumproduct.com/thought/text-messages)
. Some of you may have worked out some horrendous formula that appears to work. I applaud you if you have.

But I am going to go another way; what about this little beauty?

![](<Base64-Image-Removed>)

For the formula in cell **G13**:

**\=TRANSPOSE(FILTERXML(“<x><y>”&SUBSTITUTE(E13,”,”,”</y><y>”)&”</y></x>”,”//y”))**

Er, what the..?

Maybe this needs some explanation. Let’s start with the highly popular and frequently used **FILTERXML** function. Hands up all those who use this function regularly…

**_The FILTERXML function_**

Until Excel 2013, Excel was mostly an offline application, although you could use VBA, Power Query / Get & Transform or Power Pivot in Excel to gain access to internet and online datasets. However, Excel 2013 changed all that and introduced two new functions to the world:

1.  **WEBSERVICE**, which provides immediate and easy access to any REST WebAPI assuming you have an internet connection by downloading the HTTP response of the provided URL; _and  
    _
2.  **FILTERXML**, which **parses** an XML string (_i.e._ a text string that contains an XML document) and returns a single element (known as a node or attribute) provided by an XPath. In case you are wondering, XPath is a query language for selecting XML elements such as nodes and attributes and works with both XML and HTML.

Therefore, **FILTERXML** tends to work in tandem with **WEBSERVICE** insofar that it makes sense of the long text string delivered by the former function and finds what you are looking for in that text string.

The **FILTERXML** function employs the following syntax to operate:

**FILTERXML(xml, xpath)**

The **FILTERXML** function has the following arguments:

*   **xml:** this is required and represents a string in a valid XML format
*   **xpath:** this is also required. This represents a string in a standard XPath format.

It should be noted that:

*   if **xml** is not valid, **FILTERXML** returns the _#VALUE!_ error value
*   if **xml** contains a namespace with a prefix that is not valid, **FILTERXML** returns the _#VALUE!_ error
*   the **FILTERXML** function is not available in Excel Online
*   the **FILTERXML** function is not available in Excel (2016) for Mac
*   Further, this function may appear in the function gallery in Excel for Mac, but it relies on features of the Windows operating system, so it will not return results on a Mac.

Here are some examples:

![](<Base64-Image-Removed>)

OK, so far so good. But there is another function used…

**_The SUBSTITUTE function_**

The **SUBSTITUTE** function, like the **REPLACE** function, replaces existing text with new text in text strings. It uses the following syntax to operate:

**SUBSTITUTE(text, old\_text, new\_text, instance\_number)**

where:

*   the **text** parameter is the string of text that contains the characters that we want to substitute
*   the **old\_text** parameter is the string of text that we want the function to look for in the **text** parameter
*   the **new\_text** parameter is the text string that is going to replace the **old\_text**
*   the **instance\_number** is the instance which we want the **old\_text** to be replaced by the **new\_text** parameter if there are multiple **old\_text** strings found. If excluded, all occurrences are replaced.

It is a simple to understand function.

**_Returning to Our Suggested Solution_**

Revisiting our example:

![](<Base64-Image-Removed>)

For the formula in cell **G13**:

**\=TRANSPOSE(FILTERXML(“<x><y>”&SUBSTITUTE(E13,”,”,”</y><y>”)&”</y></x>”,”//y”))**

Let’s review the first argument of **FILTERXML** for cell **G13**:

**“<x><y>”&SUBSTITUTE(E13,”,”,”</y><y>”)&”</y></x>”**

If we calculated this, we would get

**<x><y>alpha</y><y>beta</y><y>gamma</y><y>delta</y></x>**

Oh now, it’s completely clear (!).

Do you see that the text **alpha,beta,gamma,delta** has had the comma substituted for **</y><y>**, and then this has been “wrapped” inside

**<x><y>…</y></x>**

If you are familiar with XML or even HTML, you might be starting to see where this is all going. Consider these angular bracket elements:

*   **<x>** and **</x>** denote the start and end of the data **x** (you can replace **x** with pretty much any text string)
*   **<y>** and **</y>** denote the start and end of a **y** “node”, _i.e._ a building block of XML. Again, you can change **y** to an alternative annotation. The overarching idea is that an entire document is a document node; every element in a documane is an element node; text in an element is a text node, _etc_. We have **y** nodes!

Therefore, we have broken the text string up into its text nodes. Therefore,

**\=FILTERXML(expression, “//y”)**

means parse (split up) each **y** node. This will provide a list of the **y** nodes. If you are using a version of Excel that supports [\>dynamic arrays](https://www.sumproduct.com/thought/getting-arrays-spilling-the-beans-on-seven-new-functions)
, you would get the following:

![](<Base64-Image-Removed>)

Wrapping this function in **TRANSPOSE** swaps rows to columns and _vice versa_. The [associated Excel file](https://sumproduct.com/assets/blog-pictures/2020/fff-mmm/july/mmm/sp-splitting-text-example.xlsm)
 also demonstrates how this could be performed using “legacy” Excel where dynamic arrays are not recognised by selecting several cells once you have created the formula and pressing **CTRL + SHIFT + ENTER**.

It’s a little different, but this month shows you how sometimes you can use functions meant for something else completely and use them in an entirely different environment. We doubt anyone at Redmond envisaged this trick back when this function was coded!

Until next month.

_The Final Friday Fix will return on Friday 28 August with a new Excel Challenge. In the meantime, please look out for the Daily Excel Tip on our home page and watch out for a new blog every business workday._

[More Blog Articles](https://www.sumproduct.com/blog)

*   [Log in](https://sumproduct.com/blog/monday-morning-mulling-july-2020-challenge/#0)
    
*   [Register](https://sumproduct.com/blog/monday-morning-mulling-july-2020-challenge/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/blog/monday-morning-mulling-july-2020-challenge/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/blog/monday-morning-mulling-july-2020-challenge/#0)

[](https://sumproduct.com/blog/monday-morning-mulling-july-2020-challenge/#0 "close")

top