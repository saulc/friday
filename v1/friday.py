import tkinter as tk
import tkinter.font as tkFont

import re

class App(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		# self.pack() 
		self.mode = 1 #0 files 1 db 
		self.root = root
		self.root.geometry('1000x1080')
		self.root.configure(background="black" )
		self.root.wm_attributes('-alpha', 0.8)

		n = tkFont.families()[11]
		print('Font:', n)
		self.myFont = tkFont.Font(family=n, size=12, weight="normal")
		self.scFont = tkFont.Font(family=n, size=4, weight="normal")
		self.h = 30
		self.w = 60


		self.topFrame = tk.Frame(self.root , width=500, height=800)
  

		self.info = tk.Text(self.topFrame ,wrap='word', undo=True,  font=self.myFont, width=self.w, height=self.h)
		self.info.configure(background="black", foreground="white", highlightbackground="black" )

		tab_width = self.myFont.measure(' ' * 3)
		self.info.config(tabs=(tab_width,))
		self.info.grid(row=0, column=2, sticky="nsew") 
		self.info.insert("1.0", 'friday')
		# self.info.insert("2.0", "...")

		self.infosb = tk.Scrollbar(self.topFrame , orient=tk.VERTICAL, command=self.info.yview)
		self.info.configure(yscrollcommand=self.on_scroll)

		self.sc = tk.Text(self.root ,wrap='word', font=self.scFont, width=60, height=self.h*2)
		self.sc.configure(background="black", foreground="#ff1155", highlightbackground="black" )
		self.sc.grid(row=3, column=5, padx = 6) 
		# self.update()

		# self.numsb = tk.Scrollbar(root) 
		# self.numsb.config(command=self.on_scroll)

		self.num = tk.Text(self.topFrame ,wrap='word', font=self.myFont, width=3, height=self.h)
		self.num.configure(background="black", foreground="#ff1155", highlightbackground="black" )
		self.num.grid(row=0, column=0, padx = 2, sticky="nsew") 
		self.addNums()
		self.num.config(state="disabled")

		# self.numsb = tk.Scrollbar(self.topFrame , orient=tk.VERTICAL, command=self.num.yview)
		# self.num.configure(yscrollcommand=self.infosb.set)
		# self.numsb.grid(row=3, column=3, sticky="ns")
		self.infosb.grid(row=3, column=4, sticky="ns")

		self.info.tag_config("red", foreground="red")
		self.info.tag_config("pink", foreground="#ff1155")
		self.info.tag_config("green", foreground="#00ff24")
		self.info.tag_config("blue", foreground="#00aaff")
		self.info.tag_config("purple", foreground="#aa00aa")
		self.info.tag_config("grey", foreground="#aaaaaa")

		self.topFrame.grid(row=3, column=0)
		self.topFrame.grid_columnconfigure(0, weight=1)
		self.topFrame.grid_columnconfigure(2, weight=1)
		self.topFrame.grid_rowconfigure(0, weight=1)

		self.root.bind("<Button>", self.click_handler)
		self.root.bind('<KeyPress>', self.onKeyPress) 
		self.info.bind('<KeyPress>', self.onKeyPress) 

	def on_scroll(self, e, t):
		print(e+t)
		t = float(t)# - .75
		if t == .25: t = 1
		elif t == -.25: t = -1
		print('on scroll', e, str(t))
		# self.info.yview_moveto(t) 
		self.num.yview_scroll(t, "units")

	def addNums(self, n = 24):
		self.num.config(state="normal")
		self.num.delete("1.0", "end") 
		for i in range(n): self.num.insert(str(float(i+1)),str(i+1)+'\n')

		self.num.config(state="disabled")

	def click_handler(self, event):
		# event also has x & y attributes
		print(str(event.num) + ' x y: ' + str(event.x) + ' ' + str(event.y))
		if event.num == 3:
			print("RIGHT CLICK") 
		elif event.num == 1:
			print('left click') 

	def click(self):
		pass

	def update(self):
		self.sc.delete("1.0", "end") 
		it = self.info.get("1.0", "end-1c")
		self.sc.insert("1.0", it)

		line_count = self.info.count("0.0", "end", "displaylines")[0]
		print('lines:', line_count)
		if line_count > 24: self.addNums(line_count)
		# self.info.delete("1.0", "end") 
		# for l in it.splitlines(keepends=True):
		# 	d = l.find('.')
		# 	if d == None: 
		# 		self.info.insert("1.0", l )
		# 		return
		# 	r = l[0:d]
		# 	t = l[d:]
		# 	dd = t.find('.')
		# 	rr = t[:dd]
		# 	rrr = t[dd:]
		# 	print(t, rr)
		# 	self.info.insert("1.0", r)
		# 	self.info.insert("1.0", rr , 'red')
		# 	self.info.insert("1.0", rrr)


	def highlight_syntax(self): 
		keywords = [ "def", "class", "if", "else", "elif", "for", "while", "return", 
		'get', 'set', 'append', 'remove' , 'print']
		key2 = [ 'self', 'import', 'from', 'break', 'None', 'True', 'False']
		content = self.info.get("1.0", tk.END)
		for keyword in keywords:
			for match in re.finditer(r"\b" + keyword + r"\b", content):
				start, end = match.span()
				self.info.tag_add("pink", f"1.0 + {start}c", f"1.0 + {end}c")

		for keyword in key2:
			for match in re.finditer(r"\b" + keyword + r"\b", content):
				start, end = match.span()
				self.info.tag_add("red", f"1.0 + {start}c", f"1.0 + {end}c")
		#strings
		pattern = r'\(|\)'
		for match in re.finditer(pattern, content):
				start, end = match.span()
				self.info.tag_add("purple", f"1.0 + {start}c", f"1.0 + {end}c")
		pattern = r'"*"'
		for match in re.finditer(pattern, content):
				start, end = match.span()
				self.info.tag_add("blue", f"1.0 + {start}c", f"1.0 + {end}c")
		pattern = r"'*'"
		for match in re.finditer(pattern, content):
				start, end = match.span()
				self.info.tag_add("blue", f"1.0 + {start}c", f"1.0 + {end}c")
		#numbers
		pattern = r'\b\d+\b'
		for match in re.finditer(pattern, content):
				start, end = match.span()
				self.info.tag_add("green", f"1.0 + {start}c", f"1.0 + {end}c")
		#comments
		pattern = r'#.*'
		for match in re.finditer(pattern, content):
				start, end = match.span()
				self.info.tag_add("grey", f"1.0 + {start}c", f"1.0 + {end}c")

	def undo(self):
		print('undo')
		self.info.edit_undo()

	def redo(self):
		self.info.edit_redo()

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
		elif k == 603979789: # or k == 822083616:
			#enter or space
			print('select')
			# self.click()
			self.highlight_syntax()
			self.update()

		elif k == 889192475:
			#esc
			print('exit')
			self.root.destroy()
		elif event.state == 8 and event.keysym == 'z':
			print('click undo')
			self.undo()


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