# Power Pivot 10-4

**Source:** https://sumproduct.com/news/power-pivot-10-4/

---

[Home](https://sumproduct.com/)

\> Power Pivot 10-4

*   August 4, 2015

Power Pivot 10-4
================

Power Pivot 10-4
================

4 August 2015

We recently mentioned there appears to be a problem with Power Pivot in Excel 2010 when updating to Windows 10. It appears – although we have not been able to confirm it for ourselves yet – that the problem lies with the version of .NET (version 4.6), which is installed as part of the update. Apparently, .NET version 4.6 includes a new Just-In-Time (JIT) compiler for 64-bit processes, called **RyuJIT**, which is what is causing the current problem.For now, whilst a proper fix is being created, the quick workaround is apparently to disable RyuJIT via a registry key or by using PowerShell as follows:

*   **Registry key:** Under HKEY\_LOCAL\_MACHINESOFTWAREMicrosoft.NETFramework add “useLegacyJit” DWORD with a value of 1;
*   **PowerShell:** Set-ItemProperty -Path HKLM:SoftwareMicrosoft.NETFramework -Name useLegacyJit -Type DWord -Value 1.

Hopefully, this resolves the problem for the interim.

![](<Base64-Image-Removed>)

[More Articles](https://www.sumproduct.com/news)

*   [Log in](https://sumproduct.com/news/power-pivot-10-4/#0)
    
*   [Register](https://sumproduct.com/news/power-pivot-10-4/#0)
    

Remember me 

Sign in

      

[Forgot your password?](https://sumproduct.com/news/power-pivot-10-4/#0)

Create account

      

Lost your password? Please enter your email address. You will receive mail with link to set new password.

  

Reset password

[Back to login](https://sumproduct.com/news/power-pivot-10-4/#0)

[](https://sumproduct.com/news/power-pivot-10-4/#0 "close")

top