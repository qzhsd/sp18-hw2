Compiling protobufs and compiling Java code:

`mvn protobuf:compile protobuf:compile-custom && mvn package`

Running server:
`./target/globesort/bin/runServer <server_port>`

Running client:
`./target/globesort/bin/runClient <server_ip> <server_port> <values>`

---

Create VMs in the following regions: 

- Oregon: `cse291c-hw2-qiz232-ucsd.pem`  
ssh -i cse291c-hw2-qiz232-ucsd.pem ec2-user@

- Seoul (ap-northeast-2): `cse291c-hw2-qiz232-seoul.pem`  
ssh -i cse291c-hw2-qiz232-seoul.pem ec2-user@52.79.141.174
- Ireland (eu-west-1): `cse291c-hw2-qiz232-ireland.pem`  
ssh -i cse291c-hw2-qiz232-ireland.pem ec2-user@34.245.233.13
- Sao Paulo (sa-east-1):`cse291c-hw2-qiz232-saopaulo.pem`  
ssh -i cse291c-hw2-qiz232-saopaulo.pem ec2-user@18.231.114.76
- Mumbai (ap-south-1): `cse291c-hw2-qiz232-mumbai.pem`  
ssh -i cse291c-hw2-qiz232-mumbai.pem ec2-user@13.126.133.194

create the protobuf stubs and compile java:
 mvn protobuf:compile protobuf:compile-custom && mvn package  




### Experiments: 
1. Latency experiment (round-trip):  
      - experiments date/time
      - 3 times
2. Application-level throughput experiment:  
      - experiments date/time
      - 3 times    
3. Network-level throughput experiment (one-way):  
      - modify the sortIntegers() call to return the amount of time the server took sorting the data.
      - experiments date/time
      - 3 times

### Results (unit: milliseconds):
- Seoul, Korea ↔ Dublin, Ireland (experiments date/time: May 5, 4:23pm  number of integers: 2200000) (5589.92mi)
      1. Latency experiment (round trip):  
            - 3 times:
                  - first ping: 1022.331431, 1023.917656, 1009.138885
                  - second ping: 252.440642, 252.101974, 253.593445

      2. Application-level throughput:  
            - 3 times: 19507.879249, 19632.451128, 19630.458821
 
      3. Network-level throughput experiment (one-way):  
            - 3 times:
                  - server sorting the data: 1006.562846, 1304.933873, 989.699507

- Dublin, Ireland ↔ Sao Paulo, Brazil (experiments date/time: May 5, 5:20pm, number of integers: 2800000) (5,809.52mi)
      1. Latency experiment (round trip):  
            - 3 times:
                  - first ping: 903.093246, 901.780606, 895.835927 
                  - second ping: 191.215437, 191.855698, 190.24646

      2. Application-level throughput:  
            - 3 times: 19204.500465, 19662.215222, 19155.964547 
 
      3. Network-level throughput experiment (one-way):  
            - 3 times:
                  - server sorting the data: 1424.178395, 1894.493671, 1336.20583

- Sao Paulo, Brazil ↔ Mumbai, India (experiments date/time: May 5, 2:47pm; number of integers: 2000000) (8,464.05mi)
      1. Latency experiment (round trip):  
            - 3 times:
                  - first ping: 1324.153344, 1155.289933, 1153.736149 
                  - second ping: 309.54034, 306.696571, 306.18090

      2. Application-level throughput:  
            - 3 times: 22216.61539, 21801.379021, 21131.186786
 
      3. Network-level throughput experiment (one-way):  
            - 3 times:
                  - server sorting the data: 2061.071872, 1219.832304, 1024.331339

- Mumbai, India ↔ Seoul, Korea (experiments date/time: May 5, 3:46pm; number of integers: 3500000) (3,473.20 mi) 
      1. Latency experiment (round trip):  
            - 3 times:
                  - first ping: 724.988137, 727.043714, 719.098645
                  - second ping: 163.192896, 162.900802, 162.855991

      2. Application-level throughput:  
            - 3 times: 20656.116915, 21183.522286, 20999.368883
 
      3. Network-level throughput experiment (one-way):  
            - 3 times:
                  - server sorting the data: 1708.661064, 2315.338683, 2312.151004


