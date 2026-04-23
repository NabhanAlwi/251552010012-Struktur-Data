class texteditor: 
    def __init__(self):
        self.content = ''
        self.undo_stack = []
        
    def write(self, teks):
        self.undo_stack.append(self.content)
        self.content += teks
        print(f'tulis: {self.content}')
        
    def undo(self):
        if self.undo_stack: 
            self.content = self.undo_stack.pop ()
            print (f'UNDO: {self.content}')
        else:
            print('Tidak bisa undo lagi')
    
editor = texteditor()
editor.write('mencoba')
editor.write(' belajar')
editor.write(' jangan ganggu')
editor.undo()
editor.undo()
editor.undo()
editor.undo()