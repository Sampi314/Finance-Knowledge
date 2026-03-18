# Restrict Usage of Excel 4.0 (XLM) Macros with New Macro Settings Control

**Source:** https://sumproduct.com/news/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings-control/

---

[Home](https://sumproduct.com/)

\> Restrict Usage of Excel 4.0 (XLM) Macros with New Macro Settings Control

*   July 27, 2021

Restrict Usage of Excel 4.0 (XLM) Macros with New Macro Settings Control
========================================================================

Restrict Usage of Excel 4.0 (XLM) Macros with New Macro Settings Control
========================================================================

27 July 2021

A new Excel Trust Center _(sic)_ settings option to further restrict the usage of Excel 4.0 (XLM) macros has now been made Generally Available. To better protect Microsoft 365 users against malicious macro-based threats, Microsoft recently expanded the integration of what is known as the Antimalware Scan Interface (AMSI) with Office 365 to include the runtime scanning of Excel 4.0 (XLM) macros.

Building on the recent release of AMSI integration for XLM macros, this new Trust Center setting enables Microsoft 365 customers to further protect themselves against the latest threats. Located in the ‘Trust Center Macro Settings’, this new checkbox setting, ‘Enable Excel 4.0 macros when VBA macros are enabled’, allows users to individually configure the behaviour of XLM macros **_without_** impacting their VBA macro counterparts.

The Excel Trust Center settings may be accessed through **File > Options > Trust Center > Trust Center Settings > Macro Settings**.

When the checkbox is selected, the above settings configured for VBA macros will also apply to XLM macros. To disable XLM macros without a notification, deselect the checkbox setting (this is the option recommended by Microsoft), as this configuration opts for a more secure behaviour. There is no impact to any default or previous macro settings configurations with this release; however, users should be aware that a change in default XLM macro behaviour is coming soon _(see below)_.

![](<Base64-Image-Removed>)

Customers can now independently disable XLM macros in the Trust Center Macro Settings by unchecking the setting “Enable Excel 4.0 macros when VBA macros are enabled.”

**_Availability_**

This setting is currently available in Excel (build 2104).

Administrators can also use the existing Microsoft 365 applications policy control to configure this setting. The Group Policy setting ‘Macro Notification Settings may be found at **User configuration > Administrative templates > Microsoft Excel 2016 > Excel Options > Security > Trust Center**.

Administrators also have the option to completely block all XLM macro usage (including in new user-created files) by enabling the Group Policy, ‘Prevent Excel from running XLM macros’, which is configurable via Group Policy Editor or registry key:

*   Group Policy Path: **User configuration > Administrative templates > Microsoft Excel 2016 > Excel Options > Security > Trust Center**
*   Registry Key Path: **ComputerHKEY\_CURRENT\_USERSOFTWAREPoliciesMicrosoftOffice16.0excelsecurity**

Do be aware that while the initial release of this setting does not impact any existing or default macro settings configurations, XLM macros will soon be disabled by default. Users should expect this upcoming change in default behaviour to occur in the following M365 updates:

*   2021 October Current Channel
*   2021 December Monthly Enterprise Channel
*   2022 January Semi-Annual Enterprise Channel (Preview)
*   2022 July Semi-Annual Enterprise Channel.

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings-control/#0)
    
*   [Register](https://sumproduct.com/news/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings-control/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings-control/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings-control/#0)

[](https://sumproduct.com/news/restrict-usage-of-excel-4-0-xlm-macros-with-new-macro-settings-control/#0 "close")

top