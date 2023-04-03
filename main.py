from Helper import *
from tkinter import ttk
import string

# debug playfair and one time pad page class

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Main Page")
        label.pack()

        # Create buttons to switch between pages
        button1 = ttk.Button(self, text="Vigenere Cipher Standard",
                             command=lambda: self.controller.show_frame(VigenerePage))
        button2 = ttk.Button(self, text="Extended Vigenere Cipher",
                             command=lambda: self.controller.show_frame(ExtendedVigenerePage))
        button3 = ttk.Button(self, text="Playfair Cipher",
                             command=lambda: self.controller.show_frame(PlayfairPage))
        button4 = ttk.Button(self, text="One-time pad",
                             command=lambda: self.controller.show_frame(OneTimePadPage))
        
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()

class VigenerePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Vigenere Cipher Standard")
        label.pack()

        # Create input and output text boxes
        self.inputText = InstructionText(self,instrText="Plaintext:", height=5, width=40)
        self.inputText.pack()
        self.outputText = tk.Text(self, height=5, width=40, state=tk.DISABLED)
        self.outputText.pack()

        # Create key entry box and encrypt/decrypt buttons
        self.keyEntry = InstructionEntry(self, instrText="Key:",width=30)
        self.keyEntry.pack()
        encryptButton = ttk.Button(self, text="Encrypt",
                                    command=self.encrypt)
        encryptButton.pack()
        decryptButton = ttk.Button(self, text="Decrypt",
                                    command=self.decrypt)
        decryptButton.pack() 

        # Create a back button to return to the main page
        backButton = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame(MainPage))
        backButton.pack()

    def encrypt(self):
        plaintext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        ciphertext = ""
        # Convert the key to uppercase and remove non-letter characters
        key = ''.join(filter(str.isalpha, key)).upper()
        for i in range(len(plaintext)):
            # Calculate the shift value
            shift = ord(key[i % len(key)]) - 65
            # Encrypt the current character
            if plaintext[i].isalpha():
                if plaintext[i].isupper():
                    ciphertext += chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
                else:
                    ciphertext += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
            else:
                ciphertext += plaintext[i]

        self.outputText.configure(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert("1.0", ciphertext)
        self.outputText.configure(state=tk.DISABLED)

    def decrypt(self):
        ciphertext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        plaintext = ""
        # Convert the key to uppercase and remove non-letter characters
        key = ''.join(filter(str.isalpha, key)).upper()
        for i in range(len(ciphertext)):
            # Calculate the shift value
            shift = ord(key[i % len(key)]) - 65
            # Decrypt the current character
            if ciphertext[i].isalpha():
                if ciphertext[i].isupper():
                    plaintext += chr((ord(ciphertext[i]) - shift - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
            else:
                plaintext += ciphertext[i]

        self.outputText.configure(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert("1.0", plaintext)
        self.outputText.configure(state=tk.DISABLED)

class ExtendedVigenerePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Extended Vigenere Cipher")
        label.pack()

        # Create input and output text boxes
        self.inputText = InstructionText(self,instrText="Plaintext:", height=5, width=40)
        self.inputText.pack()
        self.outputText = tk.Text(self, height=5, width=40, state=tk.DISABLED)
        self.outputText.pack()

        # Create key entry box and encrypt/decrypt buttons
        self.keyEntry = InstructionEntry(self, instrText="Key:",width=30)
        self.keyEntry.pack()
        encryptButton = ttk.Button(self, text="Encrypt",
                                    command=self.encrypt)
        encryptButton.pack()
        decryptButton = ttk.Button(self, text="Decrypt",
                                    command=self.decrypt)
        decryptButton.pack() 

        # Create a back button to return to the main page
        backButton = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame(MainPage))
        backButton.pack()

    def encrypt(self):
        plaintext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        ciphertext = ""
        for i in range(len(plaintext)):
            # Calculate the shift value
            shift = ord(key[i % len(key)]) - 32
            # Encrypt the current character
            ciphertext += chr((ord(plaintext[i]) + shift) % 256)

        self.outputText.configure(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert("1.0", ciphertext)
        self.outputText.configure(state=tk.DISABLED)

    def decrypt(self):
        ciphertext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        plaintext = ""
        for i in range(len(ciphertext)):
            # Calculate the shift value
            shift = ord(key[i % len(key)]) - 32
            # Decrypt the current character
            plaintext += chr((ord(ciphertext[i]) - shift) % 256)

        self.outputText.configure(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert("1.0", plaintext)
        self.outputText.configure(state=tk.DISABLED)

class PlayfairPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Playfair Cipher Standard")
        label.pack()

        # Create input and output text boxes
        self.inputText = InstructionText(self,instrText="Plaintext:", height=5, width=40)
        self.inputText.pack()
        self.outputText = tk.Text(self, height=5, width=40, state=tk.DISABLED)
        self.outputText.pack()

        # Create key entry box and encrypt/decrypt buttons
        self.keyEntry = InstructionEntry(self, instrText="Key:",width=30)
        self.keyEntry.pack()
        encryptButton = ttk.Button(self, text="Encrypt",
                                    command=self.encrypt)
        encryptButton.pack()
        decryptButton = ttk.Button(self, text="Decrypt",
                                    command=self.decrypt)
        decryptButton.pack()

        # Create a back button to return to the main page
        backButton = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame(MainPage))
        backButton.pack()

    def encrypt(self):
        plaintext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        ciphertext = ""
        # Convert the key to uppercase and remove non-letter characters
        key = ''.join(filter(str.isalpha, key)).upper()
        # Remove any duplicate letters from the key
        key = ''.join(sorted(set(key), key=key.index))
        # Create the playfair matrix
        matrix = ""
        for c in key:
            if c not in matrix:
                matrix += c
        for c in string.ascii_uppercase:
            if c != 'J' and c not in matrix:
                matrix += c
        # Break the plaintext into digraphs and encrypt each digraph
        plaintext = plaintext.upper().replace('J', 'I')
        for i in range(0, len(plaintext), 2):
            if i == len(plaintext) - 1:
                plaintext += 'X'
            if plaintext[i] == plaintext[i + 1]:
                plaintext = plaintext[:i + 1] + 'X' + plaintext[i + 1:]
            row1, col1 = divmod(matrix.index(plaintext[i]), 5)
            row2, col2 = divmod(matrix.index(plaintext[i + 1]), 5)
            if row1 == row2:
                ciphertext += matrix[row1 * 5 + (col1 + 1) % 5]
                ciphertext += matrix[row2 * 5 + (col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += matrix[((row1 + 1) % 5) * 5 + col1]
                ciphertext += matrix[((row2 + 1) % 5) * 5 + col2]
            else:
                ciphertext += matrix[row1 * 5 + col2]
                ciphertext += matrix[row2 * 5 + col1]

        self.outputText.configure(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert("1.0", ciphertext)
        self.outputText.configure(state=tk.DISABLED)

    def decrypt(self):
        ciphertext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        plaintext = ""
        # Convert the key to uppercase and remove non-letter characters
        key = ''.join(filter(str.isalpha, key)).upper()
        # Remove any duplicate letters from the key
        key = ''.join(sorted(set(key), key=key.index))
        # Create the playfair matrix
        matrix = ""
        for c in key:
            if c not in matrix:
                matrix += c
        for c in string.ascii_uppercase:
            if c != 'J' and c not in matrix:
                matrix += c
        # Break the ciphertext into digraphs and decrypt each digraph
        ciphertext = ciphertext.upper().replace('J', 'I')
        ciphertext = ''.join(filter(str.isalpha, ciphertext))
        ciphertext += 'X' * (len(ciphertext) % 2)
        for i in range(0, len(ciphertext), 2):
            a, b = ciphertext[i:i+2]
            a_row, a_col = divmod(matrix.index(a), 5)
            b_row, b_col = divmod(matrix.index(b), 5)
            if a_row == b_row:
                # Same row, shift columns to the left
                a = matrix[a_row * 5 + (a_col - 1) % 5]
                b = matrix[b_row * 5 + (b_col - 1) % 5]
            elif a_col == b_col:
                # Same column, shift rows up
                a = matrix[((a_row - 1) % 5) * 5 + a_col]
                b = matrix[((b_row - 1) % 5) * 5 + b_col]
            else:
                # Rectangle, swap columns
                a = matrix[a_row * 5 + b_col]
                b = matrix[b_row * 5 + a_col]
            plaintext += a + b

        self.outputText.config(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert(tk.END, plaintext)
        self.outputText.config(state=tk.DISABLED)

class OneTimePadPage (tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="One-Time Pad")
        label.pack()

        # Create input and output text boxes
        self.inputText = InstructionText(self,instrText="Plaintext:", height=5, width=40)
        self.inputText.pack()
        self.outputText = tk.Text(self, height=5, width=40, state=tk.DISABLED)
        self.outputText.pack()

        # Create key entry box and encrypt/decrypt buttons
        self.keyEntry = InstructionEntry(self, instrText="Key:",width=30)
        self.keyEntry.pack()
        encryptButton = ttk.Button(self, text="Encrypt",
                                    command=self.encrypt)
        encryptButton.pack()
        decryptButton = ttk.Button(self, text="Decrypt",
                                    command=self.decrypt)
        decryptButton.pack()
        
        # Create a back button to return to the main page
        backButton = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame(MainPage))
        backButton.pack()

    def encrypt(self):
        plaintext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        ciphertext = ""
        for i in range(len(plaintext)):
            # Convert plaintext and key characters to ASCII codes
            p = ord(plaintext[i])
            k = ord(key[i])
            # XOR plaintext and key codes to get ciphertext code
            c = p ^ k
            # Convert ciphertext code back to a character and append to ciphertext
            ciphertext += chr(c)

        self.outputText.config(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert(tk.END, ciphertext)
        self.outputText.config(state=tk.DISABLED)

    def decrypt(self):
        ciphertext = self.inputText.get("1.0", tk.END).strip()
        key = self.keyEntry.get().strip()
        plaintext = ""
        for i in range(len(ciphertext)):
            # Convert ciphertext and key characters to ASCII codes
            c = ord(ciphertext[i])
            k = ord(key[i])
            # XOR ciphertext and key codes to get plaintext code
            p = c ^ k
            # Convert plaintext code back to a character and append to plaintext
            plaintext += chr(p)

        self.outputText.config(state=tk.NORMAL)
        self.outputText.delete("1.0", tk.END)
        self.outputText.insert(tk.END, plaintext)
        self.outputText.config(state=tk.DISABLED)

class MainController(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Multi-page GUI Application")
        self.geometry("400x300")
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, VigenerePage, ExtendedVigenerePage, PlayfairPage, OneTimePadPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = MainController()
app.mainloop()
