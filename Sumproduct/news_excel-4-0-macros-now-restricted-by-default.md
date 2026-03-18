# Excel 4.0 Macros Now Restricted by Default

**Source:** https://sumproduct.com/news/excel-4-0-macros-now-restricted-by-default/

---

[Home](https://sumproduct.com/)

\> Excel 4.0 Macros Now Restricted by Default

*   January 21, 2022

Excel 4.0 Macros Now Restricted by Default
==========================================

Excel 4.0 Macros Now Restricted by Default
==========================================

21 January 2022

July last year saw the release of a new Excel Trust Center _(sic)_ setting option to restrict the usage of Excel 4.0 (XLM) macros. From mid-January 2022, this has been made the default setting when opening Excel 4.0 (XLM) macros. This is to assist users in protecting themselves against related security threats.

This setting may be managed by visiting the Excel Trust Center in **File -> Options**, _viz._

**File -> Options -> Trust Center -> Trust Center Settings -> Macro Settings**

![](<Base64-Image-Removed>)

This setting now defaults to Excel 4.0 (XLM) macros being disabled in Excel (Build 16.0.14427.10000). It should also be noted that administrators may also use the existing Microsoft 365 applications policy control to configure this setting.

The Group Policy setting ‘Macro Notification Settings’ for Excel may be found in the following path and registry key:

*   **Group Policy Path:** User configuration -> Administrative templates -> Microsoft Excel 2016 -> Excel Options -> Security -> Trust Center
*   **Registry Key Path:** ComputerHKEY\_CURRENT\_USERSOFTWAREPoliciesMicrosoftOffice16.0excelsecurity.

Administrators also have the option to completely block all XLM macro usage (including in new user-created files) by enabling the Group Policy, ‘Prevent Excel from running XLM macros’, which is configurable via Group Policy Editor or registry key.

XLM is disabled by default in the September fork, version 16.0.14527.20000+

*   Current Channel builds 2110 or greater (first released in October 2021)
*   Monthly Enterprise Channel builds 2110 or greater (first released in December 2021)
*   Semi-Annual Enterprise Channel (Preview) builds 2201 or greater (created in January 2022, but not shipping until March 2022)
*   Semi-Annual Enterprise Channel builds 2201 or greater (will ship July 2022).

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/excel-4-0-macros-now-restricted-by-default/#0)
    
*   [Register](https://sumproduct.com/news/excel-4-0-macros-now-restricted-by-default/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/excel-4-0-macros-now-restricted-by-default/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/excel-4-0-macros-now-restricted-by-default/#0)

[](https://sumproduct.com/news/excel-4-0-macros-now-restricted-by-default/#0 "close")

top