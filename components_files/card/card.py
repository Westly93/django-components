# In a file called [project root]/components/calendar/calendar.py
from django_components import component


@component.register("card")
class Card(component.Component):
    # Templates inside `[your apps]/components` dir and `[project root]/components` dir will be automatically found. To customize which template to use based on context
    # you can override def get_template_name() instead of specifying the below variable.
    template_name = "card/template.html"

    def get_context_data(self, title, body, button_text="Buy Now!"):
        return {
            "title": title,
            "body": body,
            "button_text": button_text
        }

    class Media:
        css = "css/style.css"
        js = "js/script.js"
