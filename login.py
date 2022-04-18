from msilib.schema import SelfReg
import tkinter
from tkinter.tix import COLUMN
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from turtle import left, width
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage

#PRUEBA DE COMMIT#


from tkinter import *

class Inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('500x500+400+80')
        self.protocol("WM_DELETE_WINDOW")
        self.state('zoomed')
        self.title("SISTEMA GENERAL")
        self.iconbitmap("sist.ico")
        
        image=PhotoImage(file="IUV.gif")
        image=image.subsample(2,2)
        label=Label(image=image)
        label.pack()
        
        Label(self, text="GRUPO IMISA\n SISTEMA GENERAL", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(self, text="").pack()
        Label(self, text="EMPRESA", bg="navy", fg="white",padx=5, pady=5, width=10).pack()
        var=tk.StringVar(self)
        var.set('EMPRESA')
        opciones=['IMISA', 'ARENAS','CALIZAS', 'CANTERAS', 'HOTEL', 'TOPACIO', 'OROSI']
        opcion=ttk.OptionMenu(self, var,*opciones)
        opcion.config(width=10)
        opcion.pack(padx=5, pady=5)
        #empresa=tk.Label(self, bg="navy", fg="white", textvariable=var, padx=5, pady=5, width=10)
        #empresa.pack()
        global nombreusuario_verify
        global contrasenausuario_verify
    
        nombreusuario_verify=StringVar()
        contrasenausuario_verify=StringVar()
    
        global nombreusuario_entry
        global contrasenausuario_entry
    
        Label(self, text="USUARIO").pack()
        nombreusuario_entry = Entry(self, textvariable=nombreusuario_verify)
        #nombreusuario_entry.pack(x=70, y=20)
        nombreusuario_entry.pack()
    
        Label(self, text="CONTRASEÑA").pack()
        contrasenausuario_entry = Entry(self, show="*", textvariable=contrasenausuario_verify)
        contrasenausuario_entry.pack()
    
        tk.Button(self, text="INICIO SESION", command=self.Validardatos).pack()

    def Validardatos(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )
    
        fcursor=bd.cursor()
    
        fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contrasenausuario_verify.get()+"'")
    
        if fcursor.fetchall():
            messagebox.showinfo(title="Inicio de Sesion Correcto", message="Usuario y Contraseña correcta")
            Login(self)
            self.withdraw()

        else:
            messagebox.showinfo(title="Inicio de Sesion Incorrecto", message="Usuario y Contraseña Incorrectos")
        
        bd.close()
        
        #Login(self)
        #self.withdraw()
        
            
class Login(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.geometry('500x500+400+80')
        self.protocol("WM_DELETE_WINDOW")
        self.state('zoomed')
        self.title("SISTEMA GENERAL - INICIO")
        self.iconbitmap("sist.ico")
    
    
        image=PhotoImage(file="IUV.gif")
        image=image.subsample(2,2)
        label=Label(image=image)
        label.pack()

    
        Label(self, text="BIENVENIDO AL SISTEMA GENERAL", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(self, text="").pack()
    
        barraMenu=Menu(self, bg='white')
        self.config(menu=barraMenu, width=300, height=300, bg='white')

        bbddMenu=Menu(barraMenu, tearoff=0, bg='white')
        #bbddMenu.add_command(label="Conectar")
        bbddMenu.add_command(label="Salir", command=self.main_window)

        tablaMenu=Menu(barraMenu, tearoff =0, bg='white')
        tablaMenu.add_command(label="Empresas", command=self.empresas)
        tablaMenu.add_command(label="Areas", command=self.area)
        tablaMenu.add_separator()

        tablaMenu.add_command(label="Tasa de Cambio", command=self.tasa)
        tablaMenu.add_command(label="Proveedores", command=self.proveedores)
        tablaMenu.add_command(label="Cuentas Contables", command=self.Cuentas)
        tablaMenu.add_command(label="Grupo de Elementos", command=self.Grupo)
        tablaMenu.add_command(label="Elementos de Gastos", command=self.Elemento)

        reportMenu=Menu(barraMenu, tearoff=0, bg='white')
        reportMenu.add_command(label="Reporte1")
        reportMenu.add_command(label="Reporte2")
        reportMenu.add_command(label="Reporte3")
        reportMenu.add_command(label="Reporte4")

        ayudaMenu=Menu(barraMenu, tearoff=0, bg='white')
        ayudaMenu.add_command(label="Informacion del diseñador del sistema", command=self.informacion)

        barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
        barraMenu.add_cascade(label="Tablas", menu=tablaMenu)
        barraMenu.add_cascade(label="Reportes", menu=reportMenu)
        barraMenu.add_cascade(label="Informacion", menu=ayudaMenu)

        #Button(self, text="Salir").pack()
        #tk.Button(self, text="SALIR, REGRESAR AL INICIO DE SESION", command=self.main_window).pack()

    def main_window(self):
        self.master.deiconify()
        self.destroy()
        
    def empresas(self):
        pantalla3 = Toplevel(self)
        pantalla3.geometry("480x250")
        pantalla3.resizable(0,0)
        pantalla3.title("FORMULARIO DE EMPRESAS")
        pantalla3.iconbitmap("sist.ico")
    
        global idempresa
        global nomempresa
        
        global idempresa_entry
        global nomempresa_entry
        global value
    
        idempresa=StringVar()
        nomempresa=StringVar()
        value = tk.IntVar()

    
    
        Label(pantalla3, text="SISTEMA GENERAL\n ACTUALIZACION DE EMPRESAS", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        
        
        Label(pantalla3, text="ID").pack()
        idempresa_entry = Entry(pantalla3, textvariable=idempresa)
        idempresa_entry.config(state='disabled')
        idempresa_entry.pack()
    
        Label(pantalla3, text="DESCRIPCION DE LA EMPRESA").pack()
        nomempresa_entry = Entry(pantalla3, textvariable=nomempresa)
        nomempresa_entry.pack()
        
        Checkbutton(pantalla3, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.display).pack()
        #Checkbutton.pack(pantalla3,side=tk.LEFT)
        
        Button(pantalla3, text="GUARDAR",command=self.insertar_empresas).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla3, text="ACTUALIZAR",command=self.ActualizarEmpresa).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla3, text="BUSCAR",command=self.buscarempresa).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla3, text="ELIMINAR",command=self.EliminarEmpresa).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla3, text="LIMPIAR CAMPOS",command=self.limpiarEmpre).pack(side=tk.LEFT, padx=10, pady=10)
        
        
        
        
    def display(self):
        print(value.get())
        
        if value.get() == True:
            idempresa_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            idempresa_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID deshabilitada")
            
    def limpiarEmpre(self):
    
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()

        nomempresa.set("")
        idempresa.set("")

 
    def insertar_empresas(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )
        if not nomempresa.get():
            messagebox.showwarning("Crear", "No puede guardar el registro sin la descripcion de la empresa")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.empresas (idempresa, nomempresa) VALUES ('{0}', '{1}')".format(idempresa_entry.get(), nomempresa_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Empresa guardada con exito", title="Aviso")
            #idempresa.set("")
            #nomempresa.set("")   
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar la empresa", title="Aviso") 
        
        bd.close()
         
    def buscarempresa(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.empresas WHERE idempresa='" + idempresa_entry.get()+"'")
        miEmpresa=fcursor.fetchall()
        
        if len(miEmpresa)==0:
            messagebox.showinfo("CRUD", "El registro no existe")
            return
        for empresa in miEmpresa:
            #print(empresa[0])
            #print(empresa[1])
            idempresa.set(empresa[0])
            nomempresa.set(empresa[1])
        
        bd.close()
        
    def EliminarEmpresa(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.empresas WHERE idempresa=" + idempresa.get())
        mysqldb.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")
        
    def ActualizarEmpresa(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(nomempresa.get(),)
        mycursor.execute("UPDATE python.empresas SET nomempresa=%s WHERE idempresa=" + idempresa.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("BBDD", "Registro Actualizado con exito")
    

    def area(self):
        global pantalla4
        #pantalla0.destroy()
        pantalla4 = Toplevel()
        pantalla4.geometry("350x350")
        pantalla4.resizable(0,0)
        pantalla4.title("AREAS")
        pantalla4.iconbitmap("sist.ico")
    
    
        global idarea_entry
        global nomarea_entry
        global cuenta_entry
        
        global idarea
        global nomarea
        global cuenta
    
        idarea=StringVar()
        nomarea=StringVar()
        cuenta=StringVar()
        
        global value
        value = tk.IntVar()
    
        Label(pantalla4, text="SISTEMA GENERAL\n ACTUALIZACION DE AREA", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        #Label(pantalla4, text="").pack()
    
        Label(pantalla4, text="ID").pack()
        idarea_entry = Entry(pantalla4, textvariable=idarea)
        idarea_entry.config(state='disabled')
        idarea_entry.pack()
        #Label(pantalla4).pack()
    
        Label(pantalla4, text="NOMBRE DE AREA").pack()
        nomarea_entry = Entry(pantalla4, textvariable=nomarea)
        nomarea_entry.pack()
        Label(pantalla4).pack()
    
        Label(pantalla4, text="CUENTA CONTABLE").pack()
        cuenta_entry = Entry(pantalla4, textvariable=cuenta)
        cuenta_entry.pack()
        Label(pantalla4).pack()
        
        Checkbutton(pantalla4, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.displayarea).pack()
        #check_button.grid(row=1, column=4, sticky="e", padx=10, pady=10)
    
        Button(pantalla4, text="GUARDAR",command=self.insertar_area).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla4, text="ELIMINAR", command=self.ActualizarArea).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla4, text="BUSCAR", command=self.buscararea).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla4, text="ELIMINAR", command=self.EliminarArea).pack(side=tk.LEFT, padx=10, pady=10)
        
        
    def displayarea(self):
        print(value.get())
        
        if value.get() == True:
            idarea_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            idarea_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
    
    
    def insertar_area(self):
        bd=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db="python"
        )
        
        if not nomarea.get():
            messagebox.showwarning("Crear", "No puede guardar el registro sin el nombre del area")
            return
        
        if not cuenta.get():
            messagebox.showwarning("Crear", "No puede guardar el registro sin una cuenta")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.area (idarea, nomarea, cuenta) VALUES ('{0}', '{1}', '{2}')".format(idarea_entry.get(), nomarea_entry.get(), cuenta_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Area guardada con exito", title="Aviso")
        
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar el Area", title="Aviso") 
        
        bd.close()
        
    def buscararea(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.area WHERE idarea='" + idarea_entry.get()+"'")
        miArea=fcursor.fetchall()
        
        if len(miArea)==0:
            messagebox.showinfo("CRUD", "El registro no existe")
            return
        for areas in miArea:
            idarea.set(areas[0])
            nomarea.set(areas[1])
            cuenta.set(areas[2])
        
        bd.close()
        
    def EliminarArea(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.area WHERE idarea=" + idarea.get())
        mysqldb.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")
        
    def ActualizarArea(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(nomarea.get(),cuenta.get())
        mycursor.execute("UPDATE python.area SET nomarea=%s,cuenta=%s WHERE idarea=" + idarea.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("AVISO", "Registro Actualizado con exito")
    
    def tasa(self):
        global pantalla4
        pantalla4 = Toplevel()
        pantalla4.geometry("350x350")
        pantalla4.resizable(0,0)
        pantalla4.title("TASA DE CAMBIO")
        pantalla4.iconbitmap("sist.ico")
    
    
        global fechatasa_entry
        global tasac_entry
        
        global fechatasa
        global tasac
    
        fechatasa=StringVar()
        tasac=StringVar()
        
        global value
        value = tk.IntVar()
    
        Label(pantalla4, text="SISTEMA GENERAL\n ACTUALIZACION DE TASA DE CAMBIO", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(pantalla4, text="").pack()
    
        Label(pantalla4, text="FECHA").pack()
        fechatasa_entry = Entry(pantalla4,textvariable=fechatasa)
        fechatasa_entry.config(state='disabled')
        fechatasa_entry.pack()
        Label(pantalla4).pack()
    
        Label(pantalla4, text="TASA DE CAMBIO").pack()
        tasac_entry = Entry(pantalla4, textvariable=tasac)
        tasac_entry.pack()
        Label(pantalla4).pack()
        
        Checkbutton(pantalla4, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.displayTasa).pack()
        #check_button.grid(row=1, column=4, sticky="e", padx=10, pady=10)
        
        Button(pantalla4, text="GUARDAR", command=self.insertar_tasa).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla4, text="ACTUALIZAR", command=self.ActualizarTasa).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla4, text="BUSCAR", command=self.buscartasa).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla4, text="ELIMINAR", command=self.EliminarTasa).pack(side=tk.LEFT, padx=10, pady=10)
        
        
    def displayTasa(self):
        print(value.get())
        
        if value.get() == True:
            fechatasa_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            fechatasa_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID deshabilitada")

    
    
    def insertar_tasa():
        bd=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db="python"
        )
        
        if not fechatasa.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin la tasa de cambio")
            return
        
        if not tasac.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin la tasa de cambio")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.tasa (fechatasa, tasac) VALUES ('{0}', '{1}')".format(fechatasa_entry.get(), tasac_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Tasa guardada con exito", title="Aviso")
        
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar la tasa", title="Aviso") 
        
        bd.close()
        
    def buscartasa(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.tasa WHERE fechatasa='" + fechatasa_entry.get()+"'")
        miTasa=fcursor.fetchall()
        
        if len(miTasa)==0:
            messagebox.showinfo("AVISO", "El registro no existe")
            return
        for tas in miTasa:
            idarea.set(tas[0])
            nomarea.set(tas[1])
        
        bd.close()
        
    def EliminarTasa(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.tasa WHERE fechatasa=" + fechatasa.get())
        mysqldb.commit()
        messagebox.showinfo("AVISO", "Tasa eliminado con exito")
        
    def ActualizarTasa(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(fechatasa.get(),tasac.get(),)
        mycursor.execute("UPDATE python.tasa SET fechatasa=%s,tasac=%s WHERE fechatasa=" + fechatasa.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("AVISO", "Tasa Actualizado con exito")
    
    def proveedores(self):
        global pantalla5
        pantalla5 = Toplevel()
        pantalla5.geometry("350x600")
        pantalla5.resizable(0,0)
        pantalla5.title("PROVEEDORES")
        pantalla5.iconbitmap("sist.ico")
    
    
        global id_entry
        global nompro_entry
        global ruc_entry
        global telef_entry
        global email_entry
        global direccion_entry
        
        global id
        global nompro
        global ruc
        global telef
        global email
        global direccion
    
        id=StringVar()
        nompro=StringVar()
        ruc=StringVar()
        telef=StringVar()
        email=StringVar()
        direccion=StringVar()
        
        global value
        value = tk.IntVar()

    
        Label(pantalla5, text="SISTEMA GENERAL\n ACTUALIZACION DE PROVEEDORES", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(pantalla5, text="").pack()
    
        Label(pantalla5, text="PROVEEDOR").pack()
        id_entry = Entry(pantalla5,textvariable=id)
        id_entry.config(state='disabled')
        id_entry.pack()
        Label(pantalla5).pack()
    
        Label(pantalla5, text="NOMBRE DEL PROVEEDOR").pack()
        nompro_entry = Entry(pantalla5,textvariable=nompro)
        nompro_entry.pack()
        Label(pantalla5).pack()
    
        Label(pantalla5, text="RUC").pack()
        ruc_entry = Entry(pantalla5, textvariable=ruc)
        ruc_entry.pack()
        Label(pantalla5).pack()
    
        Label(pantalla5, text="TELEFONO").pack()
        telef_entry = Entry(pantalla5, textvariable=telef)
        telef_entry.pack()
        Label(pantalla5).pack()
    
        Label(pantalla5, text="CORREO").pack()
        email_entry = Entry(pantalla5, textvariable=email)
        email_entry.pack()
        Label(pantalla5).pack()
    
        Label(pantalla5, text="DIRECCION").pack()
        direccion_entry = Entry(pantalla5, textvariable=direccion)
        
        direccion_entry.pack()
        Label(pantalla5).pack()
        
        Checkbutton(pantalla5, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.displayProve).pack()
        #check_button.grid(row=1, column=4, sticky="e", padx=10, pady=10)
    
    
        Button(pantalla5, text="GUARDAR", command=self.insertar_proveedor).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla5, text="ACTUALIZAR", command=self.ActualizarProveedor).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla5, text="BUSCAR", command=self.buscarproveedores).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla5, text="ELIMINAR",command=self.EliminarProveedor).pack(side=tk.LEFT, padx=10, pady=10)
        
        
    def displayProve(self):
        print(value.get())
        
        if value.get() == True:
            id_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            id_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID deshabilitada")
    
    
    def insertar_proveedor(self):
        bd=mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            db="python"
        )
        
        if not nompro.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin el nombre del proveedor")
            return
        
        if not ruc.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin el numero RUC")
            return
        
        if not telef.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin un numero de telefono")
            return
        
        if not email.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin un email")
            return
        if not direccion.get():
            messagebox.showwarning("ERROR", "No puede guardar el registro sin una direccion")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.proveedores (idpro, nompro, ruc, telef, email, direccion) VALUES ('{0}', '{1}', '{2}','{3}', '{4}', '{5}')".format(id_entry.get(), nompro_entry.get(), ruc_entry.get(), telef_entry.get(), email_entry.get(), direccion_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Proveedor guardado con exito", title="Aviso")
        
        
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar el Proveedor", title="Aviso") 
        
        bd.close()
        
    def buscarproveedores(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.proveedores WHERE idpro='" + id_entry.get()+"'")
        miProve=fcursor.fetchall()
        
        if len(miProve)==0:
            messagebox.showinfo("CRUD", "El registro no existe")
            return
        for prove in miProve:
            id.set(prove[0])
            nompro.set(prove[1])
            ruc.set(prove[2])
            telef.set(prove[3])
            email.set(prove[4])
            direccion.set(prove[5])
        
        bd.close()
        
    def EliminarProveedor(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.proveedores WHERE idpro=" + id.get())
        mysqldb.commit()
        messagebox.showinfo("AVISO", "Proveedor eliminado con exito")
        
    def ActualizarProveedor(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(nompro.get(),ruc.get(),telef.get(),email.get(),direccion.get())
        mycursor.execute("UPDATE python.proveedores SET nompro=%s,ruc=%s,telef=%s,email=%s,direccion=%s WHERE idpro=" + id.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("AVISO", "Proveedor Actualizado con exito")
    
    def informacion(self):
        global pantalla6
        pantalla6 = Toplevel(self)
        pantalla6.geometry("350x250")
        pantalla6.resizable(0,0)
        pantalla6.title("Sistema General - INFORMACION")
        pantalla6.iconbitmap("sist.ico")
    
        image=PhotoImage(file="IUV.gif")
        image=image.subsample(2,2)
        label=Label(image=image)
        label.pack()

    
        Label(pantalla6, text="GRUPO IMISA, SISTEMA GENERAL", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(pantalla6, text="Copyright (c) 2022").pack()
        Label(pantalla6, text="Desarrollo de Sistemas").pack()
    
        Label(pantalla6, text="Advertencia: este programa informático esta protegido por las leyes\n de derecho de autor y otros tratados internacionales.\n La reproducción o distribución no autorizadas de\n este programa, o de cualquier parte del mismo,\n puede dar lugar a responsabilidades", font=("Calibri", 8)).pack()
        
    def Cuentas(self):
        global pantalla7
        pantalla7 = Toplevel()
        pantalla7.geometry("350x600")
        pantalla7.resizable(0,0)
        pantalla7.title("CUENTAS CONTABLES")
        pantalla7.iconbitmap("sist.ico")
    
    
        global id_entry
        global nomcue_entry
        global nivel_entry
        #global ticuenta_entry
        #global natura_entry
        #global moneda_entry
        
        global id
        global nomcue
        global nivel
        global ticuenta
        global natura
        global moneda
    
        id=StringVar()
        nomcue=StringVar()
        nivel=StringVar()
        ticuenta=StringVar()
        natura=StringVar()
        moneda=StringVar()
        
        global value
        value = tk.IntVar()

    
        Label(pantalla7, text="SISTEMA GENERAL\n ACTUALIZACION DE CUENTAS", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(pantalla7, text="").pack()
    
        Label(pantalla7, text="CUENTA").pack()
        id_entry = Entry(pantalla7,textvariable=id)
        id_entry.config(state='disabled')
        id_entry.pack()
        Label(pantalla7).pack()
    
        Label(pantalla7, text="DESCRIPCION DE LA CUENTA").pack()
        nomcue_entry = Entry(pantalla7,textvariable=nomcue)
        nomcue_entry.pack()
        Label(pantalla7).pack()
    
        Label(pantalla7, text="NIVEL").pack()
        nivel_entry = Entry(pantalla7, textvariable=nivel)
        nivel_entry.pack()
        Label(pantalla7).pack()
    
        Label(pantalla7, text="TIPO DE CUENTA").pack()
        var=tk.StringVar(pantalla7)
        var.set('MAYOR')
        opciones=['MAYOR', 'DETALLE']
        opcion=ttk.OptionMenu(pantalla7, var,*opciones)
        opcion.config(width=20)
        opcion.pack(padx=10, pady=10)
    
        Label(pantalla7, text="NATURALEZA").pack()
        var=tk.StringVar(pantalla7)
        var.set('DEBITO')
        opciones=['DEBITO', 'CREDITO','AMBAS']
        opcion=ttk.OptionMenu(pantalla7, var,*opciones)
        opcion.config(width=20)
        opcion.pack(padx=10, pady=10)
        
        Label(pantalla7, text="MONEDA").pack()
        var=tk.StringVar(pantalla7)
        var.set('DOLARES')
        opciones=['DOLARES', 'CORDOBAS']
        opcion=ttk.OptionMenu(pantalla7, var,*opciones)
        opcion.config(width=20)
        opcion.pack(padx=5, pady=5)

        '''Label(pantalla7, text="MONEDA").pack()
        moneda_entry = Entry(pantalla7, textvariable=moneda)
        moneda_entry.pack()
        Label(pantalla7).pack()'''
        
        Checkbutton(pantalla7, text="Es cuenta de Banco?", variable=value, onvalue=1, offvalue=0, command=self.displayProve).pack()
        Checkbutton(pantalla7, text="Es cuenta de Gasto?", variable=value, onvalue=1, offvalue=0, command=self.displayProve).pack()
        Checkbutton(pantalla7, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.displayProve).pack()
    
    
        Button(pantalla7, text="GUARDAR", command=self.insertarCuentas).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla7, text="ACTUALIZAR", command=self.ActualizarCuentas).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla7, text="BUSCAR", command=self.buscarCuentas).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla7, text="ELIMINAR", command=self.EliminarCuentas).pack(side=tk.LEFT, padx=10, pady=10)
        
        #check_button.grid(row=1, column=4, sticky="e", padx=10, pady=10)
        
    def displayCuen(self):
        print(value.get())
        
        if value.get() == True:
            id_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            id_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID deshabilitada")
            
    def insertarCuentas(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )
        if not nomcue.get():
            messagebox.showwarning("Crear", "No puede guardar el registro sin la descripcion de la empresa")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.cuentas (id, nomcue, nivel) VALUES ('{0}', '{1}','{2}')".format(id_entry.get(), nomcue_entry.get(), nivel_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Cuentas guardada con exito", title="Aviso")
            #idempresa.set("")
            #nomempresa.set("")   
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar la cuenta", title="Aviso") 
        
        bd.close()
        
    def buscarCuentas(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.cuentas WHERE id='" + id_entry.get()+"'")
        miCuenta=fcursor.fetchall()
        
        if len(miCuenta)==0:
            messagebox.showinfo("CRUD", "El registro no existe")
            return
        for cuent in miCuenta:
            id.set(cuent[0])
            nomcue.set(cuent[1])
            nivel.set(cuent[2])
        
        bd.close()
        
    def EliminarCuentas(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.cuentas WHERE id=" + id.get())
        mysqldb.commit()
        messagebox.showinfo("BBDD", "Registro borrado con exito")
        
    def ActualizarCuentas(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(nomcue.get(),nivel.get(),)
        mycursor.execute("UPDATE python.cuentas SET nomcue=%s,nivel=%s WHERE id=" + id.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("BBDD", "Registro Actualizado con exito")
        
    def Grupo(self):
        global pantalla8
        pantalla8 = Toplevel()
        pantalla8.geometry("350x600")
        pantalla8.resizable(0,0)
        pantalla8.title("GRUPO DE ELEMENTOS")
        pantalla8.iconbitmap("sist.ico")
    
    
        global id_entry
        global nomgrupo_entry
        global usuarioAc_entry
        global usuarioCre_entry
        global fechaAc_entry
        global fechaCre_entry

        
        global id
        global nomgrupo
        global usuarioAc
        global usuarioCre
        global fechaAc
        global fechaCre
    
        id=StringVar()
        nomgrupo=StringVar()
        usuarioAc=StringVar()
        usuarioCre=StringVar()
        fechaAc=StringVar()
        fechaCre=StringVar()
        
        global value
        value = tk.IntVar()

    
        Label(pantalla8, text="SISTEMA GENERAL\n ACTUALIZACION DE GRUPOS\n DE ELEMENTOS", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(pantalla8, text="").pack()
    
        Label(pantalla8, text="ID").pack()
        id_entry = Entry(pantalla8,textvariable=id)
        id_entry.config(state='disabled')
        id_entry.pack()
        Label(pantalla8).pack()
    
        Label(pantalla8, text="DESCRIPCION DE GRUPO DE ELEMENTOS").pack()
        nomgrupo_entry = Entry(pantalla8,textvariable=nomgrupo)
        nomgrupo_entry.pack()
        Label(pantalla8).pack()
        
        Label(pantalla8, text="-----------------------------------------").pack()
        Label(pantalla8, text="CREACION",bg="navy", fg="white",padx=5, pady=5, width=10).pack()
        
        Label(pantalla8, text="USUARIO").pack()
        usuarioCre_entry = Entry(pantalla8,textvariable=usuarioCre)
        usuarioCre_entry.pack()
        
        Label(pantalla8, text="FECHA").pack()
        fechaCre_entry = Entry(pantalla8,textvariable=fechaCre)
        fechaCre_entry.pack()
        
        Label(pantalla8, text="EVENTO").pack()
        
        Label(pantalla8, text="ACTUALIZACION",bg="navy", fg="white",padx=5, pady=5, width=15).pack()
        
        Label(pantalla8, text="USUARIO").pack()
        usuarioAc_entry = Entry(pantalla8,textvariable=usuarioAc)
        usuarioAc_entry.pack()
        
        Label(pantalla8, text="FECHA").pack()
        fechaAc_entry = Entry(pantalla8,textvariable=fechaAc)
        fechaAc_entry.pack()
        
        Label(pantalla8, text="EVENTO").pack()
        Label(pantalla8, text="-----------------------------------------").pack()
        
    
    
        Checkbutton(pantalla8, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.displayGrupo).pack()
    
    
        Button(pantalla8, text="GUARDAR", command=self.insertarGrupo).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla8, text="ACTUALIZAR", command=self.ActualizarGrupo).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla8, text="BUSCAR", command=self.buscarGrupo).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla8, text="ELIMINAR", command=self.EliminarGrupo).pack(side=tk.LEFT, padx=10, pady=10)
        
        #check_button.grid(row=1, column=4, sticky="e", padx=10, pady=10)
        
    def displayGrupo(self):
        print(value.get())
        
        if value.get() == True:
            id_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            id_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID deshabilitada")
            
    def insertarGrupo(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )
        if not nomgrupo.get():
            messagebox.showwarning("Crear", "No puede guardar el registro sin la descripcion del Grupo")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.grupo (id, nomgrupo) VALUES ('{0}', '{1}')".format(id_entry.get(), nomgrupo_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Grupo guardada con exito", title="Aviso")
            #idempresa.set("")
            #nomempresa.set("")   
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar el grupo", title="Aviso") 
        
        bd.close()
        
    def buscarGrupo(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.grupo WHERE id='" + id_entry.get()+"'")
        miGrupo=fcursor.fetchall()
        
        if len(miGrupo)==0:
            messagebox.showinfo("AVISO", "El registro no existe")
            return
        for grup in miGrupo:
            id.set(grup[0])
            nomgrupo.set(grup[1])
        
        bd.close()
        
    def EliminarGrupo(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.grupo WHERE id=" + id.get())
        mysqldb.commit()
        messagebox.showinfo("AVISO", "Registro borrado con exito")
        
    def ActualizarGrupo(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(nomgrupo.get(),)
        mycursor.execute("UPDATE python.grupo SET nomgrupo=%s WHERE id=" + id.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("AVISO", "Registro Actualizado con exito")
        
    def Elemento(self):
        global pantalla9
        pantalla9 = Toplevel()
        pantalla9.geometry("350x700")
        pantalla9.resizable(0,0)
        pantalla9.title("ELEMENTOS DE GASTOS")
        pantalla9.iconbitmap("sist.ico")
    
    
        global id_entry
        global nomele_entry
        #global grupoele_entry
        global usuarioCre_entry
        global usuarioAc_entry
        global fechaAc_entry
        global fechaCre_entry

        
        global id
        global nomele
        global grupoele
        global usuarioCre
        global usuarioAc
        global fechaAc
        global fechaCre
    
        id=StringVar()
        nomele=StringVar()
        grupoele=StringVar()
        usuarioAc=StringVar()
        usuarioCre=StringVar()
        fechaAc=StringVar()
        fechaCre=StringVar()
        
        global value
        value = tk.IntVar()

    
        Label(pantalla9, text="SISTEMA GENERAL\n ACTUALIZACION DE ELEMENTOS\n DE GASTOS", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
        Label(pantalla9, text="").pack()
    
        Label(pantalla9, text="ID").pack()
        id_entry = Entry(pantalla9,textvariable=id)
        id_entry.config(state='disabled')
        id_entry.pack()
        Label(pantalla9).pack()
    
        Label(pantalla9, text="DESCRIPCION DE ELEMENTOS").pack()
        nomele_entry = Entry(pantalla9,textvariable=nomele)
        nomele_entry.pack()
        Label(pantalla9).pack()
        
        Label(pantalla9, text="GRUPO DE ELEMENTO").pack()
        var=tk.StringVar(pantalla9)
        #var.set('MAYOR')
        opciones=['PRESTACIONES', 'MEDIOAMBIENTE']
        opcion=ttk.OptionMenu(pantalla9, var,*opciones)
        opcion.config(width=20)
        opcion.pack(padx=10, pady=10)
        
        Label(pantalla9, text="-----------------------------------------").pack()
        Label(pantalla9, text="CREACION",bg="navy", fg="white",padx=5, pady=5, width=10).pack()
        
        Label(pantalla9, text="USUARIO").pack()
        usuarioCre_entry = Entry(pantalla9,textvariable=usuarioCre)
        usuarioCre_entry.pack()
        
        Label(pantalla9, text="FECHA").pack()
        fechaCre_entry = Entry(pantalla9,textvariable=fechaCre)
        fechaCre_entry.pack()
        
        Label(pantalla9, text="EVENTO").pack()
        
        Label(pantalla9, text="ACTUALIZACION",bg="navy", fg="white",padx=5, pady=5, width=15).pack()
        
        Label(pantalla9, text="USUARIO").pack()
        usuarioAc_entry = Entry(pantalla9,textvariable=usuarioAc)
        usuarioAc_entry.pack()
        
        Label(pantalla9, text="FECHA").pack()
        fechaAc_entry = Entry(pantalla9,textvariable=fechaAc)
        fechaAc_entry.pack()
        
        Label(pantalla9, text="EVENTO").pack()
        Label(pantalla9, text="-----------------------------------------").pack()

    
        Checkbutton(pantalla9, text="Habilitar/Deshabilitar Busqueda", variable=value, onvalue=1, offvalue=0, command=self.displayElem).pack()
    
    
        Button(pantalla9, text="GUARDAR", command=self.insertarElemento).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla9, text="ACTUALIZAR", command=self.ActualizarElemento).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla9, text="BUSCAR", command=self.buscarElemento).pack(side=tk.LEFT, padx=10, pady=10)
        Button(pantalla9, text="ELIMINAR", command=self.EliminarElemento).pack(side=tk.LEFT, padx=10, pady=10)
        
        #check_button.grid(row=1, column=4, sticky="e", padx=10, pady=10)
        
    def displayElem(self):
        print(value.get())
        
        if value.get() == True:
            id_entry.config(state='normal')
            #cuadroNombre.config(state='normal')
            messagebox.showinfo("Aviso", "Busqueda por ID habilitada")
        else:
            id_entry.config(state='disabled')
            #cuadroNombre.config(state='disabled')
            messagebox.showinfo("Aviso", "Busqueda por ID deshabilitada")
            
    def insertarElemento(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )
        if not nomele.get():
            messagebox.showwarning("Crear", "No puede guardar el registro sin la descripcion del Elemento")
            return
    
        fcursor=bd.cursor()
    
        sql="INSERT INTO python.elemento (id, nomele) VALUES ('{0}', '{1}')".format(id_entry.get(), nomele_entry.get())
    

        try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Elemento guardada con exito", title="Aviso")
            #idempresa.set("")
            #nomempresa.set("")   
        except:
            bd.rollback() 
            messagebox.showinfo(message="No se pudo registrar el elemento", title="Aviso") 
        
        bd.close()
        
    def buscarElemento(self):
        bd=mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        db="python"
    )

        fcursor=bd.cursor()
    
        fcursor.execute("SELECT * FROM python.elemento WHERE id='" + id_entry.get()+"'")
        miElem=fcursor.fetchall()
        
        if len(miElem)==0:
            messagebox.showinfo("AVISO", "El registro no existe")
            return
        for elem in miElem:
            id.set(elem[0])
            nomele.set(elem[1])
        
        bd.close()
        
    def EliminarElemento(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        fcursor=mysqldb.cursor()
        
        fcursor.execute("DELETE FROM python.elemento WHERE id=" + id.get())
        mysqldb.commit()
        messagebox.showinfo("AVISO", "Registro borrado con exito")
        
    def ActualizarElemento(self):
        mysqldb=mysql.connector.connect(host="localhost", user="root", password="", database="python")
        mycursor=mysqldb.cursor()
        
        datos=(nomele.get(),)
        mycursor.execute("UPDATE python.elemento SET nomele=%s WHERE id=" + id.get(),datos)
        mysqldb.commit()
        
        messagebox.showinfo("AVISO", "Registro Actualizado con exito")
Inicio().mainloop()