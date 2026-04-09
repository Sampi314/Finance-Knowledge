# Debt Service Reserve Accounts

**Source:** https://edbodmer.com/debt-service-reserve-accounts

---

### Structure of DSRA Account

The DSRA account can be structured once the debt service is established from the debt schedule.  I used to get very worried about the DSRA and the circular references.  I have gotten over this fear by beginning with the structure of the DSRA that is illustrated below.  Always start with the debt service and then derive the required debt service reserve account.  This is illustrated in the screenshot below.  I often use the OFFSET function, but I just used 1/2 of the next year’s debt service in this case.  If you are using the OFFSET function, use adjust the column with a negative sign for the periods that you want to move from the future as illustrated below:

Debt Service Requirement = SUM(OFFSET(Debt Service, 0, – DSRA Periods))

In the above formula, the zero in the middle means that you do not adjust the rows. After you have established the amount of required reserve, compute the amount of required funding or allowed extinguishment. This is the total requirement less the opening balance of the DSRA account.  Finally, after computing the required reserve, compute the balance of the DSRA account.  This is a normal account with an opening and closing balance.  When computing the required funding, separate the funding between the funding during construction which will go into the sources and uses of funds (cash flow statement 1) and into the cash flow waterfall (cash flow statement 2). This funding can be split using TRUE and FALSE switches.

In the screenshot I have not included interest income, the possibility of using a letter of credit instead of a cash DSRA and finally, letter of credit fees.  These issues can be painful, especially from the perspective of circular references.  I have included these issues in the advanced project finance modelling section.

![](https://edbodmer.com/wp-content/uploads/2019/01/A-Z-Debt-DSRA.png)

![](https://pixel.wp.com/g.gif?v=ext&blog=182904628&post=8389&tz=0&srv=edbodmer.com&j=1%3A13.2.3&host=edbodmer.com&ref=&fcp=7460&rand=0.10910146330836634)