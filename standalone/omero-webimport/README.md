# OMERO webimport

This is a prototype based on William Moore's [initial implementation](https://gitlab.com/openmicroscopy/incubator/omero-webimport) to investigate the support of image import into OMERO from a web client.

## Install

Install for development:

    $ cd omero-webimport
    $ pip install -e .

    # Add to config:

    $ omero config append omero.web.apps omero_webimport

Then restart your OMERO.web server.

## Usage:

 - Go to {your-server}/omero_webimport
 - Drag files onto the page
 - Click Import to start upload and import

NB: The selected files will be uploaded to OMERO into a single **FileSet** and
then imported into OMERO. A FileSet in OMERO is a grouping of 1 or more files
that are part of the same OMERO Image or Images.
See https://docs.openmicroscopy.org/latest/omero/developers/ImportFS.html

Bio-Formats will parse the files in the upload, find the first FileSet and
import that. If any required files are missing, the import will fail. Also,
if there are additional files in the upload that are not part
of the FileSet identified by Bio-Formats, they will not be imported, although
they will be uploaded and linked to the FileSet in the OMERO DB.

This is a limitation of web-based import. Normally, Bio-Formats is used
on the client-side to parse files so that all the required files can be
automatically uploaded for import.
