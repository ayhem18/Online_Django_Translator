# Project Description

This project is listed in the "hard" category in the "Django Developer" track offered by the online education platform
"JetBrains Academy". The project consists of 7 stages.

## Stage 1 Description:
The first step of this project is preparation for a convenient translation process. 
At this stage, there'll be only two available languages: English and French. 
The program should suggest to the user to choose the direction of the translation 
and the word to translate. Then, the confirmation message should be printed.

### Objectives
At this stage, your program should:

1. Output the welcoming message: Type "en" if you want to translate from French into English, or "fr" if you want to 
translate from English into French:
2. Take an input specifying the target language.
3. Output the message: Type the word you want to translate:
Output the confirmation message in the format You chose "language" as a language to translate "word", where language is
either "en" or "fr" and word is the word chosen by the
user. 

## Stage 2 Description:

At this stage, you'll be able to implement a real translator program! A great website called ReversoContext will help you to do that. ReversoContext is a multilingual translator tool that allows seeing original phrases that should be translated and their equivalents in other languages in contexts (example sentences). That's a very useful feature since the meaning of the word depends greatly on the context. Hence, when you see a context, it's easier for you to choose the right translation.

The goal of your program at this stage is to find translations and example sentences for a given word. The word can be either in French or in English, and the translation should be in the opposite language (that is, English or French, respectively).

To understand how to do this, go to ReversoContext and type any word you want to translate. After receiving the result, pay attention to the address bar of your browser. You will see the URL, for example:

https://context.reverso.net/translation/english-french/cheese

Here you see the language-translation pair «English-French», which represents the direction of translation, meaning that the translation is from English to French and not the other way around. After the last backslash, you can see the word being translated.

Your goal is to make your program act as if it visits the website for you. To make it happen, tell your program to generate the correct URL with the word you type, determine the translation direction, and send the URL to the website.

After getting to the needed page, the program should extract the required data: translations and sentences with usage examples. In the screenshot below, translations are highlighted with blue, and sentences for the target language are presented in a list in the right column.


### Objectives

At this stage, your program should:

1. Take an input specifying the target language (en if the user wants to translate from French into English, or fr if the user wants to translate from English into French).
2. Take an input specifying the word that should be translated.
3. Output the confirmation message in the format You chose "..." as a language to translate "...".
4. Form a request and connect to ReversoContext.
5. Check the HTTP status of the response of the website to your request. If the status code is 200, you are good to proceed! If not... Try again?
6. Output the response of the website to your request (200) and OK message to show that the connection is successful (so, the entire line should be 200 OK).
7. Output the line Translations.
8. Output a list with translations of the given word in the target language: ['bonjour', 'salut'].
9. Output a list with examples of sentences featuring the given word or any of its translations: ['Well, hello, freedom fighters.', 'Et bien, bonjour combattants de la liberté.']. Both the original versions of the sentences and their translations should be printed. You don't need to filter sentences in any way: just print all the sentences that ReversoContext output for the given language pair and the given word.

## Stage 3 Description:
mainly output related modifications

## Stage 4 Description:

