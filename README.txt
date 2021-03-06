TERMINAL BANK
    *by Ayran Campos, Felipe Passos and Kaio Carvalho*

## DESCRIPTION

We are running a rudimentary bank account management software.
Our solution utilizes a simple mysql database to store the data.

To prevent issues from concurrent access, each transaction is placed
in its own thread, and our server holds a list of busy bank accounts.
Whenever a bank account is going through an operation, its RG number 
is added to a busylist, which puts other threads on hold, and when
an operation is finished, we remove it from the busylist.

## OPERATION

To run the client, just run, on this directory:
    
    python main.py

Then input the requests as prompted and hit enter to send each.

The RG can actually be any unique string per account without whitespaces.
The name for an accountholder is a string without whitespaces. 
Different accounts can use the same name value.
As for the values, do not use negative numbers.
In case of decimal cases, use '.' dots.

Notice that, besides the responses, we get an info of the current state
of the lamport clock. It looks like such:
    > (LAMPORT_TIME=<lamport time>, LOCAL_TIME=<current datetime>)

Here are all of the requests and their syntax.

Create: c <RG number> <name>
    > OK
    > ERROR: Account already exists

Update: u <RG number> <new name>
    > OK
    > ERROR: Account does not exist

Delete: r <RG number>
    > OK
    > ERROR: Account does not exist

Consult balance: b <RG number>
    > BALANCE: <balance>
    > ERROR: Account does not exist

Withdraw: w <RG number> <value>
    > OK
    > ERROR: Account does not exist
    > ERROR: Insufficient funds

Deposit: d <RG number> <value>
    > OK
    > ERROR: Account does not exist

Transfer: t <sender RG no> <receiver RG no> <value>
    > OK
    > ERROR: Receiver account does not exist
    > ERROR: Sender account does not exist
    > ERROR: Insufficient funds

To close it, enter 'exit' instead of a request
Make sure the server is also running and is on a reachable address!
