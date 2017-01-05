#code par GLA
""" GAME IN BETA, 
that's impossible to play this. """

from tkinter import *
class snake:
    def __init__(self):
        self.touch=None
        global down,canvas,x2,y2,y1,x1,square,square2
        global total
        total=0
        lol=0
        self.size=20
        x1=290
        y1=290
        x2=x1+self.size
        y2=y1+self.size
        self.color="black"
        self.outline="white"
        master = Tk()
        master.title("snake")
        master.minsize(width=1000,height=500)
        master.resizable(0,0)
        canvas= Canvas(master,width=600,height=600,bg="white")
        square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline="white")
        square2 = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline="white")

        def Up():
            global canvas,x2,y2,y1,x1,square,square2
            if self.touch!="Down":
                canvas.delete(square)
                canvas.delete(square2)
                if y1 >=5:
                    y1-=10
                    y2-=10
                square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.outline)
                square2 = canvas.create_rectangle(x1,y1+40,x2,y2+40,fill=self.color,outline=self.outline)
                self.touch="Up"
                canvas.coords(square,x1,y1+40,x2,y2+40)


        def Down():
            global canvas,x2,y2,y1,x1,square,square2
            if self.touch!="Up":
                canvas.delete(square)
                canvas.delete(square2)
                if y1<=570:
                    y1+=10
                    y2+=10
                square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline=self.outline)
                square2 = canvas.create_rectangle(x1,y1-40,x2,y2-40,fill=self.color,outline=self.outline)
                self.touch="Down"

        def Right():
            global canvas,x2,y2,y1,x1,square,square2
            if self.touch!="Left":
                canvas.delete(square)
                canvas.delete(square2)
                if x2<=595:
    	            x1+=10
    	            x2+=10
                square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline="white")
                square2 = canvas.create_rectangle(x1-40,y1,x2-40,y2,fill=self.color,outline="white")
                self.touch="Right"

        def Left():
            global canvas,x2,y2,y1,x1,square,DrawState,square2
            if self.touch!="Right":
                canvas.delete(square)
                canvas.delete(square2)
                if x2>=30:
                    x1-=10
                    x2-=10
                square = canvas.create_rectangle(x1,y1,x2,y2,fill=self.color,outline="white")
                square2 = canvas.create_rectangle(x1+40,y1,x2+40,y2,fill=self.color,outline="white")
                self.touch="Left"

        def clavier(event):
            key = event.keysym
            if key == "Up":
                Up()
            elif key == "Down":
                Down()
            elif key == "Right":
                Right()
            elif key == "Left":
                Left()
        #interface

        Label(master,text="Utilisez les boutons ou les \nfleches directionelles pour\n vous orienter.").place(x=825,y=370)

        Button(text="Down", command=Down).place(x=870,y=500 )
        Button(text="  Up   ", command=Up).place(x=870,y=430)
        Button(text="Right", command=Right).place(x=930,y=465)
        Button(text="Left ", command=Left).place(x=820,y=465)

        canvas.focus_set()
        canvas.bind("<Key>", clavier)
        canvas.pack()
        canvas.after(60,Up)
        master.mainloop()

main=snake()

############ Read ME number1 pls ####################
###j'ai  mis un espace entre les carres de 1 carre soit###
###pour les cotes le double d'un deplacement normale####
###pour le haut et le bas il faut soustraire et aditionner###
###pour y2 comme pour y1###
##j'ai aussi fait le block pour la droite et la gauche##
