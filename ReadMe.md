# portXtract

portXtract takes an nmpa output of ports, and parses out the information to just list the ports. This can be utilized to run a port specific scan when there is a long list.

You have the option of injecting a file with the information saved, or inputing (copy/paste) into the terminal. You can paste the entire nmap export with the headers.

EXample if input:
```
Welcome to portXtract!
Select an option:
1. Enter the path to a text file
2. Enter the contents directly
Enter your choice (1 or 2): 2
Enter the contents below (press Ctrl + D to finish input):
PORT      STATE SERVICE
53/tcp    open  domain
88/tcp    open  kerberos-sec
135/tcp   open  msrpc
139/tcp   open  netbios-ssn
389/tcp   open  ldap
445/tcp   open  microsoft-ds
464/tcp   open  kpasswd5
593/tcp   open  http-rpc-epmap
636/tcp   open  ldapssl
3268/tcp  open  globalcatLDAP
3269/tcp  open  globalcatLDAPssl
5985/tcp  open  wsman
9389/tcp  open  adws
Port numbers: 53,88,135,139,389,445,464,593,636,3268,3269,5985,9389

```
