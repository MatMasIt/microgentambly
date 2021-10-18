# microgentambly

![GitHub](https://img.shields.io/github/license/MatMasIt/microgentambly)

Micro assembly-like interpreted languages
Work in progress, does not support many features atm

you can check the prorgams by running
```
python3 gg.py examples/filename.py
```
Current instruction set
|Instruction|Arguments|Description|Examples|
|---|---|---|---|
|**INT**|variable_name|Declares an integer|`INT a`|
|**SET**|variable_name,value|Sets a value|`SET a 0`|
|**INC**|variable_name|Increments variable by 1|`INC a`|
|**DEC**|variable_name|Decrements variable by 1|`DEC a`|
|**CP**|var1,var2|Copies the value of the left variable into the right one|`CP a,b`|
|**JL**|label,var1,var2 or value|If var2 or the value is less than var 1, jump to label|`JL lab v1 v2`|
|**JM**|label,var1,var2 or value|If var2 or the value is more than var 1, jump to label|`JM lab v1 v2`|
|**JLE**|label,var1,var2 or value|If var2 or the value is less or equal than var 1, jump to label|`JLE lab v1 v2`|
|**JME**|label,var1,var2 or value|If var2 or the value is more or equal than var 1, jump to label|`JME lab v1 v2`|
|**OUT**|freeform text|output text $variable$s will be replaced|`OUT Hello $user$`|
|**IN**|type,variable,request|Input a value, printing a text|`IN w Width`|
|**END**|-|Quit program|`END`|
