from django import forms
from . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('cinematica.kg', 'cinematica.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'cinematica.kg':
            cinema_parser = parser.parser()
            for i in cinema_parser:
                models.Cinema.objects.create(**i)