from logging import WARNING, warning
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from numpy import linspace
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import AxesZero

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        #Title and Geometry
        self.title("Math Tools - Beta")
        self.geometry("240x270")
        self.resizable(0,0)

        s = ttk.Style()
        s.theme_use("clam")

        # -- ROOT Solver ---
        #ROOT Solver Label Frame Definition
        Root_Solver_LF = tk.LabelFrame(self,text="Root Solver",font=('Helvetica 12 bold'))
        Root_Solver_LF.grid(row=0,column=0,padx=10, pady=10)
        #Matrix Calculations Frame Definition
        Matrix_LF = tk.LabelFrame(self,text="Matrix Calculations",font=('Helvetica 12 bold'))
        Matrix_LF.grid(row=1,column=0,padx=10, pady=10)
        # ==================== Quadratic Equation ==================== 
        #Quadratic Equation Variables
        self.quadraticEq_a_var = tk.IntVar()
        self.quadraticEq_b_var = tk.IntVar()
        self.quadraticEq_c_var = tk.IntVar()
        #Quadratic Equation Label Frame Defination
        self.quadraticEq_LF = tk.LabelFrame(Root_Solver_LF,text="Quadratic Equation",font=('Helvetica 12 bold'))
        self.quadraticEq_LF.grid(row=0,column=0,padx=10, pady=10)
        #Quadratic Equation Labels
        quadraticEq_label_a = tk.Label(self.quadraticEq_LF,text = "a =",font=('Helvetica 10 bold'))
        quadraticEq_label_a.grid(row=0,column=0)
        quadraticEq_label_b = tk.Label(self.quadraticEq_LF,text = "b =",font=('Helvetica 10 bold'))
        quadraticEq_label_b.grid(row=1,column=0)
        quadraticEq_label_c = tk.Label(self.quadraticEq_LF,text = "c =",font=('Helvetica 10 bold'))
        quadraticEq_label_c.grid(row=2,column=0)
        quadraticEq_label_root_1 = tk.Label(self.quadraticEq_LF,text = "F. Root =",font=('Helvetica 10 bold'))
        quadraticEq_label_root_1.grid(row=4,column=0)
        quadraticEq_label_root_2 = tk.Label(self.quadraticEq_LF,text = "S. Root =",font=('Helvetica 10 bold'))
        quadraticEq_label_root_2.grid(row=5,column=0)

        #Quadratic Equation Entrys
        self.quadraticEq_a_Entry = tk.Entry(self.quadraticEq_LF,textvariable=self.quadraticEq_a_var)
        self.quadraticEq_a_Entry.grid(row = 0, column = 1)
        self.quadraticEq_b_Entry = tk.Entry(self.quadraticEq_LF,textvariable=self.quadraticEq_b_var)
        self.quadraticEq_b_Entry.grid(row = 1, column = 1)
        self.quadraticEq_c_Entry = tk.Entry(self.quadraticEq_LF,textvariable=self.quadraticEq_c_var)
        self.quadraticEq_c_Entry.grid(row = 2, column = 1)
        self.quadraticEq_root_1_Entry = tk.Entry(self.quadraticEq_LF)
        self.quadraticEq_root_1_Entry.grid(row = 4, column = 1)
        self.quadraticEq_root_2_Entry = tk.Entry(self.quadraticEq_LF)
        self.quadraticEq_root_2_Entry.grid(row = 5, column = 1)

        #Quadratic Equation Solve Button
        quadraticEq_SolveButton = tk.Button(self.quadraticEq_LF,
                                            text = "Solve",
                                            command=self.solve_QuadEq,
                                            height="1",width="16",
                                            font=('Helvetica 9 bold'),background="seagreen",)
        quadraticEq_SolveButton.grid(row = 3, column = 1)
        #Quadratic Equation Graph Button
        quadraticEq_GraphButton = tk.Button(self.quadraticEq_LF,
                                            text = "Graph",
                                            command=self.graph_QuadEq,
                                            height="1",width="16",
                                            font=('Helvetica 9 bold'),background="lightblue",)
        quadraticEq_GraphButton.grid(row =6, column = 1)


        
    # ====================== Methods ======================
    #-------------------- ROOT Solver --------------------
    def solve_QuadEq(self):
        try:
            a,b,c = self.quadraticEq_a_var.get(),self.quadraticEq_b_var.get(),self.quadraticEq_c_var.get()
            self.QuadDisc = b**2-4*a*c
      
            if self.QuadDisc > 0:
                self.QuadRoot_1 = round((-b+self.QuadDisc**0.5)/(2*a),6)
                self.QuadRoot_2 = round((-b-self.QuadDisc**0.5)/(2*a),6)
                self.quadraticEq_root_1_Entry.delete(0,"end")
                self.quadraticEq_root_2_Entry.delete(0,"end")
                self.quadraticEq_root_1_Entry.insert(0,self.QuadRoot_1)
                self.quadraticEq_root_2_Entry.insert(0,self.QuadRoot_2)
                    
            if self.QuadDisc == 0:
                self.QuadRoot_12 = -b/(2*a)
                self.quadraticEq_root_1_Entry.delete(0,"end")
                self.quadraticEq_root_2_Entry.delete(0,"end")
                self.quadraticEq_root_1_Entry.insert(0,self.QuadRoot_12)
                self.quadraticEq_root_2_Entry.insert(0,self.QuadRoot_12)

            if self.QuadDisc < 0:
                self.QuadRoot_1 = complex(round(-b/(2*a),6),round(abs(self.QuadDisc)**0.5/(2*a),6))
                self.QuadRoot_2 = complex(round(-b/(2*a),6),-round(abs(self.QuadDisc)**0.5/(2*a),6))
                self.quadraticEq_root_1_Entry.delete(0,"end")
                self.quadraticEq_root_2_Entry.delete(0,"end")
                self.quadraticEq_root_1_Entry.insert(0,self.QuadRoot_1)
                self.quadraticEq_root_2_Entry.insert(0,self.QuadRoot_2)
                
        except:
            messagebox.showerror(title="Input Error!",message="Please,fill inputs (Only Numbers!)")         

    #Draw Graphs
    def graph_QuadEq(self):
        try:
            if self.QuadDisc < 0:
                messagebox.showerror(title="Graph!",message="No Real Graph!")         
            else:
                fig = plt.figure()
                ax = fig.add_subplot(axes_class=AxesZero)
                a,b,c = self.quadraticEq_a_var.get(),self.quadraticEq_b_var.get(),self.quadraticEq_c_var.get()
                title_p1,title_p2,title_p3 = "","",""
                for direction in ["xzero", "yzero"]:
                    # adds arrows at the ends of each axis
                    ax.axis[direction].set_axisline_style("-|>")

                    # adds X and Y-axis from the origin
                    ax.axis[direction].set_visible(True)

                for direction in ["left", "right", "bottom", "top"]:
                    # hides borders
                    ax.axis[direction].set_visible(False)
                if abs(self.QuadRoot_2) < 10:
                    r2_coff = 5
                elif abs(self.QuadRoot_2) < 1:
                    r2_coff = 100
                if abs(self.QuadRoot_1) < 10:
                    r1_coff = 3
                elif abs(self.QuadRoot_1) < 1:
                    r1_coff = 100
                x_values = linspace(r1_coff*self.QuadRoot_1,r2_coff*self.QuadRoot_2,1000)
                y_result = [a*x**2 + b*x + c for x in x_values]
                if a > 0:
                    title_p1 = f"{a}x^{2}"
                else:
                    pass
                
                if b > 0:
                    title_p2 = f" + {b}x"
                elif b == 0:
                    pass
                else:
                    title_p2 = f" {b}x"

                if c > 0:
                    title_p3 = f" + {c} = 0$\n"

                elif c == 0:
                    title_p3 =" = 0$\n"
                else:
                    title_p3 = f" {c} = 0$\n"

                plt.title(r"$"+title_p1+title_p2+title_p3)
                #plt.xlabel("X - Axis");plt.ylabel("Y - Axis")
                plt.plot(x_values,y_result,c = "tab:red")
                plt.scatter([self.QuadRoot_1,],[0,],c = "tab:green",label = "F. Root = {0}".format(self.QuadRoot_1))
                plt.scatter([self.QuadRoot_2,],[0,],c = "tab:blue",label = "S. Root = {0}".format(self.QuadRoot_2))
                plt.scatter([0,],[c,],label = f"Vertex P. = {c}",c = "tab:orange")
                plt.legend(loc = "upper left")
                plt.show()
                
        except ValueError:
            messagebox.showerror(title="Graph!",message="Error!")         

            
if __name__ == "__main__":
    app=App()
    app.mainloop()
