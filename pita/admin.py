from django.contrib import admin

from .models import Feature
from .models import Milestone
from .models import Priority
from .models import Project
from .models import Status
from .models import Team
from .models import Workstream

admin.site.register(Project)
admin.site.register(Priority)
admin.site.register(Feature)
admin.site.register(Milestone)
admin.site.register(Workstream)
admin.site.register(Status)
admin.site.register(Team)
