# LET Off the Leash

**Source:** https://sumproduct.com/news/let-off-the-leash/

---

[Home](https://sumproduct.com/)

\> LET Off the Leash

*   November 18, 2020

LET Off the Leash
=================

LET Off the Leash
=================

18 November 2020

March 2020 saw Microsoft announce a new Excel function, **LET**, for Office 365, albeit at the time of writing, only to the Insiders – now Beta – Channel. This allowed you to stop writing the same expressions time and time again in a formula or allowed portability of segments of a computation for different formulae. As Microsoft puts it, it’s “…names on a formula level”.

Now (November 2020), it’s been made Generally Available to all users of Excel subscribers in the Office 365 or Microsoft 365 in Production Current Channel.

In essence, this function assigned values or expressions to defined names and then passed these to calculation results. It may store intermediate calculations, values or defining names inside a formula. The defined names only apply within the scope of the **LET** function in a similar way to variables in general programming scenarios.

If you reuse the same expression multiple times in a formula, Excel calculates that expression multiple times. That’s _not_ a good thing. **LET** allows you to name the expression and refer to it using that name, similar to [**VAR** in a DAX expression](https://www.sumproduct.com/blog/article/power-pivot-principles/ppp-variables-in-dax)
, for those that know the language. Any named expression is calculated only once, even though it may be referred to many times in the formula. This can significantly improve performance considerably and speed up your spreadsheets.

Let’s recap the **LET** function. We must define pairs of names and associated values, and a calculation that uses them all, as the final argument. At least one name / value pair must be defined.

It has following syntax to operate:

**LET(name1, value1, \[name2…\], \[value2…\], calculation)**

where:

*   **name1**: the name for the first value
*   **value1**: the value to associate with the first name
*   **name2** (optional): additional names for second and subsequent values
*   **value2** (optional): additional values for the second and subsequent values
*   **calculation**: this is the calculation to perform. This is always the final argument and it can refer to any of the defined names in the **LET**.

The main benefits of using **LET** function includes:

*   **readability:****LET** function tracks the changes in defined cells or expression in dynamic way, so there is no need to remember what a specific range / cell reference referred to. With the ability to define variables, it can provide more meaningful context to end users
*   **performance:****LET** allows named expression in the formula and calculated only once, even if it is referred to many times in the formula. This can significantly improve performance for complex expressions.

Let’s return to our past example. If we are considering **LET**, how about we use the property rental market! Suppose we run a company where salespeople make commission based upon 1% of the average of the square of the weekly rent, _e.g._ if Annie makes two sales of $400 and $300, then the average of the amounts squared would be (3002 + 4002) / 2 = 125,000 and 1% of that would be $1,250. Not much incentive to make lots of sales, is there? It’s not my fault she negotiated her contract badly…

Anyway, it’s convoluted, but we are trying to construct an example which we cannot simply solve using a standard Excel formula like **[\>AVERAGEIFS](https://www.sumproduct.com/blog/article/a-to-z-of-excel-functions/the-averageifs-function)
**!

![](https://sumproduct.com/wp-content/uploads/2025/05/f32e5a15e2cf9c3e4d2d058458ce054d-26.jpg)

The formula in cell **C21** is given by

**\=LET(BusinessUnit, B3\_B15=C17,  
SalesPerson, C3\_C15=C18,  
Selection, BusinessUnit\*SalesPerson,  
Commission, C19,  
SalesAmt, D3:D15,  
SUMPRODUCT(Selection\*SalesAmt^2)\*Commission/SUMPRODUCT(Selection))**

The final argument is the formula – but more on that shortly. Before that, there are pairs of expressions where the first element is the name and the second is an expression for a value. Let’s go through all of these arguments (mainly in pairs):

*   **BusinessUnit, B3\_B15=C17** define the array **BusinessUnit**, which is an array of TRUE and FALSE values depending on whether the Business Unit is equal to the value in cell **C17** (which is “C” in the illustration). Therefore, we have {FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, TRUE, TRUE, FALSE, FALSE}
*   **SalesPerson, C3\_C15=C18** generate a similar array (named **SalesPerson**), which provides TRUE and FALSE values depending on whether the salesperson was Annie. Therefore, we have {TRUE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE, TRUE, FALSE, FALSE}
*   **Selection, BusinessUnit\*SalesPerson** now shows the value of **LET**. This names the value of the product of the first two parameters **Selection** without having to write out the formula again and, more importantly, _without having to calculate them a second time unnecessarily_. This results in TRUE/FALSE expressions multiplied by other TRUE/FALSE expressions, which results in a one if both are TRUE and zero (0) otherwise. Therefore, we have {0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0}
*   **Commission, C19** is relatively simple, naming the value in cell **C19** (1%) **Commission**
*   Similarly, **SalesAmt, D3:D15** apply the name **SalesAmt** to the range **D3:D15** _for the purposes of this formula_. Therefore, we have {374, 347, 159, 393, 478, 354, 159, 203, 371, 300, 400, 187, 140}
*   Finally, the formula **SUMPRODUCT(Selection\*SalesAmt^2)\*Commission/SUMPRODUCT(Selection)** calculates the commission similarly to the approach explained above. However, **Selection**, **SalesAmt** and **Commission** are merely referenced and neither need to be recalculated nor written out in full.

This may seem verbose, but it speeds up calculation time considerably, and makes formulae easier to read (once you get your head around this new approach). Further, **LET** only defines the range name _within_ the formula. These are not general range names in the spreadsheet – Excel will not recognise them outside of this **LET** formula.

To be crystal clear, there are two key differences between defined range names and this now Generally Available **LET** function:

1.  **LET** allows you to see the definition of the name there and then without jumping to the definition elsewhere. Yes, the formula may be longer in the cell, but the user can hopefully follow it without audit tools
2.  When Excel sees a defined name in a formula, it pauses the current formula, evaluates the defined name’s formula to get a result, and returns to the original formula. A variable defined using **LET** is only ever evaluated once.
    
    An example that shows the difference is **\=LET(x, RANDBETWEEN(1, 1000000), x – x)**. This formula will always return zero, since **RANDBETWEEN(1, 1000000)** gets evaluated and then assigned to **x**, which never changes, so **x – x** = 0.
    
    If you instead use the name manager to define the name **x** as **\=RANDBETWEEN(1, 1000000)**, then entering **\=x – x** is almost never going to be zero, since each **x** in the formula causes **RANDBETWEEN** to be evaluated.
    

It should also be noted that you must be careful with your order of arguments and defining reference names. Name definitions can only make use of prior and not subsequent names. In the example above, **Selection** could only be defined once **BusinessUnit** and **SalesAmt** had both been defined.

Now that it has become Generally Available, there have been some changes made to **LET**:

*   **Autocompletion of names:** if you have defined the name earlier, Excel will now recognise it. There is now a special icon,

![](<Base64-Image-Removed>)

which indicates that you may autocomplete the formula with the name so identified

![](<Base64-Image-Removed>)

*   **Allowed names:** due to the rich Data Types also making use of the dot (“.”), this character is no longer legal in names bound by **LET**. If you have already created such naughty names in files created during the Insider phase, the name will be “silently upgraded”. Better than euthanised, we suppose
*   **Localisation changes:** localisation has now been removed from the **LET** function. **LET** is now the name of the function in all stockkeeping units (SKUs) of Excel and is no longer localised. **LET** it be.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/let-off-the-leash/#0)
    
*   [Register](https://sumproduct.com/news/let-off-the-leash/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/let-off-the-leash/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/let-off-the-leash/#0)

[](https://sumproduct.com/news/let-off-the-leash/#0 "close")

top