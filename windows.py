import openai
import requests
import tkinter
import poopMan64 

#First window, which verifies gpt3 code
class verify():

    def __init__(self):
        self.verify_window = None
        self.code_input = None

    def start(self):
        #window initialization
        self.verify_window = tkinter.Tk()
        self.verify_window.title("Verification")
        self.verify_window.geometry("480x160")

        #window row and column setup
        self.verify_window.columnconfigure(0, weight=1)
        self.verify_window.columnconfigure(1, weight=3)
        self.verify_window.columnconfigure(2, weight=1)

        self.verify_window.rowconfigure(0, weight=1)
        self.verify_window.rowconfigure(1, weight=1)
        self.verify_window.rowconfigure(2, weight=1)

        #label


        #input box
        self.code_box = tkinter.Entry(self.verify_window, width=70)
        self.code_box.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=(20, 0))

        #button
        button = tkinter.Button(self.verify_window, text="Enter", command=self.v_button)
        button.grid(row=3, column=1, sticky="w")

        self.verify_window.mainloop()

    def v_button(self):

        #Retrieve User's API Key
        openai.api_key = self.code_box.get()

        #Issue Free Request to verify Key
        r = requests.get("https://api.openai.com/v1/engines/davinci/completions/browser_stream",
        headers={
            "Authorization": f"Bearer {openai.api_key}"
        },
        params={
            "prompt": 'Authentification',
            "max_tokens": 0,
            "logprobs": 1,
            "echo": True
        })

        #Verify Key
        if (r.reason == 'Unauthorized'):
            tkinter.messagebox.showwarning(title='Error', message='Invalid Authorization Key!')
        else:
            self.quit()


    
class central():

    def __init__(self):
        self.central_window = None

    def start(Key):
        openai.api_key = Key

        #Define the window parametets
        self.central_window = tk.Tk()
        self.central_window.title('Ask The Stig')
        self.central_window.geometry("480x776")

        #Define the text boxes
        self.textLog = tk.Text(self.central_window, state=DISABLED)
        self.entry = tk.Text(self.central_window, state=NORMAL)

        

        #User presses 'Enter' key to submit text
        self.entry.bind('<Return>', self.enter)

        self.central_window.mainloop()

    def enter(self):
        text = self.entry.get()

        if(text != None):
            self.entry.delete()
            response = poopMan64.poop(text, Key)

            self.textLog.state = NORMAL
            self.textLog.add('You: ' + text + '\n')
            self.textLog.add('The Stig: ' + response + '\n')
            self.textLog.state = DISABLED

            







