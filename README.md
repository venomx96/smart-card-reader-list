### Read name and serial numbers from smartcard devices, add a lines in list.txt

Exemple :
```
Ingenico 01730418 TL XIRING 1 0
Ingenico 01730418 TL XIRING 2 0
KAPELSE 00722157 KAP-LINK2 0 0
KAPELSE 00722157 KAP-LINK2 1 0
KAPELSE 00722157 KAP-LINK2 2 0
```

( 1x Kap&Link2 from kapelse and 1x Olaqin Set-2 )

----------------------------------------------------------------------------------------------------------------------

### To build, you need Python 3.10


You can use pre-build package :

https://github.com/venomx96/smart-card-reader-list/releases/download/Release/smart-card-reader-list.zip



Depencies :

```pip install pyscard```

```pip install py2exe```

Build : 

```setup.py py2exe```
