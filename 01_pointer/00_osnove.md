## Naslov spremenljivke
Uporabnik vnese številko.
Izpiši (v šestnajstiškem sistemu) kje v pomnilniku se nahaja številka.

## Vrednost na naslovu
Uporabnik vnese naslov pomnilnika.
Izpiši kaj se nahaja na izbranem naslovu in kje v pomnilniku se nahaja naslov.

## Rezervacija prostora
Rezerviraj prostor v pomnilniku za 10 celih številk z malloc funkcijo.
Izpiši kaj se nahaja na tem prostoru. Uporabljaj *() in [] operator.
Na koncu sprosti prostor v pomnilniku z funkcijo free.

## SPISEK JE POINTER
Definiraj spremenljivko a kot spisek predefiniranih številk.
Izpiši...
* a, &a[0]
* a[0], *(a+0)
* a[1], *(a+1)
* a[2], *(a+2)

## POINTER JE SPISEK
Definiraj pointer a z mallocom in vnesi v rezerviran prostor predefinirane številke.
Izpiši...
* a, &a[0]
* a[0], *(a+0)
* a[1], *(a+1)
* a[2], *(a+2)

## Izpiši območje v pomnilniku
Definiraj 5 spremenljivk z specifičnimi vrednostmi.
Izpiši katere vrednosti se nahaja nad naslovom zadnje spremenljivke.

## Pointer pointerja
Definiraj spremenljivko a, shrani naslov spremenljivke v pointer b, shrani naslov spremenljivke b v pointer c,
shrani naslov spremenljivke c v pointer d.
Izpiši vrednost spremenljivke a z spremenljivko d.

## Naslov funkcije in argumentov
Definiraj funkcijo ki sprejme argument in vrne isti argument.
V glavnem programu ustvari spremenljivko, izpiši kje v pomnilniku se spremenljivka nahaja.
Nato spremenljivko pošlji v klic ustvarjene funkcije in v funkciji izpiši kje se nahaja spremenljivka v pomnilniku.
V glavnem programu nato izpiši kje v pomnilniku se nahaja vračajoča vrednost funkcije.
Izpiši tudi kje v pomnilniku se funkcija nahaja.

## Spremeni vrednost spremenljivke
Definiraj funkcijo ki sprejme argument vrne pa nič.
V glavnem programu definiraj spremenljivko katero vrednost spremeni v definirani funkciji.
Preveri če se je v glavnem programu spremenljivka resnično spremenila.

## Memory leak
Z mallocom rezerviraj neskončno prostorov v pomnilniku in poglej v taskmanagerju kako
se pomnilnik polne. Pri vsaki rezervaciji prostora izpiši koliko je trenutno zasedenega prostora
v gigabayt enotah.
Izpiši pri koliko gigabaytih zmanjka prostora na pomnilniku.

## Software hacking
Ustvari 2 programa. V prvem programu definiraj spremenljivko in v njo zapiši vrednost ter njen naslov, prvi program naj vsako sekundo
izpiše vrednost spremenljivke. V drugem programu probaj spremeniti vrednost spremenljivke kjer se nahaja prva spremenljivka v prvem programu.
