import flet as ft


def main(page: ft.Page):
    page.title = "¿Hablamos de nuevo?"
    page.bgcolor="blue"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("¿Hablamos de nuevo?",
                 style=ft.TextStyle(size=40,weight="bold"))
    img1=ft.Image(src="triste.png",width=200,heigt=200)
    
    btnSi=ft.ElevatedButton("si",
                            color="green",
                            width=100,
                            height=50)
    btnNo=ft.ElevateButton("No",
                           color="red",
                           width=100,
                           height=50)
    
    
    


ft.app(main)
