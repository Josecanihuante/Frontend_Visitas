import reflex as rx
from Visita.components.navbar import navbar
from Visita.components.Title import title
from Visita.Views.center import center
from Visita.components.footer import footer
from Visita.Style import style

#class State(rx.State):
#    pass

def index() -> rx.Component:
       return rx.box(
            navbar(),
            rx.vstack(
                title("Resumen"),
                center(),
                width="100%"
            ),
            footer(),
            max_width=style.MAX_WIDTH,
            width="100%"
    )

app = rx.App(
stylesheets=style.STYLESHEETS,
style= style.BASE_STYLE
)
app.add_page(index)
app._compile()