import openai
import requests
import tkinter as tk
import poopMan64

#First window, which verifies gpt3 code
class verify():

    def __init__(self, c_win):
        self.verify_window = None
        self.code_input = None
        self.passed = c_win

    def start(self):
        #window initialization
        self.verify_window = tk.Tk()
        self.verify_window.title("Verification")
        self.verify_window.geometry("480x160")
        self.verify_window.configure(bg="light blue")
        self.verify_window.iconbitmap("gpticon.ico")

        # TODO: figure out why the heckle this doesnt work
        # #BG image
        # self.bg = tk.PhotoImage("gptb.jpg")
        # self.bg_label = tk.Label(self.verify_window, image=self.bg)
        # self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #window row and column setup
        self.verify_window.columnconfigure(0, weight=1)
        self.verify_window.columnconfigure(1, weight=3)
        self.verify_window.columnconfigure(2, weight=1)

        self.verify_window.rowconfigure(0, weight=1)
        self.verify_window.rowconfigure(1, weight=1)
        self.verify_window.rowconfigure(2, weight=1)

        #label
        tk.Label(self.verify_window, text="Please input your GPT-3 code:", bg="light blue", font=("Courier Prime", 16)).grid(row=0, column=1, columnspan=3, sticky="w")

        #input box
        self.code_box = tk.Entry(self.verify_window, width=70, bd=2)
        self.code_box.grid(row=1, column=0, columnspan=3, sticky='nsew', padx=(15, 15))

        #button
        button = tk.Button(self.verify_window, text="Enter", command=self.v_button, font=("Courier Prime", 14))
        button.grid(row=3, column=1, sticky="ew", pady=(0, 10))

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
            tk.messagebox.showwarning(title='Error', message='Invalid Authorization Key!')
        else:
            self.passed.start(openai.api_key)
            self.verify_window.destroy()


    
class central():

    def __init__(self):
        self.central_window = None

    def start(self, key):
        openai.api_key = key

        #Define the window parameters
        self.central_window = tk.Tk()
        self.central_window.title('Ask The Stig')
        self.central_window.geometry("480x240")
        self.central_window.configure(bg="light blue")
        self.central_window.iconbitmap("gpticon.ico")

        #TODO: modify layout to be more like what matt wants
        #window row and column setup
        self.central_window.columnconfigure(0, weight=1)

        self.central_window.rowconfigure(0, weight=1)
        self.central_window.rowconfigure(1, weight=3)
        self.central_window.rowconfigure(2, weight=1)
        self.central_window.rowconfigure(3, weight=3)

        #label
        tk.Label(self.central_window, text="What is your situation?", font=("Courier Prime", 12), bg="light blue").grid(row=0, column=0)

        #Define the first text box
        #self.textLog = tk.Text(self.central_window, state='disabled')

        self.entry_box = tk.Entry(self.central_window, state='normal')
        self.entry_box.grid(row=1, column=0, sticky='nsew', padx=(15, 15))

        #label
        tk.Label(self.central_window, text="The Stig's response:", font=("Courier Prime", 12), bg="light blue").grid(row=2, column=0)

        self.response_box = tk.Entry(self.central_window, state='normal')
        self.response_box.grid(row=3, column=0, sticky='nsew', padx=(15, 15))

        #User presses 'Enter' key to submit text
        self.entry_box.bind('<Return>', self.enter)

        self.central_window.mainloop()

    def enter(self, something):
        text = self.entry_box.get()

        if(text != None):
            # self.entry_box.delete()
            # response = poopMan64.poop(text, Key)
            #
            response = "pooptacular"
            self.response_box.insert(0, response)

            # self.textLog.state = "NORMAL"
            # self.textLog.add('You: ' + text + '\n')
            # self.textLog.add('The Stig: ' + response + '\n')
            # self.textLog.state = "DISABLED"


p = central()
p.start("44")
