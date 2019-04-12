---
layout: default
title: "Uncoupling by Michael Nygard [Talk]"
category: notes
keywords: transactions, database
---

# ["Uncoupling" by Michael Nygard](https://www.youtube.com/watch?v=esm-1QXtA2Q)

## Coupling is Everywhere
- We see 'coupling' in mechanical systems, phsyics, trains, etc.
- Coupling need not mean 'bad' automatically
- Some coupling is required for functionality

## Kinds of Coupling
- (they can occur together or not, and at different degrees)
- Operational: consumer cannot run without provider
- Development: changes in produce & consumer must be cooridnated
    - e.g. change a function signature e.g. APIs
- Semantic: change together because of shared concepts
    - e.g. global abstractions that everyone relies on have their behavior/properties changed
        - should proabably extract a smaller subset of the abstraction
- Functional: change together because of shared responsability
    - i.e. responsability/code repetition 
    - e.g. several pieces of code log, and the log format has changed
- Incidental: change together for no reason 
    - **latent**: happens when no one knows why it broke
        - e.g. 2 services have a hardcoded path to a file (reader and writer); when writer changes location, the reader will break to everyone's surprise

## Coupling Example 1
**C# service notifying, using SMTP, a MS Exchange service a report is ready (i.e. C# sends email, Exchange receives it and passes it along)**  
- Operational: strong coupling. SMTP is synchronous, connection-oriented. If receiver is missing, sender can't do anything.
- Development: weak coupling. SMTP has heritage and has history of planned interoperatiblity.
    - i.e. unlikely SMTP will change in a way requiring the C# service to also change
- Semantic: very strong. SMTP defines enetities, attributes tightly.
    - not necessarily a problem: unlikely to change and deprecated verrsion will be maintained a while
- Functional: very weak. sender and receiver have different busiless logic, they share network and some SMTP.


## Coupling Example 2, part 1
**Data importer fetches data from data store (a RDBMS) using SQL queries**  
- Operational: very strong. no db, no data. must be aware of topology failover
    - SQL errors not clear on whether things should be retried (because of recent failover) or the query is invalid
- Development: very strong. changes in tables, schemas, versions immediately impact the importer.
- Semantic: very strong. tables, columns, joins are must-be-shared concepts.
- Functional: weak. mostly non-overlapping code.


## Coupling Example 2, part 2 
**Data importer fetches data from a data store (still backed by RDBMS) but there's a REST interface inbetween**  
- Operational: strong but less. no db, still no data. however, no need to be aware of topology failover.
- Development: strong but less. insulated from data format changes.
- Semantic: still very strong. REST resources and C# entities must align (before it was SQL concepts and SQL queries)
- Functional: still weak


## Coupling Example 2, part 3 
**Data importer now subscribes to publications from the data store; data store uses a message broker**  
**Data importer now caches between publications**
- Operational: very weak. Data importer can work with stale cached data while broker/storage is missing for a while [if it makes sense in business domain] 
- Development: weaker. two places to make changes and insulate 
- Semantic: strong but less. broker allows for remapping [but business entities transformations are now in more places to maintain, less cohesive]
- Functional: moderate now. more communication, more remapping places.

## Chains of Semantic Coupling 
- Sometimes, we have a concept/object/entity who we consider cover and are used by the entire business domain.
    - e.g. SKUs in ecommerce
- Every service will adapt to processing the entity and it becomes a core concept in each service
- Not all service will really use the entire SKU concept (not using use all the attributes of the SKU)
    - e.g. SKUs describe a product's attributes: price, cost, shelf space taken, presentation text, description, expiry, etc.
- SKUs bundles attributes: this can make *business domain* sense in *some* facets of the business
    - e.g. some products don't have physical shelft space
    - e.g. the SKU price can be found out AFTER an order is placed (depending on quantity bought)
- We don't need SKUs to be global/God objects passed everywhere
- When the SKU is changed, every microservice that assumed it needed the entire SKU needs to change
    - e.g. new concept of 'price point' in a SKU which points to another SKU to get a final price; 
        - services were looking at the SKU but they really just wanted a price
        - now every service needs to start looking up other SKUs based on the price point

## Long Arrows 
**A system digram describing an interface/rpc call/simple interaction between 2 components that's actually a long chain of complex moving parts**
![interface_was_chain.png](/assets/interface_was_chain.png)
- Such a ["self-contained" and undocumented] "interface" has terrible characteristics
- latency, availability, throughput, security all bottlenecked by the worst link in the long chain
- [I suppose because no one is taking a look at the architecture of the chain]

