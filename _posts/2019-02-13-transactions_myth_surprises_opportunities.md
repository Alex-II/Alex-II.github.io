---
layout: default
title: "Transactions: Myths, Surprises and Opportunities by Martin Kleppmann [Talk]"
category: notes
keywords: transactions, database
---

# ["Transactions: Myths, Surprises and Opportunities" by Martin Kleppmann](https://www.youtube.com/watch?v=5ZjhNTM8XU8)

## Transactions
- 1975 IBM System R
    - first transactional database
- 2008ish
    - NoSQL is a lot about no transactional guarantees
- 2012ish
    - NewSQL is a lot about no transactional guarantees

## ACID - what does it mean exactly?  
### Durability   
- data doesn't get lost (fsync to disk, replication)

### Consistency  
- not very meaningful
 meant to mean some invariants we wish to hold true before and after DB operations
 related to the way the applicatino uses it more than the DB itself  

### Atomicity  
- not about concurrency (as one would think about atomic read/writes needed for concurrnet read/writes)
- about fault handling:
    - a transaction  can contain multiple disparate DB changes 
    - a crash/fault in one change will undo any other succesful changes in the same transaction
    - i.e. roll back writes on abort
- could be called Abortability  

### Isolation  
![transactions_surprises_isolation.png](/assets/transactions_surprises_isolation.png)
- not very clear, about concurrent changes
- vaguely means that transactions don't need to consider concurrent changes to the DB 
- levels of isolation
    - isolation: Read Committed
        - default isolation level for many DBs (Postgres, Oracle, SQL Server)
        - prevents dirty reads, dirty writes
    - issue: Read Skew
        - issue can occur even when using Read Committed isolation
        - prevents process 2 reading different data elements that's being modified by process 1
        - process 1 transfers money from X to Y, process 2 reads X and Y at different times:
        - ![transactions_surprises_read_skew.png](/assets/transactions_surprises_read_skew.png)  
    - isolation: Snapshot Isolation/Repeatable Read
        - prevents Read Skew
        - similar, sometimes used interchangeably, different implementations
        - Repeatable Read
            - taking lots of locks
            - MS SQL
        - Snapshot Isolation
            - Multi version concurrency control (MVCC)
            - Postgres (calls it Repeatable Read), Oracle (Serializable), MySQL (Repeatable Read), MS SQL
            - preserves versions of the data for different transactions to see
    - issue: Write Skew
        - read something, make decision, write decision to DB
        - between making decision and writing decision, something has changed
        - usually solved by 2-phase locking
            - lock all the things that might need to be changed
            - perf issues when transaction holds lock on many rows
    - isolation: Serializability (without 2-phase locking)
        - H-Store (prototype to VaultDB) solution
            - actually serialize the transactions
            - assumes each transaction is fast 
                - more possible with modern hardware
                - a lot will happen in memory
                - reduce back-and-forth between DB engine and client
        - Postgres
            - detect conflicts and abort
            - called 'serializable snapshop isolation'
            - looks like 2-phase locking
            - locks don't block, instead record events
            - analysis at the end of the transaction: abort if conflict occurred

## Transactions over Large Systems?
- microservices:
    - transactions guarantees per microservice, not accross several
- serializable transactions accross multiple services:
    - atomic commitment, like 2-phase, 3-phase commit
    - atomic broadcast, like consensus: expensive, brittle 
        - e.g. slow parts of the system slow down the entire system
- geographic distribution
    - poor experience for consensus over variable, large latencies
- without corss-service transactions:
    - for Atomicity:
        - compensating transations
        - abort/rollbacks at application level
    - for Consistency:
        - detect & fix contrains violations after the fact, not preventing them
        - e.g. sell more than warehouse contains, reimburse and apologize

**"Every sufficiently large deployment of a microservices contains an ad-hoc, informally-specified, bug-ridden, slow implementation of half of transactions"**

## Causality in Microservices
- microservices can have implicit causal relationship between events
- e.g. user unfriends someone, posts about how awful that person is
    - user's posts are not delivered to non-friends
    - thus, user expects the no-longer-friend to not receive spiteful message
    - user's *posts-deliving* microservice might receive data before *friend-relationship* microservice
- today: microservices are eventually consistent (or never consistent)
- serializability: probably won't happen soon
- causality: proofs show this can occur without consensus and without global coordination
- causality and efficient: can this be done efficiently? TBD
![transactions_surprises_isolation.png](/assets/transactions_surprises_isolation.png)


![transactions_surprises_isolation_bounds.png](/assets/transactions_surprises_isolation_bounds.png)