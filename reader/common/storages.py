from storages.backends.gcloud import GoogleCloudStorage


class BookFilesStorage(GoogleCloudStorage):
    """Handle static files storage."""
    location = 'content'
