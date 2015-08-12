from flask.ext.wtf import Form
from wtforms import SelectMultipleField
from wtforms.widgets import ListWidget, CheckboxInput
from jumper.blueprints.backends import fixture_data

class MultiCheckboxField(SelectMultipleField):

    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()


class IndexForm(Form):

    # Grab our fixture data and convert it to a form usable with checkboxes
    test_cities = fixture_data.desc_lat_long_to_semicolon_format()

    # Put the 'lat;long' in a list so we can set it as default
    test_cities_latlong_only = [field[0] for field in test_cities]

    cities = MultiCheckboxField(description='Cities', choices=test_cities, default=test_cities_latlong_only)