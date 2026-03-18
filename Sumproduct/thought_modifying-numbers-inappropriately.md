# Modifying Numbers Inappropriately

**Source:** https://sumproduct.com/thought/modifying-numbers-inappropriately/

---

[Home](https://sumproduct.com/)

\> Modifying Numbers Inappropriately

*   May 14, 2025

Modifying Numbers Inappropriately
=================================

How accountants can potentially cause major errors in their sums (and how to avoid it!).

Modifying Numbers Inappropriately
=================================

_As a professional modeller for more years than he’d care to admit Liam Bastick highlights some of the common mistakes prevalent in financial modelling / Excel spreadsheeting. For example, this article highlights how accountants can potentially cause major errors in their sums…_

### A Common Scenario

Often when building even the simplest financial model, unit conversion becomes necessary. For example, your business may sell 437,911 widgets at a unit price of $12.50 each. However, in your output summary sheet for senior management, do you really wish to show that the revenue earned is $5,473,888 or is it more likely that you will display this figure as $5.5m?

Sound familiar? If the latter idea strikes accord, you may be in danger of making a mistake in your additions. As a model auditor with over 25 years’ experience, I note that over 95% of all modellers will modify their number with a calculation such as

\=437911\*12.50/1000000.

Yes, cell references may be used instead and the million factor may be a range name, but in essence the value is derived by dividing the product of volume and unit sales price by one million.

It’s just so much easier to read and basically so much more _dangerous._

Let me explain: output sheets are usually dashboards of various key factors that management requires in order to make informed decisions, _e.g._

### Dashboard Output Example

![](<Base64-Image-Removed>)

The problem is, all sorts of different figures may appear on such an output. For example, key outputs could include:

*   Unit prices (in $’s)
*   Overall profitability (in $m)
*   Internal Rate of Return (%)
*   Payback date (date)
*   Asset turnover (multiple)
*   Other outputs (MWh, GBytes, KHz)

I hope that modellers are not adding percentages to KHz (not much I can do about that), but it is common for modellers to confuse financial data, _e.g._

\=$5.5m-$3.76k = $1.74??

Not only have I no idea of units, the answer should be $5,470,128. If you don’t think you have ever made that mistake, are you sure you had the units right for your accounting ratio or debt credit metric? It can be a scary thought.

### How To Avoid: Formatting Rather Than Modifying

This issue is easily overcome. We need to remember from our example that $5.5m is actually $5,473,888 and we should make the number _appear_ to be $5.5m (by formatting) rather than _actually_ be 5.5 (by modifying).

To do this we use number formatting (**CTRL+1**) on the calculation:

### Number Formatting the Calculation

![](<Base64-Image-Removed>)

In the above illustration, the unit price has simply been multiplied by the volume. Then, the resulting product has been custom number formatted as displayed in the dialog box:

$#,##0.0,,“m”

This may not be immediately obvious! Time for a crash course in hieroglyphics:

*   **$** is the currency symbol. Excel recognises various symbols, including the euro, the dollar and the yen
*   **\#** means put a number _if necessary_
*   **0** means put a number whether it’s necessary or not, e.g. the number format “000” used on the number 7 would provide you with a Licence To Kill: 007
*   **,** (comma) is the thousands separator and serves two purposes. It puts a comma in at the thousand / million / billion mark when the syntax “#,###” or “0,000” _etc._ is used, but it also **divides** by a thousand each time it is entered after the number formatting so “0,” will be in thousands, “##,,” will be in millions and so on
*   **.** (decimal point / period) is the decimal point
*   **“m” –** whatever is inserted inside inverted commas is added as text to the number format.

Therefore, **$#,##0.0,,“m”** will display numbers in $m to one decimal place (_i.e._ to the nearest hundred thousand) but the underlying number will **still** be 5,473,888 and hence avoid a common mistake in financial modelling.

### Word to the Wise

Before everyone writes in and comes up with 34,380 _(should that be 34.4k?)_ reasons why a calculation should be divided by a conversion factor rather than just given the appearance it has been, I do recognise sometimes this needs to be done. My point is, often it does not and using a divisor is fraught with risks – so why not avoid the issue?

Also, I have only touched the tip of the iceberg for custom number formatting. If you want to find out more, please refer to the associated [Excel file](https://sumproduct.com/assets/thought-files/modifying-numbers-inappropriately/sp-customising-number-formats-examples.xls)
.

[More Thoughts](https://www.sumproduct.com/thought)

*   [Log in](https://sumproduct.com/thought/modifying-numbers-inappropriately/#0)
    
*   [Register](https://sumproduct.com/thought/modifying-numbers-inappropriately/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/thought/modifying-numbers-inappropriately/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/thought/modifying-numbers-inappropriately/#0)

[](https://sumproduct.com/thought/modifying-numbers-inappropriately/#0 "close")

top