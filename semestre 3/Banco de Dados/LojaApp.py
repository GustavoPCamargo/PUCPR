from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.messagebox as msgbox
import mysql.connector as mysql

entryFields = {}
entryFieldsCatgoria = {}

colunas_tabelas = {
    'cliente': [
        ('idCliente', 'ID'),
        ('nome', 'Nome'),
        ('email', 'E-mail'),
        ('usuario', 'Usuário'),
        ('senha', 'Senha')
    ],
    'produto': [
        ('idProduto', 'ID'),
        ('nome', 'Nome'),
        ('descricao', 'Descrição'),
        ('valor', 'Valor R$'),
        ('fkIdCategoria', 'ID Categoria')
    ],
    'categoria': [
        ('idCategoria', 'ID'),
        ('nome', 'Nome'),
        ('genero', 'Gênero')
    ]
}

def connectLoja():
    try:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='Thormmond',
            database='Loja'
        )
        return con
    except mysql.Error as e:
        show_centered_error(root, 
            "Erro",
            f"Não foi possível conectar ao banco de dados:\n{e}"
        )
        return None

## ====================
##         CRUD
## ====================

#  ---------------------------
#      CREATE (INSERT)
#  ---------------------------

def create(tabela):
    if not entryFields or not any(entry.get() for entry in entryFields.values()):
        # Se ainda não houver campos de entrada, exibe uma mensagem de erro
        show_centered_error(root, 
            "Erro",
            "Primeiro selecione (READ) uma tabela / preencha os campos para INSERT de dados."
        )
        return

    dados = {k: v.get() for k, v in entryFields.items()}
    con = connectLoja()
    cursor = con.cursor()

    if tabela == 'cliente':
        if not dados['usuario'] or not dados['senha']:
            msgbox.showinfo("Alerta", "Os campos Usuário e Senha são obrigatórios.")
            return
        insert = f"INSERT INTO cliente (nome, email, usuario, senha) VALUES (%s, %s, %s, SHA2(%s, 256))" # Usando SHA2 para maior segurança
        valores = (dados['nome'], dados['email'], dados['usuario'], dados['senha'])
        cursor.execute(insert, valores)
    elif tabela == 'produto':
        if not dados['nome'] or not dados['valor'] or not dados['valor']:
            msgbox.showinfo("Alerta", "Os campos Nome e Valor são obrigatórios.")
            return
        insert = f"INSERT INTO produto (nome, descricao, valor, fkIdCategoria) VALUES (%s, %s, %s, %s)"
        valores = (dados['nome'], dados['descricao'], dados['valor'], dados['fkIdCategoria'] or None)
        cursor.execute(insert, valores)
    elif tabela == 'categoria':
        if not dados['nome'] or not dados['genero']:
            msgbox.showinfo("Alerta", "Os campos Nome e Gênero são obrigatórios.")
            return
        insert = f"INSERT INTO categoria (nome, genero) VALUES (%s, %s)"
        valores = (dados['nome'], dados['genero'])
        cursor.execute(insert, valores)
    con.commit()
    cursor.close()
    con.close()
    read(tabela)

#  ---------------------------
#      READ (SELECT)
#  ---------------------------
def read(tabela):
    if not tabela or tabela == "Selecione uma tabela":
        # Se ainda não houver campos de entrada, exibe uma mensagem de erro
        show_centered_error(root, 
            "Erro",
            "Primeiro selecione uma tabela para visualizar dados."
        )
        return
    
    tree.delete(*tree.get_children())
    tree["show"] = "headings"
    campos = colunas_tabelas.get(tabela, [])
    colunas_visiveis = [t for k, t in campos if not(k == 'senha')]
    campos_query = [k for k, t in campos if not(k == 'senha')]

    tree["columns"] = colunas_visiveis
    for col in colunas_visiveis:
        tree.heading(col, text=col)
        tree.column(col, anchor=CENTER, width=100)
    select = f"SELECT {', '.join(campos_query)} FROM {tabela}"

    con = connectLoja()
    cursor = con.cursor()
    cursor.execute(select)
    result = cursor.fetchall()
    for row in result:
        tree.insert("", END, values=row)
    cursor.close()
    con.close()
    atualizaLabels(tabela)

#  ---------------------------
#      UPDATE
#  ---------------------------
def update(tabela):
    if not entryFields or not any(entry.get() for entry in entryFields.values()):
        # Se ainda não houver campos de entrada, exibe uma mensagem de erro
        show_centered_error(root, 
            "Erro",
            "Primeiro selecione (READ) uma tabela  / selecione um registro para UPDATE de dados."
        )
        return
    
    dados = {k: v.get() for k, v in entryFields.items()}
    con = connectLoja()
    cursor = con.cursor()
    if tabela == 'cliente':
        id = dados['idCliente']
        cursor.execute("UPDATE cliente SET nome=%s, email=%s, usuario=%s, senha=SHA2(%s,256) WHERE idCliente=%s", # Usando SHA2 para maior segurança
                       (dados['nome'], dados['email'], dados['usuario'], dados['senha'], id))
    elif tabela == 'produto':
        id = dados['idProduto']
        cursor.execute("UPDATE produto SET nome=%s, descricao=%s, valor=%s, fkIdCategoria=%s WHERE idProduto=%s", 
                       (dados['nome'], dados['descricao'], dados['valor'], dados['fkIdCategoria'], id))
    elif tabela == 'categoria':
        id = dados['idCategoria']
        cursor.execute("UPDATE categoria SET nome=%s, genero=%s WHERE idCategoria=%s", 
                       (dados['nome'], dados['genero'], id))
    con.commit()
    cursor.close()
    con.close()
    read(tabela)

#  ---------------------------
#      DELETE
#  ---------------------------
def delete(tabela):
    if not entryFields or not any(entry.get() for entry in entryFields.values()):
        # Se ainda não houver campos de entrada, exibe uma mensagem de erro
        show_centered_error(root, 
            "Erro",
            "Primeiro selecione (READ) uma tabela  / selecione um registro para DELETE de dados."
        )
        return

    dados = {k: v.get() for k, v in entryFields.items()}
    con = connectLoja()
    cursor = con.cursor()
    if tabela == 'cliente':
        id = dados['idCliente']
        cursor.execute("DELETE FROM cliente WHERE idCliente=%s;",(id,))
    elif tabela =='produto':
        id = dados['idProduto']
        cursor.execute("DELETE FROM produto WHERE idProduto=%s;",(id,))
    elif tabela == 'categoria':
        id = dados['idCategoria']
        cursor.execute("DELETE FROM categoria WHERE idCategoria=%s;",(id,))
    con.commit()
    cursor.close()
    con.close()
    read(tabela)


## ====================
## === OUTRAS FUNCOES ===
## ====================

#  ---------------------------
#  Função atualizaLabels(tabela): 
#  Atualiza os labels e campos de entrada, de acordo com a tabela selecionada.
#  ---------------------------
def atualizaLabels(tabela):
    global frameEntry, entryFields, frameCategorias
    
    try:
        frameEntry.destroy()
    except:
        pass

    try:
        frameCategorias.destroy()
    except:
        pass

    entryFields.clear()
    frameEntry = Frame(root, bg='#b3c7e6')
    frameEntry.place(x=20, y=420)

    # Adiciona o label 'Dados' ao frameEntry
    label_dados = Label(frameEntry, text='Dados', font=('verdana', 12, 'bold'), bg='#b3c7e6', fg='#434343')
    label_dados.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=(0, 12))

    campos = colunas_tabelas.get(tabela, [])

    # Cria os campos de entrada dinamicamente
    for i, (chave, texto) in enumerate(campos):
        label = Label(frameEntry, text=texto, bg='#b3c7e6', fg='#434343')
        label.grid(row=i+1, column=0, sticky='w', padx=5, pady=2)
        ent = Entry(frameEntry, width=30)
        ent.grid(row=i+1, column=1, padx=5, pady=2)
        entryFields[chave] = ent
        if texto == 'ID': # Torna o campo ID somente leitura, pois no BD é auto_increment
            ent.config(state='readonly')

    # Cria um frame para a treeview de categorias
    if tabela == 'produto':
        frameCategorias = Frame(root, bg='#b3c7e6')
        frameCategorias.place(x=700, y=420, width=270, height=150)
        labelCat = Label(frameCategorias, text="Categorias", font=('verdana', 12, 'bold'), bg='#b3c7e6')
        labelCat.pack(pady=2, anchor='w') # Adiciona o label 'Categorias' ao frameCategorias, alinhado à esquerda
        carregar_categorias()

#  ---------------------------
#  Função carregar_categorias():
#  Carrega a treeview de categorias no frameCategorias.
#  ---------------------------    
def carregar_categorias():
    global treeCategorias
    treeCategorias = ttk.Treeview(frameCategorias, columns=('ID', 'Nome', 'Gênero'), show='headings', height=5)
    treeCategorias.bind("<ButtonRelease-1>", on_treeCat_select)   
    treeCategorias.heading('ID', text='ID')
    treeCategorias.heading('Nome', text='Nome')
    treeCategorias.heading('Gênero', text='Gênero')
    treeCategorias.column('ID', width=40, anchor=CENTER)
    treeCategorias.column('Nome', width=120, anchor=W)
    treeCategorias.column('Gênero', width=80, anchor=W)
    treeCategorias.pack(fill='both', expand=True)

    treeCategorias.delete(*treeCategorias.get_children())
    con = connectLoja()
    cursor = con.cursor()
    cursor.execute("SELECT idCategoria, nome, genero FROM categoria")
    for row in cursor.fetchall():
        treeCategorias.insert('', END, values=row)
    cursor.close()
    con.close()        

#  ---------------------------
#  Função on_tree_select(event):    
#  Atualiza os campos de entrada com os dados do item selecionado na treeview principal.
#  ---------------------------        
def on_tree_select(event):
    selected_item = tree.focus()
    if not selected_item:
        return

    valores = tree.item(selected_item)['values']
    campos = colunas_tabelas.get(tabela.get(), [])
    campos = [k for k, t in campos if not(k == 'senha')]

    for i, chave in enumerate(campos):
        entry = entryFields[chave]
        entry.config(state='normal')  # Permite edição antes de atualizar o valor
        entry.delete(0, END)
        entry.insert(0, valores[i])
        if chave == 'idCliente' or chave == 'idProduto' or chave == 'idCategoria':
            entry.config(state='readonly')  # Torna campo para ID somente leitura: no BD, está audo_increment 

    # Se for produto, selecionar categoria correspondente
    if tabela.get() == 'produto':
        id_categoria = valores[4]  # fkIdCategoria é o 5º campo
        for item in treeCategorias.get_children():
            if str(treeCategorias.item(item)['values'][0]) == str(id_categoria):
                treeCategorias.selection_set(item)
                treeCategorias.see(item)
                break

#  ---------------------------
#  Função on_treeCat_select(event):
#  Atualiza o campo fkIdCategoria no formulário de produto, ao selecionar uma categoria na treeview de categorias.
#  ---------------------------
def on_treeCat_select(event):
    selected_item = treeCategorias.focus()
    if not selected_item:
        return
    valores = treeCategorias.item(selected_item)['values']
    id_categoria = valores[0]
    # Procura o campo correspondente ao ID da categoria
    for chave in entryFields:
        if chave.lower() in ['fkidcategoria', 'idcategoria']:
            entry = entryFields[chave]
            entry.delete(0, END)
            entry.insert(0, id_categoria)
            break

#  ---------------------------
#  Função clearEntry():
#  Limpa todos os campos de entrada.
#  ---------------------------
def clearEntry():
    #for entry in entryFields.values():
    #    entry.delete(0, END)
    for chave, entry in entryFields.items():
        estado_atual = entry.cget('state')
        if estado_atual == 'readonly':
            entry.config(state='normal')
            entry.delete(0, END)
            entry.config(state='readonly')
        else:
            entry.delete(0, END)

#  ---------------------------
#  Função show_centered_error(parent, title, message):
#  Exibe uma mensagem de erro em um modal centralizado em relação à janela parent.
#  ---------------------------
def show_centered_error(parent, title, message):
    win = Toplevel(parent)
    win.title(title)
    win.transient(parent)
    win.grab_set()
    Label(win, text=message, font=('verdana', 10), padx=20, pady=15).pack()
    Button(win, text="OK", command=win.destroy, width=10).pack(pady=(0, 10))
    win.update_idletasks()
    # Centraliza o modal em relação ao parent
    x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (win.winfo_width() // 2)
    y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (win.winfo_height() // 2)
    win.geometry(f"+{x}+{y}")
    win.resizable(False, False)

#############################################################

#  ---------------------------
#  WIDGET: 
#  cria a janela principal e seus componentes interativos, ou cria a GUI (graphical user interface).
#  ---------------------------

root = Tk()
root.geometry("1000x600")
root.title("Loja de Departamentos")
root.configure(background='#b3c7e6')

#  ---------------------------
#  STYLES:
#  Define estilos para botões, labels, entradas e treeview.
#  ---------------------------
style = ttk.Style()
style.configure('b.TButton', 
      font=('consolas', 10), 
      bg="#6a93c7", 
      fg="#b3c7e6",
      width=15
)

style = ttk.Style()
style.configure('texto.TLabel',
      fg="#434343",
      bg='#b3c7e6'
)

style = ttk.Style()
style.configure('e.TEntry', 
      font=('verdana', 12), 
      fg="#434343"
)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview",
    background="#d0e3f0",
    foreground='#434343',
    fieldbackground='#d0e3f0')
style.map('Treeview',
    background=[('selected', "#6a93c7")])

#  ---------------------------
#  TITULO LOJA DEPARTAMENTO
#  ---------------------------
titulo = Label(root, text="LOJA DE DEPARTAMENTOS", font=('verdana', 25, 'bold'), bg='#b3c7e6')
titulo.place(relx=0.5, y=30, anchor='center')

#  ---------------------------
#  DROPDOWN P/ ESCOLHER A TABELA
#  ---------------------------
tabela = StringVar()
tabDropdown = ttk.Combobox(root, textvariable=tabela, state='readonly')
tabDropdown['values'] = ('cliente', 'produto', 'categoria')
tabDropdown.set("Selecione uma tabela")
tabDropdown.place(x=20, y=60, width=150)

#  ---------------------------
#  TREEVIEW P/ MOSTRAR AS TABELAS
#  ---------------------------
tree = ttk.Treeview(root)
tree.place(x=20, y=100, width=950, height=300)
tree.bind("<ButtonRelease-1>", on_tree_select) # Seleção de item na tabela chama a função on_tree_select

#  ---------------------------
#  BOTÃO SELECT
#  ---------------------------
btnRead = ttk.Button(root, text="READ", command=lambda: read(tabela.get()), style='b.TButton')
btnRead.place(x=200, y=58)

#  ---------------------------
#  BOTÕES CRUD
#  ---------------------------
frameCrud = Frame(root, bg='#b3c7e6')
frameCrud.place(x=320, y=445)

btnCreate = ttk.Button(frameCrud, text="INSERT", width=12, command=lambda: create(tabela.get()), style='b.TButton')
btnCreate.grid(row=0, column=0, sticky='w', padx=5, pady=2)

btnUpdate = ttk.Button(frameCrud, text="UPDATE", width=12, command=lambda: update(tabela.get()), style='b.TButton')
btnUpdate.grid(row=1, column=0, sticky='w', padx=5, pady=2)

btnDelete = ttk.Button(frameCrud, text="DELETE", width=12, command=lambda: delete(tabela.get()), style='b.TButton')
btnDelete.grid(row=2, column=0, sticky='w', padx=5, pady=2)

btnClear = ttk.Button(frameCrud, text="CLEAR", width=12, command=clearEntry, style='b.TButton')
btnClear.grid(row=3, column=0, sticky='w', padx=5, pady=2)

root.mainloop() # Mantém a janela aberta