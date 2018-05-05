Compiling protobufs:
`mvn protobuf:compile protobuf:compile-custom`

Compiling Java code:
`mvn package`

Running server:
`./target/globesort/bin/runServer <server_port>`

Running client:
`./target/globesort/bin/runClient <server_ip> <server_port> <values>`

---

Create VMs in the following regions:  
- Oregon: `cse291c-hw2-qiz232-ucsd.pem`  
ssh -i cse291c-hw2-qiz232-ucsd.pem ec2-user@
- Seoul (ap-northeast-2): `cse291c-hw2-qiz232-seoul.pem`  
ssh -i cse291c-hw2-qiz232-seoul.pem ec2-user@ec2-13-209-42-251.ap-northeast-2.compute.amazonaws.com 
- Ireland (eu-west-1): `cse291c-hw2-qiz232-ireland.pem`  
ssh -i cse291c-hw2-qiz232-ireland.pem ec2-user@ec2-54-194-70-49.eu-west-1.compute.amazonaws.com
- Sao Paulo (sa-east-1):`cse291c-hw2-qiz232-saopaulo.pem`  
ssh -i cse291c-hw2-qiz232-saopaulo.pem ec2-user@ec2-52-67-204-182.sa-east-1.compute.amazonaws.com
- Mumbai (ap-south-1): `cse291c-hw2-qiz232-mumbai.pem`  
ssh -i cse291c-hw2-qiz232-mumbai.pem ec2-user@ec2-13-232-58-114.ap-south-1.compute.amazonaws.com

create the protobuf stubs and compile java:
 mvn protobuf:compile protobuf:compile-custom
 mvn package  

### TO-DO: 
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

### Results:
- Seoul, Korea ↔ Dublin, Ireland

- Dublin, Ireland ↔ Sao Paulo, Brazil

- Sao Paulo, Brazil ↔ Mumbai, India

- Mumbai, India ↔ Seoul, Korea

