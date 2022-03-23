# Project Description

This project is listed in the "hard" category in the "Django Developer" track offered by the online education platform
"JetBrains Academy". The project consists of 7 stages.
All stages in this project were validated by the platform test cases.
The project considers several topics such as: 
1. Requests library
2. Beautiful soup library
3. Web development basics: HTML and CSS
4. Command line arguments and argparse library
5. working with files

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

At this stage, you'll be able to implement a real translator program! A great website called ReversoContext 
will help you to do that. ReversoContext is a multilingual translator tool that allows seeing original phrases that should be translated and their equivalents in other languages in contexts (example sentences). That's a very useful feature since the meaning of the word depends greatly on the context. Hence, when you see a context, it's easier for you to choose the right translation.

The goal of your program at this stage is to find translations and example sentences for a given word. 
The word can be either in French or in English, and the translation should be in the opposite language (that is, English or French, respectively).

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

Great job! You now have a basic translation app that works well. Wouldn’t it be great though to expand it and include all available languages? This will finally make our translator a multilingual one!

The maximum number of languages our translator can support is 13. They are:

Arabic
German
English
Spanish
French
Hebrew
Japanese
Dutch
Polish
Portuguese
Romanian
Russian
Turkish
They should be enumerated in the program. A great idea is to present them with relevant numbers so that the user can choose the first as the original language and the second as a translation.

### Objectives
At this stage, your program should:

1. Output the welcoming message (let's update it a bit): Hello, welcome to the translator. Translator supports:
2. Output an enumerated list of languages. The enumeration should start from 1. The order of languages should be exactly as in the list above.
3. Take input (a number from the list) specifying the source language (the language from which the translation should be performed).
4. Take input (a number from the list) specifying the target language (the language to which the translation should be performed).
5. Take input specifying the word that should be translated.
6. Output the results as in the previous stage. At this stage, you don't need to print 200 OK anymore.

## Stage 5 Description:

Perfect! Your program already became a convenient tool. There are just a couple of stages left. Your translation app is flexible enough to be appreciated by many people worldwide, so let's make it even better: add the feature of translating the word to all the languages at once, and also save the search results to a text file so that the user could read the translations later.

### Objectives
Add the following functionality to your program:

1. Before taking an input specifying the target language, output the message Type the number of a language you want to translate to or '0' to translate to all languages:
2. If the user inputs 0 as the target language, translate the word to all available languages.
3. Output results to the terminal, as in the previous stage. At this stage, it's enough to print just one translation and one sentence pair per target language.
4. Save results of the search to a file named word.txt, where word is the word that was being translated.

## Stage 6 Description:
Let's try to change the way the user interacts with the program to make the process faster. 
To make your program more convenient, you can use command-line arguments. They make it possible to provide a program with all the data it needs using a simple command.

### Objectives
At this stage, your program should:

1. Instead of all inputs, take command-line arguments. The first argument is the name of the source language, 
2. the second argument is the name of the target language, the third argument is the word. If the word should be translated to all languages, the second argument will be "all".
The rest of the functionality should remain the same as in the previous stage.
3. You'll see some significant changes in the usability of the app!

## Stage 7 Description:
Your program works as expected! However, there’s a problem you should always keep in mind: the user can always input something that will break your program.

Up to this stage, we considered "perfect" inputs. But what if things go wrong? For example, you gave your program to someone who’s not familiar with the concept behind it. What if they try to translate to or from languages different from those you have in your code, or even start typing jabberwocky? Let's find some way to avoid this.

All these situations are called exceptions because you didn’t expect them to happen, and now your program will have to handle them.

### Objectives
Add the following functionality:

1. If the user inputs a name of a language that isn't available in the program, print the line Sorry, the program doesn't support <language> and quit the program.
2. If the connection with the website isn't successful, print the line Something wrong with your internet connection
3. If the user inputs a word that's not present in ReversoContext, print the line Sorry, unable to find <word>