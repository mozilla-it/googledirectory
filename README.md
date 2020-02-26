# googledirectory

## How to use

First, navigate to Google's Directory API [python quickstart](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) and follow the instructions to enable the Directory API and generate yourself a *credentials.json*. Once you've got this file, move it to `~/.googledirectory/credentials.json`.

Next, install the library by running `pip3 install git+https://github.com/mozafrank/googledirectory`. This installs the library and places a CLI called `google-groups` in your $PATH.

To authorize your machine, run `google-groups -l`. Optionally if you choose not to use ~/.googledirectory you can specify a different directory by passing `-c <path_to_credentials.json> -t <path_to_where_you_want_to_store_session_token>`. When you run the library for the first time it'll use the credentials in credentials.json to request session creds, which are pickled and stored in token.pickle. To get the session creds it'll open a web browser to do oauth, and also print the URL to stdout in case you want to do it manually. Once you've finished the oauth flow in the browser the library will store the session toke n and continue. In this case since you specified `-l` it will output a list of groups you have access to.
