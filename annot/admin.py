from django.contrib import admin

from .models import Story
from .models import Class
from .models import Subclass
from .models import Label
from .models import Annotator
from .models import Annotation
from .models import Complete


admin.site.register(Story)
admin.site.register(Class)
admin.site.register(Subclass)
admin.site.register(Label)
admin.site.register(Annotator)
admin.site.register(Annotation)
admin.site.register(Complete)

