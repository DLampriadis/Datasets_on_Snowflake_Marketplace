# Monthly update of the aviation numbers dataset.

This dataset is being updated monthly. There are some steps that you need to follow in order to upload the dataset.
This guide explains how to update the dataset using the CSV, by downloading it locally and then uploading to the Snowflake account.

* Follow this link for more information on the dataset:
    https://opendata.cbs.nl/statline/portal.html?_la=en&_catalog=CBS&tableId=37478eng&_theme=1170

* Create a virtual environment and sett up environment variables for the following:

    SNOWFLAKE_ACCOUNT = _your snowflake account_ without the .snowflake.com <br>
    SNOWFLAKE_USER = _your username_<br>
    SNOWFLAKE_PASSWORD = _your password_

* Run the following script in your IDE:
    ```
    ../main.py
    ```
* Check in the snowflake account, in the database MARKETPLACE, and schema PUBLIC, if the datasets have been uploaded.