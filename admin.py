from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Analize_Data

# Register your models here.

class Analize_DataResource(resources.ModelResource):
    
    class Meta:
        model=Analize_Data
        skip_unchanged=True
        report_skipped=False
        import_fields = ('PublishedAt',)

@admin.register(Analize_Data)
class Video_DataAdmin(ImportExportModelAdmin):
    list_display =('id','PublishedAt','Title','URL','Duration','ViewCount','EmbedHtml','NumChats','ChatCount','ChatRate','StdRate','MaxRate')
    resource_class = Analize_DataResource
