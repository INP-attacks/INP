# INP
PoC implementation of INP with Chromium
This PoC was tested on a Windows 10 x64 machine.

## How to install INP with Chromium
### Folders creation
You must create the following folders in your PC:
* C:\Temp\INP
* C:\Temp\INP\DNS

### Download folders
Download the directories available in this repository to your Windows machine:
* [dist](https://github.com/INP-attacks/INP/tree/master/dist) -> C:\Temp\INP\dist
* [INPChromiumSupporter](https://github.com/INP-attacks/INP/tree/master/INPChromiumSupporter) -> C:\Temp\INP\INPChromiumSupporter

### Download and compile the Chromium source code with the relevant INP modifications
All details are available in [Chromium Files](https://github.com/INP-attacks/INP/tree/master/Chromium%20Files)


## How to run the PoC
* You may want to use an XML configuration files for customized IPv4 private address spaces.
** Look at [INP.xml](https://github.com/INP-attacks/INP/blob/master/INP.xml) for an example.
** Create INP.xml file, if necessary, in C:\Temp\INP\INP.xml
* Run C:\Temp\INP\INPChromiumSupporter\INPChromiumSupporter.exe
* Run your compiled chrome.exe
