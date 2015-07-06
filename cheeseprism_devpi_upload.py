"""
Upload callback that uploads packages to devpi
"""

import logging
import subprocess

logger = logging.getLogger(__name__)


def upload(context, request, uploaded_file):
    logger.info(
        'devpi.upload: uploaded_file = %r',
        uploaded_file)

    def setting(key):
        return request.settings.get('%s.%s' % (__name__, key))

    devpi_url = setting('devpi_url')
    devpi_user = setting('devpi_user')
    devpi_password = setting('devpi_password')

    if not devpi_url:
        logger.info('%s:upload: No devpi_url setting. Exiting.', __name__)
        return

    cmd = ['devpi', 'use', devpi_url]
    logger.info('Doing devpi use for %s...', devpi_url)
    logger.info('cmd = %r', cmd)
    ret = subprocess.call(cmd)
    if ret:
        logger.error('devpi use failed')
        return
    logger.info('Using devpi: %s.', devpi_url)

    cmd = ['devpi', 'login', '--password=%s' % devpi_password, devpi_user]
    logger.info('Logging into devpi...')
    logger.info('cmd = %r', cmd)
    ret = subprocess.call(cmd)
    if ret:
        logger.error('devpi login failed')
        return
    logger.info('Logged into devpi.')

    cmd = ['devpi', 'upload', uploaded_file]
    logger.info('Uploading %s to devpi...', uploaded_file)
    logger.info('cmd = %r', cmd)
    ret = subprocess.call(cmd)
    if ret:
        logger.error('devpi upload failed')
        return
    logger.info('Uploaded %s to devpi.', uploaded_file)
