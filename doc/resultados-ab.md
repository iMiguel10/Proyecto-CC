# Resultados de ab

Como podemos ver a continuación, el resultado de evaluar los servicios web que proporcionamos, nos ha permitido ver como el contenedor con **python slim** realiza más peticiones por segundo que las otros 2 contenedores, por lo tanto podemos decir que es el que mejor respuesta nos da.

**ORDEN USADA:** `ab -g resultados.tsv -n 1000 -c 10 localhost:8080`

### PYTHON_SLIM
```
Server Software:        gunicorn/20.0.0
Server Hostname:        localhost
Server Port:            8080

Document Path:          /
Document Length:        16 bytes

Concurrency Level:      10
Time taken for tests:   3.396 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      168000 bytes
HTML transferred:       16000 bytes
Requests per second:    294.50 [#/sec] (mean)
Time per request:       33.955 [ms] (mean)
Time per request:       3.396 [ms] (mean, across all concurrent requests)
Transfer rate:          48.32 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.0      0      15
Processing:     7   33   5.9     33      55
Waiting:        7   33   5.9     32      54
Total:         14   34   5.6     33      55

Percentage of the requests served within a certain time (ms)
  50%     33
  66%     35
  75%     36
  80%     37
  90%     41
  95%     44
  98%     48
  99%     50
 100%     55 (longest request)
```

### PYTHON_ALPINE
```
Server Software:        gunicorn/20.0.0
Server Hostname:        localhost
Server Port:            8080

Document Path:          /
Document Length:        16 bytes

Concurrency Level:      10
Time taken for tests:   31.748 seconds
Complete requests:      996
Failed requests:        0
Total transferred:      167328 bytes
HTML transferred:       15936 bytes
Requests per second:    31.37 [#/sec] (mean)
Time per request:       318.760 [ms] (mean)
Time per request:       31.876 [ms] (mean, across all concurrent requests)
Transfer rate:          5.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    6  11.6      0      54
Processing:     8   69 247.5     43    2530
Waiting:        0   65 247.7     40    2530
Total:          9   74 246.9     49    2530

Percentage of the requests served within a certain time (ms)
  50%     49
  66%     54
  75%     59
  80%     61
  90%     69
  95%     79
  98%     98
  99%   2503
 100%   2530 (longest request)
```
### UBUNTU
```
Server Software:        gunicorn/20.0.0
Server Hostname:        localhost
Server Port:            8080

Document Path:          /
Document Length:        16 bytes

Concurrency Level:      10
Time taken for tests:   28.460 seconds
Complete requests:      998
Failed requests:        0
Total transferred:      167664 bytes
HTML transferred:       15968 bytes
Requests per second:    35.07 [#/sec] (mean)
Time per request:       285.174 [ms] (mean)
Time per request:       28.517 [ms] (mean, across all concurrent requests)
Transfer rate:          5.75 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    8  10.8      0      48
Processing:     2   32  13.4     29      82
Waiting:        0   27  11.7     25      82
Total:         12   40  13.6     39      89

Percentage of the requests served within a certain time (ms)
  50%     39
  66%     45
  75%     48
  80%     49
  90%     59
  95%     64
  98%     73
  99%     82
 100%     89 (longest request)
```
