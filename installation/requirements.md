# System Requirements

Before installing QGISRed, verify that your computer meets the following requirements.

---

## Operating system

**Windows 10 or higher (x64)**.

QGISRed is not available for Linux or macOS. The calculation engine uses DLLs compiled in .NET that require the Windows environment.

---

##QGIS

**Version 3.28 or higher**, including the 4.x series.

### How to check your QGIS version

Go to **Help → About QGIS**. The version appears in the first line of the dialogue.

If your version is earlier than 3.28, download the latest LTR (Long Term Release) version from [qgis.org](https://qgis.org/download/).

> Versions prior to 3.28 are no longer supported by the plugin since QGISRed 0.18. If you need to work with an older version of QGIS, use QGISRed 0.17 or earlier.

---

## .NET Framework

**Version 4.8.1**.

### How to check if it is installed

1. Open **Control Panel → Programs → Programs and Features**.
2. Click **Turn Windows features on or off**.
3. Look for **.NET Framework 4.8.1** in the list. If it appears checked, it is already installed.

On Windows 11 and recent versions of Windows 10, the .NET Framework 4.8.1 may come preinstalled. On older versions or on Windows Server, you may need to download and install it manually from Microsoft.

---

## Internet connection

Necessary **the first time** the plugin is used, to download the dependencies (the DLLs of the calculation engine). Subsequent downloads (plugin updates) also require connection.

Once the dependencies are installed, QGISRed can work **without an internet connection**.

> If you do not have an internet connection, you can install the dependencies manually: ask someone to provide you with the ZIP of the dependencies and the .NET Framework 4.8.1 MSI installer. With both files you will be able to complete the installation without needing a connection. See section [Dependency management](dependencies.md) for more details.
