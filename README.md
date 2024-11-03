# pyKannada

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## 📝 Introduction

**pyKannada** is an innovative Python interpreter that allows users to write and execute Python code using Kannada keywords. This project aims to make programming more accessible to Kannada speakers, empowering a new generation of developers.

## 🚀 Features

- **Kannada Keywords**: Use Kannada keywords for common Python functions, control flow statements, and more.
- **Interactive REPL**: Enter a Read-Eval-Print Loop to execute Kannada code interactively.
- **File Execution**: Execute Kannada script files directly.
- **Keyword Mapping**: Easily edit the keyword mappings to customize the interpreter to your needs.
- **Cross-Platform Compatibility**: Works on Windows, macOS, and Linux.

## 💻 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mithun50/pyKannada.git
   cd pyKannada
   pip install .
   ```

2. Ensure you have Python 3.6 or higher installed.

3. You can run the interpreter directly using:
   ```bash
   python -m pyKannada
   ```
### OR
## 📦 PyPI

**pyKannada** is available on PyPI, allowing for easy installation via pip. You can install it using:
```bash
pip install pyKannada
```

## 📚 Usage
### (In Case of Windows and Other)

### Running in REPL Mode
To enter interactive mode:
```bash
python -m pyKannada
```

### Executing a Script File
To execute a Kannada script file:
```bash
python -m pyKannada your_script.py
```

### Editing Keywords
To edit the keyword mappings:
```bash
python -m pyKannada --edit-keywords
```
### OR You Can USE (In Case of Linux or Other)
### Running in REPL Mode
To enter interactive mode:
```bash
pyKannada
```

### Executing a Script File
To execute a Kannada script file:
```bash
pyKannada path/to/your/script.py
```

### Editing Keywords
To edit the keyword mappings:
```bash
pyKannada --edit-keywords
```


## 🗺️ Keyword Mapping

Here’s a mapping of Kannada keywords to their Python equivalents, You can Change it :

<table>
    <tr>
        <th>Kannada Keyword</th>
        <th>Python Equivalent</th>
    </tr>
    <tr>
        <td>ಮುದ್ರಿಸು</td>
        <td>print</td>
    </tr>
    <tr>
        <td>ವಿಧ</td>
        <td>type</td>
    </tr>
    <tr>
        <td>ಒಳಸೇರಿಸು</td>
        <td>input</td>
    </tr>
    <tr>
        <td>ಉದ್ದ</td>
        <td>len</td>
    </tr>
    <tr>
        <td>ಸಾಲು</td>
        <td>str</td>
    </tr>
    <tr>
        <td>ಪೂರ್ಣಸಂಖ್ಯೆ</td>
        <td>int</td>
    </tr>
    <tr>
        <td>ಸಮ್ಮತ</td>
        <td>float</td>
    </tr>
    <tr>
        <td>ಪಟ್ಟಿ</td>
        <td>list</td>
    </tr>
    <tr>
        <td>ನೆರಕೆ</td>
        <td>dict</td>
    </tr>
    <tr>
        <td>ರಾಶಿ</td>
        <td>set</td>
    </tr>
    <tr>
        <td>ಟ್ಯೂಪಲ್ಸ್</td>
        <td>tuple</td>
    </tr>
    <tr>
        <td>ಬೂಲ್</td>
        <td>bool</td>
    </tr>
    <tr>
        <td>ಒಂದು_ವೇಳೆ</td>
        <td>if</td>
    </tr>
    <tr>
        <td>ಇಲ್ಲದಿದ್ದರೆ</td>
        <td>elif</td>
    </tr>
    <tr>
        <td>ಬೇರೆ</td>
        <td>else</td>
    </tr>
    <tr>
        <td>ಬದಲು</td>
        <td>for</td>
    </tr>
    <tr>
        <td>ವೇಳೆ</td>
        <td>while</td>
    </tr>
    <tr>
        <td>ಮುರಿ</td>
        <td>break</td>
    </tr>
    <tr>
        <td>ಮುಂದುವರೆಸು</td>
        <td>continue</td>
    </tr>
    <tr>
        <td>ಹಿಂದಿರುಗು</td>
        <td>return</td>
    </tr>
    <tr>
        <td>ಪ್ರಯತ್ನಿಸು</td>
        <td>try</td>
    </tr>
    <tr>
        <td>ಹೊರತುಪಡಿಸಿ</td>
        <td>except</td>
    </tr>
    <tr>
        <td>ಕೊನೆಯದಾಗಿ</td>
        <td>finally</td>
    </tr>
    <tr>
        <td>ಜೊತೆಗೆ</td>
        <td>with</td>
    </tr>
    <tr>
        <td>ಕಾರ್ಯ</td>
        <td>def</td>
    </tr>
    <tr>
        <td>ನಿಜ</td>
        <td>True</td>
    </tr>
    <tr>
        <td>ಸುಳ್ಳು</td>
        <td>False</td>
    </tr>
    <tr>
        <td>ತೇರ್ಗಡೆ</td>
        <td>pass</td>
    </tr>
    <tr>
        <td>ವರ್ಗ</td>
        <td>class</td>
    </tr>
    <tr>
        <td>ರಲ್ಲಿ</td>
        <td>in</td>
    </tr>
    <tr>
        <td>ಲ್ಯಾಂಬ್ಡಾ</td>
        <td>lambda</td>
    </tr>
    <tr>
        <td>ಹಳಿಸು</td>
        <td>del</td>
    </tr>
    <tr>
        <td>ಸಮಗ್ರ</td>
        <td>global</td>
    </tr>
</table>

### Example Code
Here's a simple examples using Above Kannada_keywords:

**calculator.py**
- [Download calculator.py](http://raw.githubusercontent.com/mithun50/pyKannada/main/pyKannada_Examples/calculator.py)
```python
ಎ = ಪೂರ್ಣಸಂಖ್ಯೆ(ಒಳಸೇರಿಸು('ಮೊದಲ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ: '))
ಬ = ಪೂರ್ಣಸಂಖ್ಯೆ(ಒಳಸೇರಿಸು('ಎರಡನೇ ಸಂಖ್ಯೆ ನಮೂದಿಸಿ: '))
ಚಲನ = ಒಳಸೇರಿಸು('ಚಲನ ( +, -, *, /, **) ನಮೂದಿಸಿ: ')

ಕಾರ್ಯ ಎಣಿಕೆ(ಎ, ಬ, ಚಲನ):
    ಒಂದು_ವೇಳೆ ಚಲನ == '+':
        ಮುದ್ರಿಸು(ಎ + ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '-':
        ಮುದ್ರಿಸು(ಎ - ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '*':
        ಮುದ್ರಿಸು(ಎ * ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '/':
        ಮುದ್ರಿಸು(ಎ / ಬ)
    ಇಲ್ಲದಿದ್ದರೆ ಚಲನ == '**':
        ಮುದ್ರಿಸು(ಎ ** ಬ)
    ಬೇರೆ:
        ಮುದ್ರಿಸು('ತಪ್ಪು ಚಲನ')

ಎಣಿಕೆ(ಎ, ಬ, ಚಲನ)
```
**quiz.py** 
- [Download calculator.py](http://raw.githubusercontent.com/mithun50/pyKannada/main/pyKannada_Examples/quiz.py)
```python
ಪ್ರಶ್ನೆಗಳು = [
    {"ಪ್ರಶ್ನೆ": "ಕನ್ನಡದ ಜನಪ್ರಿಯ ಕವಿ ಯಾರು?", "ಉತ್ತರ": "ಕುವಿ ಎಂ. ಚಿದಾನಂದ"},
    {"ಪ್ರಶ್ನೆ": "ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ?", "ಉತ್ತರ": "ಬೆಂಗಳೂರು"},
    {"ಪ್ರಶ್ನೆ": "ಕರ್ನಾಟಕದ ರಾಜಕವಿ?", "ಉತ್ತರ": "ಕುವಿ ಬಿ. ಎನ್. ಸುಬ್ಬರಾಯ"}
]

# Function to start the quiz
ಕಾರ್ಯ ಪ್ರಾರಂಭಿಸು():
    ಅಂಕ = 0  # Initial score
    ಮುದ್ರಿಸು("ಕನ್ನಡ ಕುಯಿಸ್ ಆಟಕ್ಕೆ ಸ್ವಾಗತ!")

    # Loop through each question
    ಬದಲು ಪ್ರಶ್ನೆ in ಪ್ರಶ್ನೆಗಳು:
        ಮುದ್ರಿಸು("\n" + ಪ್ರಶ್ನೆ["ಪ್ರಶ್ನೆ"])
        ಉತ್ತರ = ಒಳಸೇರಿಸು("ನಿಮ್ಮ ಉತ್ತರ: ")

        # Check if answer is correct
        ಒಂದು_ವೇಳೆ ಉತ್ತರ == ಪ್ರಶ್ನೆ["ಉತ್ತರ"]:
            ಮುದ್ರಿಸು("ಸರಿಯಾಗಿ ಉತ್ತರಿಸಿದ್ದೀರಿ!")
            ಅಂಕ += 1
        ಬೇರೆ:
            ಮುದ್ರಿಸು("ತಪ್ಪಾಗಿದೆ. ಸರಿಯಾದ ಉತ್ತರ: " + ಪ್ರಶ್ನೆ["ಉತ್ತರ"])

    # Display final score
    ಮುದ್ರಿಸು(f"\nನಿಮ್ಮ ಅಂತಿಮ ಅಂಕ: {ಅಂಕ}/{ಉದ್ದ(ಪ್ರಶ್ನೆಗಳು)}")
    ಒಂದು_ವೇಳೆ ಅಂಕ == ಉದ್ದ(ಪ್ರಶ್ನೆಗಳು):
        ಮುದ್ರಿಸು("ಅಭಿನಂದನೆಗಳು! ನೀವು ಎಲ್ಲಾ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸರಿಯಾಗಿ ಉತ್ತರಿಸಿದ್ದೀರಿ!")
    ಬೇರೆ:
        ಮುದ್ರಿಸು("ಕನ್ನಡ ಕುಯಿಸ್ ಪೂರ್ಣಗೊಂಡಿದೆ! ಮತ್ತೆ ಪ್ರಯತ್ನಿಸಿ!")

# Start the quiz game
ಪ್ರಾರಂಭಿಸು()
```

## 🧪 Testing Experience

As part of the development process for **pyKannada**, extensive testing was conducted to ensure reliability and compatibility across various platforms. Here are some insights from my testing experience:

### Platforms Tested

1. **Pydroid 3**:
   - **Overview**: Pydroid 3 is a popular Python IDE for Android, making it accessible for users on mobile devices.
   - **Experience**: The app performed exceptionally well, allowing users to write and execute Kannada scripts seamlessly. The user interface is intuitive, and the integration of Kannada keywords worked without any issues.

2. **Visual Studio Code**:
   
   - 1. **Font Settings**: 
      - Use a font that supports Kannada characters. In your VS Code settings, search for **Terminal > Integrated: Font Family** and set it to a font like `Noto Sans Kannada` or `Noto Serif Kannada`.

   - 2. **Change Terminal Encoding**:
      - Ensure your terminal is set to use UTF-8 encoding, which supports Kannada characters. This setting can typically be found in the terminal preferences.

   - 3. **Update VS Code**:
      - Always use the latest version of Visual Studio Code, as updates may improve support for international languages.

   - 4. **Use an External Terminal**:
      - If the integrated terminal is not displaying Kannada correctly, consider configuring VS Code to use an external terminal (such as Command Prompt or Windows Terminal) for better compatibility.

   - 5. **Testing in Different Terminals**:
      - Try running your scripts in various terminals to see if they display Kannada characters correctly.

   - 6. **Check Language Pack**:
      - If you are using the Kannada language pack in VS Code, ensure it is correctly installed and configured.

Following these steps can significantly improve your experience when working with Kannada text in Visual Studio Code.


3. **Standard Python Installation**:
   - **Overview**: Testing was conducted on various operating systems, including Windows, macOS, and Linux, with a standard Python installation.
   - **Experience**: The interpreter ran smoothly on all tested platforms, demonstrating its versatility and robustness. The REPL mode and script execution performed as expected, providing consistent results.

### Key Takeaways

- **User-Friendly**: The ability to use Kannada keywords significantly lowers the entry barrier for new programmers.
- **Reliability**: Extensive testing confirmed that the interpreter can handle a variety of scripts without crashing or throwing unexpected errors.
- **Community Feedback**: Feedback from early users highlighted the usefulness of the interactive REPL and the ease of modifying keyword mappings.

These testing experiences have solidified my belief in the potential of **pyKannada** to make programming more accessible to Kannada speakers and foster a new generation of developers.



## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

For more information, questions, or suggestions, please reach out to the authors:

- **MithunGowda.B**  
  Email: mithungowda.b7411@gmail.com  
  Instagram: [@mithungowda](https://www.instagram.com/mithun.gowda.b)

- **Manvanth**  
  Email: appuka1431@gmail.com  
  Instagram: [@manvanth](https://www.instagram.com/appu.__.kannadiga)

Visit our project repository: [pyKannada PYPI](http://pypi.org/project/pyKannada)
