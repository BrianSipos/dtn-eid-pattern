# Bundle Protocol Endpoint ID Patterns

The internet-draft is hosted at [draft-sipos-dtn-eid-pattern](https://datatracker.ietf.org/doc/draft-sipos-dtn-eid-pattern/).

A local build of the current main branch is available [draft-sipos-dtn-eid-pattern.html](https://briansipos.github.io/dtn-eid-pattern/draft-sipos-dtn-eid-pattern.html) with its [misspelling.txt](https://briansipos.github.io/dtn-eid-pattern/misspelling.txt).

Prerequisites to building can be installed on Ubuntu with:
```
sudo apt-get install -y install aspell cmake python3 python3-pip python3-setuptools python3-wheel ruby xmlstarlet
sudo pip3 install xml2rfc abnf
sudo gem install cddl
```
and then the document can be built with
```
cmake -S . -B build
cmake --build build
```
