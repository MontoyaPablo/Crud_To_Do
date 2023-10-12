import flet as ft
from flet import *
from flet import colors, icons

class Childapp(UserControl):
    def __init__(self, username, deleteaction):
        super().__init__()
        self.username =  username
        self.deleteaction = deleteaction

    def build(self):
        self.name = Text(value=self.username, 
                         size=30)
        self.editAndDeleteBtn = Row([
            IconButton(icon=icons.CREATE_OUTLINED,
                       icon_color=colors.BLUE,
                       icon_size=30,
                       on_click=self.editBtn
                       ),
            IconButton(icon=icons.DELETE,
                       icon_color=colors.RED,
                       icon_size=30,
                       on_click=self.deleteBtn
                       )
        ])
        self.textForUpadate = TextField(
            value=self.name.value,
            visible=False,
            width=100)
        
        self.btnSaveEdit = IconButton(
            icon=icons.SAVE,
            icon_color="green300",
            icon_size=30,
            visible=False,
            on_click=self.saveBtnEdit)

        return Column([
            Row([
                self.name,
                self.editAndDeleteBtn,
                self.textForUpadate,
                self.btnSaveEdit,
                ], alignment="spaceEvenly")

        ], alignment="center")

    def editBtn(self, event):
        self.textForUpadate.visible= True
        self.name.visible=False
        self.btnSaveEdit.visible=True
        self.editAndDeleteBtn.visible=False
        self.name.value= self.textForUpadate.value
        self.update()

    def saveBtnEdit(self, event):
        self.textForUpadate.visible= False
        self.name.visible=True
        self.btnSaveEdit.visible=False
        self.editAndDeleteBtn.visible=True
        self.name.value= self.textForUpadate.value
        self.update()

    def deleteBtn(self, event):
        self.deleteaction(self)


class Homeapp(UserControl):
    def build(self):
        self.name =TextField(label='username')
        self.listdata = Column()
        return Column([
            Row([
                self.name,
                FloatingActionButton(
                    icon=icons.ADD,
                    bgcolor=colors.BLUE,
                    on_click= self.addtask
                )
            ]),
            self.listdata
        ])
    
    def addtask(self, event):
        self.listdata.controls.append(
            Childapp(self.name.value, self.deleteBtn)
        )
        self.update()
    
    def deleteBtn(self, element):
        self.listdata.controls.remove(element)
        self.update()


def main(page:Page):
    apptodo = Homeapp()
    page.add(apptodo)
    

ft.app(target=main)