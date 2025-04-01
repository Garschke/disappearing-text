import tkinter as tk
from modules.constants import TITLE_FONT, PROMPT_FONT, TEXT_FONT, FONT
from modules.constants import WBG, PBG, DFC, LFC, TBG, TFC, TIMER, COLORS
from modules.prompt_generator import prompt_text
from modules.logger import get_logger


class DisappearingTextApp:
    """
    A GUI application for helping with writers block.
    """

    def __init__(self, root):
        """
        Initialize the application.
        """
        self.root = root
        self.root.title("Disappearing Text App")
        self.root.config(bg=WBG, padx=10, pady=10)
        self.default_text = "Don't stop writing, or all progress will be lost."
        self.prompt_text = ""
        self.writer_open = False

    # -------------------- Root UI Design --------------------
        # Image
        self.canvas = tk.Canvas(
            root, width=156, height=150, bg=WBG, highlightthickness=0
        )
        try:
            self.pen_img = tk.PhotoImage(file="src/pen-sword.png")
        except tk.TclError as err:
            log.error(f"Image not found: src/pen-sword.png\n{err}",
                      exc_info=True)
            self.pen_img = None
        self.canvas.create_image(50, 100, image=self.pen_img)
        self.canvas.grid(column=0, row=0)

        # Labels
        self.title_label = tk.Label(
            root, text="The Most Dangerous Writing App",
            font=TITLE_FONT, bg=WBG, fg=LFC, width=37
        )
        self.title_label.grid(column=1, row=0, padx=20, pady=0)

        self.prompt_label = tk.Label(
            root, text=self.default_text, font=PROMPT_FONT,
            bg=PBG, fg=DFC, height=6, width=70, wraplength=500
        )
        self.prompt_label.grid(column=0, columnspan=3, row=2, pady=10)

        self.session_label = tk.Label(
            root, font=FONT, bg=WBG, fg=LFC,
            text=('Session time out: ' + str(TIMER) + ' seconds')
        )
        self.session_label.grid(column=2, row=3, pady=10)

        # Buttons
        self.prompt_btn = tk.Button(
            root, text='Generate a Prompt', font=FONT, height=2,
            width=20, command=self.new_prompt
        )
        self.prompt_btn.grid(column=0, row=4, pady=20)

        self.start_btn = tk.Button(
            root, text='Start Writing w/o Prompt', font=FONT, height=2,
            width=20, command=self.start_writing
        )
        self.start_btn.grid(column=2, row=4, pady=20)

        # Bind left mouse button click event to the session label
        self.session_label.bind("<ButtonPress-1>", self.change_timer)

    # --------------------End UI Design ---------------------

    def change_timer(self, event):
        """
        Changes the number of seconds for Countdown
        """
        global TIMER
        # Changes the TIMER variable between 10 > 30 in 5 second incriments
        TIMER += 5
        if TIMER > 30:
            TIMER = 10
        # Change label text
        session_time_out = f'Session time out {str(TIMER)} seconds'
        self.session_label.config(
            text=('Session time out: ' + str(TIMER) + ' seconds')
        )
        log.debug(session_time_out)            # **** LOGGING DATA *****

    def new_prompt(self):
        """
        Create Prompt to start off writing.
        """
        self.prompt_text = prompt_text()
        log.debug(f"Generating Prompt: {self.prompt_text}")  # * LOGGING DATA *
        self.title_label.config(
            text="The Most Dangerous Random Prompt Generator"
        )
        self.prompt_btn.config(text='Generate New Prompt')
        self.start_btn.config(text='Start Writing')
        self.prompt_label.config(text=self.prompt_text)

    def start_writing(self):
        """
        Open Writing dialog.
        """
        log.debug("Openning Writing dialog")   # **** LOGGING DATA *****
        writer = tk.Toplevel(self.root)
        writer.title("Don't stop writing")
        writer.geometry("980x710")
        writer.config(bg=WBG, pady=20, padx=20)
        self.writer_open = True

    # ----------------- Writer UI Design -------------------

        # Labels
        self.timer_label = tk.Label(
            writer, text=f'{TIMER}', font=FONT, fg="white", bg="black",
            width=10
        )
        self.timer_label.grid(column=1, row=0, pady=10)

        self.words_label = tk.Label(
            writer,
            text=f"{len(self.prompt_text.split())} words",
            font=FONT
        )
        self.words_label.grid(row=2, column=1, pady=10)

        # Text
        self.typing_text = tk.Text(
            writer, font=TEXT_FONT, bg=TBG, fg=TFC,
            width=75, wrap='word', padx=20, pady=20
        )
        self.typing_text.insert(
            index='1.0', chars=self.prompt_text
        )
        self.typing_text.grid(
            column=0, row=1, columnspan=3
        )

    # ------------------- End UI Design ----------------------

        def start_typing(event):
            """
            start typing monitoring
            """
            log.debug("Typing Started")        # **** LOGGING DATA *****
            characters = self.typing_text.get('1.0', tk.END)
            pre_cnt = len(characters)
            count_down(TIMER, pre_cnt)

        def count_down(timer_count, pre_cnt):
            """
            count down logic
            """
            if not self.writer_open:
                return
            characters = self.typing_text.get('1.0', tk.END)
            words = characters.split()
            character_count = len(characters)
            word_count = len(words)
            self.words_label.config(text=f"{word_count} words")
            if pre_cnt == character_count and timer_count > 0:
                self.timer_label.config(text=timer_count)
                if timer_count > len(COLORS):
                    text_color_index = len(COLORS) - 1
                else:
                    text_color_index = timer_count - 1
                    debug_log_message = (
                        f"count_down {timer_count:<3} |  " +
                        "COLORS[{text_color_index}] = " +
                        f"{COLORS[text_color_index]}"
                    )
                    log.debug(debug_log_message)  # *** LOGGING DATA ***

                self.typing_text.config(fg=COLORS[text_color_index])
                root.after(1000, count_down, timer_count - 1, pre_cnt)
            elif pre_cnt != character_count:  # restart timer & update pre_cnt
                count_down(TIMER, character_count)
            else:  # time over
                text = self.typing_text.get('1.0', 'end-1c')
                if len(text) > 0:
                    text = f"DELETED TEXT: \n{text}"
                    log.debug(text)            # **** LOGGING DATA *****
                self.typing_text.delete(index1='1.0', index2=tk.END)
                self.words_label.config(text="0 words")
                self.timer_label.config(text="0")
                self.typing_text.config(fg=TFC)
                self.typing_text.insert(
                    index='1.0',
                    chars=('\n' * 11 + ' ' * 42 +
                           'TIMED OUT - Close the window and start again.'
                           )
                )

        self.typing_text.bind("<FocusIn>", start_typing)

        def save_text():
            """
            Save the typed text
            """
            text = self.typing_text.get('1.0', 'end-1c')
            if (len(text) > 0 and
               text != self.prompt_text and
               text[-45:] != 'TIMED OUT - Close the window and start again.'):
                log.debug(f'Saving Text\n{text}')  # ** LOGGING DATA ***

        def on_close():
            """
            Actions when closing window
            """
            log.debug('Starting on_close')     # **** LOGGING DATA *****
            save_text()
            self.writer_open = False
            writer.destroy()

        writer.protocol("WM_DELETE_WINDOW", on_close)


if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    log = get_logger("disappearing_text_app")
    log.debug("starting main loop")            # **** LOGGING DATA *****
    root.mainloop()
