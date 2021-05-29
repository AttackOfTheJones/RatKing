import openai
import requests
import tkinter

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
