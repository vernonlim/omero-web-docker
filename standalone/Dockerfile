ARG PARENT_IMAGE=openmicroscopy/omero-web:latest
FROM ${PARENT_IMAGE}
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

USER root

RUN /opt/omero/web/venv3/bin/pip install \
        omero-figure \
        omero-iviewer \
        omero-fpbioimage \
        omero-mapr \
        omero-parade \
        omero-autotag \
        omero-tagsearch \
        'git+https://github.com/vernonlim/omero_crm_landing_page.git#egg=omero_crm_landing_page' \
        whitenoise

ADD 01-default-webapps.omero /opt/omero/web/config/

USER omero-web
