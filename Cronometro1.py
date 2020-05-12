import time
import tkinter as tk


class Cronometro(tk.Frame):
    def __init__(self, root, *args, precision=10, **kwargs):
        super().__init__(root, *args, **kwargs)

        self.precision = precision
        self._timer = None
        self._pausado = True
        self._time = 0

        self.boton_cronometrar = tk.Button(self,
                                           text="Comenzar",
                                           font=("Arial", 20),
                                           width=9,
                                           command=self.cronometrar
                                           )
        self.boton_resetear = tk.Button(self,
                                        text="Resetear",
                                        font=("Arial", 20),
                                        width=9,
                                        command=self.resetear
                                        )
        self.label = tk.Label(self, font=("Arial", 50), text="00:00:00:000")

        self.boton_cronometrar.grid(row=0, column=0)
        self.grid_rowconfigure(1, minsize=50)
        self.label.grid(row=2, column=0)
        self.grid_rowconfigure(3, minsize=50)
        self.boton_resetear.grid(row=4, column=0)


    def cronometrar(self):
        if self._pausado:
            self._pausado = False
            self.boton_cronometrar.config(text="Pausar")
            self._timer = time.perf_counter()
            self._run()
        else:
            self._pausado = True
            self.boton_cronometrar.config(text="Reanudar")

    def resetear(self):
        self._pausado = True
        self._set_time(0)
        self.boton_cronometrar.config(text="Iniciar")

    def _run(self):
        if self._pausado:
            return
        last_timer = self._timer
        self._timer = time.perf_counter()
        self._set_time(self._time + (self._timer - last_timer))
        self.after(self.precision, self._run)

    def _set_time(self, t):
        self._time = t
        horas = int(t)
        segundos = int(t)
        decimas = int((t - segundos) * 1000)
        horas = int((t-segundos) / 10)
        minutos, segundos = divmod(segundos, 60)
        self.label.config(text=f"{horas:02}:{minutos:02}:{segundos:02}:{decimas:03}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cronómetro")
    root.resizable(False, False)
    root.geometry("400x300")
    cronometro = Cronometro(root, width=300, height=300, bg="grey")
    cronometro.pack(side="top", fill="both", expand=True)
    root.mainloop()
