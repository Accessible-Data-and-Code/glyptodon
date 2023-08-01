# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/06_export.ipynb.

# %% auto 0
__all__ = ['createExportInfo', 'createExportName', 'createDirectoryOptions', 'createExportButton', 'createExportDownload']

# %% ../nbs/06_export.ipynb 5
from dash import dcc, html
from .information import labeledInput

# %% ../nbs/06_export.ipynb 7
def createExportInfo():
    return dcc.Markdown(
        """
    # Export
    
    This menu allows you to export the manuscript and transcriptions you've worked on as a zipped folder.
    
    You can input a name for the zipped folder and select what elements of the work you want to save:
    - If you want to share the images of your manuscript, select the 'Images' option from the dropdown.
    - If you want to share your transcription with another *glyptodon* user, select the 'States' option from the dropdown.
    
    Once you have selected the export options, click the export button and a file download will begin shortly containing the zipped folder.
    """
    )

# [Reach] - If you want to share xml transcriptions, select the 'Export Transcripts' option from the dropdown.

# %% ../nbs/06_export.ipynb 10
def createExportName():
    return labeledInput(label = "Export Folder Name", identity = "export-name")

# %% ../nbs/06_export.ipynb 13
def createDirectoryOptions():
    return dcc.Dropdown(
        [
            "Images",
            "States",
            # "Export Transcripts",
        ],
        ["Images"],
        multi=True,
        id="directory-options",
    )

# %% ../nbs/06_export.ipynb 16
def createExportButton():
    return html.Button("Export Manuscript", id="export-button")

# %% ../nbs/06_export.ipynb 19
def createExportDownload():
    return dcc.Download(id="export-download")
