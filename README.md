# SIOL 

SIOL (Standard Input-Output Language) is a file querying language designed for a Windows environment. It is currently capable of doing file reading, writing, and other related operations without a GUI interface. Many commands are designed to emulate UNIX style file operations. The current release is stable.

## Features

SIOL is a Python based command-line tool to execute file instructions directly, without direct access to any particular text editor. The goal of SIOL is to keep the instruction set basic yet complete. 

At its core, SIOL supports a few basic operations:

* Read and write capabilities

* Text counting features

* File moving operations 

## Syntax

SIOL has a simple, SQL-style syntax interface.

```SYNTAX NOTES: ONLY ONE WHITESPACE BETWEEN IDENTIFIERS, ALL PHRASES MUST START WITH A KEYWORD
KEYWORDS: QUERY, QUIT, --VERSION

/*THE GENERAL SYNTAX OF A QUERY COMMAND IS QUERY [FUNCTION] [ARGUMENT]*/
QUERY -> FILE
	 ->
	 	DEFAULT EXTENSION IS '.txt', SPECIFY FILETYPE AS THIRD ARG, E.G. 'query file .cpp hello_world' vs. 'query file hello_world' (.txt)
		CREATES A NEW FILE IF THE FILE SPECIFIED DOES NOT EXIST, ELSE OPENS IT 
	 WRITELN
	 ->	(MESSAGE) WRITES MESSAGE TO NEW LINE
	 READLN
	 ->
	 	(LINE#) SHOULD BE ARGS PASSED TO READLN 
		(all) PRINTS ALL LINES
	 DELETELN
	 ->
	 	(LINE#) SHOULD BE ARGS PASSED TO DELETELN
	 	(all) DELETES ALL LINES
	 INSERTLN
	 ->
	 	(LINE#) (MESSAGE TO BE INSERTED)
	 CLOSE
	 	FILE (CLOSES THE CURRENT ACTIVE FILE)
	 GET
	 ->
	 	DIR
		FILE (GETS CURRENT ACTIVE FILE NAME)
	 MKDIR
	 	(NEW_DIR_NAME) CREATES THE SPECIFIED DIRECTORY IN THE CURRENT WORKING DIRECTORY IF IT DOES NOT ALREADY EXIST
	 LS
	 	DIR (GETS CURRENT DIRECTORY)
	 CD
	 	(NEW_DIRECTORY) CHANGES THE CURRENT WORKING DIRECTORY TO THE NEW_DIRECTORY SUBFOLDER IN THE CURRENT WORKING DIRECTORY 
	 ..
	 REMOVE
	 ->	(FILENAME) REMOVES THE FILE SPECIFIED FROM THE CURRENT WORKING DIRECTORY
	 PRINT
	 -> 
		(MESSAGE) PRINTS THE MESSAGE TO THE TERMINAL SCREEN

/*THE GENERAL SYNTAX OF A SELECT COMMAND IS SELECT [FUNCTION] [IDENTIFIER] [ARGUMENT]*/
SELECT
	 ->
		COUNT
		->
			WORDS (COUNTS THE NUMBER OF WORDS IN THE CURRENT ACTIVE FILE)
			CHARS (COUNTS THE NUMBER OF CHARACTERS IN THE CURRENT ACTIVE FILE, INCLUDING SPACES)
			LINES (COUNTS THE NUMBER OF LINES IN THE CURRENT ACTIVE FILE)
			CHARS/SPACES (COUNTS THE NUMBER OF CHARACTERS IN THE CURRENT ACTIVE FILE, NOT INCLUDING SPACES) 
			CHARACTER (CHAR) (COUNTS THE NUMBER OF TIMES CHAR APPEARS IN THE CURRENT ACTIVE FILE)
			WORD (WORD) (COUNTS THE NUMBER OF TIMES WORD APPEARS IN THE CURRENT ACTIVE FILE)
			PHRASE (PHRASE) (COUNTS THE NUMBER OF TIMES PHRASE APPEARS IN THE CURRENT ACTIVE FILE-LENGTH OF PHRASE MUST BE > 1)

Example:
query file TESTDOC /*creates a file named testdoc.txt in the current working directory*/
query writeln hello, world! /*writes the line hello, world! to TESTDOC*/
select count character e /*counts the number of times 'e' occurs in the file*/
query close file /*closes the current active file, which is TESTDOC*/```


## Coming Soon

Future additions include an extension to select functions and in-built documentation.


