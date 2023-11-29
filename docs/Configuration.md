# Configuration

To start using the API, you need to configure the secret key and initiate the client instance.
You can use all the configurable parameters in the `configuration.py` file to customize your client (e.g. setting up proxy)

## Configuration Parameters

Here are the parameters you can set:

| Name |    Type    | Description                                                                                                          | Default                                                     | Example                                                                  |
|-------------|:----------:|:---------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------|
| **host** |  **str**   | Base URL                                                                                                             | https://api.xendit.co                                       | https://www.example.com                                                  |
| **api_key** |  **str**   | Xendit API Key                                                                                                       | None                                                        | `xnd_development_abcdefghijke9112015j1nuq808912tr`                       |
| **proxy** |  **str**   | Proxy URL                                                                                                            | None                                                        | https://www.proxy.example.com                                            |
| **ssl_ca_cert** |  **str**   | Specifies the path to a PEM format CA certificate files, which can be used to verify the backend server certificates | None                                                        | `/path/to/your/example_cert.crt`                                         |
| **logger** |  **map**   | Logging Settings (e.g. `package_logger`, `urllib3_logger`)                                                           | `{"package_logger": "xendit", "urllib3_logger": "urllib3"}` | `{"package_logger": "your_logger_package", "urllib3_logger": "urllib3"}` |
| **logger_format** |  **str**   | Log format                                                                                                           | `%(asctime)s %(levelname)s %(message)s`                     | `%(asctime)s %(levelname)s %(message)s`                                  |
| **logger_file** |  **str**   | Debug file location                                                                                                  | None                                                        | `/path/to/your/debug_file.txt`                                           |
| **debug** |  **bool**  | Debug Switch                                                                                                         | `False`                                                       | `True`                                                                   |
| **connection_pool_maxsize** | **number** | urllib3 connection pool's maximum number of connections saved per pool.                                              | `multiprocessing.cpu_count() * 5`                           | 5                                                                        |

## Sample Usage

Some parameters are able to set during initialization, e.g. `host`, `api_key`
Some are set after initialization, e.g. `proxy`

```python
import xendit

configuration = xendit.Configuration(
    host='https://www.example.com',
    api_key='xnd_development_abcdefghijke9112015j1nuq808912tr'
)
configuration.proxy = 'https://www.proxy.example.com'
configuration.ssl_ca_cert = '/path/to/your/example_cert.crt'
configuration.logger["package_logger"] = 'your_logger_package'
configuration.logger["urllib3_logger"] = 'urllib3_logger'
configuration.logger_format = '%(asctime)s %(levelname)s %(message)s`'
configuration.logger_file = 'path/to/your/debug_file.txt'
configuration.connection_pool_maxsize = 10

# Enter a context with an instance of the API client
api_client = xendit.ApiClient(configuration)
```


