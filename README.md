# Bookbot
BookBot is my first [Boot.dev](https://www.boot.dev) project! 

Script to analyze an entire book and generate a printed report
with some insights  
![My Skills](https://skillicons.dev/icons?i=python)

<img width="559" alt="image" src="https://github.com/user-attachments/assets/e0316e61-5420-4474-a74a-94b1be516cf8" alt="Printed report output">

# 📜 How to use
The script is about printing on the terminal info about a provided text file ( see Base assignment )
> [!Note]
> On using this repo and use of the command without arguments  
> `books/frankenstein.txt` folder and file should be provided
> [Frankenstein](https://www.gutenberg.org/files/84/84-h/84-h.htm)
> > select all + copy + paste in a `frankenstein.txt` file

- Execution syntax `python main.py <text-filepath?> <words?>`
- Execution examples:
  -  `python main.py`: will prompt for user to provide filepath and search word ( or skip )
  -  `python main.py books/my-text.txt`: will use custom input filepath
  -  `python main.py books/my-text.txt research, something`: will use custom inputs filepath, words + output searched words

# 💻 Development
  <details>
    <summary>&nbsp;&nbsp;&nbsp; <h2>Base Assignment</h2> </summary>
    Static file reading of text files (.txt) within folders books
    <ul>
      <li>number of words in the file</li>
      <li>letter occurrence</li>
    </ul>
  </details>
  



  <details>
    <summary>&nbsp;&nbsp;&nbsp; <h2>Extra</h2>
    
  <video src="https://github.com/user-attachments/assets/430ed682-ff2b-4869-a5ff-ff341fa8765d" alt="Demo preview CLI and extras"></video>
    </summary>
    Improving the DX - if nothing specified - the default
    would behave as the base assignment. 
    <ul>
      <li>accepting words retrieval to search occurence in document</li>
      <ul>
        <li>handling commands arguments ( filepath?, words? )</li>
        <li>handling prompt entries ( filepath?, words? )</li>
      </ul>
    </ul>
  </details>




