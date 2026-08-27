#Pin extractor
This Python program extracts a secret PIN from each poem. It splits the poem into lines and uses the **line index as the word index**. The length of the selected word is added to the PIN. If the required word does not exist in a line, 0 is added instead.
Example:
Line 0 → Word 0 → Length of word
Line 1 → Word 1 → Length of word
Line 2 → Word 2 → Length of word
The program processes multiple poems and returns a list containing the extracted PINs.
