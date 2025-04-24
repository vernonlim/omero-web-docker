#
# Copyright (c) 2019 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.shortcuts import render
import datetime
from django.http import JsonResponse
from omeroweb.webclient.decorators import login_required

from .util.import_library import ImportLibrary

@login_required()
def index(request, conn=None, **kwargs):
    """
    Home page
    """
    template = "omero_webimport/index.html"
    return render(request, template, {})


@login_required()
def submit_import(request, conn=None, **kwargs):
    try:
        def chunks_gen(open_file):
            for chunk in open_file.chunks():
                yield chunk

        def file_gen():
            for f in file_names():
                yield chunks_gen(f)

        def file_names():
            count = 0
            while request.FILES.get('file%s' % count):
                name = request.FILES.get('file%s' % count)
                count += 1
                yield name

        client_path_gen = file_names()
        folder_gen = file_gen()

        import_lib = ImportLibrary(conn.c)
        rsp = import_lib.import_image(client_path_gen, folder_gen, wait=True)

        img_ids = [p.image.id.val for p in rsp.pixels]
        return JsonResponse({'image_ids': img_ids})
    except Exception as e:
        # Log the error for server-side debugging
        import logging
        logger = logging.getLogger(__name__)
        logger.exception("Import failed")
        
        # Return a properly formatted JSON error response
        return JsonResponse({
            'error': str(e),
            'success': False
        }, status=500)
