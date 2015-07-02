
1.  Obtain your applications API Key and Shared Secret, and modify
    `shopify_settings.py` to use these values. You can also modify
    the permissions that your app needs in this settings file.

2.  Install:

    ```shell
    pip install -r requirements.txt
    ```

3.  Create the database

    ```shell
    python manage.py syncdb
    ```

4.  Start the server

    ```shell
    python manage.py runserver
    ```

5.  Visit <http://localhost:8000> to view the example.
