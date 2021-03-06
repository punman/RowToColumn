import tkinter
from tkinter.font import Font


class columnspliter():
    
    def __init__(self):
        
        self.score = ''
        self.line = []
        
        self.root = tkinter.Tk()
        self.root.title('Row To Column')
        self.label = tkinter.Label(self.root,text='Score')
        self.label.pack()

        self.tf = tkinter.Text(self.root , width = 65,height = 10)
        self.myFont = Font(family="AngsanaUPC", size=17)
        self.tf.configure(font=self.myFont)
        self.tf.pack()

        self.butt = tkinter.Button(self.root,text = 'convert',command=self.run)
        self.butt.pack()

        self.tf2 = tkinter.Text(self.root , width = 65,height = 20)
        self.tf2.configure(font=self.myFont)
        self.tf2.pack()

        self.root.mainloop()
        
    def getInput(self):
        self.score = self.tf.get('1.0','end-1c')
    
    def splittext(self):
        self.line = self.score.splitlines()
    
    def tabremover(self):
        for i in range(0,len(self.line)):
            self.line[i] = self.line[i].replace('  ','\t')
            self.line[i] = self.line[i].split('\t')
            
    def clean(self):
        for item in self.line:
            while '' in item:
                item.remove('')
        
    def display(self):
        for i in range(0,len(self.line[0])):
            for k in self.line:
                self.tf2.insert('end',k[i].strip()+'\n')
            self.tf2.insert('end','-'*10+'\n')
            
    def run(self):
        self.getInput()
        self.splittext()
        self.tabremover()
        self.clean()
        self.display()    
    
     
        
if __name__=='__main__':
    
    columnspliter()