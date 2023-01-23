import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *

def Delete(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_Nim = listBox.selection()[0]
    select = listBox.set(row_Nim)
    e1.insert(0, select['Nim'])
    e2.insert(0, select['Nama'])
    e3.insert(0, select['Mata_kuliah'])
    e4.insert(0, select['Biaya'])

def Add():
    nim_mahasiswa = e1.get()
    nama_mahasiswa = e2.get()
    mata_kuliah = e3.get()
    biaya = e4.get()

    mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="registrasi_mahasiswa")
    mycursor=mysqldb.cursor()

    try:
        sql = "INSERT INTO daftar (Nim, Nama, Mata_kuliah, Biaya) VALUES (%s, %s, %s, %s)"
        val = (nim_mahasiswa, nama_mahasiswa, mata_kuliah, biaya)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Berhasil Menambahkan Data!")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    nim_mahasiswa = e1.get()
    nama_mahasiswa = e2.get()
    mata_kuliah = e3.get()
    biaya = e4.get()

    mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="registrasi_mahasiswa")
    mycursor=mysqldb.cursor()

    try:
        sql = "update daftar set Nama= %s, Mata_kuliah= %s, Biaya= %s where Nim= %s"
        val = (nama_mahasiswa, mata_kuliah, biaya, nim_mahasiswa)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Berhasil Memperbarui Data!")
    
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def delete():
    nim_mahasiswa = e1.get()
    nama_mahasiswa = e2.get()
    mata_kuliah = e3.get()
    biaya = e4.get()
    mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="registrasi_mahasiswa")
    mycursor=mysqldb.cursor()

    try:
        sql = "delete drom daftar Nama= %s, Mata_kuliah= %s, Biaya= %s where Nim = %s"
        val = (nama_mahasiswa, mata_kuliah, biaya, nim_mahasiswa)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Berhasil Menghapus Data!")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
    mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="registrasi_mahasiswa")
    mycursor=mysqldb.cursor()
    mycursor.execute("SELECT Nim, Nama, Mata_kuliah, Biaya FROM daftar")
    daftar1 = mycursor.fetchall()
    print(daftar1)

    for i, (Nim, Nama, Mata_kuliah, Biaya) in enumerate(daftar1, start=1):
        listBox.insert("", "end", values=(Nim, Nama, Mata_kuliah, Biaya))
        mysqldb.close()

root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4

tk.Label(root, text="Registrasi Mahasiswa", fg="Black", font=(None, 30)).place(x=400, y=5)
tk.Label(root, text="NIM").place(x=10, y=10)
tk.Label(root, text="Nama").place(x=10, y=40)
tk.Label(root, text="Mata Kuliah").place(x=10, y=70)
tk.Label(root, text="Biaya").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
         
e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

Button(root, text="Tambahkan", command = Add, height=3, width=15).place(x=30, y=130)

Button(root, text="Update", command = update, height=3, width=15).place(x=160, y=130)
Button(root, text="Hapus", command = delete, height=3, width=15).place(x=290, y=130)

cols = ('Nim', 'Nama', 'Mata_kuliah', 'Biaya')
listBox = ttk.Treeview(root, columns=cols, show='headings')


for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
 
show()
listBox.bind('<Double-Button-1>',Delete)
 
root.mainloop()
























