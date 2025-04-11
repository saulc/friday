import tkinter as tk
import tkinter.font as tkFont

class App(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		# self.pack() 
		self.mode = 1 #0 files 1 db 
		self.root = root
		self.root.geometry('1200x1080')
		self.root.configure(background="black" )
		self.root.wm_attributes('-alpha', 0.8)

		n = tkFont.families()[11]
		print('Font:', n)
		self.myFont = tkFont.Font(family=n, size=14, weight="bold")
		self.h = 36
		self.w = 88
		self.info = tk.Text(self.root,wrap='word', font=self.myFont, width=self.w, height=self.h)
		self.info.configure(background="black", foreground="white", highlightbackground="black" )
		self.info.grid(row=3, column=1) 
		self.info.insert("1.0", 'friday'+ "\n")
		self.info.insert("2.0", "...")


		self.num = tk.Text(self.root,wrap='word', font=self.myFont, width=2, height=self.h)
		self.num.configure(background="black", foreground="#ff1155", highlightbackground="black" )
		self.num.grid(row=3, column=0, padx = 6) 
		for i in range(24): self.num.insert(str(float(i+1)),str(i+1)+'\n')
		self.num.config(state="disabled")


		self.root.bind("<Button>", self.click_handler)
		self.root.bind('<KeyPress>', self.onKeyPress) 

	def click_handler(self, event):
		# event also has x & y attributes
		print(str(event.num) + ' x y: ' + str(event.x) + ' ' + str(event.y))
		if event.num == 3:
			print("RIGHT CLICK") 
		elif event.num == 1:
			print('left click') 

	def click(self):
		pass

	def onKeyPress(self, event):
		print(event)
		k = event.keycode

		if k == 2113992448:
			print('arrow up' )
		elif k == 2097215233:
			print('arrow down') 

		elif k == 855638143:
			#delete
			print('up')
			self.mfiles.goUp()
		elif k == 603979789 or k == 822083616:
			#enter or space
			print('select')
			self.click()
		elif k == 889192475:
			#esc
			print('exit')
			self.root.destroy()


	def demo(self):
		families = tkFont.families()
		print(families)
		# Create a font object
		c = len(families)//21
		for j in range(c):
			for i in range(21):
				n = families[i+j*21]
				myFont = tkFont.Font(family=n, size=12, weight="bold")

				# Use the font in a label
				label = tk.Label(root, text="Hello! " + n, font=myFont)
				# label.config(bg='systemTransparent')
				label.grid(row=i, column=j, padx=2,pady=1)
		        
				# label.pack()


if __name__ == '__main__': 

	root = tk.Tk()

	f = App(root)   

	f.mainloop()