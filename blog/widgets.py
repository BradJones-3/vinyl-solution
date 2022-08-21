from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """ Clearable image input field to blogpost form """

    clear_checkbox_label = ('Remove')
    initial_text = ('Current Image')
    input_text = _('')
    template_name = ('blog/custom_widgets_templates/custom_clearable_file_input.html')
