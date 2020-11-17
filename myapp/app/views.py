from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from flask_appbuilder import BaseView, expose, has_access

from . import appbuilder, db

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

class MyTemplateView(BaseView):

    default_view = "my_template"

    @expose("/my_template")
    @has_access
    def my_template(self):

        numbers = [0, 1, 2, 3, 'a']

        return self.render_template(
                "my_template.html",
                template_h3="My Flask Template", 
                numbers=numbers
        )

## Add views to appbuilder
appbuilder.add_view(MyTemplateView, "MyTemplate", category="FlaskTutorial")

## Add a view as sub-menu under a category
appbuilder.add_link("Method2", href='/mytemplateview/method2', category='FlaskTutorial')

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
