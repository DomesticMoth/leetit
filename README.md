# leetit
1337 translator lib

# Instalation
```
$ pip install leetit
```

# Usage
Simple example:  
```Py
import leetit
 
print(leetit.leet("xacker"))
print(leetit.leet("xacker", seed=12345, percent=30))
```

# Transformations
In order to get a leetspeak from ordinary English, you need to make three transformations:  
First you need to replace words and phrases with slang acronyms like "nice one" => "n1" or "owned" => "pwnd". To do this, the leetit library provides the `acronyms` function, which accepts text and an optional seed for the PRNG.
```Py
import leetit

print(leetit.acronyms("yeah, easy"))
print(leetit.acronyms("yeah, easy"), seed=12345)
```
Secondly, you need to change the morphology of words, for example, replacing the suffixes **-er** and **-or** with **-xor** or **-zor**. To do this, the leetit library provides the `morphology` function.  
```Py
import leetit

print(leetit.morphology("xacker"))
print(leetit.morphology("xacker"), seed=12345)
```
Thirdly, you need to replace all or some of the characters with others similar to them in various ways, for example, **e** can be replaced with **3** or **&**.  To do this, the `substitution` function is provided. In addition to text, this function can also accept the following parameters:  
1) The "seed" parameter accepts the seed for the rng.
2) The "percent" parameter specifies which part of the letters will be changed.
3) The "alphabet" parameter accepts a dictionary describing the rules for replacing letters (about dictionaries below).
4) The "chars" parameter accepts a list of letters for which replacement will be performed. By default, all Latin letters are included in this list.

## Alphabets
Alphabets are dictionaries in which lowercase letters act as the key, and arrays with characters with which this letter can be replaced as the value.  
The leetit library provides several alphabets out of the box:  
- leetit.ALPHABET_NUMBERS - contains options for replacing letters with numbers. For example, **e** to **3**.
- leetit.ALPHABET_ASCII - contains everything that is in leetit.ALPHABET_NUMBERS, and in addition options for replacing letters with other letters and combinations of letters and numbers. For example, **e** to **&**.
- leetit.ALPHABET_UNICODE_ONLY - contains options for replacing latin letters with special characters and letters of other languages.
- leetit.ALPHABET_UNICODE - contains a union of leetit.ALPHABET_ASCII and leetit.ALPHABET_UNICODE_ONLY

You can also compose your alphabets.

```Py
import leetit

print(leetit.substitution("To be, or not to be, that is the question"))
print(leetit.substitution("To be, or not to be, that is the question"), seed=12345)
print(leetit.substitution("To be, or not to be, that is the question"), percent=100, alphabet=leetit.ALPHABET_NUMBERS)
print(leetit.substitution("To be, or not to be, that is the question"), percent=100, alphabet=leetit.ALPHABET_ASCII)
print(leetit.substitution("To be, or not to be, that is the question"), percent=100, alphabet=leetit.ALPHABET_UNICODE_ONLY)
print(leetit.substitution("To be, or not to be, that is the question"), percent=100, alphabet=leetit.ALPHABET_UNICODE)

MY_ALPHABET = {
  "e": ["eeeeeeee"],
  "o": ["oooooooo"],
}

print(leetit.substitution("To be, or not to be, that is the question"), percent=100, alphabet=MY_ALPHABET)
```

And finally, the leetit library provides a `leet` function that performs all three transformations on the text in turn:  
```Py
def leet(text: str, seed: int = 1337, percent:int = 50, alphabet = ALPHABET_ASCII, chars = string.ascii_lowercase) -> str
```
```Py
import leetit
 
print(leetit.leet("To be, or not to be, that is the question"))
```
