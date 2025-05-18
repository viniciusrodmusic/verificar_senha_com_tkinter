from tkinter import *
from tkinter import messagebox

def verificar_senha(senha):

	if len(senha) < 8:
		return False
	temMaius = temMinus = temNum = temEspecial = False

	for char in senha:
		if char.isupper():
			temMaius = True
		elif char.islower():
			temMinus = True
		elif char.isdigit():
			temNum = True
		else:
			temEspecial = True
	return temMaius and temMinus and temNum and temEspecial
			
def classifica_senha():
	senha_verificada = verificar_senha(entrada_senha.get())
	if senha_verificada:
		messagebox.showinfo('Intensidade da senha', 'A senha é forte')
	else:
		messagebox.showinfo('Intensidade da senha', 'A senha é fraca')



# ROOT
janela = Tk()
janela.title("Verificador de senhas")
janela.geometry("500x500")
janela.configure(bg='#1b1521')
janela.resizable(False, False)

# FRAME
campo_de_senha = Frame(janela, bg="#261e2e", borderwidth=5, relief='flat')
campo_de_senha.pack(padx=100, pady=100, fill='both', expand=True)

# LABEL(texto) DO INPUT
label_senha = Label(campo_de_senha, text="Digite sua senha", font=('Times New Roman', 20), bg="#251d2e", fg='white')
label_senha.place(relx=0.5, rely=0.1, anchor=CENTER)

# INPUT FIELD
entrada_senha = Entry(campo_de_senha)#, show='*')
entrada_senha.place(relx=0.5, rely=0.5, anchor=CENTER, width=200)

# FOTO dentro do FRAME
imagem = PhotoImage(file='cadeado.png')
new_image = imagem.subsample(27, 27)
logo = Label(campo_de_senha, image=new_image, bg='#251d2e')
logo.place(relx=0.5, rely=0.3, anchor=CENTER)

# BOTÃO PRA VERIFICAR A SENHA
botao = Button(campo_de_senha, text="Verificar", command=classifica_senha, bg="#7b6691", fg='white')
botao.place(relx=0.5, rely=0.7, anchor=CENTER)




janela.mainloop()
