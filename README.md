# Text Replacer

## Overview
The Text Replacer project is a Python-based tool designed to automatically correct misspelled words in a given text file. It leverages a predefined set of corrections to replace incorrect words with their correct counterparts, ensuring the text is free from common spelling errors.

## Features
- **Automated Word Replacement**: Automatically replaces incorrect words with the correct ones based on a predefined dictionary.
- **Whole Word Matching**: Uses regular expressions to ensure only whole words are replaced, avoiding partial matches.
- **Efficient Processing**: Processes the text efficiently, making it suitable for large text files.
- **Output to New File**: Writes the corrected text to a new file, preserving the original file.

## How It Works
1. **Load Corrections**: The tool loads a dictionary of incorrect and correct word pairs from a JSON structure.
2. **Read Text**: Reads the content of the input text file.
3. **Replace Words**: Uses regular expressions to find and replace incorrect words with the correct ones.
4. **Write Output**: Writes the corrected text to a new file, appending `_corrected` to the original filename.

## Example
Excerpt from active file `example.txt`, lines 1 to 7:
```plaintext
Last weakend, I went on a journie to the mountains with some frends. We disided to go hiking, even though the whether forcast had predictid rain. We packed our bakpacks with snacks, water, and some extra close, just in case.

The trail was beutiful, with tall treees and colorful flowrs lining the path. As we climed higher, we could see the vally below, covered in mist. It was truely a magial site. However, as we aproached the summit, it started to rain hevily.

Unfortunetly, we weren’t perpared for the storm. Our umbrelllas were too small to keep us dry, and our shoes quickly became soked with water. Despire the challenging conditions, we managed to reach the top. The veiw from the peak was amazing, even though the skys were cloudy.

After taking some picturs, we decided to head back down. On the way, we got lost and had to rely on a map we brought along to find our way. We eventully made it back to the car, tired but happy with our adventure. It was a day full of challenges, but also full of memmories that we'll cheresh forever.
