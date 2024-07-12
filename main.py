#from gui import TuMontallantasApp, tk
from login import Login, tk

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    app.conectar_bd()  # Esta línea conecta la base de datos
    root.mainloop()